# AVX, FMA, and modern vector

This generated bundle contains 89 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## VADDSUBPD

`VADDSUBPD` adds corresponding packed double-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VADDSUBPD_XMMdq_XMMdq_MEMdq` — `VADDSUBPD`
- `VADDSUBPD_XMMdq_XMMdq_XMMdq` — `VADDSUBPD`
- `VADDSUBPD_YMMqq_YMMqq_MEMqq` — `VADDSUBPD`
- `VADDSUBPD_YMMqq_YMMqq_YMMqq` — `VADDSUBPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VADDSUBPS

`VADDSUBPS` adds corresponding packed single-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VADDSUBPS_XMMdq_XMMdq_MEMdq` — `VADDSUBPS`
- `VADDSUBPS_XMMdq_XMMdq_XMMdq` — `VADDSUBPS`
- `VADDSUBPS_YMMqq_YMMqq_MEMqq` — `VADDSUBPS`
- `VADDSUBPS_YMMqq_YMMqq_YMMqq` — `VADDSUBPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBCSTNEBF162PS

`VBCSTNEBF162PS` broadcasts the selected narrow bfloat16 source values into single-precision floating-point lanes using the instruction's even/odd element selection semantics. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX_NE_CONVERT`
- XED category/categories: `BROADCAST`
- ISA set(s): `AVX_NE_CONVERT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBCSTNEBF162PS_XMMf32_MEMbf16` — `VBCSTNEBF162PS`
- `VBCSTNEBF162PS_YMMf32_MEMbf16` — `VBCSTNEBF162PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBCSTNESH2PS

`VBCSTNESH2PS` broadcasts selected binary16 source values into single-precision floating-point lanes using the instruction's narrow-source element-selection semantics. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX_NE_CONVERT`
- XED category/categories: `BROADCAST`
- ISA set(s): `AVX_NE_CONVERT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBCSTNESH2PS_XMMf32_MEMf16` — `VBCSTNESH2PS`
- `VBCSTNESH2PS_YMMf32_MEMf16` — `VBCSTNESH2PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBLENDPD

`VBLENDPD` selects packed double-precision floating-point elements from two sources under an immediate or mask control. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`; `YMM YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBLENDPD_XMMdq_XMMdq_MEMdq_IMMb` — `VBLENDPD`
- `VBLENDPD_XMMdq_XMMdq_XMMdq_IMMb` — `VBLENDPD`
- `VBLENDPD_YMMqq_YMMqq_MEMqq_IMMb` — `VBLENDPD`
- `VBLENDPD_YMMqq_YMMqq_YMMqq_IMMb` — `VBLENDPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBLENDPS

`VBLENDPS` selects packed single-precision floating-point elements from two sources under an immediate or mask control. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`; `YMM YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBLENDPS_XMMdq_XMMdq_MEMdq_IMMb` — `VBLENDPS`
- `VBLENDPS_XMMdq_XMMdq_XMMdq_IMMb` — `VBLENDPS`
- `VBLENDPS_YMMqq_YMMqq_MEMqq_IMMb` — `VBLENDPS`
- `VBLENDPS_YMMqq_YMMqq_YMMqq_IMMb` — `VBLENDPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBLENDVPD

`VBLENDVPD` selects packed double-precision floating-point elements from two sources under an immediate or mask control. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`; `YMM YMM MEM YMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBLENDVPD_XMMdq_XMMdq_MEMdq_XMMdq` — `VBLENDVPD`
- `VBLENDVPD_XMMdq_XMMdq_XMMdq_XMMdq` — `VBLENDVPD`
- `VBLENDVPD_YMMqq_YMMqq_MEMqq_YMMqq` — `VBLENDVPD`
- `VBLENDVPD_YMMqq_YMMqq_YMMqq_YMMqq` — `VBLENDVPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBLENDVPS

`VBLENDVPS` selects packed single-precision floating-point elements from two sources under an immediate or mask control. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`; `YMM YMM MEM YMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBLENDVPS_XMMdq_XMMdq_MEMdq_XMMdq` — `VBLENDVPS`
- `VBLENDVPS_XMMdq_XMMdq_XMMdq_XMMdq` — `VBLENDVPS`
- `VBLENDVPS_YMMqq_YMMqq_MEMqq_YMMqq` — `VBLENDVPS`
- `VBLENDVPS_YMMqq_YMMqq_YMMqq_YMMqq` — `VBLENDVPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBROADCASTF128

`VBROADCASTF128` replicates a scalar or smaller source value across destination lanes as its encoded scalar or vector elements. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `BROADCAST`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBROADCASTF128_YMMqq_MEMdq` — `VBROADCASTF128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VBROADCASTI128

`VBROADCASTI128` replicates a scalar or smaller source value across destination lanes as its encoded scalar or vector elements. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX2`
- XED category/categories: `BROADCAST`
- ISA set(s): `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VBROADCASTI128_YMMqq_MEMdq` — `VBROADCASTI128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VCVTNEEBF162PS

`VCVTNEEBF162PS` converts values between the source and destination numerical formats encoded by the mnemonic. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX_NE_CONVERT`
- XED category/categories: `CONVERT`
- ISA set(s): `AVX_NE_CONVERT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VCVTNEEBF162PS_XMMf32_MEM2bf16` — `VCVTNEEBF162PS`
- `VCVTNEEBF162PS_YMMf32_MEM2bf16` — `VCVTNEEBF162PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VCVTNEEPH2PS

`VCVTNEEPH2PS` converts values between the source and destination numerical formats encoded by the mnemonic. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX_NE_CONVERT`
- XED category/categories: `CONVERT`
- ISA set(s): `AVX_NE_CONVERT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VCVTNEEPH2PS_XMMf32_MEM2f16` — `VCVTNEEPH2PS`
- `VCVTNEEPH2PS_YMMf32_MEM2f16` — `VCVTNEEPH2PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VCVTNEOBF162PS

`VCVTNEOBF162PS` converts values between the source and destination numerical formats encoded by the mnemonic. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX_NE_CONVERT`
- XED category/categories: `CONVERT`
- ISA set(s): `AVX_NE_CONVERT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VCVTNEOBF162PS_XMMf32_MEM2bf16` — `VCVTNEOBF162PS`
- `VCVTNEOBF162PS_YMMf32_MEM2bf16` — `VCVTNEOBF162PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VCVTNEOPH2PS

`VCVTNEOPH2PS` converts values between the source and destination numerical formats encoded by the mnemonic. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX_NE_CONVERT`
- XED category/categories: `CONVERT`
- ISA set(s): `AVX_NE_CONVERT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VCVTNEOPH2PS_XMMf32_MEM2f16` — `VCVTNEOPH2PS`
- `VCVTNEOPH2PS_YMMf32_MEM2f16` — `VCVTNEOPH2PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VDPPD

`VDPPD` forms products of selected source elements and accumulates grouped dot-product sums. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VDPPD_XMMdq_XMMdq_MEMdq_IMMb` — `VDPPD`
- `VDPPD_XMMdq_XMMdq_XMMdq_IMMb` — `VDPPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VDPPS

`VDPPS` forms products of selected source elements and accumulates grouped dot-product sums. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`; `YMM YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VDPPS_XMMdq_XMMdq_MEMdq_IMMb` — `VDPPS`
- `VDPPS_XMMdq_XMMdq_XMMdq_IMMb` — `VDPPS`
- `VDPPS_YMMqq_YMMqq_MEMqq_IMMb` — `VDPPS`
- `VDPPS_YMMqq_YMMqq_YMMqq_IMMb` — `VDPPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VEXTRACTF128

`VEXTRACTF128` extracts a selected scalar or subvector from packed its encoded scalar or vector elements. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM YMM IMM`; `XMM YMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VEXTRACTF128_MEMdq_YMMqq_IMMb` — `VEXTRACTF128`
- `VEXTRACTF128_XMMdq_YMMqq_IMMb` — `VEXTRACTF128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VEXTRACTI128

`VEXTRACTI128` extracts a selected scalar or subvector from packed its encoded scalar or vector elements. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX2`
- XED category/categories: `AVX2`
- ISA set(s): `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM YMM IMM`; `XMM YMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VEXTRACTI128_MEMdq_YMMqq_IMMb` — `VEXTRACTI128`
- `VEXTRACTI128_XMMdq_YMMqq_IMMb` — `VEXTRACTI128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMADDPD

`VFMADDPD` computes a fused multiply/add-or-subtract operation on packed double-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMADDPD_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMADDPD`
- `VFMADDPD_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMADDPD`
- `VFMADDPD_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMADDPD`
- `VFMADDPD_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMADDPD`
- `VFMADDPD_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMADDPD`
- `VFMADDPD_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMADDPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMADDPS

`VFMADDPS` computes a fused multiply/add-or-subtract operation on packed single-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMADDPS_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMADDPS`
- `VFMADDPS_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMADDPS`
- `VFMADDPS_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMADDPS`
- `VFMADDPS_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMADDPS`
- `VFMADDPS_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMADDPS`
- `VFMADDPS_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMADDPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMADDSD

`VFMADDSD` computes a fused multiply/add-or-subtract operation on a scalar double-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMADDSD_XMMdq_XMMq_MEMq_XMMq` — `VFMADDSD`
- `VFMADDSD_XMMdq_XMMq_XMMq_MEMq` — `VFMADDSD`
- `VFMADDSD_XMMdq_XMMq_XMMq_XMMq` — `VFMADDSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMADDSS

`VFMADDSS` computes a fused multiply/add-or-subtract operation on a scalar single-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMADDSS_XMMdq_XMMd_MEMd_XMMd` — `VFMADDSS`
- `VFMADDSS_XMMdq_XMMd_XMMd_MEMd` — `VFMADDSS`
- `VFMADDSS_XMMdq_XMMd_XMMd_XMMd` — `VFMADDSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMADDSUBPD

`VFMADDSUBPD` computes a fused multiply/add-or-subtract operation on packed double-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMADDSUBPD_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMADDSUBPD`
- `VFMADDSUBPD_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMADDSUBPD`
- `VFMADDSUBPD_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMADDSUBPD`
- `VFMADDSUBPD_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMADDSUBPD`
- `VFMADDSUBPD_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMADDSUBPD`
- `VFMADDSUBPD_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMADDSUBPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMADDSUBPS

`VFMADDSUBPS` computes a fused multiply/add-or-subtract operation on packed single-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMADDSUBPS_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMADDSUBPS`
- `VFMADDSUBPS_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMADDSUBPS`
- `VFMADDSUBPS_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMADDSUBPS`
- `VFMADDSUBPS_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMADDSUBPS`
- `VFMADDSUBPS_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMADDSUBPS`
- `VFMADDSUBPS_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMADDSUBPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMSUBADDPD

`VFMSUBADDPD` computes a fused multiply/add-or-subtract operation on packed double-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMSUBADDPD_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMSUBADDPD`
- `VFMSUBADDPD_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMSUBADDPD`
- `VFMSUBADDPD_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMSUBADDPD`
- `VFMSUBADDPD_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMSUBADDPD`
- `VFMSUBADDPD_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMSUBADDPD`
- `VFMSUBADDPD_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMSUBADDPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMSUBADDPS

`VFMSUBADDPS` computes a fused multiply/add-or-subtract operation on packed single-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMSUBADDPS_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMSUBADDPS`
- `VFMSUBADDPS_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMSUBADDPS`
- `VFMSUBADDPS_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMSUBADDPS`
- `VFMSUBADDPS_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMSUBADDPS`
- `VFMSUBADDPS_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMSUBADDPS`
- `VFMSUBADDPS_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMSUBADDPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMSUBPD

`VFMSUBPD` computes a fused multiply/add-or-subtract operation on packed double-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMSUBPD_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMSUBPD`
- `VFMSUBPD_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMSUBPD`
- `VFMSUBPD_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMSUBPD`
- `VFMSUBPD_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMSUBPD`
- `VFMSUBPD_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMSUBPD`
- `VFMSUBPD_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMSUBPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMSUBPS

`VFMSUBPS` computes a fused multiply/add-or-subtract operation on packed single-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMSUBPS_XMMdq_XMMdq_MEMdq_XMMdq` — `VFMSUBPS`
- `VFMSUBPS_XMMdq_XMMdq_XMMdq_MEMdq` — `VFMSUBPS`
- `VFMSUBPS_XMMdq_XMMdq_XMMdq_XMMdq` — `VFMSUBPS`
- `VFMSUBPS_YMMqq_YMMqq_MEMqq_YMMqq` — `VFMSUBPS`
- `VFMSUBPS_YMMqq_YMMqq_YMMqq_MEMqq` — `VFMSUBPS`
- `VFMSUBPS_YMMqq_YMMqq_YMMqq_YMMqq` — `VFMSUBPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMSUBSD

`VFMSUBSD` computes a fused multiply/add-or-subtract operation on a scalar double-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMSUBSD_XMMdq_XMMq_MEMq_XMMq` — `VFMSUBSD`
- `VFMSUBSD_XMMdq_XMMq_XMMq_MEMq` — `VFMSUBSD`
- `VFMSUBSD_XMMdq_XMMq_XMMq_XMMq` — `VFMSUBSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFMSUBSS

`VFMSUBSS` computes a fused multiply/add-or-subtract operation on a scalar single-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFMSUBSS_XMMdq_XMMd_MEMd_XMMd` — `VFMSUBSS`
- `VFMSUBSS_XMMdq_XMMd_XMMd_MEMd` — `VFMSUBSS`
- `VFMSUBSS_XMMdq_XMMd_XMMd_XMMd` — `VFMSUBSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMADDPD

`VFNMADDPD` computes a fused multiply/add-or-subtract operation on packed double-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMADDPD_XMMdq_XMMdq_MEMdq_XMMdq` — `VFNMADDPD`
- `VFNMADDPD_XMMdq_XMMdq_XMMdq_MEMdq` — `VFNMADDPD`
- `VFNMADDPD_XMMdq_XMMdq_XMMdq_XMMdq` — `VFNMADDPD`
- `VFNMADDPD_YMMqq_YMMqq_MEMqq_YMMqq` — `VFNMADDPD`
- `VFNMADDPD_YMMqq_YMMqq_YMMqq_MEMqq` — `VFNMADDPD`
- `VFNMADDPD_YMMqq_YMMqq_YMMqq_YMMqq` — `VFNMADDPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMADDPS

`VFNMADDPS` computes a fused multiply/add-or-subtract operation on packed single-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMADDPS_XMMdq_XMMdq_MEMdq_XMMdq` — `VFNMADDPS`
- `VFNMADDPS_XMMdq_XMMdq_XMMdq_MEMdq` — `VFNMADDPS`
- `VFNMADDPS_XMMdq_XMMdq_XMMdq_XMMdq` — `VFNMADDPS`
- `VFNMADDPS_YMMqq_YMMqq_MEMqq_YMMqq` — `VFNMADDPS`
- `VFNMADDPS_YMMqq_YMMqq_YMMqq_MEMqq` — `VFNMADDPS`
- `VFNMADDPS_YMMqq_YMMqq_YMMqq_YMMqq` — `VFNMADDPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMADDSD

`VFNMADDSD` computes a fused multiply/add-or-subtract operation on a scalar double-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMADDSD_XMMdq_XMMq_MEMq_XMMq` — `VFNMADDSD`
- `VFNMADDSD_XMMdq_XMMq_XMMq_MEMq` — `VFNMADDSD`
- `VFNMADDSD_XMMdq_XMMq_XMMq_XMMq` — `VFNMADDSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMADDSS

`VFNMADDSS` computes a fused multiply/add-or-subtract operation on a scalar single-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMADDSS_XMMdq_XMMd_MEMd_XMMd` — `VFNMADDSS`
- `VFNMADDSS_XMMdq_XMMd_XMMd_MEMd` — `VFNMADDSS`
- `VFNMADDSS_XMMdq_XMMd_XMMd_XMMd` — `VFNMADDSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMSUBPD

`VFNMSUBPD` computes a fused multiply/add-or-subtract operation on packed double-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMSUBPD_XMMdq_XMMdq_MEMdq_XMMdq` — `VFNMSUBPD`
- `VFNMSUBPD_XMMdq_XMMdq_XMMdq_MEMdq` — `VFNMSUBPD`
- `VFNMSUBPD_XMMdq_XMMdq_XMMdq_XMMdq` — `VFNMSUBPD`
- `VFNMSUBPD_YMMqq_YMMqq_MEMqq_YMMqq` — `VFNMSUBPD`
- `VFNMSUBPD_YMMqq_YMMqq_YMMqq_MEMqq` — `VFNMSUBPD`
- `VFNMSUBPD_YMMqq_YMMqq_YMMqq_YMMqq` — `VFNMSUBPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMSUBPS

`VFNMSUBPS` computes a fused multiply/add-or-subtract operation on packed single-precision floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMSUBPS_XMMdq_XMMdq_MEMdq_XMMdq` — `VFNMSUBPS`
- `VFNMSUBPS_XMMdq_XMMdq_XMMdq_MEMdq` — `VFNMSUBPS`
- `VFNMSUBPS_XMMdq_XMMdq_XMMdq_XMMdq` — `VFNMSUBPS`
- `VFNMSUBPS_YMMqq_YMMqq_MEMqq_YMMqq` — `VFNMSUBPS`
- `VFNMSUBPS_YMMqq_YMMqq_YMMqq_MEMqq` — `VFNMSUBPS`
- `VFNMSUBPS_YMMqq_YMMqq_YMMqq_YMMqq` — `VFNMSUBPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMSUBSD

`VFNMSUBSD` computes a fused multiply/add-or-subtract operation on a scalar double-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMSUBSD_XMMdq_XMMq_MEMq_XMMq` — `VFNMSUBSD`
- `VFNMSUBSD_XMMdq_XMMq_XMMq_MEMq` — `VFNMSUBSD`
- `VFNMSUBSD_XMMdq_XMMq_XMMq_XMMq` — `VFNMSUBSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFNMSUBSS

`VFNMSUBSS` computes a fused multiply/add-or-subtract operation on a scalar single-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FMA4`
- XED category/categories: `FMA4`
- ISA set(s): `FMA4`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFNMSUBSS_XMMdq_XMMd_MEMd_XMMd` — `VFNMSUBSS`
- `VFNMSUBSS_XMMdq_XMMd_XMMd_MEMd` — `VFNMSUBSS`
- `VFNMSUBSS_XMMdq_XMMd_XMMd_XMMd` — `VFNMSUBSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VHADDPD

