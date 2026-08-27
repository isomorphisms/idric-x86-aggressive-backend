# ADOX

`ADOX` adds unsigned operands using the overflow flag as a carry chain. The pinned XED inventory represents it with 12 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `ADOX_ADCX`
- XED category/categories: `ADOX_ADCX`, `APX`
- ISA set(s): `ADOX_ADCX`, `APX_F_ADX`, `APX_F_ADX_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 GPR32 GPR32`; `GPR32 GPR32 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `ADOX_GPR32d_GPR32d` — `ADOX`
- `ADOX_GPR32d_MEMd` — `ADOX`
- `ADOX_GPR32i32_GPR32i32_APX` — `ADOX`
- `ADOX_GPR32i32_GPR32i32_GPR32i32_APX_N3` — `ADOX`
- `ADOX_GPR32i32_GPR32i32_MEMi32_APX_N3` — `ADOX`
- `ADOX_GPR32i32_MEMi32_APX` — `ADOX`
- `ADOX_GPR64i64_GPR64i64_APX` — `ADOX`
- `ADOX_GPR64i64_GPR64i64_GPR64i64_APX_N3` — `ADOX`
- `ADOX_GPR64i64_GPR64i64_MEMi64_APX_N3` — `ADOX`
- `ADOX_GPR64i64_MEMi64_APX` — `ADOX`
- `ADOX_GPR64q_GPR64q` — `ADOX`
- `ADOX_GPR64q_MEMq` — `ADOX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
