# Exact optimum with a discarded classical coin

Classical randomization changes the optimal precision attainable with borrowed qubits. In the model of [the complete return contract](model.md), the optimum half-diamond error is

```math
\delta_{\mathrm{rand}}^*(m)
=\sin^2\!\left(\frac{\pi}{4(m+2)}\right),
\qquad m\ge 0.
```

This statement concerns the averaged quantum channel after an input-independent classical coin has been discarded. If the coin label is retained and included in the scored output, the optimum instead equals the deterministic value. Both statements are proved below.

## 1. Model and inputs from the deterministic analysis

Let $`N=m+3\ge 3`$, let $`B`$ be the $`m`$-qubit borrowed register, let $`\mathcal H=(\mathbb C^2)^{\otimes N}`$, and define

```math
Q=\sum_{j=1}^{N}|1\rangle\langle1|_j,
\qquad
T=\operatorname{CCZ}_{123}\otimes I_B,
\qquad
a=\frac{\pi}{4(N-1)}.
```

The group $`G_N`$ consists of finite products of one-qubit and two-qubit unitary gates, each commuting with the charge on its support. Gates may act on any pair of qubits. The borrowed register has no prescribed initial state, and its correlations with the system or an inaccessible reference are included in the error criterion. We write $`\operatorname{Ad}_U(X)=UXU^\dagger`$.

A randomized implementation chooses $`W\in G_N`$ using a classical probability distribution independent of the quantum input and implements

```math
\Lambda_\mu(X)
=\int_{G_N} W X W^\dagger\,d\mu(W).
```

Here $`\mu`$ may be any probability measure for which the channel is defined, including a finite, countable, or continuous distribution. The classical record is discarded. The allowed randomness does not supply a measurement, reset, initialized quantum helper, or input-dependent control.

The optimum is

```math
\delta_{\mathrm{rand}}^*(m)
=\inf_\mu \frac12
\left\|\Lambda_\mu-\operatorname{Ad}_T\right\|_\diamond.
```

Let $`\Pi_k`$ project onto the charge-$`k`$ sector, of dimension $`d_k=\binom Nk`$. For a charge-preserving unitary $`V`$, write $`V_k`$ for its restriction to that sector. We use two facts established in the companion proofs.

1. The [determinant character](deterministic_bound.md)

   ```math
   \chi_N(V)
   =
   \frac{\det V_1}{\det V_{N-1}}
   \left(\frac{\det V_N}{\det V_0}\right)^{N-2}
   ```

   satisfies $`\chi_N(W)=1`$ for every $`W\in G_N`$, whereas $`\chi_N(T)=-1`$. Therefore

   ```math
   E=T^\dagger W
   \quad\Longrightarrow\quad
   \chi_N(E)=-1.
   ```

2. The [central-phase construction](construction.md), including its finite cases, gives an allowed unitary for every $`N\ge3`$ of the form

   ```math
   W_\star=T e^{i\Theta},
   \qquad
   \Theta=\sum_{k=0}^{N}\theta_k\Pi_k,
   \qquad
   -a\le\theta_k\le a.
   ```

   Both endpoints occur. In particular,

   ```math
   (\theta_0,\theta_1,\theta_{N-1},\theta_N)
   =(a,-a,a,-a).
   ```

The randomization argument below uses these facts but does not require a bound on circuit length.

## 2. A determinant-constrained trace bound

**Lemma 1.** Let $`F`$ be an $`r`$-dimensional unitary, where $`r\ge5`$, and suppose $`\det F=-1`$. Then

```math
\operatorname{Re}\operatorname{Tr}F
\le r\cos\!\left(\frac{\pi}{r}\right).
```

**Proof.** Write the eigenvalues as $`e^{i\varphi_j}`$. If at least one eigenvalue has nonpositive real part, then

```math
\operatorname{Re}\operatorname{Tr}F\le r-1
<r\cos\!\left(\frac{\pi}{r}\right).
```

The strict inequality follows from

```math
r\left[1-\cos\!\left(\frac{\pi}{r}\right)\right]
\le\frac{\pi^2}{2r}
\le\frac{\pi^2}{10}<1.
```

Otherwise every eigenvalue has positive real part, so choose its unique angle $`\varphi_j\in(-\pi/2,\pi/2)`$. The determinant condition gives

```math
S:=\sum_{j=1}^{r}\varphi_j=(2\ell+1)\pi
```

