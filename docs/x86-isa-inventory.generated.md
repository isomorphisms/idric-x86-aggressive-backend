# Generated x86 ISA inventory

> Generated from pinned Intel XED metadata. Do not hand-edit this file.

XED revision: `v2026.08.23`
Source: `intelxed/xed@0bcb6237345c5066726dcc08b3d87928df3b5b26`

- XED instruction records: **10,994**
- unique instruction classes (ICLASS): **1,987**
- unique concrete forms (IFORM): **9,001**
- XED extensions: **109**
- XED categories: **113**

XED records and IFORMs are deliberately counted separately. `generated/xed-instructions.tsv` keeps every exported XED record; `generated/xed-iform-index.tsv` has exactly one row per unique IFORM and reports how many XED records contribute to that form. Repeated IFORMs are not silently collapsed because their mode, encoding, operand, or other metadata may differ.

The complete mnemonic-class list is in `generated/xed-iclasses.txt`. 
The concrete form list is in `generated/xed-iforms.txt`. 
The full normalized record-level metadata is in `generated/xed-instructions.tsv`.

## Vendor scope stated by XED

`unspecified` means exactly that: the exported XED record did not state a vendor-only marker. It must not be read as 'shared by Intel and AMD'. Manual cross-checks remain a separate layer.

| vendor scope | records |
|---|---:|
| amd-only | 420 |
| unspecified | 10,574 |

## By XED extension

