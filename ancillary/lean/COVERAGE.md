# Partial formal coverage

The paper's headline theorems are **not fully Lean-formalized**. The formal
artifacts certify the precise finite statements below, not the concentration,
entropy, approximation, or asymptotic proofs.

## Inherited finite quantum statement

ActiveBath.lean is an unchanged MIT-licensed component of the author's companion
closed-process-memory package, with hash and attribution in SOURCE-MAP.json.
It defines positive-semidefinite trace-one complex matrices, explicit partial
trace, bath lifting, and unitary conjugation. It proves that acting only on the
bath leaves the entire retained user marginal unchanged, allowing arbitrary
initial correlations and finite references. It also proves that the reduced
and conjugated states remain lawful density matrices.

This supports the elementary no-signalling bookkeeping used at a cut. It does
not prove the stronger support-inverse decoupling theorem, an entropy inequality,
or the epoch lower bound. Reusing this lemma is not a new scientific result.

Eight dependency reports cover partialTrace_positive, partialTrace_trace,
bathLift_adjoint, bathLift_isometry, conjugate_positive, conjugate_trace,
partialTrace_close, and closing_preserves_complete_user.

## New elementary inventory statements

Inventory.lean imports only Std and proves:

1. r <= m and k <= m*r imply k <= m*m.
2. r >= 1 and k*r <= m imply k <= m.
3. N % L + L*(N/L) = N.
4. The epoch tail is shorter than L when L > 0.
5. A block of length at most b waits at most b-1 rounds.
6. At most b ququarts add at most 2b qubits to a declared bath inventory.

These are natural-number implications only. Their hypotheses are not asserted
as quantum axioms; the manuscript supplies the separate physical arguments.

## Reproduction

Lean 4.30.0, commit d024af099ca4bf2c86f649261ebf59565dc8c622.
Mathlib c5ea00351c28e24afc9f0f84379aa41082b1188f; all package revisions in
dependencies.lock.json. With an existing matching Lake package cache, run from
this directory:

    python run_checked.py --packages PATH_TO_LAKE_PACKAGES --log NEW-CHECK.txt ActiveBath.lean Inventory.lean

Use an output log outside a frozen checksummed export. The runner verifies the
kernel version, package revisions and mathlib HEAD, then checks every requested
dependency closure against only propext, Classical.choice and Quot.sound.
It refuses admissions or unexpected axioms and performs no network access.
The accompanying LEAN-CHECK.txt records the actual completed run.

There is no claim that full analytic formalization is impossible. It has not
been completed here: stabilized channel norms, entropy continuity, probabilistic
matrix estimates, polar repair, and asymptotic limits still require separate
formal development. The human-readable proofs are complete independently of
this partial artifact.
