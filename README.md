# Closed Mixed-Apparatus Compression of Schur Channels: Exact-Approximate Separation and Scheduled Delivery

Seth Douglas | [seth.douglas@gmail.com](mailto:seth.douglas@gmail.com)

**Status:** manuscript candidate revised following independent AI-session reviews.
Not published; no release, repository URL, or DOI has been assigned.
The intended repository name is **closed-schur-channel-compression**.

[Read the paper](output/pdf/manuscript.pdf) |
[Readable proof source](paper/manuscript.md) |
[TeX](paper/manuscript.tex) |
[Theorem and evidence map](THEOREMS.md)

## What the paper establishes

A Schur channel on a d-dimensional system, with Gram rank k, admits an
approximate implementation by one fixed square unitary using apparatus dimension
O(epsilon^-2 (sqrt(k) + ln d)). Its initializer is maximally mixed on a
rank-Theta(sqrt(k)) support. The guarantee is unconditional half diamond error
at most epsilon, including arbitrary references. There is no free public seed,
postselection, reset, or accessible purifier.

For the known extreme rank-two ququart channel, T tensor factors have:

- Exact joint service, with all T inputs presented together: minimum initial
  entropy deficit P = T and log-dimension Q = T.
- Joint half diamond error T^-4 (T >= 2): Q = T/2 + O(log T), P = O(log T),
  with matching first-order Q lower bound.
- A separate scheduled-delivery consequence: sublogarithmic delay forces
  P,Q >= T-o(T); superlogarithmic delay permits P=o(T), Q=T/2+o(T).

Both halves of the scheduled statement require the specified error T^-4,
mandatory arrivals, identical real/ideal release schedules, and observation-only
stopping without flushing an incomplete block. The device is closed: no fresh
ancillary supplies arrive after time zero. Retained user
payload adds up to 2b qubits beyond the initial apparatus. Gate efficiency,
arbitrary-channel compression, autonomous timing, and the critical-delay optimum
are not proved. This is separate from the immediate repeated-interaction paper
[Bath dimension and initial entropy](https://doi.org/10.5281/zenodo.22779673).

## Reproduce

Python 3.10+, NumPy and pypdf are listed in requirements.txt. A standard TeX
installation with pdflatex and bibtex builds the distributed TeX offline:

    python scripts/build.py

The rebuilt PDF is placed in ignored build/, never over the distributed PDF.
To regenerate TeX from the authoritative Markdown, additionally install Pandoc
and run:

    python scripts/build.py --refresh-tex

Use --pandoc PATH if it is not on PATH. The template and BibTeX source are in
paper/. No helper installs or downloads dependencies automatically.

Run finite checks and package checks:

    python ancillary/check_schur.py
    python ancillary/check_package.py
    python scripts/verify.py
    python scripts/verify.py --rebuilt build/manuscript.pdf

Rebuilt PDFs are compared by extracted page text, not bytes, because timestamps
and PDF identifiers can vary. Any manuscript change additionally requires visual
inspection. Recorded validation is in [VALIDATION.md](VALIDATION.md).
Use appropriate operating-system memory and time limits for your environment.

### Partial Lean, not headline formalization

[Coverage](ancillary/lean/COVERAGE.md) distinguishes an inherited finite complex
density-matrix no-signalling theorem from six elementary inventory/epoch lemmas.
Neither Gaussian concentration, entropy bounds, two-polar compression, nor the
asymptotic separation is Lean-formalized. The pinned kernel/dependency report
must not be described as full proof certification.

## Repository and public package

- paper/: complete Markdown, generated TeX, template, and primary bibliography.
- output/pdf/manuscript.pdf: inspected final manuscript candidate.
- ancillary/: finite numerical controls and honest partial Lean coverage.
- scripts/: offline build, verification, and allowlisted export.
- SOURCE-MAP.json: exact scientific inputs and copied-code provenance.
- THEOREMS.md and VALIDATION.md: scope, evidence, and checks.
- LICENSES/, LICENSE.md, CITATION.cff, zenodo/: scoped licensing and metadata.

Run python scripts/export.py to create a new clean directory and ZIP under
public-export/. The ZIP includes only the explicit public allowlist and an
LF-terminated SHA-256 checksum manifest. Existing
private research archives are retained locally and ignored by Git. Never publish
the old research corpus by recursively copying the working directory.

Frozen exports must stay unchanged. Rebuild one with an external output path:

    python scripts/build.py --output-dir PATH_OUTSIDE_EXPORT
    python scripts/verify.py --rebuilt PATH_OUTSIDE_EXPORT/manuscript.pdf

The verifier rejects all unexpected files, including build files and caches.
On systems providing sha256sum, `sha256sum -c SHA256SUMS.txt` additionally checks
the payload bytes. Do not regenerate TeX in a frozen export; edit the working
source and produce a new candidate instead.

The current checkout retains its original folder name during preparation.
Rename it to closed-schur-channel-compression only after active work has ended;
all public links here are relative and no fictitious GitHub address is embedded.

The manuscript is CC BY 4.0; original software is MIT. Read LICENSE.md for scopes.
AI-assisted research and independent AI-session checking are disclosed in the
paper and are not presented as human external peer review.
