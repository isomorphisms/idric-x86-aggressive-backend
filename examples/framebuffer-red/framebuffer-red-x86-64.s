.intel_syntax noprefix

.equ SYS_mmap,       9
.equ SYS_ioctl,     16
.equ SYS_nanosleep, 35
.equ SYS_exit,      60
.equ SYS_openat,   257

.equ AT_FDCWD,       -100
.equ O_RDWR,            2
.equ PROT_READ,         1
.equ PROT_WRITE,        2
.equ MAP_SHARED,        1

.equ FBIOGET_VSCREENINFO, 0x4600
.equ FBIOGET_FSCREENINFO, 0x4602

.section .text
.global _start
.type _start, @function

_start:
    # Try Android's traditional framebuffer path first.
    # openat(AT_FDCWD, "/dev/graphics/fb0", O_RDWR, 0)

    mov     eax, SYS_openat
    mov     rdi, AT_FDCWD
    lea     rsi, [rip + fb_path_android]
    mov     edx, O_RDWR
    xor     r10d, r10d
    syscall

    test    rax, rax
    jns     opened

    # Then ordinary Linux /dev/fb0.

    mov     eax, SYS_openat
    mov     rdi, AT_FDCWD
    lea     rsi, [rip + fb_path_linux]
    mov     edx, O_RDWR
    xor     r10d, r10d
    syscall

    test    rax, rax
    js      fail_open

opened:
    mov     r12, rax                    # framebuffer fd

    # ioctl(fd, FBIOGET_VSCREENINFO, &vinfo)

    mov     eax, SYS_ioctl
    mov     rdi, r12
    mov     esi, FBIOGET_VSCREENINFO
    lea     rdx, [rip + vinfo]
    syscall

    test    rax, rax
    jne     fail_vinfo

    # ioctl(fd, FBIOGET_FSCREENINFO, &finfo)

    mov     eax, SYS_ioctl
    mov     rdi, r12
    mov     esi, FBIOGET_FSCREENINFO
    lea     rdx, [rip + finfo]
    syscall

    test    rax, rax
    jne     fail_finfo

    # First version supports packed 16-bit and 32-bit pixels.

    lea     rbx, [rip + vinfo]
    mov     eax, DWORD PTR [rbx + 24]   # bits_per_pixel

    cmp     eax, 16
    je      pixels_16

    cmp     eax, 32
    je      pixels_32

    jmp     fail_format

pixels_16:
    mov     r13d, 2                     # bytes per pixel
    jmp     make_red

pixels_32:
    mov     r13d, 4

make_red:
    # fb_var_screeninfo.red begins at byte 32:
    #
    #   +32 red.offset
    #   +36 red.length
    #
    # pixel = ((1 << red.length) - 1) << red.offset

    mov     r8d, DWORD PTR [rbx + 32]   # red.offset
    mov     r9d, DWORD PTR [rbx + 36]   # red.length

    test    r9d, r9d
    jz      fail_format
    cmp     r9d, 31
    ja      fail_format
    cmp     r8d, 31
    ja      fail_format

    mov     r10d, r8d
    add     r10d, r9d
    cmp     r10d, DWORD PTR [rbx + 24]
    ja      fail_format

    mov     eax, 1
    mov     ecx, r9d
    shl     eax, cl
    dec     eax
    mov     ecx, r8d
    shl     eax, cl
    mov     r14d, eax                   # red pixel

    # mmap(
    #     0,
    #     finfo.smem_len,
    #     PROT_READ | PROT_WRITE,
    #     MAP_SHARED,
    #     fd,
    #     0
    # )
    #
    # x86-64 uses mmap, whose offset argument is in bytes.  The 32-bit ARM
    # program uses mmap2, whose offset is in pages.  Zero is identical here.

    lea     r15, [rip + finfo]

    xor     edi, edi
    mov     esi, DWORD PTR [r15 + 24]   # smem_len (x86-64 fb_fix_screeninfo)
    mov     edx, PROT_READ | PROT_WRITE
    mov     r10d, MAP_SHARED
    mov     r8, r12
    xor     r9d, r9d
    mov     eax, SYS_mmap
    syscall

    # Linux syscall errors are in -4095 ... -1.

    cmp     rax, -4095
    jae     fail_mmap

    mov     r12, rax                    # framebuffer memory

    # Recover the visible geometry.  On x86-64, unsigned long is 8 bytes in
    # fb_fix_screeninfo, so line_length is at byte 48 rather than ARM's 44.

    mov     r11d, DWORD PTR [r15 + 48]  # line_length / stride
    mov     ebp, DWORD PTR [rbx + 0]    # xres
    mov     r15d, DWORD PTR [rbx + 4]   # yres

    test    ebp, ebp
    jz      fail_format
    test    r15d, r15d
    jz      fail_format

    # framebuffer address of visible upper-left pixel:
    #
    # base
    # + yoffset * line_length
    # + xoffset * bytes_per_pixel

    mov     eax, DWORD PTR [rbx + 20]   # yoffset
    imul    rax, r11
    lea     r10, [r12 + rax]

    mov     eax, DWORD PTR [rbx + 16]   # xoffset
    imul    rax, r13
    add     r10, rax

row:
    mov     rdx, r10                    # current pixel
    mov     ecx, ebp                    # pixels remaining

    cmp     r13d, 4
    je      row_32

row_16:
    mov     WORD PTR [rdx], r14w
    add     rdx, 2
    dec     ecx
    jne     row_16
    jmp     next_row

row_32:
    mov     DWORD PTR [rdx], r14d
    add     rdx, 4
    dec     ecx
    jne     row_32

next_row:
    add     r10, r11
    dec     r15d
    jne     row

    # Sleep for three seconds.  struct timespec uses two 64-bit longs here.

    lea     rdi, [rip + sleep_time]
    xor     esi, esi
    mov     eax, SYS_nanosleep
    syscall

    xor     edi, edi
    jmp     exit

fail_open:
    mov     edi, 10
    jmp     exit

fail_vinfo:
    mov     edi, 11
    jmp     exit

fail_finfo:
    mov     edi, 12
    jmp     exit

fail_format:
    mov     edi, 13
    jmp     exit

fail_mmap:
    mov     edi, 14

exit:
    mov     eax, SYS_exit
    syscall

.size _start, .-_start

.section .rodata
.balign 8

fb_path_android:
    .asciz "/dev/graphics/fb0"

fb_path_linux:
    .asciz "/dev/fb0"

.balign 8
sleep_time:
    .quad 3
    .quad 0

.section .bss
.balign 8

vinfo:
    .zero 160

finfo:
    .zero 80

.section .note.GNU-stack,"",@progbits
