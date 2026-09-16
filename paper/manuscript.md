---
title: "Closed Mixed-Apparatus Compression of Schur Channels: Exact-Approximate Separation and Scheduled Delivery"
author: "Seth Douglas"
email: "seth.douglas@gmail.com"
date: "September 15, 2026"
abstract: |
  We study closed unitary implementations of Schur channels when both the full dimension and the entropy deficit of an initially mixed apparatus are charged. Let \(\Phi:M_d\to M_d\) be a Schur channel with Gram rank \(k\), which equals its minimal Kraus rank. For \(0<\epsilon\le1\), we prove by a probabilistic existence argument that there is a square unitary on \(\mathbb C^d\otimes\mathbb C^m\), with
  \[
  m=O\!\left(\epsilon^{-2}(\sqrt{k}+\ln d)\right),
  \]
  and an initially independent apparatus maximally mixed on a rank-\(\Theta(\sqrt{k})\) support, whose induced channel has half-diamond error at most \(\epsilon\). The construction uses no public randomness, measurement, postselection, reset, or accessible purifier. A universal entropy converse gives \(2Q-P\ge S(J_\Phi)\) up to the standard continuity correction, while exact implementation of an extreme channel of Kraus rank \(k\) requires \(P,Q\ge\log_2k\).

  For a known extreme rank-two ququart Schur channel, \(T\) tensor factors presented jointly therefore exhibit an asymptotic exact-versus-vanishing-error separation. Exact service has \(P=Q=T\), while error \(T^{-4}\) admits
  \[
  Q\le \frac T2+8\log_2T+O(1),\qquad
  P\le8\log_2T+O(1),
  \]
  and every implementation at that error satisfies \(Q\ge T/2-o(1)\).

  Under a separate scheduled-delivery contract with mandatory arrivals, a common physical release schedule, and observation-only stopping that never flushes an unfinished block, a support-inverse entropy argument shows that sublogarithmic delay restores \(P,Q\ge T-o(T)\). Superlogarithmic delay permits \(P=o(T)\) and \(Q=T/2+o(T)\) for the initially supplied apparatus. Retained user payloads are separate physical custody and can add \(2b\) qubits at delay \(b\). The results do not provide an efficient compiler, a guarantee for caller-paced arrivals or early flushing, or a sharp frontier at logarithmic delay.
---

# Introduction {.unnumbered}

How much physical environment is needed to implement a noisy channel when the environment may start mixed, but no fresh environment, discarded branch, or public random seed is free? A pure Stinespring environment has dimension equal to the channel's Kraus rank. A mixed environment supplies additional mathematical purification degrees of freedom, but those degrees of freedom cannot be acted upon. Common-unitary compatibility therefore makes a simple rank count insufficient [@terhal1999; @zalka2002].

We prove that Schur channels nevertheless admit an approximate square implementation whose physical apparatus dimension is of order \(\sqrt{k}+\ln d\), multiplied by \(\epsilon^{-2}\). Here \(k\) is the Gram rank, equivalently the minimal Kraus rank. A single random tensor must satisfy two constraints simultaneously: its physical slices must be nearly isometric, and its vectorization must preserve the full Kraus-coordinate space. Separate polar normalizations enforce the two requirements. Orthogonality of the system labels then gives a common-Stinespring operator bound, avoiding any dimension loss when reference systems are included. This is a probabilistic existence proof, not an efficient deterministic synthesis algorithm.

The square-root rank scale is a known counting limit for exact service, not a newly proposed ceiling: a physical environment of dimension \(m\) and state rank \(r\le m\) yields at most \(mr\le m^2\) Kraus operators [@terhal1999]. Our contribution is an approximate Schur construction approaching that scale, with explicit accuracy and dimension overhead and a charged entropy deficit; Section 4 proves optimality of its leading memory rate for a particular tensor-power family. This does not evade the diamond-norm obstruction to reducing Kraus rank discussed by Lancien and Winter [@lancien2024]. The implemented channel may have Kraus rank as large as \(mr\): it is the physical register dimension, not necessarily the Kraus rank, that is compressed.

For a known extreme ququart Schur channel, this produces a sharp leading-order distinction. Exact tensor-power service needs one apparatus qubit and one bit of initial entropy deficit per factor. Polynomially accurate joint service needs only one half apparatus qubit per factor and a vanishing entropy-deficit rate. The distinction is asymptotic in the number of factors, not a discontinuity assertion for a fixed finite system.

A subordinate result asks what survives when outputs have deadlines. Under mandatory arrivals, a shared release schedule, and observation-only stopping, short delays force the exact leading cost, whereas sufficiently long delays permit independent compressed blocks. The scheduling and payload-custody assumptions are part of the theorem, not implementation details.

Section 2 gives the construction; Sections 3--4 establish the matching comparison; Sections 5--9 develop the scheduled consequence. Section 11 distinguishes the results from mixed-environment simulation, low-Kraus-rank approximation, and exact-on-success simulation.

# Model and resource ledger

All resource logarithms and entropies use base two. Natural logarithms are written \(\ln\).

For an apparatus \(C\) of physical dimension \(m\) in state \(\beta\), define
\[
Q(C)=\log_2m,\qquad
P(C)=\log_2m-S(\beta).
\]
Thus \(Q\) charges physical Hilbert-space dimension and \(P\) charges entropy deficit. An inaccessible mathematical purification of \(\beta\) is not physical inventory. If such a purifier were made accessible to the implementation, it would have to be charged.

For states,
\[
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
\]
and for channels we use half diamond distance
\[
D_\diamond(\Phi,\Psi)=\frac12\|\Phi-\Psi\|_\diamond.
\]

A **closed square implementation** of \(\Psi:M_d\to M_d\) consists of a fixed unitary
\[
U:\mathbb C^d\otimes\mathbb C^m
\longrightarrow
\mathbb C^d\otimes\mathbb C^m
\]
and an initial apparatus state \(\beta\), independent of the input and every reference, such that
\[
\Psi(\rho)=\operatorname{Tr}_C U(\rho\otimes\beta)U^\dagger.
\]
The partial trace describes the user's reduced channel; it is not a physical reset or disposal operation available for reuse.


# Closed mixed-apparatus compression of Schur channels

## Theorem 1 -- two-polar Schur compression {.unnumbered}

Let
\[
\Phi(|i\rangle\langle j|)
  =\langle v_j,v_i\rangle |i\rangle\langle j|,
\qquad
v_i\in\mathbb C^k,\quad \|v_i\|=1,
\]
be a Schur channel on \(M_d\), with the \(v_i\) spanning \(\mathbb C^k\). Its Gram matrix and normalized Choi state have the same rank \(k\): the isometry \(|i\rangle\mapsto|i\rangle|i\rangle\) identifies the Gram matrix divided by \(d\) with the nonzero Choi block. Thus \(k\) is also the minimal Kraus rank. For \(0<\epsilon\le1\), put
\[
\delta=\epsilon/3,
\qquad
r=\left\lceil\sqrt{k+2}\right\rceil,
\]
and
\[
m=
\left\lceil
256\delta^{-2}\bigl(r+\ln(4d)\bigr)
\right\rceil .
\]

Then there exists a unitary
\[
U:\mathbb C^d\otimes\mathbb C^m
\longrightarrow
\mathbb C^d\otimes\mathbb C^m
\]
and an initially independent apparatus state
\[
\beta=\frac{I_r}{r},
\]
embedded on a fixed rank-\(r\) subspace of \(\mathbb C^m\), such that the induced channel \(\Psi\) satisfies
\[
D_\diamond(\Psi,\Phi)\le2\delta\le\epsilon.
\]

There is no public random register, measurement, postselection, reset, accessible purifier, or uncharged physical branch. The full \(m\)-dimensional apparatus is charged.