`VHADDPD` adds corresponding packed double-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VHADDPD_XMMdq_XMMdq_MEMdq` — `VHADDPD`
- `VHADDPD_XMMdq_XMMdq_XMMdq` — `VHADDPD`
- `VHADDPD_YMMqq_YMMqq_MEMqq` — `VHADDPD`
- `VHADDPD_YMMqq_YMMqq_YMMqq` — `VHADDPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VHADDPS

`VHADDPS` adds corresponding packed single-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VHADDPS_XMMdq_XMMdq_MEMdq` — `VHADDPS`
- `VHADDPS_XMMdq_XMMdq_XMMdq` — `VHADDPS`
- `VHADDPS_YMMqq_YMMqq_MEMqq` — `VHADDPS`
- `VHADDPS_YMMqq_YMMqq_YMMqq` — `VHADDPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VHSUBPD

`VHSUBPD` subtracts corresponding packed double-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VHSUBPD_XMMdq_XMMdq_MEMdq` — `VHSUBPD`
- `VHSUBPD_XMMdq_XMMdq_XMMdq` — `VHSUBPD`
- `VHSUBPD_YMMqq_YMMqq_MEMqq` — `VHSUBPD`
- `VHSUBPD_YMMqq_YMMqq_YMMqq` — `VHSUBPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VHSUBPS

