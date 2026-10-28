# A matching construction for every borrowed-register size

For every $`m\geq0`$, a finite circuit of one- and two-qubit gates that conserve excitation number attains the [deterministic lower bound](deterministic_bound.md). The construction specifies its full unitary matrix through a scalar correction in each total-charge sector. An established synthesis theorem then realizes that matrix using the same $`N=m+3`$ qubits.

The result is

```math
\min_{W\in G_N}
\frac12\left\|\operatorname{Ad}_W-\operatorname{Ad}_T\right\|_\diamond
=
\sin\!\left(\frac{\pi}{4(N-1)}\right),
\qquad
T=\operatorname{CCZ}_{123}\otimes I_B.
```

Here $`B`$ denotes the $`m`$-qubit borrowed register. As in the [model](model.md), $`G_N`$ is the group of finite products of arbitrary continuous one- and two-qubit unitaries that each conserve excitation number on their support. No additional qubits are supplied to the construction.

## 1. Exact reachability inside the charge sectors

Let

```math
Q=\sum_{j=1}^{N}n_j,
\qquad
n_j=|1\rangle\langle1|_j,
\qquad
\Pi_k=\text{projector onto }\mathcal H_k,
\qquad
d_k=\binom Nk.
```

The synthesis argument uses the following established statement:

> Every unitary $`V=\bigoplus_{k=0}^{N}V_k`$ with $`V_k\in\operatorname{SU}(\mathcal H_k)`$ belongs to $`G_N`$.

Thus determinant-one transformations can be chosen independently in all charge sectors. In the one-dimensional sectors, determinant one means $`V_0=V_N=1`$.

