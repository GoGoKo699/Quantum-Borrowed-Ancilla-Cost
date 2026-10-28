# Deterministic accuracy lower bound

A coherent circuit built from one- and two-qubit gates that conserve excitation number cannot implement CCZ exactly on three data qubits while acting as the identity on an arbitrary finite borrowed register. Its minimum error is bounded below by a quantity proportional to the reciprocal of the total register size. This page proves the converse; the [matching construction](construction.md) attains it for every register size.

## Model and statement

There are three data qubits and $`m\geq0`$ borrowed qubits, so $`N=m+3`$. Write

```math
n_j=|1\rangle\langle1|_j,
\qquad
Q=\sum_{j=1}^{N}n_j,
\qquad
T=\mathrm{CCZ}_{123}\otimes I_B.
```

Here $`I_B`$ is the identity on the $`m`$-qubit borrowed register $`B`$. Let $`G_N`$ consist of all finite products of one- and two-qubit unitary gates, each of which commutes with the sum of $`n_j`$ on its support. Arbitrary continuous gate parameters and arbitrary pairs of qubits are allowed. Every circuit therefore commutes with $`Q`$.

For $`W\in G_N`$, define

```math
\delta(W)
=
\frac12\left\|\mathrm{Ad}_W-\mathrm{Ad}_T\right\|_\diamond,
\qquad
\mathrm{Ad}_U(\rho)=U\rho U^\dagger.
```

The channel comparison acts on the complete $`N`$-qubit register. It covers arbitrary borrowed inputs, correlations with the data, and entanglement with an untouched reference. The identity on the borrowed register is part of the target operation. At positive error, restoration is approximate in this joint sense. See the [model](model.md) for the full operational contract.

**Theorem.** For every integer $`m\geq0`$ and every $`W\in G_N`$,

```math
\delta(W)\geq
\sin a,
\qquad
a=\frac{\pi}{4(N-1)}
=\frac{\pi}{4(m+2)}.
```