`VHSUBPS` subtracts corresponding packed single-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VHSUBPS_XMMdq_XMMdq_MEMdq` — `VHSUBPS`
- `VHSUBPS_XMMdq_XMMdq_XMMdq` — `VHSUBPS`
- `VHSUBPS_YMMqq_YMMqq_MEMqq` — `VHSUBPS`
- `VHSUBPS_YMMqq_YMMqq_YMMqq` — `VHSUBPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VINSERTF128

`VINSERTF128` inserts a scalar or subvector into selected positions of a destination containing its encoded scalar or vector elements. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM YMM MEM IMM`; `YMM YMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VINSERTF128_YMMqq_YMMqq_MEMdq_IMMb` — `VINSERTF128`
- `VINSERTF128_YMMqq_YMMqq_XMMdq_IMMb` — `VINSERTF128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VINSERTI128

`VINSERTI128` inserts a scalar or subvector into selected positions of a destination containing its encoded scalar or vector elements. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX2`
- XED category/categories: `AVX2`
- ISA set(s): `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM YMM MEM IMM`; `YMM YMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VINSERTI128_YMMqq_YMMqq_MEMdq_IMMb` — `VINSERTI128`
- `VINSERTI128_YMMqq_YMMqq_XMMdq_IMMb` — `VINSERTI128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VLDDQU

