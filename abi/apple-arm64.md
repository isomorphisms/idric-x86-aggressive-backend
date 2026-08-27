# Apple arm64 ABI

Apple platforms use AArch64 machine instructions with a platform ABI, not a proprietary Apple CPU ISA. Important compiler rules include reserving `x18`, maintaining the Apple frame-record convention with `x29`, Apple's variadic-argument rules, 64-bit `long`/pointers, signed 32-bit `wchar_t`, signed `char`, binary64 `long double`, and Mach-O rather than ELF.

Source: https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
