# Ancillary checks

`python ancillary/check_schur.py` requires NumPy and performs finite convention
checks: the known ququart Kraus operators, their independent products and
flat normalized Choi spectrum, the tetrahedral inverse on all 2-by-2 matrix
units, and a fixed small Gaussian realization with both polar normalizations.
It includes one three-dimensional reference input. Seed 20260915, k=r=2,
m=128, absolute Frobenius tolerance 2e-11. The sample is a diagnostic, not a
randomized proof or an implementation at the theorem's conservative m.

The diagnostics do not optimize diamond distance, prove concentration, prove
entropy continuity, establish an asymptotic law, or certify novelty.

`python ancillary/check_package.py` tests publication integrity separately:
portable LF checksums, rejection of duplicate or malformed manifests, unexpected
build/cache files, and changed payload bytes. Temporary fixtures are removed at
the end of the test; no scientific sources are modified.

`lean/COVERAGE.md` states the exact partial formal scope and reproduction command.
All source code is MIT-licensed; mathematical manuscript text is CC BY 4.0.