Consequently
\[
Q=\log_2m,\qquad
P=\log_2(m/r),
\]
and
\[
Q\le
\frac12\log_2k
+2\log_2(1/\epsilon)
+\log_2\!\left(
1+\frac{\ln(4d)}{\sqrt{k}}
\right)
+O(1),
\]
while
\[
P\le
2\log_2(1/\epsilon)
+\log_2\!\left(
1+\frac{\ln(4d)}{\sqrt{k}}
\right)
+O(1).
\]

### Proof

Choose independently, for \(a=1,\ldots,k\), matrices
\[
G_a:\mathbb C^r\to\mathbb C^m
\]
whose entries are circular complex Gaussian variables with variance \(1/m\). Define
\[
F_i=\sum_{a=1}^k(v_i)_aG_a.
\]
Because \(v_i\) is unit, each individual \(F_i\) is an \(m\times r\) normalized complex Gaussian matrix with independent entries of variance \(1/m\). Different \(F_i\)'s need not be independent.

Define also
\[
\Gamma:\mathbb C^k\to\mathbb C^r\otimes\mathbb C^m
\]
by
\[
\Gamma|a\rangle
=
\frac1{\sqrt r}
\sum_{j=1}^r
|j\rangle\otimes G_a|j\rangle.
\]
In matrix form \(\Gamma\) is an \(mr\times k\) Gaussian matrix with independent entries of variance \(1/(mr)\).

### Gaussian concentration

Let \(Z\) be an \(n\times s\) complex Gaussian matrix with entry variance \(1/n\). For every \(0<\delta<1\),
\[
\Pr\!\left[\|Z^\dagger Z-I_s\|>\delta\right]
\le
2\exp\!\left(2s\ln9-\frac{n\delta^2}{32}\right).
\tag{2.1}
\]

For completeness, fix a unit vector \(u\). Then \(\|Zu\|^2\) is the average of \(n\) independent mean-one exponential variables. The elementary Chernoff bound gives
\[
\Pr\bigl[|\|Zu\|^2-1|>a\bigr]
\le2e^{-na^2/4},
\qquad0<a<1.
\]
A \(1/4\)-net of the unit sphere of \(\mathbb C^s\), viewed as a real \(2s\)-dimensional sphere, can be chosen with cardinality at most \(9^{2s}\). If \(L\) is Hermitian,
\[
\|L\|\le2\max_{u\in\mathcal N}|u^\dagger Lu|.
\]
Thus \(\|Z^\dagger Z-I\|>\delta\) implies a net point with quadratic-form error \(>\delta/2\). The union bound already yields the same statement with \(16\) in place of \(32\); (2.1) is therefore conservative.

Apply (2.1) to all \(F_i\), with \((n,s)=(m,r)\), and to \(\Gamma\), with \((n,s)=(mr,k)\). The failure probability is at most
\[
2d\,e^{2r\ln9-m\delta^2/32}
+
2e^{2k\ln9-mr\delta^2/32}.
\tag{2.2}
\]
By construction,
\[
\frac{m\delta^2}{32}
\ge8\bigl(r+\ln(4d)\bigr),
\]
and \(r^2\ge k+2\). Hence the first exponent is at most
\[
-(8-2\ln9)r-8\ln(4d),
\]
and the second is at most
\[
-(8-2\ln9)k-16.
\]
Since \(8-2\ln9>0\), the sum in (2.2) is strictly below one for all \(d,k\ge1\). Therefore one fixed deterministic realization satisfies
\[
\|F_i^\dagger F_i-I_r\|<\delta
\quad\text{for every }i,
\tag{2.3}
\]
and
\[
\|\Gamma^\dagger\Gamma-I_k\|<\delta.
\tag{2.4}
\]

No Gaussian randomness is used at run time.

### First polar normalization: physical slices

Define
\[
W_i=F_i(F_i^\dagger F_i)^{-1/2}.
\]
By (2.3), \(F_i\) has full column rank and
\[
W_i^\dagger W_i=I_r.
\]
Thus \(W_i:\mathbb C^r\to\mathbb C^m\) is an isometry.

If \(s_\ell(F_i)\) are its singular values, (2.3) gives
\[
1-\delta<s_\ell(F_i)^2<1+\delta.
\]
Therefore
\[
\|W_i-F_i\|
=
\|I-(F_i^\dagger F_i)^{1/2}\|
\le\delta.
\tag{2.5}
\]

Let \(S\subset\mathbb C^m\) be the same fixed \(r\)-dimensional subspace on which \(\beta\) is supported. Identify \(S\cong\mathbb C^r\). Extend the isometry \(W_i:S\to\mathbb C^m\) to a full unitary \(U_i\in U(m)\). This is possible by completing orthonormal bases of \(S\) and \(W_iS\).

Set
\[
U=\sum_{i=1}^d |i\rangle\langle i|\otimes U_i.
\]
This is one square unitary on \(\mathbb C^d\otimes\mathbb C^m\).

If a mathematical purifier of \(\beta\) is introduced only for analysis,
\[
|\Omega_r\rangle
=
\frac1{\sqrt r}\sum_{j=1}^r|j\rangle_E|j\rangle_C,
\]
then the actual Stinespring environment vector associated with system basis state \(i\) is
\[
w_i
=
\frac1{\sqrt r}\operatorname{vec}(W_i)
\in\mathbb C^r\otimes\mathbb C^m.
\]
Consequently
\[
\langle w_j,w_i\rangle
=
\frac1r\operatorname{Tr}(W_j^\dagger W_i),
\]
and the physical channel is the Schur multiplier with these Gram coefficients.

The \(r\)-dimensional factor appearing in \(w_i\) is solely a purification used in the proof. The physical apparatus remains \(m\)-dimensional.

### Second polar normalization: common virtual environment

From (2.4) define
\[
J=\Gamma(\Gamma^\dagger\Gamma)^{-1/2}.
\]
Then
\[
J^\dagger J=I_k
\]
and, by the same singular-value argument,
\[
\|\Gamma-J\|\le\delta.
\tag{2.6}
\]

Directly from the definition of \(\Gamma\),
\[
\Gamma v_i
=
\frac1{\sqrt r}\operatorname{vec}(F_i).
\]
Hence, using \(\|X\|_F\le\sqrt r\,\|X\|\) for an \(m\times r\) matrix,
\[
\begin{aligned}
\|w_i-\Gamma v_i\|
&=
\frac1{\sqrt r}\|W_i-F_i\|_F\\
&\le\|W_i-F_i\|\\
&\le\delta.
\end{aligned}
\tag{2.7}
\]
Combining (2.6) and (2.7),
\[
\|w_i-Jv_i\|\le2\delta
\quad\text{for all }i.
\tag{2.8}
\]

Now define two Stinespring isometries on the same environment:
\[
V_{\rm act}|i\rangle=|i\rangle\otimes w_i,
\qquad
V_{\rm tar}|i\rangle=|i\rangle\otimes Jv_i.
\]
Because \(J\) is an isometry,
\[
\langle Jv_j,Jv_i\rangle=\langle v_j,v_i\rangle,
\]
so \(V_{\rm tar}\) dilates exactly \(\Phi\).

Crucially, the system labels \(|i\rangle\) are orthogonal. Thus
\[
(V_{\rm act}-V_{\rm tar})^\dagger
(V_{\rm act}-V_{\rm tar})
=
\sum_i
\|w_i-Jv_i\|^2|i\rangle\langle i|,
\]
and therefore
\[
\|V_{\rm act}-V_{\rm tar}\|
=
\max_i\|w_i-Jv_i\|
\le2\delta.
\tag{2.9}
\]
There is no sum over \(i\), hence no \(d\) or \(\sqrt d\) loss.