| extension | ICLASSes | IFORMs | records |
|---|---:|---:|---:|
| 3DNOW | 25 | 49 | 49 |
| 3DNOW_PREFETCH | 3 | 7 | 7 |
| ACE | 16 | 25 | 25 |
| ADOX_ADCX | 2 | 24 | 24 |
| AES | 6 | 12 | 12 |
| AMD_INVLPGB | 2 | 2 | 3 |
| AMX_TILE | 27 | 40 | 40 |
| APXEVEX | 132 | 1,136 | 2,308 |
| APXLEGACY | 3 | 3 | 3 |
| AVX | 256 | 702 | 728 |
| AVX2 | 130 | 286 | 286 |
| AVX2GATHER | 8 | 16 | 16 |
| AVX512EVEX | 791 | 3,915 | 4,358 |
| AVX512VEX | 51 | 67 | 69 |
| AVXAES | 6 | 12 | 12 |
| AVX_IFMA | 2 | 8 | 8 |
| AVX_NE_CONVERT | 7 | 16 | 16 |
| AVX_VNNI | 4 | 16 | 16 |
| AVX_VNNI_INT16 | 6 | 24 | 24 |
| AVX_VNNI_INT8 | 6 | 24 | 24 |
| BASE | 250 | 777 | 975 |
| BMI1 | 6 | 66 | 80 |
| BMI2 | 8 | 68 | 84 |
| CET | 14 | 18 | 18 |
| CLDEMOTE | 1 | 1 | 1 |
| CLFLUSHOPT | 1 | 1 | 1 |
| CLFSH | 1 | 1 | 1 |
| CLWB | 1 | 1 | 1 |
| CLZERO | 1 | 1 | 1 |
| CMPCCXADD | 16 | 32 | 32 |
| ENQCMD | 2 | 2 | 2 |
| F16C | 2 | 8 | 8 |
| FMA | 60 | 192 | 192 |
| FMA4 | 20 | 96 | 128 |
| FRED | 2 | 2 | 2 |
| GFNI | 6 | 18 | 18 |
| HRESET | 1 | 1 | 1 |
| IBHF | 1 | 1 | 1 |
| ICACHE_PREFETCH | 2 | 2 | 2 |
| INVPCID | 1 | 3 | 3 |
| KEYLOCKER | 7 | 7 | 7 |
| KEYLOCKER_WIDE | 4 | 4 | 4 |
| LKGS | 1 | 2 | 2 |
| LONGMODE | 24 | 26 | 31 |
| LZCNT | 1 | 6 | 10 |
| MCOMMIT | 1 | 1 | 1 |
| MMX | 60 | 132 | 136 |
| MONITOR | 2 | 2 | 5 |
| MONITORX | 2 | 2 | 5 |
| MOVBE | 1 | 5 | 10 |
| MOVDIR | 2 | 5 | 6 |
| MOVRS | 2 | 5 | 6 |
| MPX | 7 | 19 | 30 |
| MSRLIST | 2 | 2 | 2 |
| MSR_IMM | 2 | 4 | 4 |
| PAUSE | 1 | 1 | 1 |
| PBNDKB | 1 | 1 | 1 |
| PCLMULQDQ | 1 | 2 | 2 |
| PCONFIG | 1 | 2 | 2 |
| PKU | 2 | 2 | 2 |
| PREFETCHWT1 | 1 | 1 | 1 |
| PTWRITE | 1 | 2 | 2 |
| RAO | 4 | 16 | 16 |
| RDPID | 1 | 2 | 2 |
| RDPRU | 1 | 1 | 1 |
| RDRAND | 1 | 1 | 1 |
| RDSEED | 1 | 1 | 1 |
| RDTSCP | 1 | 1 | 1 |
| RDWRFSGS | 4 | 4 | 4 |
| RTM | 4 | 4 | 4 |
| SERIALIZE | 1 | 1 | 1 |
| SGX | 2 | 2 | 2 |
| SGX_ENCLV | 1 | 1 | 1 |
| SHA | 7 | 14 | 14 |
| SHA512 | 3 | 3 | 3 |
| SM3 | 3 | 6 | 6 |
| SM4 | 2 | 8 | 8 |
| SMAP | 2 | 2 | 2 |
| SMX | 1 | 1 | 1 |
| SNP | 4 | 4 | 4 |
| SSE | 57 | 110 | 110 |
| SSE2 | 124 | 272 | 277 |
| SSE3 | 11 | 22 | 22 |
| SSE4 | 59 | 119 | 125 |
| SSE4a | 4 | 6 | 6 |
| SSSE3 | 16 | 64 | 64 |
| SVM | 8 | 8 | 8 |
| TBM | 10 | 40 | 40 |
| TDX | 4 | 4 | 5 |
| TSX_LDTRK | 2 | 2 | 2 |
| UINTR | 5 | 5 | 5 |
| USER_MSR | 2 | 8 | 8 |
| VAES | 4 | 8 | 8 |
| VIA_PADLOCK_AES | 5 | 5 | 5 |
| VIA_PADLOCK_MONTMUL | 1 | 1 | 2 |
| VIA_PADLOCK_RNG | 2 | 2 | 2 |
| VIA_PADLOCK_SHA | 2 | 2 | 2 |
| VMFUNC | 1 | 1 | 1 |
| VPCLMULQDQ | 1 | 2 | 2 |
| VTX | 12 | 22 | 22 |
| WAITPKG | 3 | 3 | 3 |
| WBNOINVD | 1 | 1 | 1 |
| WRMSRNS | 1 | 1 | 1 |
| X87 | 91 | 146 | 166 |
| XOP | 59 | 153 | 172 |
| XSAVE | 6 | 6 | 6 |
| XSAVEC | 2 | 2 | 2 |
| XSAVEOPT | 2 | 2 | 2 |
| XSAVES | 4 | 4 | 4 |

## By XED category

