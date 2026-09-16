import Std

/-! Natural-number inventory only. No entropy, norm, or quantum result is assumed. -/
namespace SchurInventory

theorem square_environment_capacity (m k r : Nat)
    (supportFits : r ≤ m) (krausFits : k ≤ m * r) : k ≤ m * m := by
  exact Nat.le_trans krausFits (Nat.mul_le_mul_left m supportFits)

theorem extreme_rank_floor (m k r : Nat)
    (occupied : 1 ≤ r) (orthogonalCopies : k * r ≤ m) : k ≤ m := by
  have h : k * 1 ≤ k * r := Nat.mul_le_mul_left k occupied
  simpa using Nat.le_trans h orthogonalCopies

theorem epoch_partition (N L : Nat) :
    N % L + L * (N / L) = N := by
  exact Nat.mod_add_div N L

theorem epoch_tail_lt (N L : Nat) (positive : 0 < L) : N % L < L := by
  exact Nat.mod_lt N positive

theorem block_wait (length delay : Nat)
    (positive : 1 ≤ length) (fits : length ≤ delay) :
    length - 1 ≤ delay - 1 := by omega

theorem custody_bound (bath block delay : Nat) (fits : block ≤ delay) :
    bath + 2 * block ≤ bath + 2 * delay := by omega

#print axioms square_environment_capacity
#print axioms extreme_rank_floor
#print axioms epoch_partition
#print axioms epoch_tail_lt
#print axioms block_wait
#print axioms custody_bound
end SchurInventory