Tensoring either isometry with an arbitrary identity reference leaves (2.9) unchanged. For two unit vectors \(x,y\),
\[
D(|x\rangle\langle x|,|y\rangle\langle y|)
\le\|x-y\|.
\]
Thus every reference-entangled pure input gives output dilation states at trace distance at most \(2\delta\). Partial trace is contractive, and purification covers mixed inputs. Hence
\[
D_\diamond(\Psi,\Phi)\le2\delta.
\]
This proves the theorem.

### Resource asymptotics

Since
\[
m=O\!\left(
\epsilon^{-2}(\sqrt{k}+\ln d)
\right)
\]
and \(r=\Theta(\sqrt{k})\),
\[
\log_2m
\le
\frac12\log_2k
+2\log_2(1/\epsilon)
+\log_2\!\left(
1+\frac{\ln(4d)}{\sqrt k}
\right)
+O(1),
\]
and
\[
\log_2(m/r)
\le
2\log_2(1/\epsilon)
+\log_2\!\left(
1+\frac{\ln(4d)}{\sqrt k}
\right)
+O(1).
\]

The proof establishes existence of a fixed deterministic realization. It does not establish a polynomial-time search, efficient uniform circuit family, locality, bounded gate count, or autonomous implementation.


# Universal converse and the exact extreme endpoint

## Theorem 2 -- entropy converse {.unnumbered}

Let \(\Psi:M_d\to M_d\) have any closed square implementation with physical apparatus dimension \(m\) and initial state \(\beta\). Put
\[
Q=\log_2m,\qquad P=\log_2m-S(\beta).
\]
Then
\[
S(J_\Psi)\le2Q-P,
\tag{3.1}
\]
where \(J_\Psi\) is the normalized Choi state.

Let \(\Phi:M_d\to M_d\) be any channel. If
\[
D_\diamond(\Psi,\Phi)\le\epsilon,
\qquad
0\le\epsilon\le1-\frac1{d^2},
\]
then
\[
2Q-P
\ge
S(J_\Phi)
-\epsilon\log_2(d^2-1)
-h_2(\epsilon).
\tag{3.2}
\]

### Proof

Feed half of the normalized maximally entangled state
\[
|\Omega_d\rangle_{RA}
=
\frac1{\sqrt d}\sum_i|i\rangle_R|i\rangle_A
\]
to the implementation. The initial state on \(RAC\) is
\[
|\Omega_d\rangle\langle\Omega_d|\otimes\beta.
\]
After the unitary on \(AC\), let the state be \(\omega_{RBC}\). Unitarity gives
\[
S(RBC)_\omega=S(\beta).
\]
The \(RB\) marginal is \(J_\Psi\). Araki--Lieb gives
\[
S(RB)\le S(RBC)+S(C),
\]
hence
\[
S(J_\Psi)
\le
S(\beta)+\log_2m
=
2Q-P.
\]

If the half diamond distance is at most \(\epsilon\), testing on the normalized Bell state gives
\[
D(J_\Psi,J_\Phi)\le\epsilon.
\]
Audenaert's sharp entropy-continuity bound on dimension \(d^2\), together with the stated range where its right side is monotone in the available upper bound \(\epsilon\), gives
\[
S(J_\Phi)
\le
S(J_\Psi)
+\epsilon\log_2(d^2-1)
+h_2(\epsilon).
\]
Combining this with (3.1) yields (3.2).

The entropy step is Araki--Lieb [@araki1970]; the stated continuity correction is due to Audenaert [@audenaert2007].

## Theorem 3 -- exact extreme-channel cost {.unnumbered}

Let \(\Phi:M_d\to M_d\) be an extreme point of the convex set of CPTP maps, with minimal Kraus rank \(k\). Every exact closed square implementation with apparatus state \(\beta\) of rank \(r_0\) satisfies
\[
m\ge kr_0.
\tag{3.3}
\]
Consequently
\[
P\ge\log_2k,\qquad Q\ge\log_2k+\log_2r_0.
\tag{3.4}
\]
A pure minimal Stinespring environment attains \(P=Q=\log_2k\). The qualitative obstruction to improving an extreme channel's minimal environment by using mixedness is already present in Terhal et al. [@terhal1999]. The factor \(r_0\) in (3.3) makes explicit the additional dimension required by an initially mixed support; it does not assert that every larger implementation must start pure.

### Proof

Diagonalize the positive part of the apparatus state:
\[
\beta=\sum_{j=1}^{r_0}
\lambda_j|j\rangle\langle j|,
\qquad\lambda_j>0.
\]
For every \(j\), define the isometry
\[
V_j|\psi\rangle
=
U(|\psi\rangle\otimes|j\rangle).
\]
Because distinct apparatus input columns are orthogonal and \(U\) is unitary,
\[
V_i^\dagger V_j=\delta_{ij}I.
\tag{3.5}
\]

The implemented channel is
\[
\Phi=\sum_j\lambda_j\Phi_j,
\qquad
\Phi_j(\rho)=\operatorname{Tr}_C V_j\rho V_j^\dagger.
\]
Every \(\Phi_j\) is CPTP. Extremality of \(\Phi\) therefore forces
\[
\Phi_j=\Phi
\quad\text{for every }j.
\tag{3.6}
\]

Let
\[
V=\sum_{a=1}^kK_a\otimes|a\rangle
\]
be a minimal Stinespring isometry for \(\Phi\). Minimal Stinespring uniqueness [@stinespring1955] gives an isometry
\[
W_j:\mathbb C^k\to\mathbb C^m
\]
such that
\[
V_j=(I\otimes W_j)V.
\tag{3.7}
\]
Substituting (3.7) into (3.5),
\[
\sum_{a,b=1}^k
(W_i^\dagger W_j)_{ab}\,
K_a^\dagger K_b
=
\delta_{ij}I.
\tag{3.8}
\]
Since \(\sum_aK_a^\dagger K_a=I\), the right side has coefficient matrix
\(\delta_{ij}I_k\).

Choi's extremality criterion states that for a minimal Kraus family of an extreme CPTP map the \(k^2\) matrices
\[
\{K_a^\dagger K_b:a,b=1,\ldots,k\}
\]
are linearly independent. See Choi's extremality criterion [@choi1975].  Therefore (3.8) implies
\[
W_i^\dagger W_j=\delta_{ij}I_k.
\tag{3.9}
\]
The \(r_0\) ranges \(W_j\mathbb C^k\) are mutually orthogonal \(k\)-dimensional subspaces of \(\mathbb C^m\). Hence
\[
m\ge kr_0.
\]

Finally,
\[
S(\beta)\le\log_2r_0,
\]
so
\[
P
=\log_2m-S(\beta)
\ge
\log_2(kr_0)-\log_2r_0
=\log_2k,
\]
and \(Q=\log_2m\ge\log_2k+\log_2r_0\).

Conversely, a pure minimal \(k\)-dimensional Stinespring environment can be completed to a square unitary, giving
\[
P=Q=\log_2k.
\]

The exact argument is intrinsically an exact one: extremality does not imply that approximate spectral branches individually approximate the target.


# Explicit extreme ququart separation

Consider
\[
K_0=
\operatorname{diag}
\left(
1,\frac1{\sqrt3},\frac1{\sqrt3},\frac1{\sqrt3}
\right),
\]
and
\[
K_1=
\sqrt{\frac23}\,
\operatorname{diag}(0,1,\omega,\omega^2),
\qquad
\omega=e^{2\pi i/3}.
\tag{4.1}
\]
These are precisely the \(s=1/3\) specialization of Haagerup and Musat's rank-two ququart Schur example. Their paper gives
\[
a_1(s)=\operatorname{diag}(1,\sqrt s,\sqrt s,\sqrt s),
\quad
a_2(s)=\sqrt{1-s}\operatorname{diag}
(0,1,\omega,\bar\omega),
\]
and explicitly notes independence of the four Kraus products [@haagerup2011, Example 3.2].