The proof uses a multiplicative combination of four sector determinants. Determinant constraints on local symmetric circuits are part of the established theory of symmetric gate groups [Marvian 2024](../references/RELATED_WORK.md#marvian2024). The argument below derives the particular character and its quantitative consequence directly; the lower bound does not require a sufficient condition for membership in $`G_N`$.

## 1. A determinant character on four charge sectors

Let $`\Pi_k`$ project onto the subspace $`\mathcal H_k`$ of states with $`k`$ excitations. Its dimension is

```math
d_k=\dim\mathcal H_k=\binom Nk,
\qquad
\mathcal H=\bigoplus_{k=0}^{N}\mathcal H_k.
```

For a unitary $`U`$ commuting with $`Q`$, let $`U_k`$ denote its restriction to $`\mathcal H_k`$. Define

```math
\chi_N(U)
=
\frac{\det U_1}{\det U_{N-1}}
\left(\frac{\det U_N}{\det U_0}\right)^{N-2}.
```

Determinants multiply even when their matrices do not commute, so $`\chi_N(UV)=\chi_N(U)\chi_N(V)`$. Also, $`\chi_N`$ is unchanged by a global phase. Indeed, replacing $`U`$ by $`e^{i\gamma}U`$ multiplies the character by

```math
\exp\!\left(
i\gamma\left[
d_1-d_{N-1}+(N-2)(d_N-d_0)
\right]
\right)=1,
```

because $`d_1=d_{N-1}=N`$ and $`d_0=d_N=1`$. Thus $`\chi_N`$ is well-defined on unitary channels.

### Every allowed gate has character one

Consider an allowed two-qubit gate $`A`$. In the local excitation decomposition it has blocks $`A_0,A_1,A_2`$ of dimensions $`1,2,1`$. Put $`\eta_j=\det A_j`$. If $`\widehat A`$ denotes this gate embedded in the $`N`$-qubit register, then

```math
\det \widehat A_k
=
\eta_0^{\binom{N-2}{k}}
\eta_1^{\binom{N-2}{k-1}}
\eta_2^{\binom{N-2}{k-2}}.
```

We use $`\binom rs=0`$ when $`s<0`$ or $`s>r`$. To obtain the formula, decompose the total charge-$`k`$ sector according to the charge $`j`$ on the gate's two qubits. The block $`A_j`$ occurs once for each spectator basis state of weight $`k-j`$, giving precisely $`\binom{N-2}{k-j}`$ copies.

For the four relevant sectors, this reduces to

| Sector $`k`$ | $`\det \widehat A_k`$ |
|---|---|
| $`0`$ | $`\eta_0`$ |
| $`1`$ | $`\eta_0^{N-2}\eta_1`$ |
| $`N-1`$ | $`\eta_1\eta_2^{N-2}`$ |
| $`N`$ | $`\eta_2`$ |

Substitution gives

```math
\chi_N(\widehat A)
=
\frac{\eta_0^{N-2}\eta_1}
{\eta_1\eta_2^{N-2}}
\left(\frac{\eta_2}{\eta_0}\right)^{N-2}
=1.
```

An allowed one-qubit gate, tensored with the identity on one other qubit, is an allowed two-qubit gate. It therefore satisfies the same conclusion. Multiplicativity now proves

```math
\chi_N(W)=1
\qquad\text{for every }W\in G_N.
```

### The target has character minus one

CCZ changes the sign of a computational basis vector exactly when its first three bits are $`111`$. Within sector $`k`$, the number of such vectors is

```math
b_k=\binom{m}{k-3},
\qquad
\det T_k=(-1)^{b_k}.
```

In the four relevant sectors, the determinants are $`1,1,(-1)^m,-1`$, respectively. These formulas include $`m=0`$ under the binomial convention above. Consequently,

```math
\chi_N(T)
=
(-1)^{-m}(-1)^{N-2}
=
(-1)^{N-2-m}
=-1.
```

For the target-relative error unitary $`E=T^\dagger W`$, it follows that

```math
[E,Q]=0,
\qquad
\chi_N(E)=\chi_N(T)^*\chi_N(W)=-1.
```

## 2. Diamond error controls the spectral arc

For two unitary channels, their half-diamond distance can be expressed through the eigenvalues of their relative unitary:

```math
\delta(W)
=
\sqrt{1-\nu(E)^2},
\qquad
\nu(E)=\min_{\rho}\left|\mathrm{Tr}(\rho E)\right|
=
\mathrm{dist}\!\left(
0,\mathrm{conv}(\mathrm{spec}E)
\right).
```

Here the minimum ranges over density operators on the acted-on register. To see the first equality, purify an arbitrary input $`\rho`$ to $`|\Psi\rangle`$. The two unitary outputs are pure, their overlap is $`\langle\Psi|(E\otimes I)|\Psi\rangle=\mathrm{Tr}(\rho E)`$, and their half-trace distance is the square root in the formula. Purification cannot reduce distinguishability, because tracing out the purifying system is a channel. It therefore suffices to optimize over these pure joint inputs. For the second equality, diagonalize $`E`$: the diagonal entries of $`\rho`$ in this basis are an arbitrary probability distribution on its eigenvalues.

If $`\delta(W)=1`$, the claimed lower bound already holds. Suppose instead that $`\delta(W)<1`$. Then the origin lies outside the convex hull of the eigenvalues, so they lie in an open semicircle. Let $`2\alpha<\pi`$ be the length of their shortest containing arc. After multiplying $`E`$ by a global phase, all its eigenvalues have the form $`e^{i\varphi}`$ with $`\varphi\in[-\alpha,\alpha]`$, and both endpoints of this shortest arc occur.

Every convex combination of these eigenvalues has real part at least $`\cos\alpha`$. The midpoint of the two endpoint eigenvalues is $`\cos\alpha`$, so

```math
\nu(E)=\cos\alpha,
\qquad
\delta(W)=\sin\alpha,
\qquad
\alpha=\arcsin\delta(W).
```

The global rephasing does not alter $`\chi_N(E)`$.

## 3. The character requires a finite phase budget

Choose the eigenangles of each rephased block $`E_k`$ as $`\varphi_{k,r}\in[-\alpha,\alpha]`$, for $`1\leq r\leq d_k`$. Introduce the integer weights

```math
c_0=-(N-2),\qquad
c_1=1,\qquad
c_{N-1}=-1,\qquad
c_N=N-2,
```

with $`c_k=0`$ on every other sector. The angle of the character is represented by the real number

```math
\Phi=\sum_{k=0}^{N}c_k\sum_{r=1}^{d_k}\varphi_{k,r}.
```

Since $`\exp(i\Phi)=\chi_N(E)=-1`$, the number $`\Phi`$ is an odd multiple of $`\pi`$ and hence $`|\Phi|\geq\pi`$. On the other hand,

```math
\begin{aligned}
|\Phi|
&\leq \alpha\sum_{k=0}^{N}|c_k|d_k\\
&=\alpha\bigl[(N-2)+N+N+(N-2)\bigr]\\
&=4(N-1)\alpha.
\end{aligned}
```

Combining the two inequalities gives $`\alpha\geq a`$. Since sine is increasing on $`[0,\pi/2]`$,

```math
\boxed{\delta(W)\geq
\sin\!\left(\frac{\pi}{4(m+2)}\right).}
```

This bound holds for every finite circuit in the allowed group and every finite borrowed-register size. In particular, exact implementation is impossible with arbitrary borrowed qubits alone. The [construction](construction.md) saturates the bound, including the case $`m=0`$.

