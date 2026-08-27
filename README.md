# Apple CPU target atlas

This branch records Apple CPU ISA generations, ABI/object-format profiles, SoC capability deltas, and device-family mappings. It is a target-profile/reference overlay, not an independent instruction selector for every Apple chip.

- modern Apple `arm64`/`arm64e` codegen reuses the generic `a64-backend` branch;
- Intel-Mac codegen reuses the canonical x86-64 backend;
- historical ARMv6/ARMv7/armv7s/armv7k, i386, and PowerPC material remains documentary unless explicitly reactivated;
- Apple GPU/Metal architecture and shader work lives separately in `isomorphisms/idris-shader-backend:Apple`.

Every concrete Apple implementation must pin the actual ISA/features, Apple ABI/data model, Mach-O boundary, toolchain/deployment target, and executable device evidence. A-series and M-series folders describe feature masks; they do not grow separate backends.

Tracking issue: [#9](https://github.com/isomorphisms/idric-x86-aggressive-backend/issues/9).