Let \(\Phi_4(\rho)=\sum_{a=0}^1K_a\rho K_a^\dagger\) be the resulting channel. Haagerup and Musat write their map as \(\sum_a a_a^*x a_a\); our Schrödinger convention uses the Hilbert--Schmidt adjoint of that displayed map. The Kraus entries are the same, and the Schur matrices are complex conjugates. This convention change does not affect any property used below. CPTP extremality follows from Choi's criterion and the independently verified products in the proof, rather than from an assertion of CPTP extremality in their example.

Explicitly, take \(v_i=((K_0)_{ii},(K_1)_{ii})\in\mathbb C^2\). These unit vectors span \(\mathbb C^2\), and give the Schur representation in Theorem 1. Thus the Gram rank and minimal Kraus rank are both two.

## Lemma 4 {.unnumbered}

\(\Phi_4\) is CPTP-extreme, has Kraus rank two, and its normalized Choi state has spectrum
\[
(1/2,1/2).
\]

### Proof

Trace preservation follows coordinatewise:
\[
K_0^\dagger K_0+K_1^\dagger K_1=I_4.
\]

The four products are
\[
K_0^\dagger K_0
=
\operatorname{diag}(1,1/3,1/3,1/3),
\]
\[
K_1^\dagger K_1
=
\frac23\operatorname{diag}(0,1,1,1),
\]
\[
K_0^\dagger K_1
=
\frac{\sqrt2}{3}
\operatorname{diag}(0,1,\omega,\omega^2),
\]
and its adjoint.

If a linear combination vanishes, the first diagonal coordinate forces the coefficient of \(K_0^\dagger K_0\) to vanish. On the last three coordinates, the remaining three coefficient vectors are the three Fourier modes
\[
(1,1,1),\quad
(1,\omega,\omega^2),\quad
(1,\omega^2,\omega),
\]
which are independent. Thus all four Kraus products are independent, and Choi's criterion [@choi1975] gives extremality.

Moreover
\[
\operatorname{Tr}(K_a^\dagger K_b)=2\delta_{ab}.
\]
Under vectorization the two Kraus vectors are therefore orthogonal and have squared norm two. Since \(d=4\), the normalized Choi state is
\[
J_{\Phi_4}
=
\frac14\sum_{a=0}^1
|K_a\rangle\!\rangle
\langle\!\langle K_a|,
\]
so its two nonzero eigenvalues are \(2/4=1/2\). Hence
\[
S(J_{\Phi_4})=1.
\]

For
\[
\Phi_T=\Phi_4^{\otimes T},
\]
we have
\[
d_T=4^T,\qquad
k_T=2^T,\qquad
S(J_{\Phi_T})=T.
\tag{4.2}
\]
Tensor products of the spanning Gram vectors have span \((\mathbb C^2)^{\otimes T}\), so \(k_T=2^T\) in (4.2) is both the Gram rank used in Theorem 1 and the minimal Kraus rank used in Theorem 3. Tensor products of the locally independent Kraus-product families remain linearly independent, so \(\Phi_T\) is also extreme.

## Corollary 5 -- exact versus polynomially accurate service {.unnumbered}

Consider service of \(\Phi_T\) with all \(T\) inputs presented together, including arbitrary joint reference entanglement. In the approximation and limiting statements below, take integer \(T\ge2\).

For exact service,
\[
P_{\rm exact}=Q_{\rm exact}=T.
\tag{4.3}
\]

For
\[
\epsilon_T=T^{-4},
\]
there exist closed approximate implementations satisfying
\[
Q
\le
\frac T2+8\log_2T+O(1),
\tag{4.4}
\]
and
\[
P
\le
8\log_2T+O(1).
\tag{4.5}
\]
Conversely every implementation at half-diamond error \(T^{-4}\) satisfies
\[
Q\ge\frac T2-o(1).
\tag{4.6}
\]

Thus
\[
\boxed{
\frac QT\to\frac12,\qquad
\frac PT\to0
}
\]
is achievable at polynomially vanishing error, whereas exact service has
\[
\boxed{
\frac{Q_{\rm exact}}T
=
\frac{P_{\rm exact}}T
=1.
}
\]

### Proof

The exact statement follows from Theorem 3 with \(k_T=2^T\), and is attained by the pure minimal environment.

For the upper bound, Theorem 1 gives
\[
\frac12\log_2k_T=\frac T2,
\qquad
2\log_2(1/\epsilon_T)=8\log_2T.
\]
Furthermore
\[
\frac{\ln(4d_T)}{\sqrt{k_T}}
=
O(T2^{-T/2}),
\]
so its logarithmic contribution is \(o(1)\). Equations (4.4) and (4.5) follow.

For the converse, Theorem 2 gives
\[
2Q-P
\ge
T
-
T^{-4}\log_2(16^T-1)
-h_2(T^{-4})
=
T-o(1).
\]
Since \(P\ge0\),
\[
2Q\ge T-o(1),
\]
which proves (4.6).

This is an **asymptotic exact-versus-vanishing-error separation**. It should not be described as a discontinuity theorem at one fixed finite dimension.


# The support-inverse lemma

The timing result needs a stabilized way to recover support coordinates from a marginal.

## Lemma 6 -- full-domain support inverse {.unnumbered}

Let \(\Phi:M_d\to M_d\) be extreme, let \(J\) be its normalized Choi state of rank \(k\), and let
\[
T_0:\mathbb C^k\to R\otimes Y
\]
be any isometry onto \(\operatorname{supp}J\). Write
\[
J=T_0\sigma T_0^\dagger,
\qquad
\sigma=T_0^\dagger JT_0.
\tag{5.1}
\]
Define
\[
\Theta:M_k\to M_d,
\qquad
\Theta(Z)=\operatorname{Tr}_Y(T_0ZT_0^\dagger).
\tag{5.2}
\]

Then:

1. \(\Theta\) is injective.
2. Its inverse on \(\operatorname{im}\Theta\) has a linear extension
   \[
   \Lambda:M_d\to M_k
   \]
   satisfying
   \[
   \Lambda\Theta=\operatorname{id}_{M_k}.
   \tag{5.3}
   \]
3. \(\Lambda\) need not be positive or completely positive.
4. Every such finite-dimensional extension has finite diamond norm.
5. Since \(\Phi\) is trace preserving,
   \[
   \Theta(\sigma)=I_d/d,
   \qquad
   \Lambda(I_d/d)=\sigma.
   \tag{5.4}
   \]

### Proof

Choose an orthonormal basis of the Choi support. Under the vectorization correspondence, the support vectors represent a minimal Kraus family after an invertible change of Kraus coordinates. With the convention \(|K\rangle\!\rangle=\sum_i|i\rangle_R\otimes K|i\rangle_Y\), partial trace produces transposed Kraus products: \(\operatorname{Tr}_Y|K_a\rangle\!\rangle\langle\!\langle K_b|=(K_b^\dagger K_a)^T\). Transposition and the change of Kraus coordinates are invertible, so injectivity is equivalent to independence of the products
\[
K_a^\dagger K_b.
\]
For an extreme channel those \(k^2\) products are linearly independent by Choi's criterion. Thus
\[
\Theta(Z)=0\implies Z=0,
\]
so \(\Theta\) is injective.

Hence
\[
\Theta^{-1}:\operatorname{im}\Theta\to M_k
\]
is a well-defined linear map. Choose any vector-space complement
\[
M_d=\operatorname{im}\Theta\oplus W
\]
and any linear projection
\[
\pi:M_d\to\operatorname{im}\Theta
\]
that is the identity on \(\operatorname{im}\Theta\). Then
\[
\Lambda=\Theta^{-1}\pi
\]
is a full-domain linear extension satisfying (5.3). Nothing in this construction makes \(\pi\) or \(\Lambda\) positive, and no positivity is required.

