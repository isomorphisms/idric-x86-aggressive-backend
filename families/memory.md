# Loads, stores, addressing, atomics

Address calculation and memory width belong to the ISA layer; pointer width and layout belong to the ABI layer. Atomics and acquire/release forms must be capability-gated by architecture generation. Mach-O is not part of load/store semantics.