`VLDDQU` loads unaligned vector integer data using the VEX-encoded LDDQU streaming-load form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VLDDQU_XMMdq_MEMdq` — `VLDDQU`
- `VLDDQU_YMMqq_MEMqq` — `VLDDQU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VLDMXCSR

`VLDMXCSR` loads MXCSR through the VEX-encoded form of the floating-point control-state load. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `MXCSR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VLDMXCSR_MEMd` — `VLDMXCSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPAND

`VPAND` computes bitwise AND over 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `LOGICAL`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPAND_XMMdq_XMMdq_MEMdq` — `VPAND`
- `VPAND_XMMdq_XMMdq_XMMdq` — `VPAND`
- `VPAND_YMMqq_YMMqq_MEMqq` — `VPAND`
- `VPAND_YMMqq_YMMqq_YMMqq` — `VPAND`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPANDN

`VPANDN` ANDs a complemented source with another over its encoded scalar or vector elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `LOGICAL`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPANDN_XMMdq_XMMdq_MEMdq` — `VPANDN`
- `VPANDN_XMMdq_XMMdq_XMMdq` — `VPANDN`
- `VPANDN_YMMqq_YMMqq_MEMqq` — `VPANDN`
- `VPANDN_YMMqq_YMMqq_YMMqq` — `VPANDN`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPBLENDD

`VPBLENDD` selects 32-bit doubleword elements from two sources under an immediate or mask control. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX2`
- XED category/categories: `AVX2`
- ISA set(s): `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`; `YMM YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPBLENDD_XMMdq_XMMdq_MEMdq_IMMb` — `VPBLENDD`
- `VPBLENDD_XMMdq_XMMdq_XMMdq_IMMb` — `VPBLENDD`
- `VPBLENDD_YMMqq_YMMqq_MEMqq_IMMb` — `VPBLENDD`
- `VPBLENDD_YMMqq_YMMqq_YMMqq_IMMb` — `VPBLENDD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPBLENDVB

`VPBLENDVB` selects byte elements from two sources under an immediate or mask control. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`; `YMM YMM MEM YMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPBLENDVB_XMMdq_XMMdq_MEMdq_XMMdq` — `VPBLENDVB`
- `VPBLENDVB_XMMdq_XMMdq_XMMdq_XMMdq` — `VPBLENDVB`
- `VPBLENDVB_YMMqq_YMMqq_MEMqq_YMMqq` — `VPBLENDVB`
- `VPBLENDVB_YMMqq_YMMqq_YMMqq_YMMqq` — `VPBLENDVB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPBLENDW

`VPBLENDW` selects 16-bit word elements from two sources under an immediate or mask control. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`; `YMM YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPBLENDW_XMMdq_XMMdq_MEMdq_IMMb` — `VPBLENDW`
- `VPBLENDW_XMMdq_XMMdq_XMMdq_IMMb` — `VPBLENDW`
- `VPBLENDW_YMMqq_YMMqq_MEMqq_IMMb` — `VPBLENDW`
- `VPBLENDW_YMMqq_YMMqq_YMMqq_IMMb` — `VPBLENDW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMPESTRI

`VPCMPESTRI` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 4 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `STTNI`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `EAX EDX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMPESTRI_XMMdq_MEMdq_IMMb` — `VPCMPESTRI`
- `VPCMPESTRI_XMMdq_XMMdq_IMMb` — `VPCMPESTRI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMPESTRI64

