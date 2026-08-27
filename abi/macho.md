# Mach-O boundary

Apple native code uses Mach-O rather than ELF. An Apple follower needs Mach-O object emission or an assembler handoff, Apple symbol/relocation rules, platform load commands and minimum-OS metadata, correct sections, platform ABI conventions, and the final linker/signing workflow. Keep these concerns out of core instruction semantics.