| category | ICLASSes | records |
|---|---:|---:|
| 3DNOW | 24 | 48 |
| ADOX_ADCX | 2 | 8 |
| AES | 12 | 24 |
| AMX_TILE | 42 | 65 |
| APX | 94 | 976 |
| AVX | 190 | 475 |
| AVX2 | 118 | 257 |
| AVX2GATHER | 8 | 16 |
| AVX512 | 310 | 1,670 |
| AVX512_4FMAPS | 4 | 4 |
| AVX512_4VNNIW | 2 | 2 |
| AVX512_BITALG | 3 | 6 |
| AVX512_VBMI | 4 | 24 |
| AVX512_VP2INTERSECT | 2 | 12 |
| AVX_IFMA | 2 | 8 |
| BINARY | 19 | 588 |
| BITBYTE | 11 | 34 |
| BLEND | 6 | 36 |
| BMI1 | 6 | 80 |
| BMI2 | 8 | 84 |
| BROADCAST | 22 | 105 |
| CALL | 2 | 6 |
| CET | 14 | 18 |
| CLDEMOTE | 1 | 1 |
| CLFLUSHOPT | 1 | 1 |
| CLWB | 1 | 1 |
| CLZERO | 1 | 1 |
| CMOV | 16 | 32 |
| COMPRESS | 6 | 36 |
| COND_BR | 24 | 79 |
| CONFLICT | 4 | 24 |
| CONVERT | 165 | 1,061 |
| DATAXFER | 117 | 690 |
| DECIMAL | 6 | 6 |
| ENQCMD | 2 | 2 |
| EXPAND | 6 | 36 |
| FCMOV | 8 | 8 |
| FLAGOP | 10 | 10 |
| FMA4 | 20 | 128 |
| FP16 | 72 | 362 |
| FRED | 2 | 2 |
| GATHER | 16 | 32 |
| GFNI | 6 | 36 |
| HRESET | 1 | 1 |
| IFMA | 2 | 12 |
| INTERRUPT | 5 | 8 |
| IO | 2 | 8 |
| IOSTRINGOP | 12 | 48 |
| KEYLOCKER | 7 | 7 |
| KEYLOCKER_WIDE | 4 | 4 |
| KMASK | 51 | 89 |
| LEGACY | 10 | 16 |
| LKGS | 1 | 2 |
| LOGICAL | 38 | 515 |
| LOGICAL_FP | 18 | 104 |
| LZCNT | 1 | 10 |
| MISC | 20 | 31 |
| MMX | 73 | 150 |
| MOVDIR | 2 | 6 |
| MPX | 7 | 30 |
| MSRLIST | 2 | 2 |
| NOP | 1 | 2 |
| PBNDKB | 1 | 1 |
| PCLMULQDQ | 1 | 2 |
| PCONFIG | 1 | 2 |
| PKU | 2 | 2 |
| POP | 9 | 23 |
| PREFETCH | 10 | 14 |
| PREFETCHWT1 | 1 | 1 |
| PTWRITE | 1 | 2 |
| PUSH | 9 | 26 |
| RDPID | 1 | 2 |
| RDPRU | 1 | 1 |
| RDRAND | 1 | 1 |
| RDSEED | 1 | 1 |
| RDWRFSGS | 4 | 4 |
| RET | 5 | 11 |
| ROTATE | 4 | 264 |
| SCATTER | 16 | 32 |
| SEGOP | 5 | 5 |
| SEMAPHORE | 8 | 18 |
| SERIALIZE | 1 | 1 |
| SETCC | 16 | 96 |
| SGX | 3 | 3 |
| SHA | 7 | 14 |
| SHA512 | 3 | 3 |
| SHIFT | 5 | 408 |
| SMAP | 2 | 2 |
| SSE | 194 | 392 |
| STRINGOP | 48 | 120 |
| STTNI | 7 | 20 |
| SYSCALL | 3 | 4 |
| SYSRET | 5 | 6 |
| SYSTEM | 42 | 60 |
| TBM | 10 | 40 |
| TSX_LDTRK | 2 | 2 |
| UINTR | 5 | 5 |
| UNCOND_BR | 4 | 10 |
| USER_MSR | 2 | 4 |
| VAES | 4 | 32 |
| VBMI2 | 12 | 72 |
| VEX | 39 | 112 |
| VFMA | 72 | 588 |
| VIA_PADLOCK | 10 | 11 |
| VPCLMULQDQ | 1 | 8 |
| VTX | 13 | 23 |
| WAITPKG | 3 | 3 |
| WIDENOP | 1 | 56 |
| WRMSRNS | 1 | 1 |
| X87_ALU | 84 | 161 |
| XOP | 59 | 172 |
| XSAVE | 12 | 12 |
| XSAVEOPT | 2 | 2 |

## Inventory rule

Inventory completeness and backend support are different questions. Nothing in these generated files implies that the Idriç backend should emit every listed instruction. Backend support is intentionally tracked outside the generated inventory.