`VPCMPESTRI64` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `STTNI`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `RAX RDX RCX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMPESTRI64_XMMdq_MEMdq_IMMb` — `VPCMPESTRI64`
- `VPCMPESTRI64_XMMdq_XMMdq_IMMb` — `VPCMPESTRI64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMPESTRM

`VPCMPESTRM` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 4 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `STTNI`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `EAX EDX XMM0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMPESTRM_XMMdq_MEMdq_IMMb` — `VPCMPESTRM`
- `VPCMPESTRM_XMMdq_XMMdq_IMMb` — `VPCMPESTRM`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMPESTRM64

`VPCMPESTRM64` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `STTNI`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `RAX RDX XMM0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMPESTRM64_XMMdq_MEMdq_IMMb` — `VPCMPESTRM64`
- `VPCMPESTRM64_XMMdq_XMMdq_IMMb` — `VPCMPESTRM64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMPISTRI

`VPCMPISTRI` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 4 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `STTNI`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMPISTRI_XMMdq_MEMdq_IMMb` — `VPCMPISTRI`
- `VPCMPISTRI_XMMdq_XMMdq_IMMb` — `VPCMPISTRI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMPISTRI64

`VPCMPISTRI64` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `STTNI`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `RCX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMPISTRI64_XMMdq_MEMdq_IMMb` — `VPCMPISTRI64`
- `VPCMPISTRI64_XMMdq_XMMdq_IMMb` — `VPCMPISTRI64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMPISTRM

`VPCMPISTRM` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `STTNI`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `XMM0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMPISTRM_XMMdq_MEMdq_IMMb` — `VPCMPISTRM`
- `VPCMPISTRM_XMMdq_XMMdq_IMMb` — `VPCMPISTRM`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPERM2F128

`VPERM2F128` reorders its encoded scalar or vector elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM YMM MEM IMM`; `YMM YMM YMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPERM2F128_YMMqq_YMMqq_MEMqq_IMMb` — `VPERM2F128`
- `VPERM2F128_YMMqq_YMMqq_YMMqq_IMMb` — `VPERM2F128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPERM2I128

`VPERM2I128` reorders its encoded scalar or vector elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX2`
- XED category/categories: `AVX2`
- ISA set(s): `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM YMM MEM IMM`; `YMM YMM YMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPERM2I128_YMMqq_YMMqq_MEMqq_IMMb` — `VPERM2I128`
- `VPERM2I128_YMMqq_YMMqq_YMMqq_IMMb` — `VPERM2I128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDD

`VPHADDD` adds corresponding 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDD_XMMdq_XMMdq_MEMdq` — `VPHADDD`
- `VPHADDD_XMMdq_XMMdq_XMMdq` — `VPHADDD`
- `VPHADDD_YMMqq_YMMqq_MEMqq` — `VPHADDD`
- `VPHADDD_YMMqq_YMMqq_YMMqq` — `VPHADDD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDSW

`VPHADDSW` adds corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDSW_XMMdq_XMMdq_MEMdq` — `VPHADDSW`
- `VPHADDSW_XMMdq_XMMdq_XMMdq` — `VPHADDSW`
- `VPHADDSW_YMMqq_YMMqq_MEMqq` — `VPHADDSW`
- `VPHADDSW_YMMqq_YMMqq_YMMqq` — `VPHADDSW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDW

`VPHADDW` adds corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDW_XMMdq_XMMdq_MEMdq` — `VPHADDW`
- `VPHADDW_XMMdq_XMMdq_XMMdq` — `VPHADDW`
- `VPHADDW_YMMqq_YMMqq_MEMqq` — `VPHADDW`
- `VPHADDW_YMMqq_YMMqq_YMMqq` — `VPHADDW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHMINPOSUW

`VPHMINPOSUW` selects minima of corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHMINPOSUW_XMMdq_MEMdq` — `VPHMINPOSUW`
- `VPHMINPOSUW_XMMdq_XMMdq` — `VPHMINPOSUW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHSUBD

`VPHSUBD` subtracts corresponding 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHSUBD_XMMdq_XMMdq_MEMdq` — `VPHSUBD`
- `VPHSUBD_XMMdq_XMMdq_XMMdq` — `VPHSUBD`
- `VPHSUBD_YMMqq_YMMqq_MEMqq` — `VPHSUBD`
- `VPHSUBD_YMMqq_YMMqq_YMMqq` — `VPHSUBD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHSUBSW

`VPHSUBSW` subtracts corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHSUBSW_XMMdq_XMMdq_MEMdq` — `VPHSUBSW`
- `VPHSUBSW_XMMdq_XMMdq_XMMdq` — `VPHSUBSW`
- `VPHSUBSW_YMMqq_YMMqq_MEMqq` — `VPHSUBSW`
- `VPHSUBSW_YMMqq_YMMqq_YMMqq` — `VPHSUBSW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHSUBW

`VPHSUBW` subtracts corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHSUBW_XMMdq_XMMdq_MEMdq` — `VPHSUBW`
- `VPHSUBW_XMMdq_XMMdq_XMMdq` — `VPHSUBW`
- `VPHSUBW_YMMqq_YMMqq_MEMqq` — `VPHSUBW`
- `VPHSUBW_YMMqq_YMMqq_YMMqq` — `VPHSUBW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMASKMOVD

`VPMASKMOVD` copies 32-bit doubleword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX2`
- XED category/categories: `AVX2`
- ISA set(s): `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM XMM`; `MEM YMM YMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMASKMOVD_MEMdq_XMMdq_XMMdq` — `VPMASKMOVD`
- `VPMASKMOVD_MEMqq_YMMqq_YMMqq` — `VPMASKMOVD`
- `VPMASKMOVD_XMMdq_XMMdq_MEMdq` — `VPMASKMOVD`
- `VPMASKMOVD_YMMqq_YMMqq_MEMqq` — `VPMASKMOVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMASKMOVQ

`VPMASKMOVQ` copies 64-bit quadword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX2`
- XED category/categories: `AVX2`
- ISA set(s): `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM XMM`; `MEM YMM YMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMASKMOVQ_MEMdq_XMMdq_XMMdq` — `VPMASKMOVQ`
- `VPMASKMOVQ_MEMqq_YMMqq_YMMqq` — `VPMASKMOVQ`
- `VPMASKMOVQ_XMMdq_XMMdq_MEMdq` — `VPMASKMOVQ`
- `VPMASKMOVQ_YMMqq_YMMqq_MEMqq` — `VPMASKMOVQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMOVMSKB

`VPMOVMSKB` extracts vector sign bits and packs them into an integer mask. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 XMM`; `VGPR32 YMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMOVMSKB_GPR32d_XMMdq` — `VPMOVMSKB`
- `VPMOVMSKB_GPR32d_YMMqq` — `VPMOVMSKB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPOR

`VPOR` computes bitwise OR over its encoded scalar or vector elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `LOGICAL`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPOR_XMMdq_XMMdq_MEMdq` — `VPOR`
- `VPOR_XMMdq_XMMdq_XMMdq` — `VPOR`
- `VPOR_YMMqq_YMMqq_MEMqq` — `VPOR`
- `VPOR_YMMqq_YMMqq_YMMqq` — `VPOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSIGNB

`VPSIGNB` conditionally negates, zeros, or preserves each packed integer element according to the sign of the corresponding control element. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPSIGNB_XMMdq_XMMdq_MEMdq` — `VPSIGNB`
- `VPSIGNB_XMMdq_XMMdq_XMMdq` — `VPSIGNB`
- `VPSIGNB_YMMqq_YMMqq_MEMqq` — `VPSIGNB`
- `VPSIGNB_YMMqq_YMMqq_YMMqq` — `VPSIGNB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSIGND

`VPSIGND` conditionally negates, zeros, or preserves each packed integer element according to the sign of the corresponding control element. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPSIGND_XMMdq_XMMdq_MEMdq` — `VPSIGND`
- `VPSIGND_XMMdq_XMMdq_XMMdq` — `VPSIGND`
- `VPSIGND_YMMqq_YMMqq_MEMqq` — `VPSIGND`
- `VPSIGND_YMMqq_YMMqq_YMMqq` — `VPSIGND`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSIGNW

