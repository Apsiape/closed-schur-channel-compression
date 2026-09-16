# Post-review validation: September 15, 2026

This record describes the revised candidate following three independent
AI-session reviews and an author-side response checking their recommendations.
The reviews found no defect in the eight main statements, but requested scope,
attribution, and packaging corrections. This is not human peer review, full
formal verification, or exhaustive novelty certification. Publication remains
an explicit later action.

## Mathematical integration

- Full two-polar proof retained, including one simultaneous Gaussian event,
  square unitary completion, common virtual environment and arbitrary references.
- Exact extremality argument kept separate from approximation. Corollary 5
  explicitly restricts the finite-error statements to T >= 2.
- Choi-support partial trace now explicitly produces transposed Kraus products;
  the full-domain inverse is linear and need not be positive. A finite block
  expansion explicitly bounds its norm uniformly over every spectator dimension.
- The epoch proof retains one physical residual and every outward d-dimensional
  factor. The scheduled upper assumes mandatory arrivals, identical releases,
  and no incomplete-block flush. Payload custody is separately counted.
- Unrelated Werner-Holevo, public-record and general unital-compiler material
  remains in preserved research history, not this paper.
- The abstract now qualifies the error-dependent converse and states existence
  rather than promising efficient synthesis. Gram and minimal Kraus rank are
  identified explicitly. The joint-input and closed scheduled contracts are
  stated where used and beneath the combined table.
- The linear inverse norm 3 is proved optimal among linear extensions. This
  does not establish an optimal physical logarithmic-delay frontier.
- Complete dephasing is an explicit negative control for removing extremality.

## Completed executable checks

All diagnostic/build processes used a Windows job memory cap and explicit wall
timeout. Numerical checks used one numerical thread. No background job was left
running. No unrelated AK suite was run.

| Check | Result |
| --- | --- |
| Offline TeX build, BibTeX, two resolving TeX passes | PASS on revised source; 25 pages and 17 cited references; no overfull boxes, undefined citations/references, or multiply-defined labels |
| Poppler page rendering | PASS; all 25 revised pages rendered and visually inspected in contact sheets, with selected dense pages inspected individually |
| Layout | Rate and resource tables remain together; no clipping or overlapping material found |
| Finite Schur diagnostic | PASS at tolerance 2e-11; TP, minimum product-family singular value 0.81649658, Choi spectrum, SIC identities, inverse and partial-trace conventions |
| Fixed Gaussian indexing/control | PASS; k=r=2,m=128, seed 20260915; simultaneous defect 0.17225594, dilation-vector discrepancy 0.08302337 |
| Finite reference diagnostic | PASS; three-dimensional reference, half trace distance 0.02259361 below the dilation discrepancy |
| Lean Inventory.lean | Fresh rerun PASS, six dependency closures; no admitted proof or scientific axiom |
| Lean ActiveBath.lean | Fresh rerun PASS against pinned Lean/mathlib, eight dependency closures; only standard foundations; harmless unused-section-variable linter warnings |
| Package regression controls | PASS; rejects CRLF checksums, duplicates, missing final newline, stray build/cache files, and modified payload bytes |

During the earlier finishing pass, the first attempted Lean cache had matching revisions but lacked an imported
object file and correctly failed. A complete matching read-only cache was then
used; no dependencies or source corpora were altered or downloaded. This was
not a retry after a resource-limit failure.

Commands, from the repository root unless noted:

    python scripts/build.py --refresh-tex --pandoc PATH_TO_PANDOC
    python ancillary/check_schur.py
    python ancillary/check_package.py
    python scripts/verify.py
    python scripts/verify.py --rebuilt build/manuscript.pdf
    python scripts/export.py

The package commands verify the public allowlist, complete PDF/TeX metadata,
citation keys, source hashes, absence of local machine paths/placeholders, and
the clean export's checksums. A rebuilt-PDF check compares extracted text page
by page. It is not a substitute for visual review.

Frozen exports are rebuilt outside their own directories using
`python scripts/build.py --output-dir PATH_OUTSIDE_EXPORT`. The verifier checks
every file without exempting build or cache folders. ZIP creation uses the
explicit allowlist plus the LF-terminated checksum manifest, not recursive
directory archiving. Existing earlier candidates remain preserved and must not
be substituted for the newly verified package.

Lean rerun, from ancillary/lean:

    python run_checked.py --packages PATH_TO_LAKE_PACKAGES --log NEW-CHECK.txt ActiveBath.lean Inventory.lean

Build/render/numerical diagnostics used 512 MiB; the Lean dependency run used
1536 MiB. Timeouts were 60 seconds for small diagnostics and rendering, and
180 seconds for multi-pass build and Lean. Public helpers remain portable and
expect the user to supply platform-appropriate limits.

## Literature and bibliographic scope

Primary arXiv records/full texts were rechecked for Terhal et al., Zalka-Rieffel,
Haagerup-Musat, Kotowski-Kotowski, Lancien-Winter, Audenaert, Winter, Gutoski,
and Holevo. Following review, the primary Rybár-Ziman, both Bisio, and
Faist-Berta-Brandão sources were additionally checked and cited. Theorem-level
comparison focused on the nearest contracts:
mixed environments, exact-on-success randomization, and small-Kraus output
approximation. This is a bounded comparison, not worldwide novelty certification.
Classical citations include Choi, Araki-Lieb and Stinespring with complete
published bibliographic metadata. DOI resolution is not assumed to establish
the mathematical statement of any cited theorem.

The Haagerup-Musat diagonal entries were checked in the primary arXiv PDF;
publisher PDF access was unavailable, so a separate inspection of the printed
journal pages is not claimed. The manuscript states the adjoint convention
and derives CPTP extremality using Choi's criterion. Terhal et al. receive
credit for the known rank scale and qualitative extreme-channel obstruction;
no unrestricted prohibition on harmless mixed spectators is asserted.
Two additional recent suggestions were inspected at relevant sections and
were not used as theorem dependencies. The scope remains a bounded comparison.

The self-citation to the companion closed-process paper was reconciled with
its local manuscript, citation record and byte-verified public v1.0.0 release
evidence. Its DOI is 10.5281/zenodo.22779673. A fresh public-record web fetch
was unavailable, so this pass does not claim it independently retrieved that
record. No proof relies on a result from that companion paper.

## Release boundary

No commit, push, tag, remote creation, publication, DOI minting, or collaborator
contact occurred. Existing private sources and untracked edits were preserved.
The intended repository name is closed-schur-channel-compression. The active
checkout was not renamed; rename and reconcile pointers after work is idle.
The allowlisted export, rather than the historical working tree, is the clean
publication candidate. Initial Git history and a remote still need the owner's
authorization; their absence is not a defect in the mathematical proofs.