Finiteness is uniform over the spectator dimension. For any
\(X=\sum_{i,j}E_{ij}\otimes X_{ij}\in M_d\otimes M_s\), block compression gives
\(\|X_{ij}\|_1\le\|X\|_1\), and therefore
\[
\|(\Lambda\otimes\operatorname{id}_s)(X)\|_1
\le\sum_{i,j}\|\Lambda(E_{ij})\|_1\,\|X_{ij}\|_1
\le\left(\sum_{i,j}\|\Lambda(E_{ij})\|_1\right)\|X\|_1.
\]
The finite sum is independent of \(s\), so
\(\|\Lambda\|_\diamond<\infty\).

Finally,
\[
\operatorname{Tr}_YJ=I_d/d
\]
for a normalized Choi state of a trace-preserving channel. Substituting (5.1) gives
\[
\Theta(\sigma)=I_d/d,
\]
and applying the left inverse gives (5.4).

The explicit retention of \(\sigma\) matters: the Choi spectrum need not be flat.


# Scheduled-delivery lower bound

This section is a separate operational application of the static result, not part of the static theorem.

## Scheduled interaction contract {.unnumbered}

There are \(N\) \(d\)-dimensional inputs. Input \(t\) arrives at mandatory integer round \(t\). For a delay parameter \(1\le b\le N\), its corresponding \(d\)-dimensional output must be released no later than round
\[
t+b-1.
\]

Real and ideal processes use the same allowed physical release schedule. The ideal process applies a fresh independent copy of \(\Phi\) to each arrival and holds its output until that schedule releases it. A tester may prepare a scheduled input from arbitrary private quantum memory and outputs already released at earlier rounds.

The real device is closed: all of its evolution is unitary, with no reset, discarded internal system, or fresh ancillary system supplied after round zero. Every physical factor held by the device is either part of its initially supplied apparatus or an input already delivered by the tester. Any workspace, controller, or clock implemented as a physical register must be included in that inventory. A prescribed sequence of externally timed unitaries is allowed; no autonomous-control construction is claimed.

At each cut used below there is one branch-independent tensor factorization into the current residual and all outward physical \(d\)-dimensional output factors. The same residual is used for Hilbert-space dimension, entropy, and continuation to the next epoch.

Stopping is observation-only: at a cut the tester observes only systems already released. It does not demand that the device flush an incomplete block. The theorem gives no guarantee for a caller who withholds a mandatory future input until an earlier output is returned.

Assume real and ideal processes have half stopped adaptive strategy distance at most \(\epsilon\): in particular, every allowed tester at every deterministic cut produces states at trace distance at most \(\epsilon\). Gutoski's strategy norm supplies the operational framework for multi-round distinguishability [@gutoski2012].

## Theorem 7 -- extreme-channel scheduled-purity bound {.unnumbered}

Let \(\Phi:M_d\to M_d\) be extreme, with normalized Choi state \(J\). Take \(T_0,\Theta,\sigma,\Lambda\) from Lemma 6 and choose
\[
\lambda\ge\|\Lambda\|_\diamond.
\]
For any integer \(r\ge1\), define
\[
\delta_r
=
\min\{1,(1+\lambda^r)\sqrt\epsilon\},
\tag{6.1}
\]
and
\[
e_r
=
2\delta_r\,r\log_2(d^2)
+
(1+\delta_r)
h_2\!\left(
\frac{\delta_r}{1+\delta_r}
\right).
\tag{6.2}
\]

At a cut, write \(\rho_C\) for the actual state of the complete residual and define \(P(C)=\log_2\dim C-S(\rho_C)\). In particular \(P_{\rm initial}=P(C_0)\), where \(C_0\) is the entire initially supplied apparatus, before any user input arrives. Under the scheduled contract above,
\[
\boxed{
P_{\rm initial}
\ge
\left\lfloor
\frac{N}{r+b-1}
\right\rfloor
\bigl[rS(J)-e_r\bigr].
}
\tag{6.3}
\]

### Step 1: stabilized support recovery

Take \(r\) fresh Bell inputs and suppose their reference-output marginal obeys
\[
D(\rho_{RY},J^{\otimes r})\le\epsilon.
\tag{6.4}
\]
Let \(F\) be any spectator for which exact no-signalling gives
\[
\rho_{RF}
=
\frac{I_R}{d^r}\otimes\rho_F.
\tag{6.5}
\]

Let
\[
P_{\rm supp}=T_0^{\otimes r}T_0^{\dagger\otimes r}
\]
be the projector onto \(\operatorname{supp}(J)^{\otimes r}\). Because the ideal state is fully supported there, (6.4) implies
\[
\operatorname{Tr}(P_{\rm supp}\rho_{RY})\ge1-\epsilon.
\tag{6.6}
\]

For completeness, the needed gentle-projection estimate is elementary. If \(|\psi\rangle\) purifies \(\rho\) and \(|\phi\rangle=(P_{\rm supp}\otimes I)|\psi\rangle\), then
\[
\|\psi-\phi\|^2\le\epsilon.
\]
For unnormalized rank-one operators,
\[
\bigl\|
|\psi\rangle\langle\psi|
-
|\phi\rangle\langle\phi|
\bigr\|_1
\le
(\|\psi\|+\|\phi\|)\|\psi-\phi\|
\le2\sqrt\epsilon.
\]
Tracing out the purifier therefore gives
\[
\|\rho-\omega\|_1\le2\sqrt\epsilon,
\qquad
\omega=(P_{\rm supp}\otimes I_F)\rho(P_{\rm supp}\otimes I_F).
\tag{6.7}
\]

Write the projected state in support coordinates:
\[
\omega
=
(T_0^{\otimes r}\otimes I_F)
Z
(T_0^{\dagger\otimes r}\otimes I_F).
\tag{6.8}
\]
Taking the \(RF\) marginal of (6.7), using (6.5), gives
\[
\left\|
(\Theta^{\otimes r}\otimes\operatorname{id}_F)(Z)
-
\frac{I_R}{d^r}\otimes\rho_F
\right\|_1
\le2\sqrt\epsilon.
\tag{6.9}
\]

The diamond norm controls arbitrary spectators and is submultiplicative under tensor products, so
\[
\|\Lambda^{\otimes r}\|_\diamond
\le\lambda^r.
\]
Apply \(\Lambda^{\otimes r}\otimes\operatorname{id}_F\) to (6.9). From (5.4),
\[
\left\|
Z-\sigma^{\otimes r}\otimes\rho_F
\right\|_1
\le2\lambda^r\sqrt\epsilon.
\tag{6.10}
\]
Conjugating by \(T_0^{\otimes r}\) and combining with (6.7),
\[
D\!\left(
\rho_{RYF},
J^{\otimes r}\otimes\rho_F
\right)
\le
(1+\lambda^r)\sqrt\epsilon.
\tag{6.11}
\]
Capping the right side at one gives \(\delta_r\).

Winter's conditional-entropy continuity lemma states that if
\[
D(\rho_{AB},\sigma_{AB})\le\delta,
\]
then
\[
|S(A|B)_\rho-S(A|B)_\sigma|
\le
2\delta\log_2|A|
+
(1+\delta)
h_2\!\left(
\frac{\delta}{1+\delta}
\right).
\]
This is Winter's Lemma 2 [@winter2016].

Taking \(A=RY\), whose dimension is \(d^{2r}\), (6.11) gives
\[
S(RY|F)_\rho
\ge
rS(J)-e_r.
\tag{6.12}
\]

### Step 2: epoch telescope

Set
\[
L=r+b-1.
\]
Partition the arrivals into as many complete epochs of \(L\) arrivals as possible. In each epoch, the first \(r\) arrivals are the core and the next \(b-1\) are guards. By the deadline, every core output has crossed the output cut by the end of the epoch.

