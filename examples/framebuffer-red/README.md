# Framebuffer red — x86-64 target example

This is the x86-64 Linux syscall equivalent of the ARM Thumb framebuffer
reference: open the framebuffer, query its geometry, map it, fill the visible
surface with the framebuffer's native full-red pixel value, wait three seconds,
and exit.

It is a handwritten target example for the x86-64 backend. Its presence does
**not** claim that Idriç currently lowers this program through the checked
compiler route; that remains separate backend work.

The program tries `/dev/graphics/fb0` first and `/dev/fb0` second. It supports
packed 16-bit and 32-bit framebuffers and uses `red.offset`/`red.length` from
`fb_var_screeninfo`, so it is not hard-coded to RGB565 or one 32-bit channel
layout.

Important x86-64 ABI differences from the ARMv7 version:

- Linux x86-64 uses `mmap` syscall 9; its offset argument is in bytes. The
  ARMv7 version uses `mmap2` with a page-scaled offset. Both pass zero here.
- `fb_fix_screeninfo` contains 64-bit `unsigned long` fields on x86-64, so
  `smem_len` is at byte 24 and `line_length` at byte 48. The ARMv7 offsets
  20 and 44 are not valid on x86-64.
- x86-64 `struct timespec` has two 64-bit `long` fields, so the three-second
  sleep value is stored as two `.quad` values.

Rebuild the checked-in executable with GNU binutils:

```sh
as --64 -o framebuffer-red-x86-64.o framebuffer-red-x86-64.s
ld -m elf_x86_64 -nostdlib --build-id=none -z noexecstack -s \
  -o framebuffer-red-x86-64.elf framebuffer-red-x86-64.o
```

Validation of the checked-in build:

```text
source sha256: 5cb33db549d66192eb840c59c3285b32c12071d6e4c0f3791b10fa07a4df15e4
ELF sha256:    34c24f4a820b09c45766624e0c47ab1733132dc834700e2dedfa1a2b7adccb1b
ELF:           64-bit LSB x86-64, statically linked, stripped, no PT_INTERP
```

On a Linux build host with neither framebuffer device present, this exact ELF
exits 10, exercising the intended `fail_open` path. That is executable-host
evidence only; it is not a claim that the red-screen path has run on physical
framebuffer hardware.

Exit codes are 10=open, 11=variable-info ioctl, 12=fixed-info ioctl,
13=unsupported/inconsistent pixel format, and 14=mmap.