`VPSIGNW` conditionally negates, zeros, or preserves each packed integer element according to the sign of the corresponding control element. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `AVX`, `AVX2`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPSIGNW_XMMdq_XMMdq_MEMdq` — `VPSIGNW`
- `VPSIGNW_XMMdq_XMMdq_XMMdq` — `VPSIGNW`
- `VPSIGNW_YMMqq_YMMqq_MEMqq` — `VPSIGNW`
- `VPSIGNW_YMMqq_YMMqq_YMMqq` — `VPSIGNW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPTEST

`VPTEST` tests vector bits or lanes and reduces the selected result into flags or mask state. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `LOGICAL`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`; `YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPTEST_XMMdq_MEMdq` — `VPTEST`
- `VPTEST_XMMdq_XMMdq` — `VPTEST`
- `VPTEST_YMMqq_MEMqq` — `VPTEST`
- `VPTEST_YMMqq_YMMqq` — `VPTEST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPXOR

`VPXOR` computes bitwise XOR over its encoded scalar or vector elements and writes the lane-wise result. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`
- XED category/categories: `LOGICAL`
- ISA set(s): `AVX`, `AVX2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPXOR_XMMdq_XMMdq_MEMdq` — `VPXOR`
- `VPXOR_XMMdq_XMMdq_XMMdq` — `VPXOR`
- `VPXOR_YMMqq_YMMqq_MEMqq` — `VPXOR`
- `VPXOR_YMMqq_YMMqq_YMMqq` — `VPXOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VRCPPS