For qubits, this is the U(1) specialization of Theorem 3 and Section IV.4 of [Marvian 2024](../references/RELATED_WORK.md#marvian2024). Equal-weight computational basis strings are connected by conserving two-qubit swaps, which gives the required transitivity and hence semi-universality. The term *semi-universality* here means that all these independent special-unitary factors are available, while relative determinant phases remain constrained.

A direct finite synthesis is provided by Section V, Step 3, Proposition 13 of [Bai and Marvian 2024](../references/RELATED_WORK.md#bai2024). It implements every such sectorwise determinant-one unitary without ancillary qubits, using gates from a subset of our allowed gate set. This is exact membership in the group of finite gate sequences, not merely membership in its topological closure. Arbitrary continuous rotation angles are part of the native-gate model.

This imported statement does not supply an efficient implementation of the particular family below. It establishes exact finite-circuit reachability on the stated register. No polynomial gate-count or depth bound in $`N`$ is claimed here.

## 2. An allowed quadratic phase

Set

```math
a=\frac{\pi}{4(N-1)}
\qquad\text{and}\qquad
p(k)
=
a-\frac{\pi(N+3)}{2N(N-1)}k
+\frac{3\pi}{2N(N-1)}k^2.
```

The unitary $`P=\exp(ip(Q))`$ is in $`G_N`$. Indeed, using $`n_j^2=n_j`$,

```math
Q^2=Q+2\sum_{1\leq i<j\leq N}n_i n_j,
```

and all terms commute. Hence

```math
P=
e^{ia}
\prod_{j=1}^{N}
\exp\!\left(-\frac{i\pi}{2(N-1)}n_j\right)
\prod_{1\leq i<j\leq N}
\exp\!\left(\frac{3i\pi}{N(N-1)}n_i n_j\right).
```

Each factor acts on at most two qubits and conserves their excitation number. The scalar $`e^{ia}`$ can itself be included as a one-qubit scalar unitary; it is also irrelevant to the implemented channel.

The polynomial has the four useful values

```math
p(0)=a,\qquad
p(1)=-a,\qquad
p(N-1)=a+\frac{\pi(N-3)}{N},\qquad
p(N)=\pi-a.
```

These values place the extremal correction phases at the four sectors appearing in the determinant converse.

## 3. Correcting the target determinants

As in the lower bound, put

```math
b_k=\binom{m}{k-3},
\qquad
\det T_k=(-1)^{b_k},
```

with the convention that a binomial coefficient is zero outside its usual range. Define the wrapping function explicitly by

```math
\operatorname{wrap}(x)
=
x-2\pi\left\lfloor\frac{x+\pi}{2\pi}\right\rfloor
\in[-\pi,\pi).
```

In particular, the boundary value $`\pi`$ is represented by $`-\pi`$. Now set

```math
\theta_k
=
\frac{\operatorname{wrap}\!\left(d_kp(k)-\pi b_k\right)}{d_k},
\qquad
\Theta=\sum_{k=0}^{N}\theta_k\Pi_k,
\qquad
W=T e^{i\Theta}.
```

The appearance of $`T`$ in this definition specifies a desired matrix; it does not assume that a CCZ gate is already available as a primitive. We prove that $`W`$ belongs to $`G_N`$ by matching its determinants to those of the allowed quadratic phase.

For each sector, there is an integer

```math
\ell_k=
\left\lfloor
\frac{d_kp(k)-\pi b_k+\pi}{2\pi}
\right\rfloor
```

such that $`d_k\theta_k=d_kp(k)-\pi b_k-2\pi\ell_k`$. Therefore

```math
\begin{aligned}
\det W_k
&=\det T_k\,e^{id_k\theta_k}\\
&=\exp\!\left(i\pi b_k+id_k\theta_k\right)\\
&=\exp\!\left(id_kp(k)\right).
\end{aligned}
```

Define $`V=P^\dagger W`$. It commutes with $`Q`$, and in every charge sector

```math
\det V_k
=
e^{-id_kp(k)}\det W_k
=1.
```

The imported sectorwise synthesis theorem gives $`V\in G_N`$. Since $`P\in G_N`$, the factorization $`W=PV`$ proves $`W\in G_N`$. Both factors act on the same $`N`$ qubits. The proof uses no auxiliary register and no assumption about the initial borrowed state.

## 4. Bounding every correction phase

### The four edge sectors

The relevant dimensions and target multiplicities are

```math
(d_0,d_1,d_{N-1},d_N)=(1,N,N,1),
\qquad
(b_0,b_1,b_{N-1},b_N)=(0,0,m,1).
```

Using $`m=N-3`$ and the four values of $`p`$ above gives the unwrapped residuals

```math
\begin{aligned}
d_0p(0)-\pi b_0&=a,\\
d_1p(1)-\pi b_1&=-Na,\\
d_{N-1}p(N-1)-\pi b_{N-1}&=Na,\\
d_Np(N)-\pi b_N&=-a.
\end{aligned}
```

Since $`N\geq3`$ implies $`Na=\pi N/[4(N-1)]<\pi`$, all four residuals already lie strictly inside the wrapping interval. Dividing by their sector dimensions yields

```math
(\theta_0,\theta_1,\theta_{N-1},\theta_N)
=(a,-a,a,-a).
```

### Interior sectors when $`N\geq8`$

The definition of wrapping gives $`|\theta_k|\leq\pi/d_k`$. For $`2\leq k\leq N-2`$, symmetry and unimodality of the binomial coefficients give $`d_k\geq\binom N2`$. Consequently,

```math
|\theta_k|
\leq\frac{\pi}{\binom N2}
=\frac{2\pi}{N(N-1)}
\leq\frac{\pi}{4(N-1)}
=a
\qquad(N\geq8).
```

Together with the edge identities, this proves $`|\theta_k|\leq a`$ in every sector for $`N\geq8`$.

### The five smaller registers

For $`3\leq N\leq7`$, direct substitution into the same wrapping formula gives the following exact rational values. Each row lists $`(\theta_0/\pi,\ldots,\theta_N/\pi)`$ in increasing charge order.

| $`N`$ | $`m=N-3`$ | Correction phases divided by $`\pi`$ |
|---:|---:|---|
| $`3`$ | $`0`$ | $`(\frac18,-\frac18,\frac18,-\frac18)`$ |
| $`4`$ | $`1`$ | $`(\frac1{12},-\frac1{12},0,\frac1{12},-\frac1{12})`$ |
| $`5`$ | $`2`$ | $`(\frac1{16},-\frac1{16},-\frac3{80},\frac3{80},\frac1{16},-\frac1{16})`$ |
| $`6`$ | $`3`$ | $`(\frac1{20},-\frac1{20},-\frac1{20},0,\frac1{20},\frac1{20},-\frac1{20})`$ |
| $`7`$ | $`4`$ | $`(\frac1{24},-\frac1{24},\frac1{24},-\frac{19}{840},\frac{19}{840},-\frac1{24},\frac1{24},-\frac1{24})`$ |

Every listed phase has absolute value at most $`a/\pi=1/[4(N-1)]`$, and both endpoints occur. These finite rational evaluations complete the proof for all $`N\geq3`$.

## 5. Exact channel error

For the constructed circuit, $`T^\dagger W=e^{i\Theta}`$. All its eigenphases lie in $`[-a,a]`$, and both endpoint phases occur. For any density operator $`\rho`$,

```math
\operatorname{Re}\operatorname{Tr}(\rho e^{i\Theta})
=
\sum_{k=0}^{N}\operatorname{Tr}(\rho\Pi_k)\cos\theta_k
\geq\cos a.
```

Equal weight on a phase-$`a`$ eigenvector and a phase-$`-a`$ eigenvector attains overlap $`\cos a`$. The unitary-channel distance formula proved in the [converse](deterministic_bound.md#2-diamond-error-controls-the-spectral-arc) therefore gives

```math
\delta(W)=\sqrt{1-\cos^2a}=\sin a.
```

Together with the lower bound, this establishes

```math
\boxed{
\delta_{\mathrm{det}}^*(m)
=
\sin\!\left(\frac{\pi}{4(m+2)}\right)
\qquad\text{for every integer }m\geq0.
}
```

Finally, $`T=T^\dagger`$ and $`[T,\Theta]=0`$. Inverting the finite circuit for $`W`$ therefore gives a second allowed circuit

```math
W^\dagger=T e^{-i\Theta}\in G_N.
```

The pair has equal and opposite sector phases. It supplies the two branches used to attain the [randomized optimum](randomized_optimum.md).

