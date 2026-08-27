# SIMD / vectors

ARMv7 uses NEON/VFP-family vector instructions; AArch64 uses Advanced SIMD/FP; Intel Macs use SSE/AVX families; historical PowerPC Macs may use VMX/AltiVec. Express vector operations semantically and let each follower select the available family.