for an integer $`\ell`$. In particular, $`|S|\ge\pi`$, while $`S/r\in(-\pi/2,\pi/2)`$. Cosine is concave on this interval, even, and decreasing on $`[0,\pi/2]`$. Jensen's inequality therefore gives

```math
\frac1r\operatorname{Re}\operatorname{Tr}F
=\frac1r\sum_{j=1}^{r}\cos\varphi_j
\le\cos(S/r)
\le\cos(\pi/r).
```

This proves the claim. Equality is attained by $`F=e^{i\pi/r}I_r`$ or $`F=e^{-i\pi/r}I_r`$.

## 3. One fixed probe bounds every allowed circuit

Set $`r=4(N-1)\ge8`$ and define the density operator

```math
\tau
=\frac{\Pi_1+\Pi_{N-1}
       +(N-2)(\Pi_0+\Pi_N)}{r}.
```

It is normalized because $`d_0=d_N=1`$ and $`d_1=d_{N-1}=N`$. Its definition depends only on $`N`$, not on the circuit.

**Lemma 2.** Every $`W\in G_N`$ satisfies

```math
\left|\operatorname{Tr}(\tau T^\dagger W)\right|
\le\cos a.
```

**Proof.** Put $`E=T^\dagger W`$ and $`z=\operatorname{Tr}(\tau E)`$. A global phase leaves the character unchanged:

```math
\chi_N(e^{i\gamma}E)
=e^{i\gamma[d_1-d_{N-1}+(N-2)(d_N-d_0)]}\chi_N(E)
=\chi_N(E).
```

If $`z\ne0`$, choose $`\widetilde E=e^{-i\arg z}E`$. If $`z=0`$, take $`\widetilde E=E`$. In both cases,

```math
\chi_N(\widetilde E)=-1,
\qquad
\operatorname{Tr}(\tau\widetilde E)=|z|.
```

Form the auxiliary matrix

```math
F
=\widetilde E_1
\oplus
\widetilde E_N^{\oplus(N-2)}
\oplus
\widetilde E_{N-1}^{\dagger}
\oplus
(\widetilde E_0^\dagger)^{\oplus(N-2)}.
```

Its dimension is $`N+(N-2)+N+(N-2)=r`$, and

```math
\det F=\chi_N(\widetilde E)=-1.
```

Moreover, the real part of a trace is unchanged by taking the adjoint. Consequently,

```math
\begin{aligned}
\operatorname{Re}\operatorname{Tr}F
&=\operatorname{Re}\Big[
 \operatorname{Tr}\widetilde E_1
 +\operatorname{Tr}\widetilde E_{N-1}
 +(N-2)\big(
 \operatorname{Tr}\widetilde E_0+
 \operatorname{Tr}\widetilde E_N\big)\Big]\\
&=r\,\operatorname{Re}\operatorname{Tr}(\tau\widetilde E)
=r|z|.
\end{aligned}
```

Applying Lemma 1 gives $`|z|\le\cos(\pi/r)=\cos a`$.

The direct sums defining $`F`$ are an algebraic device for applying a trace inequality. They do not require physical copies of the system, extra implementing qubits, or an operation that takes the adjoint of an unknown gate. The circuit-dependent rephasing is also only a proof step; it changes neither the channel nor the modulus of the overlap.

## 4. Lower bound for arbitrary mixtures

Let $`|\Omega_\tau\rangle\in\mathcal H\otimes\mathcal H_R`$ be any fixed purification of $`\tau`$. Define

```math
|\Omega_T\rangle=(T\otimes I_R)|\Omega_\tau\rangle,
\qquad
P_T=|\Omega_T\rangle\langle\Omega_T|.
```

For each allowed circuit,

```math
\begin{aligned}
\langle\Omega_T|
(W\otimes I_R)|\Omega_\tau\rangle
&=\operatorname{Tr}(\tau T^\dagger W),\\
\operatorname{Tr}\!\left[
P_T(\operatorname{Ad}_W\otimes\operatorname{id}_R)
(|\Omega_\tau\rangle\langle\Omega_\tau|)
\right]
&\le\cos^2a.
\end{aligned}
```

Thus, for the output

```math
\rho_\mu
=(\Lambda_\mu\otimes\operatorname{id}_R)
(|\Omega_\tau\rangle\langle\Omega_\tau|),
```

linearity gives

```math
\operatorname{Tr}(P_T\rho_\mu)
=\int_{G_N}
\left|\operatorname{Tr}(\tau T^\dagger W)\right|^2\,d\mu(W)
\le\cos^2a.
```

