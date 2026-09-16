import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.RCLike.Basic
import Mathlib.Analysis.Complex.Basic

set_option autoImplicit false

/-! Finite-dimensional complex quantum states and the bath-only closing theorem.
The user index may include every output and arbitrary finite references.
No entropy, norm bound, or asymptotic theorem is assumed or claimed here. -/

open Matrix
open scoped BigOperators ComplexOrder

namespace ClosedMemory

noncomputable section

variable {A B : Type*} [Fintype A] [Fintype B] [DecidableEq A] [DecidableEq B]

structure Density (I : Type*) [Fintype I] where
  matrix : Matrix I I ℂ
  positive : matrix.PosSemidef
  normalized : matrix.trace = 1

/-- A concrete legal pure initializer in every nonempty finite dimension. -/
def basisState (a : A) : Density A where
  matrix := Matrix.diagonal fun i => if i = a then 1 else 0
  positive := Matrix.PosSemidef.diagonal (by
    intro i
    dsimp
    split_ifs <;> simp)
  normalized := by simp [Matrix.trace, Matrix.diag, Matrix.diagonal]

def partialTrace (X : Matrix (A × B) (A × B) ℂ) : Matrix A A ℂ :=
  fun a a' => ∑ b, X (a,b) (a',b)

def bathLift (U : Matrix B B ℂ) : Matrix (A × B) (A × B) ℂ :=
  fun ab ab' => if ab.1 = ab'.1 then U ab.2 ab'.2 else 0

theorem partialTrace_positive (X : Matrix (A × B) (A × B) ℂ)
    (hX : X.PosSemidef) : (partialTrace X).PosSemidef := by
  have hs (s : Finset B) :
      (∑ b ∈ s, X.submatrix (fun a => (a,b)) (fun a => (a,b))).PosSemidef := by
    induction s using Finset.induction_on with
    | empty => simpa using (Matrix.PosSemidef.zero : (0 : Matrix A A ℂ).PosSemidef)
    | @insert b s hb ih =>
      rw [Finset.sum_insert hb]
      exact (hX.submatrix (fun a => (a,b))).add ih
  have he : partialTrace X =
      ∑ b : B, X.submatrix (fun a => (a,b)) (fun a => (a,b)) := by
    ext a a'
    simp [partialTrace, Matrix.sum_apply]
  rw [he]
  exact hs Finset.univ

theorem partialTrace_trace (X : Matrix (A × B) (A × B) ℂ) :
    (partialTrace X).trace = X.trace := by
  simp [partialTrace, Matrix.trace, Matrix.diag, Fintype.sum_prod_type]

def userState (rho : Density (A × B)) : Density A where
  matrix := partialTrace rho.matrix
  positive := partialTrace_positive _ rho.positive
  normalized := (partialTrace_trace _).trans rho.normalized

theorem bathLift_adjoint (U : Matrix B B ℂ) :
    (bathLift (A := A) U)ᴴ = bathLift Uᴴ := by
  ext ⟨a,b⟩ ⟨a',b'⟩
  by_cases h : a = a'
  · subst a'
    simp [bathLift, Matrix.conjTranspose_apply]
  · simp only [bathLift, Matrix.conjTranspose_apply, if_neg h,
      if_neg (Ne.symm h), star_zero]

theorem bathLift_isometry (U : Matrix B B ℂ) (hU : Uᴴ * U = 1) :
    (bathLift (A := A) U)ᴴ * bathLift U = 1 := by
  ext ⟨a,b⟩ ⟨a',b'⟩
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, bathLift,
    Fintype.sum_prod_type, apply_ite]
  by_cases ha : a = a'
  · subst a'
    simpa [Matrix.one_apply, ← Matrix.mul_apply, Matrix.conjTranspose_apply] using
      congrArg (fun M : Matrix B B ℂ => M b b') hU
  · simp [ha, Ne.symm ha, Prod.ext_iff]

def conjugate (X U : Matrix (A × B) (A × B) ℂ) := U * X * Uᴴ

theorem conjugate_positive (X U : Matrix (A × B) (A × B) ℂ)
    (hX : X.PosSemidef) : (conjugate X U).PosSemidef :=
  hX.mul_mul_conjTranspose_same U

theorem conjugate_trace (X U : Matrix (A × B) (A × B) ℂ)
    (hU : Uᴴ * U = 1) : (conjugate X U).trace = X.trace := by
  rw [conjugate, trace_mul_cycle, hU, Matrix.one_mul]

def closeBath (rho : Density (A × B)) (U : Matrix B B ℂ)
    (hU : Uᴴ * U = 1) : Density (A × B) where
  matrix := conjugate rho.matrix (bathLift U)
  positive := conjugate_positive _ _ rho.positive
  normalized := (conjugate_trace rho.matrix (bathLift U)
    (bathLift_isometry (A := A) U hU)).trans rho.normalized

def bathBlock (X : Matrix (A × B) (A × B) ℂ) (a a' : A) : Matrix B B ℂ :=
  fun b b' => X (a,b) (a',b')

theorem bathBlock_conjugate (X : Matrix (A × B) (A × B) ℂ)
    (U : Matrix B B ℂ) (a a' : A) :
    bathBlock (conjugate X (bathLift U)) a a' =
      U * bathBlock X a a' * Uᴴ := by
  ext b b'
  simp [bathBlock, conjugate, bathLift, Matrix.mul_apply,
    Matrix.conjTranspose_apply, Fintype.sum_prod_type, apply_ite,
    ite_mul, Finset.sum_mul]

theorem partialTrace_close (X : Matrix (A × B) (A × B) ℂ)
    (U : Matrix B B ℂ) (hU : Uᴴ * U = 1) :
    partialTrace (conjugate X (bathLift U)) = partialTrace X := by
  ext a a'
  change (bathBlock (conjugate X (bathLift U)) a a').trace =
    (bathBlock X a a').trace
  rw [bathBlock_conjugate, trace_mul_cycle, hU, Matrix.one_mul]

/-- Closing an active bath changes no entry of the complete user density matrix,
even when that user and bath were initially correlated. -/
theorem closing_preserves_complete_user (rho : Density (A × B))
    (U : Matrix B B ℂ) (hU : Uᴴ * U = 1) :
    partialTrace (closeBath rho U hU).matrix = partialTrace rho.matrix :=
  partialTrace_close rho.matrix U hU

#print axioms partialTrace_positive
#print axioms partialTrace_trace
#print axioms bathLift_adjoint
#print axioms bathLift_isometry
#print axioms conjugate_positive
#print axioms conjugate_trace
#print axioms partialTrace_close
#print axioms closing_preserves_complete_user

end
end ClosedMemory