`VRCPPS` computes approximate reciprocals of packed single-precision floating-point elements. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`; `YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VRCPPS_XMMdq_MEMdq` — `VRCPPS`
- `VRCPPS_XMMdq_XMMdq` — `VRCPPS`
- `VRCPPS_YMMqq_MEMqq` — `VRCPPS`
- `VRCPPS_YMMqq_YMMqq` — `VRCPPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VRCPSS

`VRCPSS` computes approximate reciprocals of a scalar single-precision floating-point element. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VRCPSS_XMMdq_XMMdq_MEMd` — `VRCPSS`
- `VRCPSS_XMMdq_XMMdq_XMMd` — `VRCPSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VROUNDPD

`VROUNDPD` forms products of selected source elements and accumulates grouped dot-product sums. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`; `YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VROUNDPD_XMMdq_MEMdq_IMMb` — `VROUNDPD`
- `VROUNDPD_XMMdq_XMMdq_IMMb` — `VROUNDPD`
- `VROUNDPD_YMMqq_MEMqq_IMMb` — `VROUNDPD`
- `VROUNDPD_YMMqq_YMMqq_IMMb` — `VROUNDPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VROUNDPS

`VROUNDPS` forms products of selected source elements and accumulates grouped dot-product sums. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`; `YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VROUNDPS_XMMdq_MEMdq_IMMb` — `VROUNDPS`
- `VROUNDPS_XMMdq_XMMdq_IMMb` — `VROUNDPS`
- `VROUNDPS_YMMqq_MEMqq_IMMb` — `VROUNDPS`
- `VROUNDPS_YMMqq_YMMqq_IMMb` — `VROUNDPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VROUNDSD