The same input and the same two-outcome test $`\{P_T,I-P_T\}`$ work for every distribution. Their outcome probabilities imply

```math
\begin{aligned}
\frac12\|\rho_\mu-P_T\|_1
&\ge\operatorname{Tr}[P_T(P_T-\rho_\mu)]\\
&=1-\operatorname{Tr}(P_T\rho_\mu)
\ge\sin^2a.
\end{aligned}
```

Taking the supremum over inputs in the diamond norm can only increase this value. Therefore every allowed mixture satisfies

```math
\frac12\|\Lambda_\mu-\operatorname{Ad}_T\|_\diamond
\ge\sin^2a.
```

No proximity assumption on the individual circuits is used. In particular, mixing far-away circuits cannot evade the lower bound. The integral proof also covers continuous distributions directly; it does not assume a finite support or interchange a circuit-dependent optimizing input with an average.

## 5. Exact diamond error of a symmetric two-branch mixture

We first prove the channel-norm statement needed for achievability.

**Lemma 3.** Let $`\Theta`$ be a Hermitian operator on a finite-dimensional Hilbert space whose eigenvalues lie in $`[-a,a]`$, where $`0\le a\le\pi/2`$. Define

```math
\Psi_\Theta(X)
=\frac12\left(e^{i\Theta}Xe^{-i\Theta}
             +e^{-i\Theta}Xe^{i\Theta}\right).
```

Then

```math
\frac12\|\Psi_\Theta-\operatorname{id}\|_\diamond
\le\sin^2a.
```

If both $`-a`$ and $`a`$ occur in the spectrum, equality holds.

**Proof.** It suffices to bound the output trace norm for every normalized pure input with an arbitrary finite-dimensional reference. Convexity then gives the same bound for mixed states. To see why this also controls arbitrary operators in the diamond norm, let $`\Delta=\operatorname{id}-\Psi_\Theta`$. For any operator $`X`$ on the input and a reference, introduce an extra two-dimensional reference factor and form

```math
H_X=\frac12
\begin{pmatrix}0&X\\X^\dagger&0\end{pmatrix}.
```

The identities $`\|H_X\|_1=\|X\|_1`$ and

```math
\|(\Delta\otimes\operatorname{id})(H_X)\|_1
=\|(\Delta\otimes\operatorname{id})(X)\|_1
```

follow from the singular values and the fact that $`\Delta`$ preserves adjoints. The positive and negative parts of $`H_X`$ are nonnegative multiples of states, with coefficients summing to $`\|H_X\|_1`$. A uniform bound for states therefore bounds the induced trace norm for arbitrary operators and arbitrary references, which is the diamond norm.

Diagonalize $`\Theta=\sum_i\theta_i|i\rangle\langle i|`$ and write a normalized pure input as

```math
|\psi\rangle=\sum_i |i\rangle|v_i\rangle,
\qquad
p_i=\langle v_i|v_i\rangle,
\qquad
\sum_i p_i=1.
```

Omit indices with $`p_i=0`$; they contribute zero rows and columns to the matrices below. For the remaining indices the vectors

```math
|e_i\rangle
=|i\rangle\frac{|v_i\rangle}{\sqrt{p_i}}
```

are orthonormal, even when the reference vectors are not orthogonal. In this basis, the output difference

```math
\big[(\operatorname{id}-\Psi_\Theta)
\otimes\operatorname{id}_R\big]
(|\psi\rangle\langle\psi|)
```

is isometrically equivalent to the real symmetric matrix

```math
M(p)=D_p A D_p,
\qquad
D_p=\operatorname{diag}(\sqrt{p_i}),
\qquad
A_{ij}=1-\cos(\theta_i-\theta_j).
```

Isometric embedding preserves the nonzero eigenvalues and trace norm. With $`c_i=\cos\theta_i`$ and $`s_i=\sin\theta_i`$,

```math
A=\mathbf 1\mathbf 1^{\mathsf T}
-cc^{\mathsf T}-ss^{\mathsf T}.
```

It follows that $`M(p)`$ has at most one strictly positive eigenvalue. Indeed, its quadratic form is nonpositive on the subspace orthogonal to $`D_p\mathbf1`$. Its diagonal vanishes, so its trace is zero. Therefore

```math
\frac12\|M(p)\|_1=\lambda_{\max}(M(p)),
```

including the case $`M(p)=0`$.

