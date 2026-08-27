#!/usr/bin/env python3
"""Strengthen semantic prose for instruction families not covered by the base generator.

This wrapper deliberately keeps coverage generation in generate-instruction-docs.py
but replaces its weak fallback path with reviewed family rules.  Any ICLASS still
not understood remains in generated/instruction-doc-fallbacks.txt, making semantic
coverage auditable instead of silently inventing prose.
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("instruction_docs_base", HERE / "generate-instruction-docs.py")
base = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(base)
base_general_semantics = base.general_semantics

EXACT = {
    # APX / RAO-INT and recent architectural additions.
    "AADD": "atomically adds a register value to a memory operand without using the LOCK prefix spelling, implementing the RAO-INT atomic-add operation",
    "AAND": "atomically ANDs a register value into a memory operand, implementing the RAO-INT atomic-AND operation",
    "AOR": "atomically ORs a register value into a memory operand, implementing the RAO-INT atomic-OR operation",
    "AXOR": "atomically XORs a register value into a memory operand, implementing the RAO-INT atomic-XOR operation",
    "BEXTR_XOP": "extracts a variable contiguous bit field using AMD XOP's BEXTR encoding, with the start position and field length supplied by the control operand",
    "IBHF": "forms an indirect-branch-history fence, preventing older branch history from influencing selected later indirect-branch predictions when the processor's BHI controls enable that behavior",
    "HRESET": "resets processor history components selected by a bitmap in EAX, giving privileged software an architectural way to discard selected hardware-history state",
    "UDB": "is the permanently undefined one-byte instruction in 64-bit mode and therefore raises the invalid-opcode exception there",
    "LKGS": "loads the kernel GS-base state used by FRED-compatible operating systems without performing a full SWAPGS-style exchange",

    # MPX bounds operations.
    "BNDCL": "checks a pointer against the lower bound in a bound register and raises the MPX bounds exception when the pointer is below that bound",
    "BNDCN": "checks a pointer against the one's-complement upper bound held by an MPX bound register and raises the bounds exception when it exceeds the represented upper limit",
    "BNDCU": "checks a pointer against the upper bound represented by an MPX bound register and raises the bounds exception when it is above that bound",
    "BNDLDX": "loads MPX bounds metadata for a pointer from the bounds-directory/bounds-table structures associated with the current address space",
    "BNDMK": "constructs an MPX lower/upper bound pair from an effective address and a bound-size expression and writes it to a bound register",
    "BNDMOV": "copies an MPX bound pair between bound registers and memory without performing a bounds check",
    "BNDSTX": "stores MPX bounds metadata for a pointer into the bounds-table structures associated with the current address space",

    # ACE v1 block-scale and tile movement.
    "BSRINIT": "initializes the ACE block-scale register so every scale byte encodes a multiplicative scale factor of 1.0",
    "BSRMOVF": "loads the full 1024-bit ACE block-scale register from two 512-bit source halves",
    "BSRMOVH": "moves the high half of the ACE block-scale register between the block-scale state and a vector source or destination as defined by its form",
    "BSRMOVL": "moves the low half of the ACE block-scale register between the block-scale state and a vector source or destination as defined by its form",
    "TILEMOVCOL": "moves a selected column of ACE tile data into the instruction's vector destination so column-oriented tile data can be consumed outside the tile register file",
    "TILEMOVROW": "moves a selected row of ACE tile data into the instruction's vector destination so row-oriented tile data can be consumed outside the tile register file",

    # Legacy decimal and odd historical instructions.
    "DAA": "adjusts AL after addition so the low and high nibbles represent a valid packed-BCD result, updating legacy arithmetic flags",
    "DAS": "adjusts AL after subtraction so the low and high nibbles represent a valid packed-BCD result, updating legacy arithmetic flags",
    "SALC": "sets AL to all ones when carry is set and to zero when carry is clear; it is a historical undocumented instruction on processors that implement it",
    "XLAT": "uses the unsigned byte in AL as an index from the implicit table base register, loads that table byte, and replaces AL with the result",

    # x87 data, state, and transcendental operations missed by the compact base rules.
    "FBLD": "loads an 80-bit packed-BCD integer from memory, converts it to x87 extended precision, and pushes the result on the x87 stack",
    "FBSTP": "converts ST(0) to an 80-bit packed-BCD integer in memory and pops the x87 stack",
    "FDECSTP": "decrements the x87 TOP stack-pointer field modulo eight without moving register contents",
    "FINCSTP": "increments the x87 TOP stack-pointer field modulo eight without moving register contents",
    "FDISI8087_NOP": "uses an encoding that disabled x87 interrupt reporting on the 8087 but is architecturally treated as a no-operation on later x87 implementations",
    "FENI8087_NOP": "uses an encoding that enabled x87 interrupt reporting on the 8087 but is architecturally treated as a no-operation on later x87 implementations",
    "FEMMS": "performs AMD's faster MMX-state exit operation, marking the shared MMX/x87 register state available for x87 use",
    "FICOM": "compares ST(0) with a signed integer memory operand and records the result in the x87 condition-code state",
    "FICOMP": "compares ST(0) with a signed integer memory operand, records x87 condition codes, and pops ST(0)",
    "FIDIV": "divides ST(0) by a signed integer memory operand using x87 floating-point arithmetic",
    "FIDIVR": "divides a signed integer memory operand by ST(0) using x87 floating-point arithmetic",
    "FISUB": "subtracts a signed integer memory operand from ST(0) using x87 floating-point arithmetic",
    "FISUBR": "subtracts ST(0) from a signed integer memory operand and leaves the x87 floating-point result in ST(0)",
    "FNCLEX": "clears pending x87 exception flags and busy state without first performing the implicit wait used by the waiting form",
    "FNINIT": "resets the x87 control, status, tag, pointer, and opcode state to its initialization values without first waiting for pending exceptions",
    "FNSAVE": "stores the x87 environment and register stack to memory, then reinitializes x87 state, without first waiting for pending exceptions",
    "FNSTCW": "stores the x87 control word to memory without first waiting for pending x87 exceptions",
    "FNSTENV": "stores the x87 environment to memory without first waiting for pending x87 exceptions",
    "FNSTSW": "stores the x87 status word to memory or AX without first waiting for pending x87 exceptions",
    "FPREM": "performs an iterative partial remainder of ST(0) by ST(1), using truncation-style quotient selection and reporting whether further reduction is required",
    "FPREM1": "performs an iterative IEEE-style partial remainder of ST(0) by ST(1), using nearest-integer quotient selection and reporting whether further reduction is required",
    "FPTAN": "computes the tangent of ST(0), leaves the tangent in the x87 stack, and pushes 1.0 as required by the historical x87 result convention",
    "FRSTOR": "restores the x87 environment and register-stack contents from an FSAVE-format memory image",
    "FSETPM287_NOP": "uses the 80287 protected-mode setup encoding, which later x87 processors retain as a no-operation",

    # Segment/protection machinery.
    "LAR": "loads access-rights information from a visible segment descriptor into a general-purpose register when privilege and descriptor checks succeed",
    "LDS": "loads an offset and an accompanying selector from memory, placing the selector in DS and the offset in a general-purpose register",
    "LES": "loads an offset and an accompanying selector from memory, placing the selector in ES and the offset in a general-purpose register",
    "LFS": "loads an offset and an accompanying selector from memory, placing the selector in FS and the offset in a general-purpose register",
    "LGS": "loads an offset and an accompanying selector from memory, placing the selector in GS and the offset in a general-purpose register",
    "LSS": "loads an offset and an accompanying selector from memory, placing the selector in SS and the offset in a general-purpose register with the instruction's stack-segment ordering semantics",
    "LSL": "loads a segment or system descriptor's effective limit into a general-purpose register when descriptor and privilege checks succeed",
    "VERR": "tests whether the segment selected by its operand is readable at the current privilege level and reports the result in ZF",
    "VERW": "tests whether the segment selected by its operand is writable at the current privilege level and reports the result in ZF",

    # Interrupt, control, and system state.
    "CLGI": "clears AMD SVM's global-interrupt flag, blocking interrupt delivery governed by that virtualization state until it is set again",
    "STGI": "sets AMD SVM's global-interrupt flag, permitting interrupt delivery governed by that virtualization state",
    "CLTS": "clears CR0.TS so x87/SIMD state can be used without triggering the device-not-available exception used by lazy context switching",
    "CLZERO": "zeros the cache line containing the addressed byte using AMD's cache-line-zero operation",
    "RSM": "returns from System Management Mode by restoring processor state from the SMRAM save-state area",
    "WBNOINVD": "writes modified cache lines back toward memory without invalidating the caches, providing a whole-cache writeback operation distinct from WBINVD",

    # User interrupts.
    "CLUI": "clears the user-interrupt flag so maskable user interrupts are not delivered in the current user-interrupt context",
    "STUI": "sets the user-interrupt flag so eligible user interrupts may be delivered after the architecture's defined enabling boundary",
    "TESTUI": "copies the current user-interrupt enable state into the zero flag so software can test whether user interrupts are enabled",
    "SENDUIPI": "sends a user interprocessor interrupt to the target selected through the user-interrupt target table",
    "UIRET": "returns from a user-interrupt handler by restoring the user-interrupt return state established on delivery",

    # FRED.
    "ERETS": "returns from a FRED-delivered event while remaining in supervisor context, restoring the saved event-return state without a privilege transition",
    "ERETU": "returns from a FRED-delivered event to user context, restoring the saved user return state and performing the FRED privilege transition",

    # Intel SGX / Key Locker / platform configuration.
    "ENCLS": "dispatches a privileged Intel SGX enclave-management leaf selected in EAX, with the other implicit registers interpreted according to that leaf",
    "ENCLU": "dispatches an unprivileged Intel SGX enclave leaf selected in EAX, including enclave entry, exit, acceptance, and related operations",
    "ENCLV": "dispatches a virtualization-oriented Intel SGX leaf selected in EAX for enclave-management operations exposed to a VMM",
    "ENCODEKEY128": "encodes a 128-bit AES key under Intel Key Locker's internal wrapping key and writes the resulting key handle",
    "ENCODEKEY256": "encodes a 256-bit AES key under Intel Key Locker's internal wrapping key and writes the resulting key handle",
    "LOADIWKEY": "loads the internal wrapping key used by Intel Key Locker to create and consume encoded AES key handles",
    "PBNDKB": "binds a platform key to a binary large object using the platform's key-binding mechanism and returns the architecture-defined result state",
    "PCONFIG": "invokes a platform-configuration leaf selected by registers, providing a privileged architectural entry point for configuration operations such as key programming",

    # AMD SEV/SNP and lightweight profiling.
    "PVALIDATE": "validates or rescinds validation of an AMD SEV-SNP guest page's reverse-map-table entry and returns status through EAX and flags",
    "PSMASH": "splits an AMD SEV-SNP 2 MiB reverse-map-table entry into the corresponding set of 4 KiB entries",
    "RMPADJUST": "changes AMD SEV-SNP reverse-map-table permissions for a guest page, including VMPL-targeted permissions selected by register state",
    "RMPUPDATE": "writes a new AMD SEV-SNP reverse-map-table entry for the selected system physical page using state supplied by privileged software",
    "LLWPCB": "loads AMD Lightweight Profiling configuration from the Lightweight Profiling Control Block addressed by its operand",
    "SLWPCB": "stores or exposes the current AMD Lightweight Profiling Control Block address according to the LWP architectural interface",
    "LWPINS": "records an AMD Lightweight Profiling instrumentation event using the LWP control state and operands",
    "LWPVAL": "records an AMD Lightweight Profiling value event using the LWP control state and operands",
    "RDPRU": "reads an AMD processor register selected by ECX into EDX:EAX when the selected register is permitted to software at the current privilege level",
    "SKINIT": "enters AMD Secure Startup by measuring and launching the secure loader identified by the instruction's implicit state",

    # CET shadow stack.
    "CLRSSBSY": "clears the busy bit in a shadow-stack restore token so that the corresponding CET shadow stack is no longer marked busy",
    "RDSSPD": "reads the current shadow-stack pointer into a 32-bit general-purpose destination",
    "RDSSPQ": "reads the current shadow-stack pointer into a 64-bit general-purpose destination",
    "RSTORSSP": "restores the CET shadow-stack pointer from a restore token in memory and updates the token state required by shadow-stack switching",
    "SAVEPREVSSP": "writes a restore token for the previous CET shadow-stack pointer after a shadow-stack switch",
    "SETSSBSY": "sets the busy state associated with a supervisor shadow stack so CET can track exclusive active use",
    "WRSSD": "writes a 32-bit value to shadow-stack memory through CET's explicit shadow-stack store mechanism",
    "WRSSQ": "writes a 64-bit value to shadow-stack memory through CET's explicit shadow-stack store mechanism",
    "WRUSSD": "writes a 32-bit value to a user shadow stack from privileged software using CET's explicit user-shadow-stack store mechanism",
    "WRUSSQ": "writes a 64-bit value to a user shadow stack from privileged software using CET's explicit user-shadow-stack store mechanism",

    # TDX / SEAM.
    "SEAMCALL": "transfers from legacy VMX-root operation into SEAM VMX-root operation to invoke a SEAM-module service",
    "SEAMOPS": "invokes a SEAM-specific operation while software is executing in SEAM root operation",
    "SEAMRET": "returns from SEAM VMX-root operation to the calling legacy VMX-root environment",
    "TDCALL": "causes a Trust Domain guest to exit to the SEAM module so it can request a TDX service",

    # Transactional memory and load-address tracking.
    "XABORT": "explicitly aborts the current RTM transaction and records the immediate abort code in the transactional status returned to the fallback path",
    "XBEGIN": "starts a Restricted Transactional Memory region and encodes the relative fallback target to receive control if the transaction aborts",
    "XEND": "attempts to commit the current RTM transaction, making its speculative memory updates architecturally visible atomically if commit succeeds",
    "XTEST": "sets ZF according to whether execution is currently inside a transactional region",
    "XRESLDTRK": "resumes transactional load-address tracking after a matching suspend operation in the TSX load-address-tracking facility",
    "XSUSLDTRK": "suspends transactional load-address tracking while leaving the surrounding RTM transaction active",

    # Tracing, memory and MSR helpers.
    "PTWRITE": "writes a software-supplied payload into Intel Processor Trace when PTWRITE tracing is enabled, allowing software events to appear in the trace stream",
    "RDMSRLIST": "reads a hardware-defined list of model-specific registers using the MSR-list interface and stores their values in the associated list structure",
    "WRMSRLIST": "writes a hardware-defined list of model-specific registers using the MSR-list interface",
    "WRMSRNS": "writes the model-specific register selected by ECX using the non-serializing WRMSR variant",
    "URDMSR": "reads an operating-system-authorized user-mode MSR through the user-MSR facility without granting arbitrary RDMSR privilege",
    "UWRMSR": "writes an operating-system-authorized user-mode MSR through the user-MSR facility without granting arbitrary WRMSR privilege",
    "MCOMMIT": "orders AMD persistent-memory writes so prior stores covered by the instruction's persistence rules are committed toward the persistence domain before later dependent software proceeds",
    "MOVRS": "loads data with the MOVRS read-shared semantic hint, allowing coherent shared-data reads to avoid unnecessarily requesting exclusive ownership",

    # MXCSR and vector-state save variants.
    "LDMXCSR": "loads the SSE/AVX floating-point control and status register MXCSR from a 32-bit memory image",
    "STMXCSR": "stores the SSE/AVX floating-point control and status register MXCSR to a 32-bit memory destination",
    "VLDMXCSR": "loads MXCSR through the VEX-encoded form of the floating-point control-state load",
    "VSTMXCSR": "stores MXCSR through the VEX-encoded form of the floating-point control-state store",
    "LDDQU": "loads 128 bits of unaligned integer data with the SSE3 load hint intended for cache-line-crossing streaming patterns",
    "VLDDQU": "loads unaligned vector integer data using the VEX-encoded LDDQU streaming-load form",

    # Packed alignment/insertion/sign/shift helpers.
    "PALIGNR": "concatenates two packed byte vectors, right-shifts the combined byte string by an immediate byte count, and returns the selected aligned window",
    "PSWAPD": "swaps the two 32-bit halves of an MMX register using AMD 3DNow! semantics",

    # Scalar rounding / compare helpers.
    "ROUNDSD": "rounds the low scalar double-precision floating-point element according to immediate rounding control while preserving the defined upper destination bits",
    "ROUNDSS": "rounds the low scalar single-precision floating-point element according to immediate rounding control while preserving the defined upper destination bits",
    "VROUNDSD": "rounds a scalar double-precision floating-point element according to immediate rounding control using the VEX-encoded three-operand form",
    "VROUNDSS": "rounds a scalar single-precision floating-point element according to immediate rounding control using the VEX-encoded three-operand form",

    # VIA PadLock.
    "XSTORE": "requests random bytes from VIA PadLock's hardware random-number generator and stores them through the instruction's implicit destination/count interface",
}

X87_FCMOV = {
    "B": "carry is set", "BE": "carry or zero is set", "E": "zero is set", "NB": "carry is clear",
    "NBE": "carry and zero are clear", "NE": "zero is clear", "NU": "parity is clear", "U": "parity is set",
}


def _condition_from_cmpxadd(name: str) -> str | None:
    m = re.fullmatch(r"CMP([A-Z]+)XADD", name)
    if not m:
        return None
    cc = m.group(1)
    aliases = {
        "BE": "unsigned below-or-equal", "B": "unsigned below", "LE": "signed less-or-equal", "L": "signed less-than",
        "NBE": "unsigned above", "NB": "unsigned above-or-equal", "NLE": "signed greater-than", "NL": "signed greater-or-equal",
        "NO": "no overflow", "NP": "no parity", "NS": "non-negative", "NZ": "nonzero",
        "O": "overflow", "P": "parity", "S": "negative", "Z": "zero/equal",
    }
    cond = aliases.get(cc)
    if not cond:
        return None
    return f"performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is {cond}"


def _fcmov(name: str) -> str | None:
    if not name.startswith("FCMOV"):
        return None
    cc = name[5:]
    cond = X87_FCMOV.get(cc)
    if cond:
        return f"copies an x87 source register into ST(0) only when the integer EFLAGS condition says {cond}, leaving ST(0) unchanged otherwise"
    return None


def _stack(name: str) -> str | None:
    d = {
        "PUSHA": "pushes the legacy set of 16-bit general-purpose registers in the architecturally defined order while preserving the original SP value in the saved image",
        "PUSHAD": "pushes the legacy set of 32-bit general-purpose registers in the architecturally defined order while preserving the original ESP value in the saved image",
        "POPA": "pops the legacy 16-bit general-purpose register set in the architecturally defined order while discarding the saved SP slot",
        "POPAD": "pops the legacy 32-bit general-purpose register set in the architecturally defined order while discarding the saved ESP slot",
        "PUSHF": "pushes the 16-bit FLAGS image onto the stack subject to privilege-defined masking of individual flag bits",
        "PUSHFD": "pushes the 32-bit EFLAGS image onto the stack subject to privilege-defined masking of individual flag bits",
        "PUSHFQ": "pushes the 64-bit RFLAGS image onto the stack, with reserved and privilege-controlled bits represented as defined by the architecture",
        "POPF": "pops a 16-bit FLAGS image from the stack and updates those flag bits the current privilege level is allowed to modify",
        "POPFD": "pops a 32-bit EFLAGS image from the stack and updates those flag bits the current privilege level is allowed to modify",
        "POPFQ": "pops a 64-bit RFLAGS image from the stack and updates those flag bits the current privilege level is allowed to modify",
        "PUSH2": "uses Intel APX to push two general-purpose register values with one instruction, updating RSP once for the combined stack allocation",
        "PUSH2P": "uses Intel APX's paired push form to save two general-purpose register values with the preserve-oriented semantics defined for the P-suffixed form",
        "POP2": "uses Intel APX to pop two general-purpose register values with one instruction and advances RSP by their combined stack size",
        "POP2P": "uses Intel APX's paired pop form to restore two general-purpose registers with the preserve-oriented semantics defined for the P-suffixed form",
        "PUSHP": "uses the Intel APX P-suffixed push encoding, including the extended-register and paired-stack forms provided by APX",
        "POPP": "uses the Intel APX P-suffixed pop encoding, including the extended-register and paired-stack forms provided by APX",
    }
    return d.get(name)


def _xsave(name: str) -> str | None:
    if name in {"FXSAVE64", "FXRSTOR64"}:
        return ("stores x87, MMX, SSE, and MXCSR state using the 64-bit FXSAVE pointer layout" if name == "FXSAVE64" else "restores x87, MMX, SSE, and MXCSR state using the 64-bit FXRSTOR pointer layout")
    if name.startswith("XSAVE"):
        flavor = "optimized" if "OPT" in name else "compacted" if "C" in name and "OPT" not in name else "supervisor-aware" if "S" in name and name.startswith("XSAVES") else "standard"
        layout = " with the 64-bit pointer-format variant" if name.endswith("64") else ""
        return f"saves the enabled extended processor-state components to an XSAVE area using the {flavor} XSAVE semantics{layout}"
    if name.startswith("XRSTOR"):
        flavor = "supervisor-aware" if name.startswith("XRSTORS") else "standard"
        layout = " with the 64-bit pointer-format variant" if name.endswith("64") else ""
        return f"restores selected extended processor-state components from an XSAVE-format memory area using the {flavor} restore semantics{layout}"
    return None


def _comi(name: str) -> str | None:
    n = name[1:] if name.startswith("V") else name
    unordered = n.startswith("UCOMI") or n.startswith("UCOMX")
    ordered = n.startswith("COMI") or n.startswith("COMX")
    if not (unordered or ordered):
        return None
    typ = "double-precision" if n.endswith("D") else "single-precision" if n.endswith("S") else "binary16" if n.endswith("H") else "bfloat16" if n.endswith("BF16") else "scalar floating-point"
    q = "uses unordered-comparison exception behavior" if unordered else "uses ordered-comparison exception behavior"
    return f"compares two scalar {typ} values, writes the integer condition flags used by branches and SET/CMOV instructions, and {q} for NaNs"


def _packed_shift(name: str) -> str | None:
    n = name[1:] if name.startswith("V") else name
    if re.match(r"PSLL(DQ|D|Q|W|VD|VQ|VW)$", n):
        return "shifts packed integer elements left logically, filling vacated low bits with zeros; vector-count forms obtain counts from vector operands while immediate/scalar-count forms use their encoded count source"
    if re.match(r"PSRL(DQ|D|Q|W|VD|VQ|VW)$", n):
        return "shifts packed integer elements right logically, filling vacated high bits with zeros; vector-count forms permit per-element counts where the encoding provides them"
    if re.match(r"PSRA(D|Q|W|VD|VQ|VW)$", n):
        return "shifts packed signed integer elements right arithmetically, replicating each element's sign bit into the vacated high positions"
    if re.match(r"PSIGN(B|D|W)$", n):
        return "conditionally negates, zeros, or preserves each packed integer element according to the sign of the corresponding control element"
    if re.match(r"PROL(V)?[DQ]$", n):
        return "rotates each packed 32-bit or 64-bit element left by an immediate or per-element variable count"
    if re.match(r"PROT[BWDQ]$", n):
        return "performs AMD XOP packed per-element rotates using signed variable rotate counts supplied by the control operand"
    if re.match(r"PSHA[BWDQ]$", n):
        return "performs AMD XOP packed arithmetic shifts with per-element signed counts, using count sign to choose left versus arithmetic-right direction"
    if re.match(r"PSHL[BWDQ]$", n):
        return "performs AMD XOP packed logical shifts with per-element signed counts, using count sign to choose left versus logical-right direction"
    if re.match(r"PSHLD(D|Q|W|VD|VQ|VW)$", n):
        return "performs packed double-width left shifts, shifting destination elements left while importing replacement low bits from the paired source elements"
    if re.match(r"PSHRD(D|Q|W|VD|VQ|VW)$", n):
        return "performs packed double-width right shifts, shifting destination elements right while importing replacement high bits from the paired source elements"
    return None


def _insert_extract_align(name: str) -> str | None:
    n = name[1:] if name.startswith("V") else name
    if n.startswith("PINSR"):
        width = {"B": "byte", "W": "16-bit word", "D": "32-bit doubleword", "Q": "64-bit quadword"}.get(n[-1], "integer")
        return f"inserts a scalar {width} from a register or memory source into the packed destination lane selected by the immediate index"
    if n.startswith("PEXTR"):
        width = {"B": "byte", "W": "16-bit word", "D": "32-bit doubleword", "Q": "64-bit quadword"}.get(n[-1], "integer")
        return f"extracts the packed {width} lane selected by an immediate index and writes it to a general-purpose register or memory destination"
    if n == "PALIGNR":
        return "concatenates two byte vectors, shifts the concatenation right by an immediate byte count, and returns the aligned low window"
    return None


def _vector_advanced(name: str) -> str | None:
    n = name[1:] if name.startswith("V") else name
    kind = base.element_kind(n)
    if n.startswith("AESENC"):
        return "performs an AES encryption-round transformation on packed 128-bit AES state blocks using the supplied round key" + (" without MixColumns for the final-round form" if "LAST" in n else "")
    if n.startswith("AESDEC"):
        return "performs an AES decryption-round transformation on packed 128-bit AES state blocks using the supplied round key" + (" without inverse MixColumns for the final-round form" if "LAST" in n else "")
    if n == "AESIMC": return "applies AES inverse MixColumns to an encoded round key so it can be used by the AES decryption-round instructions"
    if n == "AESKEYGENASSIST": return "computes S-box, rotation, and round-constant helper values used during AES key-schedule expansion"
    if n.startswith("ALIGND"): return "concatenates vector sources and selects a 32-bit-lane-aligned window controlled by an immediate count"
    if n.startswith("ALIGNQ"): return "concatenates vector sources and selects a 64-bit-lane-aligned window controlled by an immediate count"
    if n.startswith("BCSTNEBF162PS"): return "broadcasts the selected narrow bfloat16 source values into single-precision floating-point lanes using the instruction's even/odd element selection semantics"
    if n.startswith("BCSTNESH2PS"): return "broadcasts selected binary16 source values into single-precision floating-point lanes using the instruction's narrow-source element-selection semantics"
    if n.startswith("EXP2"): return f"computes a hardware approximate 2^x operation independently for {kind}"
    if n.startswith("FIXUPIMM"): return f"classifies exceptional floating-point cases in {kind} and selects replacement/result actions from table and immediate control operands"
    if n.startswith("FPCLASS"): return f"classifies each {kind} against floating-point classes selected by an immediate and writes the classification result to a mask register"
    if n.startswith("FRCZ"): return f"extracts the fractional part of {kind} using AMD XOP FRCZ semantics"
    if n.startswith("GETEXP"): return f"extracts unbiased base-2 exponent values from {kind}, with special values handled according to the instruction's floating-point rules"
    if n.startswith("GETMANT"): return f"normalizes {kind} to expose mantissas in an interval selected by immediate control and applies the requested sign control"
    if n.startswith("P2INTERSECT"):
        return "compares every element of two packed integer vectors and produces two mask results indicating which elements of each source occur anywhere in the other source"
    if n.startswith("PCONFLICT"):
        return "computes, for each packed integer element, a bit mask identifying earlier lanes in the same vector that contain the same value"
    if n.startswith("PLZCNT"):
        return "counts leading zero bits independently in each packed 32-bit or 64-bit integer lane"
    if n.startswith("POPCNT"):
        return "counts set bits independently in each packed integer lane and writes the per-lane population counts"
    if n.startswith("PTERNLOG"):
        return "computes an arbitrary three-input bitwise Boolean function on packed integer operands, with the immediate byte acting as the truth table"
    if n.startswith("RANGE"):
        return f"selects and sign-controls range extrema for {kind} according to immediate control, combining min/max-style selection with the encoded sign rule"
    if n.startswith("REDUCE"):
        return f"reduces {kind} by subtracting an integer multiple of a power of two selected by immediate control, using the instruction's explicit rounding mode"
    if n.startswith("RNDSCALE"):
        return f"scales and rounds {kind} according to immediate rounding/scale control, then rescales the rounded values to the requested numerical domain"
    if n.startswith("SCALEF"):
        return f"scales {kind} by powers of two whose exponents are derived from the corresponding second-source elements"
    if n.startswith("SHA512MSG1"): return "performs the first SHA-512 message-schedule helper transformation on packed 64-bit words"
    if n.startswith("SHA512MSG2"): return "performs the second SHA-512 message-schedule helper transformation on packed 64-bit words"
    if n.startswith("SHA512RNDS2"): return "executes two SHA-512 compression rounds on packed state and message words"
    if n.startswith("SM3MSG1"): return "performs the first SM3 message-schedule expansion transformation on packed 32-bit words"
    if n.startswith("SM3MSG2"): return "performs the second SM3 message-schedule expansion transformation on packed 32-bit words"
    if n.startswith("SM3RNDS2"): return "executes two SM3 compression rounds using packed state and message words"
    if n.startswith("SM4KEY4"): return "computes four SM4 key-schedule words from packed 32-bit state"
    if n.startswith("SM4RNDS4"): return "executes four SM4 cipher rounds on packed 32-bit state"
    return None


def _xop_3dnow(name: str) -> str | None:
    d = {
        "PF2ID": "converts two packed 3DNow! floating-point values to signed 32-bit integers using truncation semantics",
        "PF2IW": "converts two packed 3DNow! floating-point values to signed 16-bit integer results represented in MMX lanes",
        "PFACC": "adds pairs of 3DNow! floating-point values horizontally to form two accumulated results",
        "PFNACC": "performs AMD 3DNow! negative horizontal accumulation over packed floating-point elements",
        "PFPNACC": "performs AMD 3DNow! mixed positive/negative horizontal accumulation over packed floating-point elements",
        "PFRSQIT1": "performs the first Newton-Raphson refinement step used with the 3DNow! reciprocal-square-root estimate",
        "PI2FD": "converts packed signed 32-bit integers to 3DNow! floating-point values",
        "PI2FW": "converts packed signed 16-bit integers to 3DNow! floating-point values",
    }
    if name in d: return d[name]
    if name.startswith("VPCOM"):
        return "performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results"
    if name.startswith("VPMAC") or name.startswith("VPMADC"):
        return "performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior"
    return None


def _vmx_svm(name: str) -> str | None:
    d = {
        "VMCLEAR": "marks the referenced VMCS inactive and ensures its current implementation state is written to the VMCS region in memory",
        "VMFUNC": "invokes a VM function selected by EAX while executing in VMX non-root operation, subject to VMCS enablement of that function",
        "VMPTRLD": "loads the physical address of a VMCS region as the current VMCS pointer after validating the region",
        "VMPTRST": "stores the current VMCS pointer's physical address to memory",
        "VMRUN": "enters an AMD SVM guest using the virtual-machine control block whose physical address is supplied in the implicit register",
        "VMXOFF": "leaves Intel VMX operation on the current logical processor",
        "VMXON": "enters Intel VMX operation using the VMXON region identified by the operand after validating VMX control requirements",
    }
    return d.get(name)


def _ace_outer(name: str) -> str | None:
    if name.startswith("TOP2BF16PS"):
        return "computes an ACE tile outer-product from paired bfloat16 source values and accumulates the resulting products into single-precision destination elements"
    if name.startswith("TOP4"):
        if "MX" in name:
            return "computes an ACE block-scaled mixed-format tile outer-product, applying block-scale-register factors to the encoded low-precision source formats before accumulating wider results"
        return "computes an ACE four-way low-precision integer tile outer-product and accumulates widened products, with signedness selected by the mnemonic"
    return None


def _misc(name: str) -> str | None:
    if name.startswith("SYSCALL_AMD"):
        return "enters the AMD64 operating-system system-call target using the AMD-defined SYSCALL model-specific register state and register return convention"
    if name.startswith("SYSRET_AMD"):
        return "returns from an AMD64 SYSCALL handler using the AMD-defined SYSRET privilege and register-restoration rules"
    if name == "TLBSYNC":
        return "waits for earlier AMD broadcast TLB invalidations initiated by INVLPGB to complete before subsequent execution depends on their global effect"
    return None


def reviewed_general_semantics(name, rows):
    desc, fallback = base_general_semantics(name, rows)
    if not fallback:
        return desc, False

    if name in EXACT:
        return EXACT[name], False

    for fn in (_condition_from_cmpxadd, _fcmov, _stack, _xsave, _comi, _packed_shift,
               _insert_extract_align, _vector_advanced, _xop_3dnow, _vmx_svm,
               _ace_outer, _misc):
        value = fn(name) if fn not in {_xsave} else fn(name)
        if value:
            return value, False

    # These vector families have a stable mnemonic grammar even when individual
    # lane widths or saturating variants differ.  Keep the description at the
    # family operation level and let the page's XED operands/forms carry the
    # exact width/encoding details.
    n = name[1:] if name.startswith("V") else name
    if re.match(r"P(?:SLL|SRL|SRA|SIGN)", n):
        value = _packed_shift(name)
        if value: return value, False
    if n.startswith("PINSR") or n.startswith("PEXTR"):
        value = _insert_extract_align(name)
        if value: return value, False

    return desc, True


base.general_semantics = reviewed_general_semantics

if __name__ == "__main__":
    base.main()