`VROUNDSD` rounds a scalar double-precision floating-point element according to immediate rounding control using the VEX-encoded three-operand form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VROUNDSD_XMMdq_XMMdq_MEMq_IMMb` — `VROUNDSD`
- `VROUNDSD_XMMdq_XMMdq_XMMq_IMMb` — `VROUNDSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VROUNDSS

`VROUNDSS` rounds a scalar single-precision floating-point element according to immediate rounding control using the VEX-encoded three-operand form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VROUNDSS_XMMdq_XMMdq_MEMd_IMMb` — `VROUNDSS`
- `VROUNDSS_XMMdq_XMMdq_XMMd_IMMb` — `VROUNDSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VRSQRTPS

`VRSQRTPS` computes square roots of packed single-precision floating-point elements. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`; `YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VRSQRTPS_XMMdq_MEMdq` — `VRSQRTPS`
- `VRSQRTPS_XMMdq_XMMdq` — `VRSQRTPS`
- `VRSQRTPS_YMMqq_MEMqq` — `VRSQRTPS`
- `VRSQRTPS_YMMqq_YMMqq` — `VRSQRTPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VRSQRTSS

`VRSQRTSS` computes square roots of a scalar single-precision floating-point element. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VRSQRTSS_XMMdq_XMMdq_MEMd` — `VRSQRTSS`
- `VRSQRTSS_XMMdq_XMMdq_XMMd` — `VRSQRTSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSTMXCSR

`VSTMXCSR` stores MXCSR through the VEX-encoded form of the floating-point control-state store. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `MXCSR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSTMXCSR_MEMd` — `VSTMXCSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VTESTPD

`VTESTPD` tests vector bits or lanes and reduces the selected result into flags or mask state. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `LOGICAL_FP`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`; `YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VTESTPD_XMMdq_MEMdq` — `VTESTPD`
- `VTESTPD_XMMdq_XMMdq` — `VTESTPD`
- `VTESTPD_YMMqq_MEMqq` — `VTESTPD`
- `VTESTPD_YMMqq_YMMqq` — `VTESTPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VTESTPS

`VTESTPS` tests vector bits or lanes and reduces the selected result into flags or mask state. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `LOGICAL_FP`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`; `YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VTESTPS_XMMdq_MEMdq` — `VTESTPS`
- `VTESTPS_XMMdq_XMMdq` — `VTESTPS`
- `VTESTPS_YMMqq_MEMqq` — `VTESTPS`
- `VTESTPS_YMMqq_YMMqq` — `VTESTPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VZEROALL

`VZEROALL` clears the architecturally visible contents of the vector registers covered by the instruction's AVX state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VZEROALL` — `VZEROALL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VZEROUPPER

`VZEROUPPER` clears the upper portions of YMM registers while preserving the low 128 bits, avoiding transition penalties when mixing AVX and legacy SSE code on affected processors. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VZEROUPPER` — `VZEROUPPER`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