All entries of $`M(p)`$ are nonnegative. A normalized eigenvector $`v`$ for its largest eigenvalue can therefore be chosen entrywise nonnegative, by the Perron-Frobenius theorem. Equivalently, replacing a real vector by its entrywise absolute value cannot decrease its Rayleigh quotient.

Put

```math
z_i=\sqrt{p_i}v_i,
\qquad
b=\sum_i z_i.
```

Because zero probabilities were omitted and $`v`$ is a nonzero nonnegative vector, $`b>0`$. Cauchy-Schwarz gives $`b\le(\sum_i p_i)^{1/2}(\sum_i v_i^2)^{1/2}=1`$. Hence $`q_i=z_i/b`$ is a probability distribution, and

```math
\begin{aligned}
\lambda_{\max}(M(p))
&=v^{\mathsf T}M(p)v\\
&=\sum_{i,j}z_i z_j\big[1-\cos(\theta_i-\theta_j)\big]\\
&=b^2\left[1-\left|\sum_iq_i e^{i\theta_i}\right|^2\right].
\end{aligned}
```

Since $`|\theta_i|\le a\le\pi/2`$,

```math
\operatorname{Re}\sum_iq_i e^{i\theta_i}
=\sum_iq_i\cos\theta_i
\ge\cos a\ge0.
```

Consequently,

```math
\lambda_{\max}(M(p))
\le b^2(1-\cos^2a)
\le\sin^2a.
```

This proves the upper bound for every pure input and every reference, and thus for the diamond norm.

If $`a=0`$, the channel is the identity and equality holds trivially. Otherwise, normalized eigenvectors $`|u_-\rangle`$ and $`|u_+\rangle`$ with eigenvalues $`-a`$ and $`a`$ are orthogonal. Use the input

```math
|\psi_{\mathrm{end}}\rangle
=\frac{|u_-\rangle+|u_+\rangle}{\sqrt2}.
```

No reference is needed for this input. Its output difference has matrix

```math
\begin{pmatrix}
0 & [1-\cos(2a)]/2\\
[1-\cos(2a)]/2 & 0
\end{pmatrix}
=
\begin{pmatrix}
0 & \sin^2a\\
\sin^2a & 0
\end{pmatrix}.
```

The half-trace norm is exactly $`\sin^2a`$, proving equality.

## 6. Achievability and the exact resource law

Take $`W_\star=T e^{i\Theta}`$ from [the construction](construction.md). Because $`\Theta`$ is scalar on every charge sector, it commutes with $`T`$. Also $`T=T^\dagger`$. Thus

```math
W_\star^\dagger=e^{-i\Theta}T=T e^{-i\Theta}.
```

The inverse of every allowed elementary gate is allowed, so both $`W_\star`$ and $`W_\star^\dagger`$ belong to $`G_N`$. An unbiased classical coin implements the channel

```math
\begin{aligned}
\Lambda_\star
&=\frac12\left(
\operatorname{Ad}_{W_\star}
+\operatorname{Ad}_{W_\star^\dagger}
\right)\\
&=\operatorname{Ad}_T\circ\Psi_\Theta.
\end{aligned}
```

Unitary invariance of the diamond norm and Lemma 3 yield

```math
\frac12\|\Lambda_\star-\operatorname{Ad}_T\|_\diamond
=\frac12\|\Psi_\Theta-\operatorname{id}\|_\diamond
=\sin^2a.
```

Together with the all-mixture lower bound, this proves

```math
\boxed{
\delta_{\mathrm{rand}}^*(m)
=\sin^2\!\left(\frac{\pi}{4(m+2)}\right)
}
\qquad (m\ge0).
```

The infimum is attained by two allowed circuits. Combining this with the [deterministic optimum](deterministic_bound.md) gives

```math
\delta_{\mathrm{rand}}^*(m)=\big[\delta_{\mathrm{det}}^*(m)\big]^2,
\qquad
m_{\mathrm{rand}}(\epsilon)=\Theta(\epsilon^{-1/2}),
\qquad
m_{\mathrm{det}}(\epsilon)=\Theta(\epsilon^{-1})
\quad\text{as }\epsilon\downarrow0.
```

Both optimizations score the full borrowed register. At nonzero error the complete return is approximate, as specified by the channel distance.

## 7. The optimum when the coin record is scored

The role of discarding the coin can be stated exactly. Consider a finite or countable input-independent distribution $`\{p_j,W_j\}`$. Let

```math
\widehat\Lambda(X)
=\sum_j p_j|j\rangle\langle j|_C\otimes W_j XW_j^\dagger
```

