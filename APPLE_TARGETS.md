# Apple CPU target atlas

This branch is a reference/follower target for Apple hardware. Keep three layers separate: ISA, Apple ABI/object format, and Apple SoC/microarchitecture generation.

Practical ISA/ABI targets represented here:

- ARMv6: original iPhone / iPhone 3G era
- ARMv7: iPhone 3GS/4/4S and early iPad era
- armv7s: Apple A6 / iPhone 5/5c
- armv7k: historical Apple Watch
- AArch64 `arm64`: iPhone 5s onward, modern iPad, Apple TV, Apple-silicon Mac, Vision Pro
- `arm64e`: Apple ABI/extension target layered on AArch64
- `arm64_32`: Apple Watch AArch64 instructions with a 32-bit pointer/data model
- i386: historical Intel Mac / first Apple TV
- x86_64: Intel Mac
- PowerPC32/64: historical Mac OS X

A-series and M-series folders record generation capability deltas. They should normally reuse one of the ISA backends rather than grow independent instruction selectors.
