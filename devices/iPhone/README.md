# iPhone CPU generations

- original / 3G: ARMv6
- 3GS / 4 / 4S: ARMv7
- 5 / 5c: A6 `armv7s`, Thumb-2
- 5s and later: AArch64 `arm64`
- A12-era and later toolchains may use `arm64e` capabilities/ABI where appropriate

The practical old-device follower is AArch64 from A7/A8/A9 upward. ARMv6/v7/v7s remain historical targets unless an old-toolchain/sideload path is intentionally maintained.