and compare it with the ideal recorded channel using the same coin distribution,

```math
\widehat{\mathcal T}(X)
=\sum_j p_j|j\rangle\langle j|_C\otimes TXT^\dagger.
```

**Proposition 4.** The optimum half-diamond error in this recorded model is

```math
\inf_{\{p_j,W_j\}}
\frac12\|\widehat\Lambda-\widehat{\mathcal T}\|_\diamond
=\sin a.
```

**Proof.** Use the same purification $`|\Omega_\tau\rangle`$ as in the mixture lower bound. Write $`|\Omega_j\rangle=(W_j\otimes I_R)|\Omega_\tau\rangle`$. Lemma 2 and the trace-distance identity for two pure states give, for every branch,

```math
\frac12\left\|
|\Omega_j\rangle\langle\Omega_j|-P_T
\right\|_1
=\sqrt{1-\left|\operatorname{Tr}(\tau T^\dagger W_j)\right|^2}
\ge\sin a.
```

The classical labels are orthogonal, so the trace norm of the recorded output difference is the sum of the block trace norms:

```math
\frac12\left\|
\sum_jp_j|j\rangle\langle j|_C
\otimes
\left(|\Omega_j\rangle\langle\Omega_j|-P_T\right)
\right\|_1
=
\sum_jp_j\frac12
\left\||\Omega_j\rangle\langle\Omega_j|-P_T\right\|_1
\ge\sin a.
```

This proves the lower bound for every recorded ensemble. A single deterministic optimal circuit attains $`\sin a`$. More generally, one may use that same circuit for every label in any prescribed input-independent coin distribution; adjoining its unchanged classical state does not change diamond distance.

The two branches $`W_\star`$ and $`W_\star^\dagger`$ also each have deterministic error $`\sin a`$. The triangle inequality gives recorded error at most their average, $`\sin a`$, so their retained-record protocol attains the recorded optimum as well.

Thus the same two-branch implementation has error $`\sin a`$ when its label is scored and $`\sin^2a`$ after that label is discarded.

## 8. A charge-invariant realization of the lower-bound probe

The witness in Section 4 does not require an input state that breaks the global charge symmetry. To see this, write

```math
\tau=\sum_{x\in\{0,1\}^{N}}\lambda_x|x\rangle\langle x|
```

and take an $`N`$-qubit reference $`R`$ with the same single-qubit charge convention. Denote the full acted-on register, including all borrowed qubits, by $`A`$, so $`Q_A=Q`$. Let $`\overline x`$ denote the bitwise complement of $`x`$ and define

```math
|\Omega_\tau\rangle
=\sum_x\sqrt{\lambda_x}\,|x\rangle_A|\overline x\rangle_R.
```

This is a purification of $`\tau`$. Every component has joint charge $`|x|+|\overline x|=N`$, so

```math
(Q_A+Q_R)|\Omega_\tau\rangle=N|\Omega_\tau\rangle.
```

Because $`T`$ and every $`W\in G_N`$ preserve $`Q_A`$, all relevant outputs remain in this joint charge sector. In particular, the ideal output projector $`P_T`$ and both effects of $`\{P_T,I-P_T\}`$ commute with $`Q_A+Q_R`$.

The preparation state and distinguishing measurement are therefore globally $`U(1)`$ invariant. The reference belongs to the certification experiment and remains inaccessible to the implementing circuit. This observation does not supply the implementation with a clean helper or imply an efficient preparation or measurement circuit.

This experiment is different from imposing a fixed-charge promise on the acted-on register $`A`$ alone. Such a promise excludes the correlations across its charge sectors that this complete-channel witness uses.

## 9. Relation to probabilistic synthesis

The suppression of coherent synthesis error by classical mixing is established in [Campbell's mixing analysis](../references/RELATED_WORK.md#campbell2017). Here the inverse pair is available because the target is an involution and the optimal correction commutes with it. Lemma 3 evaluates that pair's error exactly.

[Akibue, Kato, and Tani](../references/RELATED_WORK.md#akibue2024) give general bounds for optimal probabilistic unitary synthesis. Their pointwise lower bound is at least $`(2/d)\epsilon_{\mathrm{det}}^2`$ in dimension $`d`$, where $`\epsilon_{\mathrm{det}}`$ is the best deterministic error for the supplied set of unitaries. Applied without additional structure at $`d=2^N`$, that bound does not match the result here. The determinant-constrained fixed probe provides the stronger lower bound needed to certify the exact optimum for this conserving circuit group.