Use one passive experiment consisting of independent Bell inputs at every arrival. At an epoch start let:

- \(C\) be the actual device residual;
- \(F\) be its untouched mathematical purifier, including any previous outward systems needed to purify it;
- \(R_c\) be the \(r\) new core Bell references;
- \(R_g\) be the \(L-r\) guard references;
- \(M\) be the number of physical \(d\)-dimensional outputs that cross during the epoch;
- \(Y_c\) be the \(r\) core outputs;
- \(O'\) be the other \(M-r\) released outputs;
- \(C'\) be the residual after the epoch.

Write
\[
O=Y_cO'.
\]

The full evolution over the epoch is unitary from
\[
C\otimes(\mathbb C^d)^{\otimes L}
\]
to
\[
C'\otimes(\mathbb C^d)^{\otimes M}.
\]
Therefore dimension conservation gives
\[
\log\dim C-\log\dim C'
=
(M-L)\log_2d.
\tag{6.13}
\]

The global state including \(F,R_c,R_g\) is pure before and after the epoch. Hence
\[
S(C')=S(OR_cR_gF),
\qquad
S(C)=S(F),
\]
so
\[
P(C)-P(C')
=
(M-L)\log_2d
+
S(OR_cR_g|F).
\tag{6.14}
\]

Expand the conditional entropy in the order
\[
R_g,\quad R_cY_c,\quad O'.
\]
The guard references are fresh maximally mixed systems independent of \(F\), so
\[
S(R_g|F)=(L-r)\log_2d.
\tag{6.15}
\]
The stabilized support result (6.12), with \(FR_g\) treated as the spectator, gives
\[
S(R_cY_c|FR_g)
\ge
rS(J)-e_r.
\tag{6.16}
\]
Finally
\[
S(O'|FR_gR_cY_c)
\ge
-\log\dim O'
=
-(M-r)\log_2d.
\tag{6.17}
\]

Substituting (6.15)--(6.17) into (6.14),
\[
\begin{aligned}
P(C)-P(C')
&\ge
(M-L)\log_2d
+(L-r)\log_2d\\
&\quad+rS(J)-e_r
-(M-r)\log_2d\\
&=
rS(J)-e_r.
\end{aligned}
\tag{6.18}
\]
Every physical-dimension term cancels.

After the last complete epoch, place every remaining arrival and every pending output into one tail. Let \(L'\) be the number of arrivals in that tail and \(M'\) the number of outputs it releases. The same identity without a core gives
\[
P(C)-P(C')
=
(M'-L')\log_2d+S(OR|F).
\]
Here
\[
S(R|F)=L'\log_2d
\]
and
\[
S(O|FR)\ge-M'\log_2d,
\]
so the tail decrement is nonnegative.

There are
\[
\left\lfloor
\frac{N}{r+b-1}
\right\rfloor
\]
complete epochs. Telescoping (6.18) and using
\[
P(C_{\rm final})\ge0
\]
proves (6.3).

### Why the error is not multiplied by the number of epochs

Each epoch invokes the original stopped-strategy assumption on a different deterministic-cut passive tester. The global hypothesis already says that each such test has distance at most \(\epsilon\). The proof derives an entropy inequality from each marginal separately; it never approximates the actual process by a sequence of different channels. Therefore there is no union bound or hybrid sum over epochs.

This is different from the constructive block upper bound below. There, \(K\) genuinely distinct approximate block channels are substituted one at a time, so the triangle inequality produces \(K\eta\).

### Why extremality cannot be replaced by Choi entropy

Complete qubit dephasing, \(\Delta(\rho)=(\rho+Z\rho Z)/2\), has \(S(J_\Delta)=1\), but \(N\) exact independent immediate calls need no initial entropy deficit. Supply \(N\) independent maximally mixed control qubits at round zero, and at call \(t\) apply \(Z\) to the input controlled by the \(t\)-th such qubit. Retain all controls. The resulting process is exactly \(\Delta^{\otimes N}\), also under adaptive use, with \(P_{\rm initial}=0\) and \(Q_{\rm initial}=N\). This is the standard random-unitary implementation, using independent initial labels rather than reusing one label. Thus a positive Choi entropy alone cannot imply Theorem 7's purity lower bound; the extreme-channel support hypothesis is essential.


# The ququart support inverse and the sublogarithmic lower bound

For \(\Phi_4\), define
\[
T_0|a\rangle
=
\frac1{\sqrt2}|K_a\rangle\!\rangle,
\qquad a=0,1.
\]
The two columns are orthonormal, and
\[
J_{\Phi_4}=T_0\frac{I_2}{2}T_0^\dagger.
\]
Thus
\[
\sigma=I_2/2.
\]

For diagonal entries \(K_a(i)\), define unit vectors
\[
q_i=
\begin{pmatrix}
\overline{K_0(i)}\\
\overline{K_1(i)}
\end{pmatrix},
\qquad
\Pi_i=|q_i\rangle\langle q_i|.
\]
A direct partial-trace calculation gives
\[
\Theta(Z)
=
\frac12
\operatorname{diag}
\bigl(
\operatorname{Tr}(Z\Pi_1),\ldots,
\operatorname{Tr}(Z\Pi_4)
\bigr).
\tag{7.1}
\]
The four \(\Pi_i\)'s form the tetrahedral qubit SIC:
\[
\sum_i\Pi_i=2I,
\qquad
\operatorname{Tr}(\Pi_i\Pi_j)=
\begin{cases}
1,&i=j,\\
1/3,&i\ne j.
\end{cases}
\tag{7.2}
\]

If \(X\in M_4\), define
\[
\Lambda(X)
=
\sum_{i=1}^4
X_{ii}(3\Pi_i-I).
\tag{7.3}
\]
If \(X=\Theta(Z)\), write \(x_i=X_{ii}\). Then
\[
x_i=\frac12\operatorname{Tr}(Z\Pi_i).
\]
The SIC identities give
\[
Z
=
3\sum_i x_i\Pi_i
-
\left(\sum_i x_i\right)I.
\tag{7.4}
\]
Indeed, taking the Hilbert--Schmidt inner product of the right side with any \(\Pi_j\) gives
\[
3\left(x_j+\frac13\sum_{i\ne j}x_i\right)
-\sum_i x_i
=
2x_j
=
\operatorname{Tr}(Z\Pi_j),
\]
and the four \(\Pi_j\)'s span \(M_2\). Thus \(\Lambda\Theta=\mathrm{id}\).

Moreover
\[
\|3\Pi_i-I\|_1=3.
\]
The map \(\Lambda\) ignores off-diagonal entries, so it factors through diagonal pinching. Since \(\Lambda\) is Hermiticity preserving, the diamond-norm supremum may be taken on Hermitian inputs. Pinching is trace-norm contractive there, and
\[
\begin{aligned}
\|(\Lambda\otimes\mathrm{id})(X)\|_1
&\le
\sum_i
\|3\Pi_i-I\|_1\,\|X_{ii}\|_1\\
&=
3\sum_i\|X_{ii}\|_1\\
&\le3\|X\|_1.
\end{aligned}
\]
A single diagonal basis projector attains three. Hence
\[
\boxed{\|\Lambda\|_\diamond=3.}
\tag{7.5}
\]

The constant three is minimal among all full-domain linear left inverses of this \(\Theta\). Indeed, \(\Theta\) maps a four-dimensional operator space injectively into the four-dimensional diagonal subalgebra of \(M_4\), so its image is that entire subalgebra. Every left inverse must therefore send \(|i\rangle\langle i|\) to \(3\Pi_i-I\), whose trace norm is three. This optimality concerns only the linear support-inverse constant; it does not establish an optimal physical delay curve.

Now take
\[
\epsilon_T=T^{-4}
\]
and
\[
r_T=\lfloor a\log_2T\rfloor,
\qquad
0<a<\frac2{\log_2 3}.
\]
Then
\[
(1+3^{r_T})\sqrt{\epsilon_T}
=
O\!\left(
T^{-2+a\log_2 3}
\right)
\to0.
\]
Because \(d=4\) is fixed and \(r_T=O(\log T)\),
\[
e_{r_T}=o(1).
\tag{7.6}
\]

If a delay sequence satisfies
\[
b_T=o(\log T),
\]
then
\[
\frac{r_T}{r_T+b_T-1}\to1,
\]
and Theorem 7, with \(S(J_{\Phi_4})=1\), gives
\[
\boxed{
P_{\rm initial}\ge T-o(T).
}
\tag{7.7}
\]
Since \(P\le Q\),
\[
\boxed{
Q_{\rm initial}\ge T-o(T).
}
\tag{7.8}
\]

The pure minimal-environment bank attains \(P=Q=T\) with immediate outputs, so the leading lower rate is achievable.


# A proved lower curve at logarithmic delay

This is a consequence of Theorem 7, not a sharp frontier.

Suppose
\[
b_T=c\log_2T+o(\log T),
\qquad c\ge0.
\]
For the same
\[
r_T=a\log_2T+o(\log T),
\qquad
a<2/\log_2 3,
\]
we have
\[
\frac1T
\left\lfloor
\frac{T}{r_T+b_T-1}
\right\rfloor r_T
\longrightarrow
\frac{a}{a+c}.
\]
Using \(e_{r_T}=o(1)\),
\[
\liminf_{T\to\infty}
\frac{P_{\rm initial}}T
\ge
\frac{a}{a+c}.
\]
Letting
\[
a\uparrow\frac2{\log_2 3}
\]
yields
\[
\boxed{
\liminf_{T\to\infty}
\frac{P_{\rm initial}}T
\ge
\frac{2}{2+c\log_2 3}.
}
\tag{8.1}
\]

Equation (8.1) is only a lower bound. It does not determine the optimal coefficient at \(b=c\log T\).


# Superlogarithmic-delay upper bound

## Theorem 8 -- independent delayed blocks {.unnumbered}

Let
\[
\epsilon_T=T^{-4}
\]
and let
\[
1\le b_T\le T,
\qquad
\frac{b_T}{\log T}\to\infty.
\tag{9.1}
\]
Under the same mandatory-arrival, common-release-schedule, no-flush contract, there is an implementation of
\[
\Phi_4^{\otimes T}
\]
with stopped strategy error at most \(T^{-4}\) and
\[
\boxed{
Q_{\rm initial}
\le
\frac T2+o(T),
\qquad
P_{\rm initial}=o(T).
}
\tag{9.2}
\]

### Proof

Partition the \(T\) mandatory arrivals into
\[
K=\left\lceil\frac{T}{b_T}\right\rceil
\]
consecutive blocks of sizes
\[
t_j\le b_T.
\]
Supply every block with its own independent Theorem 1 apparatus at time zero. Set the per-block half-diamond error to
\[
\eta=\frac{T^{-4}}K.
\tag{9.3}
\]

For a block of \(t_j\) ququart channels,
\[
k_j=2^{t_j},\qquad d_j=4^{t_j}.
\]
Theorem 1 therefore gives uniformly
\[
Q_j
\le
\frac{t_j}{2}+O(\log T),
\tag{9.4}
\]
and
\[
P_j=O(\log T),
\tag{9.5}
\]
because
\[
\log(1/\eta)=O(\log T).
\]

Collect every input of a block before exposing any output from that block. After the final scheduled input arrives, execute the block map and release all its outputs at that end-of-block cut. The earliest input waits at most
\[
t_j-1\le b_T-1
\]
rounds.

During collection of block \(j\), the tester may use all outputs from earlier blocks and arbitrary private memory to prepare its current inputs. But it has received no output from the unfinished current block. Therefore the entire collection of \(t_j\) inputs is simply an arbitrary joint input, possibly entangled with an arbitrary reference. The diamond guarantee for that block applies directly.

Replace completed real blocks by ideal blocks sequentially. Once a block has been replaced, every later operation of the tester and device is CPTP, so trace distance cannot increase. The triangle inequality therefore gives total strategy error
\[
\le K\eta=T^{-4}.
\tag{9.6}
\]
This is the error accumulation that was absent from the lower-bound epoch proof.

If a stopped test occurs while a block is unfinished, no current-block-dependent output has been released. The real and ideal processes expose the same interface at that cut, so the unfinished approximation contributes no observational error.

Summing (9.4) and (9.5),
\[
Q_{\rm initial}
\le
\frac12\sum_jt_j+O(K\log T)
=
\frac T2+O(K\log T),
\]
and
\[
P_{\rm initial}=O(K\log T).
\]
Condition (9.1) implies
\[
K\log T
=
O\!\left(\frac{T\log T}{b_T}+\log T\right)
=o(T),
\]
which proves (9.2).

## Payload custody {.unnumbered}

Equation (9.2) counts **initially supplied apparatus**.

The unfinished block may physically retain as many as \(b_T\) ququart inputs. Since one ququart has log dimension two, this adds at most
\[
2b_T
\]
qubits of peak payload custody:
\[
Q_{\rm peak}
\le
Q_{\rm initial}+2b_T.
\tag{9.7}
\]
Therefore a peak total-device leading rate of \(1/2\) follows from this construction only if
\[
\frac{b_T}{\log T}\to\infty
\quad\text{and}\quad
b_T=o(T).
\tag{9.8}
\]
Superlogarithmic delay alone is sufficient only for the initial-apparatus rate.


\clearpage

# Combined asymptotic picture

For the fixed ququart channel \(\Phi_4\) and target error \(T^{-4}\):

| Delay regime | Initial purity \(P\) | Initial apparatus \(Q\) |
|---|---:|---:|
| Exact service | \(T\) exactly | \(T\) exactly |
| \(b_T=o(\log T)\) | \(T-o(T)\) lower bound; \(T\) attainable | \(T-o(T)\) lower bound; \(T\) attainable |
| \(b_T/\log T\to\infty\) | \(o(T)\) attainable | \(T/2-o(1)\) lower bound; \(T/2+o(T)\) attainable |
| \(b_T=c\log_2T+o(\log T)\) | lower curve (8.1) | at least the same lower bound via \(Q\ge P\) |

Rows two to four assume the scheduled interaction contract of Section 6: mandatory arrivals, identical real and ideal physical release schedules, and observation-only stopping with no flush of an unfinished block. Both resource columns count the initially supplied apparatus. The payload custody in Section 9 adds up to \(2b_T\) qubits to peak storage; the attainable half-rate peak bound additionally requires \(b_T=o(T)\).

For the third-row converse, a tester may prepare all inputs jointly with an arbitrary reference, deliver their respective factors at the scheduled arrivals, and stop after the final release. This allowed test identifies the induced joint channel and shows that half stopped-strategy distance dominates its half-diamond distance. Corollary 5 therefore applies to the initial apparatus of any implementation obeying the stronger strategy guarantee. The last row is not a matched frontier.


# Prior art and contract comparison

Initially mixed environments and their common-unitary compatibility constraints are established [@terhal1999; @zalka2002]. Terhal et al. already give the pure-environment simulation of a mixed environment with quadratic dimension overhead and the qualitative extreme-channel obstruction. Theorem 1 concerns approximate, reference-stabilized attainability for Schur channels with explicit overheads; Theorem 3 records the sharper occupied-rank inequality \(m\ge k\,\operatorname{rank}\beta\). Neither the implementation model nor the square-root counting scale is claimed as new. The exact rank count by itself is not a robust converse at nonzero error: the matched leading-order bound in Corollary 5 comes from Choi entropy instead.

The ququart Kraus family in Section 4 specializes Haagerup and Musat's Example 3.2 [@haagerup2011], with the adjoint convention explained there. Their example establishes nonfactorizability and verifies independence of the Kraus products. CPTP extremality follows by applying Choi's criterion to those products, as reproduced in Lemma 4; we do not attribute that explicit conclusion to Haagerup and Musat. Neither property is claimed as a new channel example. Our apparatus is not maximally mixed on its entire physical space: it has a nonzero entropy deficit. Sublinear deficit per tensor factor does not mean zero total deficit, so the approximate construction does not contradict obstructions to tracial factorization.

Kotowski and Kotowski [@kotowski2026, Definition 2.3] allow classical randomization and an output success flag. Their simulation is exact conditional on success; approximate diamond simulation is identified separately as a further direction. Theorem 1 instead supplies one unconditional square implementation for Schur channels, with no free classical mixture or success flag. Its rate optimality is confined to the charged closed-square model and the tensor-power family of Corollary 5; it is not a smallest-ancilla claim across randomized or heralded simulation models, and it does not resolve their general approximate-simulation question.

Lancien and Winter [@lancien2024] reduce Kraus rank under output-state approximation guarantees, including induced \(1\!\to\!1\) norm. Their resource and norm differ from the square mixed-apparatus diamond contract here. The actual channel in Theorem 1 can have Kraus rank as large as \(mr\), not merely \(m\); mixing the initial apparatus is not equivalent to reducing total Kraus rank to its physical dimension.

Extremality, support injectivity, and complementary-channel formulations are established channel structure [@choi1975; @holevo2013]. Our full-domain inverse is a linear, not necessarily positive, reconstruction map. Its role is to transfer support stability uniformly across a spectator and then telescope the resulting conditional entropy through physical release cuts.

Rybár and Ziman [@rybar2008] study repeated use of a fixed unitary and finite memory without resetting it, and use entropy accumulation to obstruct repeatability of nonunital channels. Their per-use channel condition permits correlations between different outputs; our ideal requires independent channel calls tested with arbitrary references and adaptive inputs. Their open classification of unital repeatable channels is therefore not settled here. The common no-reset setting and entropy accounting are important precedents, while the present purity, error, and deadline statements use the stronger service contract.

Bisio, Chiribella, D'Ariano, and Perinotti [@bisio2011, Theorem 2] identify the minimal ancillary dimension at a cut of a coherent isometric realization with the rank of the corresponding truncated Choi operator. Bisio, D'Ariano, Perinotti, and Sedlak [@bisio2012] optimize coherent memory assisted by classical memory, define approximate memory cost, and show that separate cutwise optimizations need not be simultaneously attainable. These are prior realization and memory-optimization frameworks, not consequences of this paper. Our resource pair instead charges the full physical apparatus, including classical degrees of freedom, and its initial entropy deficit; the additional claims concern this closed inventory at vanishing error and under the specified deadlines.

Faist, Berta, and Brandão [@faist2021, Theorem 5.1] characterize collective asymptotic implementation cost for trivial Hamiltonians by \(\max_\rho[S(\rho)-S(\Phi(\rho))]\), which is zero for a unital channel. Their thermodynamic model optimizes work using a battery and free thermal resources, not the total initially retained apparatus studied here. Thus vanishing collective work cost is compatible with a positive short-delay initial-purity cost; this paper does not identify these two resources or replace their thermodynamic result.

The separately released paper on closed repeated use [@douglas2026] fixes one repeated interaction and requires immediate output return. The present upper bound instead permits a tensor-block unitary and delayed block release. The former's immediate-service lower bounds and this paper's delayed constructions therefore have different contracts. This paper does not replace that result.

The contribution established here is the two-polar closed Schur compression theorem, its matched leading-order exact-versus-vanishing-error separation, and its separately scoped scheduled-delivery consequence. The literature comparison is targeted rather than a claim of exhaustive priority certification.

\clearpage

# Resource and error ledger

| Item | What is charged / proved |
|---|---|
| Physical apparatus | Entire dimension \(m\), including support initially outside \(\beta\) |
| Initial occupied rank | \(r=\lceil\sqrt{k+2}\rceil\) |
| Initial entropy | \(S(\beta)=\log_2r\) |
| Dimension resource | \(Q=\log_2m\) |
| Purity resource | \(P=\log_2(m/r)\) |
| Mathematical purifier | Inaccessible; not physical inventory |
| Public randomness | None |
| Runtime Gaussian randomness | None; Gaussian argument proves existence of a fixed realization |
| Reset/disposal | None available to the implementation |
| Postselection | None |
| Static approximation | \(D_\diamond(\Psi,\Phi)\le2\epsilon/3\le\epsilon\) |
| Uniform references | Included through common-Stinespring operator norm |
| Hardware complexity | Unrestricted; no efficient compiler claimed |
| Exact extreme endpoint | \(m\ge k\,\mathrm{rank}\beta\), hence \(P,Q\ge\log_2k\) |
| Timing lower error | Every epoch uses the original global stopped error \(\epsilon\); errors are not summed |
| Timing upper error | \(K\) block substitutions at error \(\eta\) give \(K\eta\) |
| Scheduled arrivals | Mandatory |
| Current-block feedback | Not available before block release |
| Unfinished-block stop | Observation only; no flush |
| Payload custody | Up to \(b\) ququarts, adding at most \(2b\) qubits |
| Autonomous clock | Not proved or supplied for free |


# Limitations

The results do not establish an efficient or uniform circuit compiler. The deterministic Gaussian realization may require an arbitrarily expensive offline search and arbitrary fixed hardware.

The static theorem is Schur-specific. The entropy converse is general, but it does not turn the upper construction into a theorem for arbitrary channels.

The exact lower bound uses CPTP extremality essentially and must not be transferred to nonzero error branch by branch.

The scheduled upper bound requires mandatory arrivals. A user who refuses to provide input \(t+1\) until receiving output \(t\) can prevent a multi-input block from ever being assembled. Diamond accuracy of the completed joint block does not repair a missing physical input.

The scheduled theorem does not provide an autonomous clock, optional-arrival service, early flushing, or a sharp \(b=c\log T\) frontier.

Finally, initial apparatus size is not the same quantity as all physical matter temporarily in the device; retained input payloads must be added separately when peak storage is reported.



# Verification and reproducibility {.unnumbered}

The ancillary checks verify finite matrix identities for the ququart Kraus family, the tetrahedral inverse on matrix units and with a small reference, the two Gaussian-indexing conventions, and a small fixed Gaussian realization followed by both polar normalizations. They are finite diagnostics, not proofs of the concentration event, diamond bound, or asymptotic theorem.

The accompanying Lean sources contain an inherited finite complex-density-matrix proof that a bath-only unitary preserves the complete user marginal, and six elementary natural-number inventory and epoch lemmas. The no-signalling lemma permits arbitrary initial correlations and finite references. These files do not formalize entropy, Gaussian concentration, polar decomposition, or the headline theorems. Exact coverage, dependency reports, and reproduction instructions are in the ancillary documentation.

The authoritative readable proof is this manuscript. The repository supplies Markdown, generated TeX, a compiled PDF, build instructions, provenance hashes, and a narrowly allowlisted public export. The original research notes remain private historical sources and are not necessary to read or rebuild the paper.

# AI assistance {.unnumbered}

AI systems assisted with proof exploration, manuscript preparation and checking. Additional independent AI sessions audited the arguments and their relationship to prior work. These sessions were not human external peer review. The author is responsible for the manuscript and its claims. The limited Lean coverage is stated explicitly above and in the accompanying coverage document.

# Data, code, and licensing {.unnumbered}

This work uses no experimental dataset. The accompanying finite diagnostics and source-build scripts are provided for reproducibility. The manuscript is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0); original ancillary software is MIT-licensed. Third-party works and dependencies retain their own licenses.
