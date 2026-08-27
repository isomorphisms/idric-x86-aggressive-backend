# Sources

Primary Apple ABI references:

- https://developer.apple.com/documentation/xcode/application-binary-interfaces
- https://developer.apple.com/documentation/xcode/writing-arm64-code-for-apple-platforms
- https://developer.apple.com/documentation/xcode/writing-64-bit-intel-code-for-apple-platforms

Architecture references:

- Arm A-profile architecture: https://developer.arm.com/Architectures
- Intel 64/IA-32 manuals: https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- Power ISA: https://openpowerfoundation.org/specifications/isa/

The plain mnemonic inventories are public architectural names. Optional extensions are not assumed to exist on every generation. A backend must gate optional instructions by the target capability set.
