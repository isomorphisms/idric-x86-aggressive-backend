#!/usr/bin/env python3
"""
Generate one human-readable Markdown page per XED ICLASS.

The instruction-name set comes from generated/xed-iclasses.txt and the metadata
comes from generated/xed-instructions.tsv. The prose is generated from
instruction-specific semantic rules rather than from a generic sentence.
Unknown mnemonics are still documented, but are also emitted to a fallback list
so their prose can be reviewed and strengthened.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


SPECIAL = {
    "AAA": "adjusts the low byte of AX after adding two unpacked BCD digits, correcting AL and AH and updating the arithmetic status used by legacy decimal code",
    "AAD": "adjusts two unpacked BCD digits in AH:AL before division, combining them into a binary value in AL",
    "AAM": "adjusts the binary result of an 8-bit multiply into two unpacked BCD digits in AH and AL",
    "AAS": "adjusts the low byte of AX after subtracting unpacked BCD digits, correcting AL and AH for legacy decimal arithmetic",
    "ARPL": "adjusts the requested privilege level field of a protected-mode segment selector so it is not more privileged than a comparison selector",
    "BOUND": "checks a signed array index against lower and upper bounds stored in memory and raises a bounds exception when it lies outside them",
    "CALL_NEAR": "transfers control to a procedure in the current code segment while saving a return address on the stack",
    "CALL_FAR": "performs a far procedure call, changing code-segment context as well as the instruction pointer and saving return state",
    "RET_NEAR": "returns from a near procedure by restoring the saved instruction pointer from the stack",
    "RET_FAR": "returns from a far procedure, restoring both instruction-pointer and code-segment state",
    "LEA": "computes the arithmetic address expression encoded by a memory-style operand and writes that numerical address to a general-purpose register without reading memory",
    "NOP": "performs no architectural data computation while consuming an instruction slot; multi-byte encodings are commonly used for alignment and patchable padding",
    "PAUSE": "provides a processor hint inside spin-wait loops so the core can treat repeated polling more efficiently than an ordinary empty loop",
    "CPUID": "queries processor identification and feature information selected by EAX and, for some leaves, ECX, returning structured capability data in general-purpose registers",
    "RDTSC": "reads the processor time-stamp counter into EDX:EAX, exposing a high-resolution cycle-like counter without fully serializing surrounding execution",
    "RDTSCP": "reads the time-stamp counter and IA32_TSC_AUX with ordering stronger than RDTSC on its leading side, returning the counter in EDX:EAX and auxiliary value in ECX",
    "SERIALIZE": "acts as a fully serializing instruction for instruction execution, forcing prior architectural effects to complete before later instructions execute",
    "LFENCE": "orders prior loads before subsequent loads and, on current x86 implementations, is also used as an execution-ordering barrier in selected speculation-sensitive sequences",
    "SFENCE": "orders prior stores before subsequent stores, especially for weakly ordered or non-temporal store sequences",
    "MFENCE": "orders prior loads and stores before later loads and stores, providing a full memory fence at the architectural level",
    "CLFLUSH": "invalidates the cache line containing a specified memory address from the coherent cache hierarchy and writes back modified data as required",
    "CLFLUSHOPT": "requests cache-line writeback and invalidation like CLFLUSH but with weaker ordering that permits more overlap between multiple flushes",
    "CLWB": "writes back a modified cache line toward memory without requiring the line to be invalidated from the caches",
    "CLDEMOTE": "hints that the cache line containing an address should be demoted from a nearer cache level to reduce pressure while retaining it in the hierarchy",
    "PREFETCHNTA": "hints that a memory line will be read soon with low temporal locality, encouraging placement that minimizes pollution of the most valuable cache levels",
    "PREFETCHT0": "hints that a memory line will be read soon and should be fetched with high temporal locality",
    "PREFETCHT1": "hints that a memory line will be read soon with intermediate temporal locality",
    "PREFETCHT2": "hints that a memory line will be read soon with lower temporal locality than PREFETCHT0",
    "PREFETCHW": "hints that a memory line will soon be written and should be brought into a state suitable for modification",
    "PREFETCHWT1": "hints that a memory line will soon be written while expressing a weaker temporal-locality preference",
    "HLT": "halts instruction execution until an enabled interrupt, reset, or another architecturally defined wake event occurs; it is privileged in normal protected execution",
    "INT": "invokes an interrupt or exception handler through an interrupt vector encoded in the instruction, saving control state according to the current mode",
    "INT1": "raises the debug exception through the one-byte ICEBP encoding, historically used by debuggers and in-system emulators",
    "INT3": "raises the breakpoint exception using the dedicated one-byte breakpoint encoding",
    "INTO": "raises the overflow exception when the overflow flag is set; this legacy instruction is not available in 64-bit mode",
    "IRET": "returns from an interrupt or exception handler by restoring saved control state and, when required, privilege-stack state",
    "IRETD": "returns from an interrupt using the 32-bit operand-size form of the interrupt-return mechanism",
    "IRETQ": "returns from an interrupt in 64-bit mode, restoring RIP, CS, RFLAGS, and any privilege-transition state required by the saved frame",
    "SYSCALL": "enters an operating-system system-call handler through model-specific entry state, saving the user return location in registers rather than building a normal call frame",
    "SYSRET": "returns from a SYSCALL-style system-call handler to a less-privileged context using model-specific return state",
    "SYSRET64": "performs the 64-bit return form of SYSRET from a SYSCALL-style privileged entry",
    "SYSENTER": "enters a privileged operating-system service routine through model-specific fast-system-call state",
    "SYSEXIT": "returns from a SYSENTER-style fast system call to a less-privileged context",
    "SWAPGS": "exchanges the current GS base with the kernel GS base stored in a model-specific register, supporting fast per-CPU context changes around kernel entry and exit",
    "RDMSR": "reads a model-specific register selected by ECX and returns its 64-bit value in EDX:EAX; ordinary user-mode code cannot execute it",
    "WRMSR": "writes EDX:EAX to the model-specific register selected by ECX; it is privileged and can change processor control state",
    "RDPMC": "reads a selected performance-monitoring counter into EDX:EAX when privilege and control settings permit it",
    "RDRAND": "requests a hardware-generated random value and reports success through the carry flag",
    "RDSEED": "requests a hardware seed value intended for seeding a software pseudorandom generator and reports availability through the carry flag",
    "RDPID": "reads the processor identifier stored in IA32_TSC_AUX into a general-purpose register without reading the timestamp counter",
    "RDPKRU": "reads the protection-key rights register that controls access permissions for pages associated with user protection keys",
    "WRPKRU": "writes the protection-key rights register, changing user-space access-disable and write-disable state for protection-key domains",
    "RDFSBASE": "reads the current FS segment base address into a general-purpose register when FSGSBASE is enabled",
    "RDGSBASE": "reads the current GS segment base address into a general-purpose register when FSGSBASE is enabled",
    "WRFSBASE": "writes a general-purpose register value as the FS segment base when FSGSBASE is enabled",
    "WRGSBASE": "writes a general-purpose register value as the GS segment base when FSGSBASE is enabled",
    "LAHF": "copies selected arithmetic status flags into AH, providing a compact way to materialize condition-code state in a general-purpose register",
    "SAHF": "copies selected bits of AH into arithmetic status flags, restoring a subset of condition-code state",
    "PUSH": "decrements the stack pointer and stores an operand on the current stack using the instruction's operand size",
    "POP": "loads a value from the current stack and increments the stack pointer, moving stack data into a register, memory location, or selected segment register",
    "ENTER": "builds a stack frame, optionally creating a chain of nested lexical frames as specified by its immediate operands",
    "LEAVE": "dismantles a conventional stack frame by copying the frame pointer to the stack pointer and restoring the previous frame pointer",
    "CLC": "clears the carry flag",
    "STC": "sets the carry flag",
    "CMC": "complements the carry flag",
    "CLD": "clears the direction flag so string instructions advance their implicit index registers",
    "STD": "sets the direction flag so string instructions decrement their implicit index registers",
    "CLI": "clears the interrupt-enable flag when privilege permits, disabling maskable external interrupts on the current logical processor",
    "STI": "sets the interrupt-enable flag when privilege permits, enabling maskable external interrupts after the architecture's defined delay",
    "CLAC": "clears the SMAP access-control flag so supervisor-mode explicit accesses to user pages are blocked again",
    "STAC": "sets the SMAP access-control flag so supervisor code can temporarily access user pages",
    "UD0": "unconditionally raises the invalid-opcode exception using an encoding reserved for that purpose",
    "UD1": "unconditionally raises the invalid-opcode exception using a ModRM-bearing reserved encoding",
    "UD2": "unconditionally raises the invalid-opcode exception and is the conventional x86 trap instruction used for deliberately unreachable code",
    "XGETBV": "reads an extended-control register selected by ECX, most commonly XCR0, to determine which processor-managed extended states are enabled",
    "XSETBV": "writes an extended-control register selected by ECX, changing which extended processor states are enabled; it is privileged by control-state rules",
    "XSAVE": "saves the enabled subset of extended processor state to a memory area using the component layout defined by XCR0 and related control state",
    "XRSTOR": "restores selected extended processor-state components from an XSAVE-format memory area",
    "FXSAVE": "stores x87, MMX, SSE, and MXCSR state in the legacy FXSAVE memory format",
    "FXRSTOR": "restores x87, MMX, SSE, and MXCSR state from the legacy FXSAVE memory format",
    "EMMS": "marks the MMX/x87 register-file tags as empty after MMX use so subsequent x87 floating-point code sees an empty stack",
    "VZEROUPPER": "clears the upper portions of YMM registers while preserving the low 128 bits, avoiding transition penalties when mixing AVX and legacy SSE code on affected processors",
    "VZEROALL": "clears the architecturally visible contents of the vector registers covered by the instruction's AVX state",
    "ENDBR32": "marks a valid 32-bit indirect branch target for Control-flow Enforcement Technology indirect-branch tracking",
    "ENDBR64": "marks a valid 64-bit indirect branch target for Control-flow Enforcement Technology indirect-branch tracking",
    "INCSSPD": "advances the shadow-stack pointer by a scaled 32-bit count without reading or writing ordinary stack memory",
    "INCSSPQ": "advances the shadow-stack pointer by a scaled 64-bit count without reading or writing ordinary stack memory",
    "UMONITOR": "arms user-mode monitoring of a linear address so UMWAIT can enter an optimized wait state until the monitored location or another event changes execution conditions",
    "UMWAIT": "enters a user-mode optimized wait state until a monitored-store event, timeout, or other wake condition occurs",
    "TPAUSE": "enters a timed pause state until the timestamp counter reaches a requested deadline or another wake condition occurs",
    "MONITOR": "arms hardware monitoring of a memory address for use with MWAIT",
    "MWAIT": "enters an optimized processor wait state until an event such as a store to a monitored address or an interrupt wakes execution",
    "MONITORX": "AMD's extended monitor instruction arms monitoring of a memory address for use with MWAITX",
    "MWAITX": "AMD's extended wait instruction sleeps until a monitored event, interrupt, or optional timeout wakes execution",
    "WBINVD": "writes back modified cache lines and invalidates the processor caches; it is a privileged whole-cache maintenance operation",
    "INVD": "invalidates processor caches without writing modified lines back to memory and is therefore a privileged, destructive cache-management operation",
    "INVLPG": "invalidates the translation-lookaside-buffer entry associated with a linear address for the current address-space context",
    "INVPCID": "invalidates selected translation-cache entries using a process-context identifier and an invalidation type",
    "MOV_CR": "moves a value between a general-purpose register and a control register, exposing privileged processor control state",
    "MOV_DR": "moves a value between a general-purpose register and a debug register",
    "LGDT": "loads the global descriptor-table register from a memory descriptor",
    "SGDT": "stores the current global descriptor-table register to memory",
    "LIDT": "loads the interrupt descriptor-table register from a memory descriptor",
    "SIDT": "stores the current interrupt descriptor-table register to memory",
    "LLDT": "loads the local descriptor-table register from a segment selector",
    "SLDT": "stores the current local descriptor-table selector",
    "LTR": "loads the task register from a task-state-segment selector",
    "STR": "stores the current task-register selector",
    "LMSW": "loads selected low control bits of CR0 from a source operand, a legacy protected-mode control operation",
    "SMSW": "stores the machine-status word, exposing selected low CR0 state",
    "IN": "reads a byte, word, or doubleword from an I/O port into the accumulator using x86's separate port-I/O address space",
    "OUT": "writes the accumulator to an I/O port using x86's separate port-I/O address space",
}

COND = {
    "B": "below (carry set)", "BE": "below or equal", "L": "less in signed comparison", "LE": "less or equal in signed comparison",
    "NB": "not below / unsigned above-or-equal", "NBE": "unsigned above", "NL": "signed greater-or-equal", "NLE": "signed greater",
    "NO": "no signed overflow", "NP": "not parity", "NS": "non-negative", "NZ": "nonzero", "O": "signed overflow",
    "P": "parity", "S": "negative", "Z": "zero / equal", "F": "false", "T": "true",
}

TYPE_SUFFIX = {
    "PS": "packed single-precision floating-point elements", "PD": "packed double-precision floating-point elements",
    "SS": "a scalar single-precision floating-point element", "SD": "a scalar double-precision floating-point element",
    "PH": "packed IEEE binary16 floating-point elements", "SH": "a scalar IEEE binary16 floating-point element",
    "BF16": "bfloat16 elements", "B": "byte elements", "W": "16-bit word elements", "D": "32-bit doubleword elements",
    "Q": "64-bit quadword elements", "DQ": "double-quadword vector data",
}


def clean_extensions(rows):
    return sorted({r.get("extension", "").strip() or "UNKNOWN" for r in rows})


def clean_categories(rows):
    return sorted({r.get("category", "").strip() or "UNKNOWN" for r in rows})


def element_kind(name):
    for suffix in ("BF16", "PS", "PD", "SS", "SD", "PH", "SH", "DQ", "B", "W", "D", "Q"):
        if name.endswith(suffix):
            return TYPE_SUFFIX[suffix]
    return "its encoded scalar or vector elements"


def condition_semantics(name):
    for prefix, action in (("CMOV", "copies the source operand to the destination only when"), ("SET", "writes a one-byte Boolean value that is 1 when"), ("J", "transfers control to the branch target when"), ("CCMP", "performs the architecture's conditional compare operation when"), ("CTEST", "performs the architecture's conditional test operation when"), ("CFCMOV", "conditionally moves an x87 value when")):
        if name.startswith(prefix):
            cc = name[len(prefix):]
            if cc in COND:
                return f"{action} the condition-code state denotes {COND[cc]}; otherwise it follows the instruction family's defined non-taken behavior"
    return None


def string_semantics(name):
    m = re.match(r"(?:(REP|REPE|REPNE)_)?(MOVS|LODS|STOS|SCAS|CMPS|INS|OUTS)(B|W|D|Q)$", name)
    if not m:
        return None
    rep, op, width = m.groups()
    widths = {"B": "byte", "W": "16-bit word", "D": "32-bit doubleword", "Q": "64-bit quadword"}
    thing = widths[width]
    base = {
        "MOVS": f"copies one {thing} from the implicit source address to the implicit destination address and updates both string indices according to the direction flag",
        "LODS": f"loads one {thing} from the implicit source address into the accumulator and updates the source index",
        "STOS": f"stores the accumulator's low {thing} to the implicit destination address and updates the destination index",
        "SCAS": f"compares the accumulator's low {thing} with memory at the implicit destination address, sets flags, and updates the destination index",
        "CMPS": f"compares a {thing} at the implicit source address with one at the implicit destination address, sets flags, and updates both indices",
        "INS": f"reads one {thing} from an I/O port into memory at the implicit destination address and updates the destination index",
        "OUTS": f"writes one {thing} from memory at the implicit source address to an I/O port and updates the source index",
    }[op]
    if rep == "REP": return base + "; REP repeats while the count register is nonzero"
    if rep == "REPE": return base + "; REPE repeats while the count is nonzero and the previous comparison remains equal"
    if rep == "REPNE": return base + "; REPNE repeats while the count is nonzero and the previous comparison remains unequal"
    return base


def x87_semantics(name):
    exact = {
        "F2XM1": "computes 2^x minus 1 for ST(0) over the instruction's defined input range", "FABS": "replaces ST(0) with its absolute value",
        "FCHS": "changes the sign of ST(0)", "FCOS": "computes the cosine of ST(0)", "FSIN": "computes the sine of ST(0)",
        "FSINCOS": "computes both sine and cosine of ST(0), leaving both results on the x87 stack", "FSQRT": "computes the square root of ST(0)",
        "FPATAN": "computes an atan2-style arctangent from the top two x87 stack values", "FRNDINT": "rounds ST(0) to an integral floating-point value according to the x87 rounding mode",
        "FSCALE": "scales ST(0) by an integral power of two derived from ST(1)", "FXTRACT": "splits ST(0) into significand and exponent components",
        "FYL2X": "computes ST(1) times log2(ST(0)) and pops the x87 stack", "FYL2XP1": "computes ST(1) times log2(ST(0)+1) and pops the x87 stack",
        "FXCH": "exchanges ST(0) with another x87 stack register", "FTST": "compares ST(0) with positive zero and records x87 condition codes",
        "FXAM": "classifies ST(0)'s sign and floating-point kind into x87 condition-code bits", "FWAIT": "checks for pending unmasked x87 exceptions before continuing",
        "FNOP": "performs an x87 no-operation while retaining x87 exception semantics",
    }
    if name in exact: return exact[name]
    rules = [
        ("FADDP", "adds x87 floating-point operands and pops ST(0)"), ("FADD", "adds x87 floating-point operands"), ("FIADD", "adds an integer memory operand to ST(0) using x87 arithmetic"),
        ("FSUBRP", "subtracts x87 operands in reverse order and pops ST(0)"), ("FSUBP", "subtracts x87 operands and pops ST(0)"), ("FSUBR", "subtracts x87 operands in reverse order"), ("FSUB", "subtracts x87 floating-point operands"),
        ("FMULP", "multiplies x87 floating-point operands and pops ST(0)"), ("FMUL", "multiplies x87 floating-point operands"), ("FIMUL", "multiplies ST(0) by an integer memory operand using x87 arithmetic"),
        ("FDIVRP", "divides x87 operands in reverse order and pops ST(0)"), ("FDIVP", "divides x87 operands and pops ST(0)"), ("FDIVR", "divides x87 operands in reverse order"), ("FDIV", "divides x87 floating-point operands"),
        ("FLD", "pushes a floating-point value onto the x87 stack"), ("FILD", "converts an integer memory operand to x87 precision and pushes it"),
        ("FSTP", "stores ST(0) and pops the x87 stack"), ("FST", "stores ST(0) without popping the x87 stack"), ("FISTTP", "converts ST(0) to an integer by truncation, stores it, and pops"),
        ("FISTP", "converts ST(0) to an integer using the x87 rounding mode, stores it, and pops"), ("FIST", "converts ST(0) to an integer and stores it without popping"),
        ("FCOMPP", "compares x87 values and pops two stack entries"), ("FCOMP", "compares x87 values and pops one stack entry"), ("FCOM", "compares x87 values and records x87 condition codes"),
        ("FUCOMPP", "performs an unordered x87 comparison and pops two stack entries"), ("FUCOMP", "performs an unordered x87 comparison and pops one stack entry"), ("FUCOM", "performs an unordered x87 comparison"),
        ("FFREE", "marks an x87 stack register empty in the tag state without moving its stored bits"),
    ]
    for prefix, desc in rules:
        if name.startswith(prefix): return desc
    return None


def crypto_semantics(name):
    if name.startswith("AESENC"): return "performs an AES encryption-round transformation on a 128-bit state using the supplied round key" + (" without MixColumns in the final-round form" if "LAST" in name else "")
    if name.startswith("AESDEC"): return "performs an AES decryption-round transformation on a 128-bit state using the supplied round key" + (" without inverse MixColumns in the final-round form" if "LAST" in name else "")
    if name == "AESIMC": return "applies the AES inverse MixColumns transformation to a round key"
    if name == "AESKEYGENASSIST": return "computes S-box, rotation, and round-constant helper values used in AES key expansion"
    if name.startswith("SHA1MSG"): return "computes part of the SHA-1 message schedule over packed 32-bit words"
    if name.startswith("SHA1NEXTE"): return "computes a SHA-1 E-state update used between grouped rounds"
    if name.startswith("SHA1RNDS4"): return "executes four SHA-1 compression rounds using a selected SHA-1 round function"
    if name.startswith("SHA256MSG"): return "computes part of the SHA-256 message schedule over packed 32-bit words"
    if name.startswith("SHA256RNDS2"): return "executes two SHA-256 compression rounds using packed state and message values"
    if "PCLMULQDQ" in name or "CLMUL" in name: return "performs carry-less multiplication of selected binary-polynomial operands for CRC and finite-field arithmetic"
    if "GF2P8MULB" in name: return "multiplies packed bytes in GF(2^8) using the instruction-defined reduction polynomial"
    if "GF2P8AFFINEINVQB" in name: return "applies a packed GF(2^8) multiplicative inverse followed by an affine transformation"
    if "GF2P8AFFINEQB" in name: return "applies a packed affine transformation over GF(2^8) to bytes"
    return None


def amx_semantics(name):
    if name == "LDTILECFG": return "loads AMX tile configuration from memory, defining tile dimensions and palette"
    if name == "STTILECFG": return "stores the current AMX tile configuration to memory"
    if name == "TILERELEASE": return "releases AMX tile state so the processor may reclaim tile resources"
    if name.startswith("TILELOAD"): return "loads a two-dimensional AMX tile from strided memory according to the active tile configuration"
    if name.startswith("TILESTORE"): return "stores a two-dimensional AMX tile to strided memory according to the active tile configuration"
    if name.startswith("TILEZERO"): return "fills an AMX tile register with zeros within its configured active dimensions"
    if name.startswith("TDP"): return "performs an AMX tile dot-product accumulation, multiplying source tile elements and accumulating widened products into the destination tile"
    if name.startswith("TCMM"): return "performs an AMX complex matrix multiply-accumulate over tile data"
    if name.startswith("TCVTROW"): return "converts an AMX tile row between the floating-point formats encoded by the mnemonic"
    return None


def general_semantics(name, rows):
    if name in SPECIAL: return SPECIAL[name], False
    s = condition_semantics(name)
    if s: return s, False
    s = string_semantics(name)
    if s: return s, False
    exts = set(clean_extensions(rows))
    if "X87" in exts or name.startswith("F"):
        s = x87_semantics(name)
        if s: return s, False
    s = crypto_semantics(name)
    if s: return s, False
    if any("AMX" in e or "TILE" in e for e in exts) or name.startswith(("TILE", "TDP", "TCMM", "TCVTROW", "LDTILE", "STTILE")):
        s = amx_semantics(name)
        if s: return s, False
    if name.endswith("_LOCK"):
        base, _ = general_semantics(name[:-5], rows)
        return base + "; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form", False
    if name.startswith("REP_") and name[4:].startswith(("XCRYPT", "XSHA", "XSTORE", "MONTMUL")):
        return "repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count", False

    integer = {
        "ADD": "adds the source to the destination and writes the sum while updating arithmetic flags", "ADC": "adds the source and incoming carry flag to the destination, enabling multiword addition",
        "ADCX": "adds unsigned operands using the carry flag as a carry chain while leaving overflow available for a second chain", "ADOX": "adds unsigned operands using the overflow flag as a carry chain",
        "SUB": "subtracts the source from the destination and writes the difference while updating arithmetic flags", "SBB": "subtracts the source and incoming borrow from the destination",
        "CMP": "subtracts conceptually to set arithmetic flags for a comparison and discards the numerical result", "TEST": "computes a bitwise AND only to set logical flags and discards the result",
        "AND": "computes bitwise AND", "OR": "computes bitwise inclusive OR", "XOR": "computes bitwise exclusive OR", "NOT": "inverts every destination bit without changing arithmetic flags",
        "NEG": "forms the two's-complement negation of its operand", "INC": "increments its destination by one while preserving carry", "DEC": "decrements its destination by one while preserving carry",
        "MUL": "performs unsigned widening multiplication using the accumulator implicitly", "IMUL": "performs signed integer multiplication in widening or truncated explicit-destination forms",
        "DIV": "performs unsigned division of the implicit double-width dividend, producing quotient and remainder", "IDIV": "performs signed division of the implicit double-width dividend, producing quotient and remainder",
        "MULX": "performs unsigned widening multiplication with separate low/high destinations without modifying arithmetic flags", "BSWAP": "reverses the byte order within a general-purpose register",
        "MOV": "copies a value from source to destination without arithmetic", "MOVSX": "copies a smaller signed integer and sign-extends it", "MOVSXD": "sign-extends a 32-bit integer to 64 bits",
        "MOVZX": "copies a smaller integer and zero-extends it", "MOVBE": "loads or stores an integer while reversing byte order",
        "XCHG": "exchanges two operands; a memory form has implicit atomic exchange semantics", "XADD": "exchanges an addend with the old destination while storing their sum",
        "CMPXCHG": "compares the accumulator with a destination and conditionally replaces the destination with a source", "CMPXCHG8B": "atomically compares and conditionally replaces a 64-bit memory value",
        "CMPXCHG16B": "atomically compares and conditionally replaces a 128-bit memory value", "BT": "copies a selected bit into carry", "BTS": "copies a selected bit into carry and sets it",
        "BTR": "copies a selected bit into carry and clears it", "BTC": "copies a selected bit into carry and complements it", "BSF": "finds the least-significant set bit index",
        "BSR": "finds the most-significant set bit index", "LZCNT": "counts leading zero bits", "TZCNT": "counts trailing zero bits", "POPCNT": "counts set bits",
        "PDEP": "deposits low source bits into positions selected by a mask", "PEXT": "extracts mask-selected bits and packs them into low destination bits", "BEXTR": "extracts a contiguous variable bit field",
        "BZHI": "copies source bits below a variable bit index and clears higher bits", "BLSI": "isolates the lowest set bit", "BLSR": "clears the lowest set bit", "BLSMSK": "makes a mask through the lowest set bit",
        "ANDN": "ANDs the complemented first source with the second", "RORX": "rotates right without modifying flags", "SHLX": "shifts left without modifying flags", "SHRX": "logically shifts right without modifying flags",
        "SARX": "arithmetically shifts right without modifying flags", "CRC32": "updates a CRC-32C checksum accumulator using the Castagnoli polynomial",
    }
    if name in integer: return integer[name], False
    if name in ("SHL", "SAL"): return "shifts the destination left, filling low bits with zero and updating shift-related flags", False
    if name == "SHR": return "shifts the destination logically right, filling high bits with zero", False
    if name == "SAR": return "shifts the destination arithmetically right, replicating the sign bit", False
    if name in ("SHLD", "SHRD"): return "performs a double-width logical shift, pulling replacement bits from a second source", False
    if name in ("ROL", "ROR", "RCL", "RCR"): return "rotates destination bits, optionally through carry, by the requested count", False
    if name in ("JMP", "JMPABS", "JMP_FAR"): return "unconditionally transfers control to the encoded direct, indirect, absolute, or far target without saving a normal return address", False
    if name in ("JCXZ", "JECXZ", "JRCXZ"): return "branches to a short target when the mode-specific count register is zero", False
    if name in ("LOOP", "LOOPE", "LOOPNE"): return "decrements the count register and conditionally branches according to the remaining count and, for the E/NE forms, the zero flag", False
    ext_helpers = {"CBW": "sign-extends AL into AX", "CWDE": "sign-extends AX into EAX", "CDQE": "sign-extends EAX into RAX", "CWD": "sign-extends AX into DX:AX", "CDQ": "sign-extends EAX into EDX:EAX", "CQO": "sign-extends RAX into RDX:RAX"}
    if name in ext_helpers: return ext_helpers[name], False

    original = name
    vector = name.startswith("V") and len(name) > 1
    stripped = name[1:] if vector else name
    kind = element_kind(stripped)
    if stripped.startswith(("FMADD", "FMSUB", "FNMADD", "FNMSUB")) or re.match(r"FM?(ADD|SUB)", stripped):
        return f"computes a fused multiply/add-or-subtract operation on {kind} with one rounding step for each fused result", False
    simdish = vector or stripped.startswith("P") or any(x in " ".join(exts) for x in ("SSE", "AVX", "MMX", "XOP", "3DNOW"))
    if simdish:
        for token, phrase in (("ADD", "adds corresponding"), ("SUB", "subtracts corresponding"), ("MUL", "multiplies corresponding"), ("DIV", "divides corresponding"), ("MAX", "selects maxima of corresponding"), ("MIN", "selects minima of corresponding"), ("ABS", "takes absolute values of"), ("AVG", "computes rounded averages of corresponding"), ("ANDN", "ANDs a complemented source with another over"), ("AND", "computes bitwise AND over"), ("XOR", "computes bitwise XOR over"), ("OR", "computes bitwise OR over")):
            if token in stripped: return f"{phrase} {kind} and writes the lane-wise result", False
        if "SQRT" in stripped: return f"computes square roots of {kind}", False
        if "RSQRT" in stripped: return f"computes approximate reciprocal square roots of {kind}", False
        if "RCP" in stripped: return f"computes approximate reciprocals of {kind}", False
        if "BLEND" in stripped: return f"selects {kind} from two sources under an immediate or mask control", False
        if "SHUF" in stripped or "PERM" in stripped: return f"reorders {kind} according to an immediate, index vector, or fixed permutation", False
        if "UNPCK" in stripped: return f"interleaves high or low portions of source vectors containing {kind}", False
        if "PACK" in stripped: return "narrows and packs source elements using the saturation behavior encoded by the mnemonic", False
        if "BROADCAST" in stripped: return f"replicates a scalar or smaller source value across destination lanes as {kind}", False
        if "GATHER" in stripped: return f"loads non-contiguous memory elements selected by vector indices into {kind} lanes", False
        if "SCATTER" in stripped: return f"stores {kind} lanes to non-contiguous addresses selected by vector indices", False
        if "COMPRESS" in stripped: return f"packs mask-selected active {kind} contiguously into low lanes or memory", False
        if "EXPAND" in stripped: return f"expands contiguous source data into mask-selected positions for {kind}", False
        if "INSERT" in stripped: return f"inserts a scalar or subvector into selected positions of a destination containing {kind}", False
        if "EXTRACT" in stripped: return f"extracts a selected scalar or subvector from packed {kind}", False
        if "MOV" in stripped:
            if "MSK" in stripped: return "extracts vector sign bits and packs them into an integer mask", False
            if "NT" in stripped: return f"moves {kind} using non-temporal memory semantics intended for streaming data", False
            return f"copies {kind} between the register and memory forms allowed by its alignment and masking rules", False
        if "CMP" in stripped: return f"compares corresponding {kind} under the encoded predicate and produces mask or Boolean lane results", False
        if "TEST" in stripped: return "tests vector bits or lanes and reduces the selected result into flags or mask state", False
        if "CVT" in stripped: return "converts values between the source and destination numerical formats encoded by the mnemonic", False
        if "DOT" in stripped or "DP" in stripped: return "forms products of selected source elements and accumulates grouped dot-product sums", False
        if "SAD" in stripped: return "computes grouped sums of absolute differences between source elements", False
        if "MADD" in stripped: return "multiplies adjacent source elements and adds grouped products into wider destinations", False

    if "CVT" in original: return "converts numerical values between the source and destination integer or floating-point formats encoded by the mnemonic", False
    if original.startswith("K") and len(original) > 2:
        if "MOV" in original: return "moves data between AVX-512 mask registers and permitted general-purpose or memory operands", False
        if "TEST" in original: return "tests combinations of AVX-512 mask bits and reduces the result into integer flags", False
        if "SHIFT" in original: return "shifts bits of an AVX-512 mask register by an immediate count", False
        for token, op in (("ANDN", "AND of a complemented source with another"), ("AND", "bitwise AND"), ("XNOR", "bitwise XNOR"), ("XOR", "bitwise XOR"), ("OR", "bitwise OR"), ("NOT", "bitwise complement"), ("ADD", "modular addition")):
            if token in original: return f"computes {op} on AVX-512 mask-register bits", False
    if original.startswith("PREFETCH"): return "issues a prefetch hint for the addressed cache line with the locality or exclusivity preference encoded by the mnemonic", False
    if original.startswith("MOVDIR64B"): return "performs a 64-byte direct store using the architecture's direct-write semantics", False
    if original.startswith("MOVDIRI"): return "performs a direct store from a general-purpose register to memory", False
    if original.startswith("ENQCMD"): return "submits a 64-byte command descriptor to a device portal and reports acceptance or retry status", False
    if original.startswith(("BLC", "BLS", "T1MSK")): return "computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit", False
    if "INSERT" in original: return "inserts a selected scalar field or subvector into a packed destination", False
    if "EXTRACT" in original or original.startswith("PEXTR"): return "extracts a selected scalar field or packed element into a register or memory destination", False
    if "SHUF" in original or "PERM" in original: return "reorders packed elements according to an immediate, index vector, or fixed permutation", False
    if "BLEND" in original: return "combines packed elements from two sources under an immediate or mask selector", False
    if original.startswith("VM"):
        if "READ" in original: return "reads a field from the current virtual-machine control structure", False
        if "WRITE" in original: return "writes a field in the current virtual-machine control structure", False
        if "LAUNCH" in original: return "enters a guest from a not-yet-launched VM control structure", False
        if "RESUME" in original: return "re-enters a previously launched virtual machine", False
        if "CALL" in original: return "transfers from guest context to a hypervisor-defined service through the architecture's virtualization call mechanism", False
        if "LOAD" in original: return "loads virtualization control or guest-state information", False
        if "SAVE" in original: return "saves virtualization guest or host state", False
    if original.startswith("INV"): return "invalidates processor-maintained translation or virtualization-caching state selected by its operands", False

    for token, desc in (("LOAD", "loads data or architectural state from its encoded source"), ("STORE", "stores data or architectural state to its encoded destination"), ("MOV", "moves or copies data between its permitted operand classes"), ("SAVE", "saves the architectural state selected by the instruction"), ("RESTOR", "restores architectural state from its defined source"), ("READ", "reads the architectural state or device value selected by its operands"), ("WRITE", "writes the architectural state or device value selected by its operands"), ("ADD", f"adds values in the operand format encoded by the mnemonic ({kind})"), ("SUB", f"subtracts values in the operand format encoded by the mnemonic ({kind})"), ("MUL", f"multiplies values in the operand format encoded by the mnemonic ({kind})"), ("DIV", f"divides values in the operand format encoded by the mnemonic ({kind})"), ("CMP", "compares its encoded operands and records the result through flags or mask state"), ("TEST", "tests its encoded operands and records the Boolean result through flags or mask state"), ("AND", "computes a bitwise conjunction over its operands"), ("XOR", "computes a bitwise exclusive-or over its operands"), ("OR", "computes a bitwise inclusive-or over its operands"), ("SHIFT", "shifts the encoded operand or mask"), ("ROT", "rotates encoded bit fields"), ("ZERO", "writes zero values to the selected destination")):
        if token in original: return desc, True
    return f"implements the distinct architectural operation named {original} in XED category {', '.join(clean_categories(rows))}; the pinned Intel/AMD reference defines its exact data transformation", True


def mode_summary(rows):
    values = sorted({r.get("mode_restriction", "").strip() for r in rows if r.get("mode_restriction", "").strip()})
    return "no single extra XED mode restriction is common to all forms" if not values else "XED mode restriction(s): " + ", ".join(f"`{x}`" for x in values)


def cpl_summary(rows):
    values = sorted({r.get("cpl", "").strip() for r in rows if r.get("cpl", "").strip()})
    if values == ["3"]: return "usable at CPL 3 subject to feature and OS enablement"
    if values == ["0"]: return "requires CPL 0; ordinary user-mode code must not emit it"
    return "CPL value(s): " + (", ".join(f"`{x}`" for x in values) if values else "not uniformly recorded")


def preview_values(rows, key, limit=3):
    values = sorted({r.get(key, "").strip() for r in rows if r.get(key, "").strip()})
    if not values: return "not uniformly recorded"
    s = "; ".join(f"`{x}`" for x in values[:limit])
    return s + ("; …" if len(values) > limit else "")


def backend_paragraph(iclass, rows):
    exts = " ".join(clean_extensions(rows)).upper()
    cats = " ".join(clean_categories(rows)).upper()
    cpls = {r.get("cpl", "").strip() for r in rows}
    if cpls == {"0"} or any(x in cats for x in ("SYSTEM", "VTX", "SVM")):
        return "For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary."
    if any(x in exts for x in ("AVX512", "AVX10", "AMX", "APX")):
        return "For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle."
    if any(x in exts for x in ("AVX", "SSE", "FMA", "BMI", "XOP", "3DNOW", "MMX")):
        return "For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability."
    if any(x in cats for x in ("COND_BR", "UNCOND_BR", "CALL", "RET")) or iclass.startswith(("J", "CALL", "RET", "LOOP")):
        return "For Idriç this is directly relevant to control-flow lowering. Selection must preserve branch/call semantics while making relocation form, indirect-target behavior, prediction, and ABI effects explicit."
    if iclass in {"MOV", "LEA", "ADD", "SUB", "CMP", "TEST", "AND", "OR", "XOR", "SHL", "SHR", "SAR", "IMUL", "PUSH", "POP"}:
        return "For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit."
    return "For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence."


def page(iclass, rows, pins):
    desc, fallback = general_semantics(iclass, rows)
    extensions = clean_extensions(rows)
    categories = clean_categories(rows)
    vendors = sorted({r.get("vendor", "").strip() or "shared-or-unspecified" for r in rows})
    isa_sets = sorted({r.get("isa_set", "").strip() for r in rows if r.get("isa_set", "").strip()})
    forms = sorted({(r.get("iform", "").strip(), r.get("disasm_intel", "").strip()) for r in rows})
    form_lines = []
    for iform, dis in forms[:12]:
        label = f"`{iform or '(IFORM not supplied)'}`"
        if dis: label += f" — `{dis}`"
        form_lines.append(f"- {label}")
    if len(forms) > 12: form_lines.append(f"- … {len(forms)-12} additional concrete forms in `generated/xed-instructions.tsv`")
    xed = pins.get("intel_xed", {})
    sdm = pins.get("intel_sdm", {})
    prose = f"`{iclass}` {desc}. The pinned XED inventory represents it with {len(rows)} normalized encoding record{'s' if len(rows) != 1 else ''} and {len(forms)} distinct IFORM/disassembly combination{'s' if len(forms) != 1 else ''}. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation."
    return "\n".join([
        f"# {iclass}", "", prose, "",
        "## Family and availability", "",
        f"- XED extension(s): {', '.join(f'`{x}`' for x in extensions)}",
        f"- XED category/categories: {', '.join(f'`{x}`' for x in categories)}",
        f"- ISA set(s): {', '.join(f'`{x}`' for x in isa_sets) if isa_sets else '`not normalized`'}",
        f"- vendor classification: {', '.join(f'`{x}`' for x in vendors)}",
        f"- {mode_summary(rows)}", f"- {cpl_summary(rows)}", "",
        "## Architectural effects", "",
        f"Representative explicit operands: {preview_values(rows, 'explicit_operands')}. Representative implicit state: {preview_values(rows, 'implicit_operands')}.", "",
        f"Recorded flag behavior: {preview_values(rows, 'flags')}.", "",
        "## Important forms", "", *form_lines, "",
        "The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.", "",
        "## Backend notes", "", backend_paragraph(iclass, rows), "",
        "## Sources", "",
        f"- Intel XED `{xed.get('release', 'unknown')}` / commit `{xed.get('commit', 'unknown')}` — machine-readable ICLASS/IFORM and encoding metadata.",
        f"- Intel 64 and IA-32 SDM revision `{sdm.get('revision', 'unknown')}` — architectural semantics.",
        "- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.", ""
    ]), fallback


def build(inventory, iclasses_path, out_dir, pins_path):
    with inventory.open(newline="") as f: rows = list(csv.DictReader(f, delimiter="\t"))
    groups = defaultdict(list)
    for r in rows:
        if r.get("iclass"): groups[r["iclass"]].append(r)
    expected = [x.strip() for x in iclasses_path.read_text().splitlines() if x.strip()]
    if set(expected) != set(groups):
        raise SystemExit(f"ICLASS mismatch: missing={sorted(set(expected)-set(groups))[:20]} extra={sorted(set(groups)-set(expected))[:20]}")
    pins = json.loads(pins_path.read_text())
    pages, fallbacks = {}, []
    for iclass in sorted(expected):
        text, fallback = page(iclass, groups[iclass], pins)
        pages[f"{iclass}.md"] = text
        if fallback: fallbacks.append(iclass)
    pages["README.md"] = "\n".join(["# x86 instruction reference", "", f"This directory contains one generated Markdown page for each of the **{len(expected):,}** XED ICLASS values in the pinned inventory.", "", "The pages are mnemonic-level documentation. Concrete encodings remain in `../../generated/xed-instructions.tsv`; backend support is a separate decision.", "", "Regenerate with `python3 scripts/generate-instruction-docs.py` and verify with `python3 scripts/generate-instruction-docs.py --check`.", ""])
    return pages, fallbacks


def write_pages(out_dir, pages):
    out_dir.mkdir(parents=True, exist_ok=True)
    for p in out_dir.glob("*.md"): p.unlink()
    for name, text in pages.items(): (out_dir / name).write_text(text)


def check_pages(out_dir, pages):
    expected, actual = set(pages), {p.name for p in out_dir.glob("*.md")}
    if expected != actual:
        print("instruction-document filename set differs", file=sys.stderr); print("missing:", sorted(expected-actual)[:50], file=sys.stderr); print("extra:", sorted(actual-expected)[:50], file=sys.stderr); return False
    bad = [name for name, text in pages.items() if (out_dir / name).read_text() != text]
    if bad: print("instruction-document contents differ:", ", ".join(bad[:50]), file=sys.stderr); return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", type=Path, default=Path("generated/xed-instructions.tsv"))
    ap.add_argument("--iclasses", type=Path, default=Path("generated/xed-iclasses.txt"))
    ap.add_argument("--out-dir", type=Path, default=Path("docs/instructions"))
    ap.add_argument("--pins", type=Path, default=Path("research/source-pins.json"))
    ap.add_argument("--fallbacks", type=Path, default=Path("generated/instruction-doc-fallbacks.txt"))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    pages, fallbacks = build(args.inventory, args.iclasses, args.out_dir, args.pins)
    fallback_text = "\n".join(fallbacks) + ("\n" if fallbacks else "")
    if args.check:
        ok = check_pages(args.out_dir, pages)
        ok = ok and ((args.fallbacks.read_text() == fallback_text) if args.fallbacks.exists() else not fallbacks)
        if not ok: raise SystemExit(1)
        print(f"checked {len(pages)-1} instruction pages; semantic fallbacks: {len(fallbacks)}")
        return
    write_pages(args.out_dir, pages)
    args.fallbacks.write_text(fallback_text)
    print(f"generated {len(pages)-1} instruction pages; semantic fallbacks: {len(fallbacks)}")


if __name__ == "__main__":
    main()
