# From quantum channels to the cost of borrowed workspace

The question is whether unknown quantum memory can replace an initialized helper when every elementary gate conserves excitation number. For CCZ on three data qubits, the answer is quantitative: with $`m`$ borrowed qubits, the optimal half-diamond errors are $`\sin a_m`$ for one circuit and $`\sin^2a_m`$ for an averaged randomized circuit, where $`a_m=\pi/[4(m+2)]`$. Understanding this statement requires both the channel requirement on the memory and the restriction on the implementing gates.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). Section and statement numbers here refer to the [2018 author-hosted pre-publication manuscript](https://cs.uwaterloo.ca/~watrous/TQI/), as in the [milestone map](MILESTONES.md). The book supplies the operator and channel framework. The conserving circuit group, its determinant obstruction, and the exact width law are developed in this project using the research results cited below.

## Navigation

| Bridge section | Milestones |
|---|---|
| [Registers and information that must survive](#memory) | [M01](MILESTONES.md#m01)–[M05](MILESTONES.md#m05) |
| [The complete implementation task](#task) | [M06](MILESTONES.md#m06)–[M12](MILESTONES.md#m12) |
| [The obstruction and the attaining construction](#obstruction) | [M13](MILESTONES.md#m13)–[M20](MILESTONES.md#m20) |
| [Six gates with no borrowed qubits](#six-gates) | [M21](MILESTONES.md#m21) |
| [One input against every mixture](#common-probe) | [M22](MILESTONES.md#m22)–[M24](MILESTONES.md#m24) |
| [The exact averaged error](#averaging) | [M25](MILESTONES.md#m25)–[M27](MILESTONES.md#m27) |
| [Keeping the classical record](#record) | [M28](MILESTONES.md#m28) |
| [Charge promises and the meaning of the law](#scope) | [M29](MILESTONES.md#m29)–[M30](MILESTONES.md#m30) |

## Targeted source pointers and notation

The relevant starting points are Watrous Sections 1.1.2–1.1.3 for operators and norms, Sections 2.1.2–2.1.3 for states and purification, and Section 2.2.1 for channels. Sections 3.1.1, 3.2, and 3.3.1–3.3.3 support the error criterion. Sections 4.1.1 and 4.1.3 supply the language for unitary mixtures and entrywise channel action. These are targeted pointers into [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), and [Chapter 4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf).

| Watrous notation | Meaning in this project |
|---|---|
| $`\mathrm L(\mathcal X)`$ | Operators on a Hilbert space; $`X`$ in $`\mathcal E(X)`$ is an operator. |
| $`\mathrm D(\mathcal X)`$ | Positive operators of trace one, including $`\rho`$ and $`\tau`$. |
| $`\mathrm U(\mathcal X)`$ | Unitary operators, including $`T`$ and $`W`$. Two-space notation $`\mathrm U(\mathcal X,\mathcal Y)`$ instead allows rectangular isometries. |
| $`\mathrm C(\mathcal X,\mathcal Y)`$ | Completely positive, trace-preserving maps: quantum channels. |
| $`U^*`$ and $`uu^*`$ | $`U^\dagger`$ and $`\lvert u\rangle\langle u\rvert`$. |
| $`1_{\mathcal X}`$ and $`1_{\mathrm L(\mathcal X)}`$ | Identity operator $`I`$ and identity channel $`\mathrm{id}`$. |
| $`\lVert A\rVert_1`$ and $`\lVert A\rVert_\infty`$ | Trace norm and operator norm. |
| $`\lvert\!\lvert\!\lvert\Phi\rvert\!\rvert\!\rvert_1`$ | The diamond norm $`\lVert\Phi\rVert_\diamond`$. The project's error is half this norm for a channel difference. |

<a id="memory"></a>

## 1. Registers and information that must survive

A qubit has basis states $`\lvert0\rangle`$ and $`\lvert1\rangle`$. A register of $`N`$ qubits has a basis indexed by $`N`$-bit strings and dimension $`2^N`$. Here three qubits form the data register $`S`$, the other $`m`$ form the borrowed register $`B`$, and $`N=m+3`$. An untouched reference $`R`$ represents information correlated with either register.

CCZ changes the sign of $`\lvert111\rangle_S`$ and leaves the other basis vectors unchanged. Its effect is visible in superpositions: changing one component's sign changes a relative phase. Multiplying every component by the same phase has no effect on the resulting density operator.

Unknown memory requires preserving correlations. For example, consider

```math
\lvert\Gamma_+\rangle_{BR}
=\frac{\lvert0\rangle_B\lvert1\rangle_R
+       \lvert1\rangle_B\lvert0\rangle_R}{\sqrt2}.
```

Applying $`Z`$ to $`B`$ produces the orthogonal state $`\lvert\Gamma_-\rangle`$ with a minus sign between the terms. The reduced state of $`B`$ remains $`I/2`$. A marginal-return check therefore accepts an operation that has completely changed the joint information. Both joint states even have the same fixed total excitation number. Purification and partial trace, introduced in Watrous Section 2.1.3, make this distinction explicit.

The physical subsystem decomposition is
$`\mathcal H_{SB}=\mathcal H_S\otimes\mathcal H_B`$.
Charge gives a different decomposition. With $`n_j=\lvert1\rangle\langle1\rvert_j`$ and $`Q=\sum_jn_j`$,

```math
\mathcal H_{SB}=\bigoplus_{k=0}^{N}\mathcal H_k,
\qquad
\dim\mathcal H_k=\binom Nk.
```

The tensor product separates physical registers; the direct sum groups basis strings by their number of ones. For three qubits, the sector dimensions are $`1,3,3,1`$. These dimensions will control how much determinant phase a small scalar correction can absorb.

<a id="task"></a>

## 2. The complete implementation task

Every primitive gate acts on at most two qubits and commutes with the excitation number on its support. The group $`G_N`$ contains finite products of these gates, with arbitrary real angles. No extra prepared quantum register, reset, measurement, or discarded quantum workspace is supplied. Circuit length is unrestricted.

Every allowed circuit commutes with $`Q`$, but this condition alone does not characterize $`G_N`$. A target may conserve total charge and still be unreachable using conserving two-qubit primitives. CCZ is the example studied here. The distinction concerns the intermediate operations as well as the final matrix.

The ideal action is specified on the whole register:

```math
T=\mathrm{CCZ}_S\otimes I_B,
\qquad
\mathcal T(X)=TXT^\dagger.
```

More generally, $`\mathrm{Ad}_W(X)=WXW^\dagger`$ denotes the channel implemented by a unitary $`W`$.

An implementation is judged by

```math
\delta(\mathcal E,\mathcal T)
=\frac12\|\mathcal E-\mathcal T\|_\diamond
=\max_{\rho_{SBR}}
\frac12\left\|
\big[(\mathcal E-\mathcal T)\otimes\mathrm{id}_R\big](\rho_{SBR})
\right\|_1.
```

This scores the data transformation, restoration of borrowed information, and preservation of its correlations together. At positive error, return is approximate in this joint sense. A reference of dimension $`2^N`$ suffices. It belongs to the distinguishing experiment and is inaccessible to the implementing circuit.

Watrous's Definition 3.43 defines the full completely bounded trace norm; the factor $`1/2`$ above is additional. Theorem 3.51 justifies optimization over pure joint inputs for a channel difference. The error ranges from zero to one. A specified measurement provides a lower bound on it.

The fidelity convention also matters. Watrous Definition 3.11 uses

```math
F(P,Q)=\|\sqrt P\sqrt Q\|_1.
```

For pure states, this is the overlap modulus. Their half-trace distance is
$`\sqrt{1-\lvert\langle u\mid v\rangle\rvert^2}`$,
as in Eq. (1.186). For a pure target projector $`P`$ and mixed output $`\rho`$, its acceptance probability is $`F(P,\rho)^2=\mathrm{Tr}(P\rho)`$.

A classical random choice gives the channel $`\sum_jp_j\mathrm{Ad}_{W_j}`$, with probabilities independent of the input. It averages output density operators. The random choice record is discarded in the randomized optimization; Section 7 below examines what changes when it is scored.

Initialization changes the input promise. A known helper in $`\lvert0\rangle`$ leaves the orthogonal helper branch unspecified. For example, the four-qubit unitary that flips the signs of $`\lvert1110\rangle`$ and $`\lvert1101\rangle`$ has determinant one in each charge sector. Established sectorwise reachability makes it implementable. On helper-zero inputs it gives exact CCZ, while the other branch compensates the determinant. A borrowed helper requires the target action on both branches and their superpositions. The [prepared-helper explanation](../science/interpretation.md#why-a-prepared-qubit-helps) and [research attribution](../references/RELATED_WORK.md#marvian2024) give the precise imported result.

<a id="obstruction"></a>

## 3. The obstruction and the attaining construction

A conserving unitary decomposes as $`W=\bigoplus_kW_k`$. Its block determinant records the sum of eigenphases in sector $`k`$, modulo $`2\pi`$. The project combines four such determinants:

```math
\chi_N(W)=
\frac{\det W_1}{\det W_{N-1}}
\left(\frac{\det W_N}{\det W_0}\right)^{N-2}.
```

The weighted block dimensions balance, so a global phase leaves $`\chi_N`$ unchanged. When a two-qubit gate is embedded in $`N`$ qubits, each of its local charge blocks is repeated according to the number of compatible spectator basis strings. Substituting those multiplicities into $`\chi_N`$ cancels all local determinant factors. Every primitive therefore has character one. Determinants multiply under composition, so every finite allowed circuit also has character one. Spectators here are tensor factors of the matrix, without any specified initial state.

The target has a different sign. In sector $`k`$, CCZ flips $`\binom{m}{k-3}`$ basis vectors, giving
$`\det T_k=(-1)^{\binom{m}{k-3}}`$.
The four-sector combination equals $`-1`$ for every $`m`$. Adding finitely many borrowed qubits never removes this exact mismatch. The [character proof](../science/deterministic_bound.md#1-a-determinant-character-on-four-charge-sectors) establishes these identities.

To obtain a precision bound, compare the target and circuit through $`E=T^\dagger W`$. The overlap of their purified outputs is $`\mathrm{Tr}(\rho E)`$. Diagonalizing $`E`$ turns this into a probability-weighted average of its eigenvalues. If they occupy a shortest arc of half-width $`\alpha<\pi/2`$, their convex hull comes closest to zero at distance $`\cos\alpha`$. The channel error is consequently $`\sin\alpha`$. The [spectral argument](../science/deterministic_bound.md#2-diamond-error-controls-the-spectral-arc) includes the remaining case of error one.

The character is invariant under a global phase, so the containing arc can be centered at zero before bounding its eigenangles. Each eigenangle then lies in $`[-\alpha,\alpha]`$. The character of $`E`$ is $`-1`$, so its weighted eigenphase sum must be an odd multiple of $`\pi`$. The total absolute weight of the four sectors is
$`(N-2)+N+N+(N-2)=4(N-1)`$.
Hence

```math
\pi\leq4(N-1)\alpha,
\qquad
\delta_{\mathrm{det}}^*(m)\geq
\sin\!\left(\frac{\pi}{4(N-1)}\right).
```

The matching construction uses a scalar phase $`\theta_k`$ within each charge sector. Such a phase changes its determinant by $`e^{id_k\theta_k}`$. A larger block can therefore absorb a given determinant correction through a smaller phase per state.

First choose an allowed quadratic phase $`P=e^{ip(Q)}`$. It factors into one- and two-qubit diagonal gates because

```math
Q^2=Q+2\sum_{i<j}n_i n_j.
```

Then choose $`\Theta=\sum_k\theta_k\Pi_k`$ so that $`W=T e^{i\Theta}`$ has the same determinant as $`P`$ in every sector. The remaining factor $`P^\dagger W`$ has determinant one in every block. [Marvian's sectorwise result](../references/RELATED_WORK.md#marvian2024) and [Bai–Marvian's finite synthesis](../references/RELATED_WORK.md#bai2024) put that factor in $`G_N`$. Writing $`T`$ in the desired matrix has not supplied CCZ as an elementary gate.

The [construction](../science/construction.md) specifies the polynomial and wrapped phases. Every phase lies in $`[-a_m,a_m]`$, with both endpoints present. A dimension estimate handles $`N\geq8`$; exact rational evaluations handle $`N=3,\ldots,7`$. Thus the lower bound is attained for every width. This is finite reachability, with no assertion that the resulting circuits are short.

<a id="six-gates"></a>

## 4. Six gates with no borrowed qubits

For $`m=0`$, set $`a=\pi/8`$. The optimal circuit has an elementary form:

```math
W_0=e^{i\pi/8}
\prod_{j=1}^{3}e^{-i\pi n_j/4}
\prod_{j<\ell}e^{i\pi n_jn_\ell/2}
=T e^{iaP},
\qquad
P=(-1)^Q=Z_1Z_2Z_3.
```

Apart from the irrelevant scalar phase, there are three one-qubit and three two-qubit phase gates. They commute and conserve charge. Evaluating their phase on a string of weight $`k`$ gives $`\pi[1/8-k/4+\binom{k}{2}/2]`$. Subtracting the target's phase leaves $`+a`$ on even charge and $`-a`$ on odd charge. The [eight-basis-state identity](../science/examples.md#no-borrowed-qubits-six-diagonal-gates-suffice) verifies the full matrix.

Take $`\lvert e\rangle=\lvert000\rangle`$, $`\lvert o\rangle=\lvert001\rangle`$, and $`\lvert\psi\rangle=(\lvert e\rangle+\lvert o\rangle)/\sqrt2`$. CCZ is the identity on their span. The circuit and its inverse produce

```math
\lvert\psi_\pm\rangle
=\frac{e^{\pm ia}\lvert e\rangle+e^{\mp ia}\lvert o\rangle}{\sqrt2},
\qquad
\rho_\pm=
\frac12\begin{pmatrix}
1&e^{\pm2ia}\\
e^{\mp2ia}&1
\end{pmatrix}.
```

Their overlap with the ideal state is $`\cos a`$. Each output has half-trace distance $`\sin a=0.3826834324\ldots`$ from the ideal. The full channel error equals this value because the residual spectrum has exactly the two endpoint phases. The universal converse certifies optimality over all allowed circuits.

<a id="common-probe"></a>

## 5. One input against every mixture

A deterministic lower bound has the logical form “for each circuit, some input reveals an error.” The revealing input could change with the circuit. That statement does not supply one test for a distribution over circuits. The randomized converse establishes the stronger quantifier order: one fixed input and one fixed test work for every allowed circuit.

Set $`r=4(N-1)`$ and choose

```math
\tau=
\frac{\Pi_1+\Pi_{N-1}
+      (N-2)(\Pi_0+\Pi_N)}{r}.
```

The four sector dimensions normalize this density operator. Its weights are determined by the same character that produced the phase budget. The [trace-bound argument](../science/randomized_optimum.md#3-one-fixed-probe-bounds-every-allowed-circuit) proves

```math
\left|\mathrm{Tr}(\tau T^\dagger W)\right|
\leq\cos a_m
\qquad\text{for every }W\in G_N.
```

It converts the character into the determinant of an auxiliary direct-sum matrix and bounds that matrix's real trace. The direct sum is an algebraic device, without extra implementing qubits. For $`m=0`$, $`\tau=I_8/8`$; for larger registers it concentrates weight near the four charge edges.

Purify this same $`\tau`$ to $`\lvert\Omega_\tau\rangle`$ and let $`P_T`$ project onto its ideal output. Each circuit passes the test $`\{P_T,I-P_T\}`$ with probability at most $`\cos^2a_m`$. Averaging circuits averages these probabilities:

```math
\mathrm{Tr}(P_T\rho_{\mathrm{av}})
=\sum_jp_j
\left|\mathrm{Tr}(\tau T^\dagger W_j)\right|^2
\leq\cos^2a_m.
```

The ideal output passes with probability one, so this particular measurement gives

```math
\frac12\|\rho_{\mathrm{av}}-P_T\|_1
\geq1-\mathrm{Tr}(P_T\rho_{\mathrm{av}})
\geq\sin^2a_m.
```

The acceptance probability is squared fidelity in the convention established above. The calculation uses a fixed measurement, with no claim that trace distance always equals one minus squared fidelity. It also makes no assumption that the individual circuits are good approximations. The [full converse](../science/randomized_optimum.md#4-lower-bound-for-arbitrary-mixtures) covers arbitrary probability measures as well.

<a id="averaging"></a>

## 6. The exact averaged error

For the attaining circuit $`W=T e^{i\Theta}`$, the facts $`T=T^\dagger`$ and $`[T,\Theta]=0`$ give $`W^\dagger=T e^{-i\Theta}`$. Inverting allowed gates remains allowed. An equal classical choice between these two circuits therefore realizes the target followed by

```math
\Psi_\Theta(X)=
\frac12\left(e^{i\Theta}Xe^{-i\Theta}
+e^{-i\Theta}Xe^{i\Theta}\right).
```

In an eigenbasis of $`\Theta`$, this channel multiplies the matrix element $`X_{ij}`$ by $`\cos(\theta_i-\theta_j)`$. This is the Schur-channel form described in Watrous Section 4.1.3. Cancellation of coherent error by mixing is established in [Campbell's synthesis analysis](../references/RELATED_WORK.md#campbell2017). The [project's norm lemma](../science/randomized_optimum.md#5-exact-diamond-error-of-a-symmetric-two-branch-mixture) proves the error is exactly $`\sin^2a_m`$ when both endpoint phases occur. It bounds all joint inputs with a reference; cancellation of a first-order expansion alone would not establish that exact result.

For the three-qubit example, the calculation is especially transparent:

```math
\rho_{\mathrm{av}}
=\frac12\begin{pmatrix}
1&\cos(2a)\\
\cos(2a)&1
\end{pmatrix},
\qquad
\rho_{\mathrm{id}}
=\frac12\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
```

Their half-trace distance is $`[1-\cos(2a)]/2=\sin^2a`$. Moreover, since $`P^2=I`$, the entire residual channel is

```math
\Psi_{aP}
=\cos^2a\,\mathrm{id}+\sin^2a\,\mathrm{Ad}_P.
```

The states $`\lvert\psi\rangle`$ and $`P\lvert\psi\rangle`$ are orthogonal. Thus $`\mathrm{id}`$ and $`\mathrm{Ad}_P`$ have half-diamond distance one, and the displayed channel has error exactly $`\sin^2(\pi/8)=0.1464466094\ldots`$.

Combining the attaining mixture with the common-probe converse gives the exact squared relation between the two optima. The [integer width formulas](../science/model.md#required-number-of-borrowed-qubits) yield, as $`\epsilon\downarrow0`$,

```math
m_{\mathrm{det}}(\epsilon)=\frac{\pi}{4\epsilon}+O(1),
\qquad
m_{\mathrm{rand}}(\epsilon)=\frac{\pi}{4\sqrt\epsilon}+O(1).
```

For example, one-percent error requires at least 77 borrowed qubits deterministically, or six with the averaged randomized channel. These counts use the stated native gates and unrestricted circuit length.

<a id="record"></a>

## 7. Keeping the classical record

Retain the branch label of the three-qubit example in an orthogonal classical register $`C`$. The actual and ideal joint outputs are

```math
\sigma_{\mathrm{rec}}
=\frac12|0\rangle\langle0|_C\otimes\rho_+
+\frac12|1\rangle\langle1|_C\otimes\rho_-,
\qquad
\sigma_{\mathrm{id}}=\frac{I_C}{2}\otimes\rho_{\mathrm{id}}.
```

The ideal channel uses the same coin distribution. Because the labels occupy orthogonal blocks, their trace norms add:

```math
\frac12\|\sigma_{\mathrm{rec}}-\sigma_{\mathrm{id}}\|_1
=\frac12\left[
\frac12\|\rho_+-\rho_{\mathrm{id}}\|_1+
\frac12\|\rho_--\rho_{\mathrm{id}}\|_1
\right]
=\sin a.
```

Tracing out $`C`$ gives the smaller error calculated in Section 6. Each chosen circuit still has its coherent phase error; the label determines whether those opposite errors remain separately distinguishable in the scored output.

The [recorded-coin proposition](../science/randomized_optimum.md#7-the-optimum-when-the-coin-record-is-scored) extends this conclusion to the optimum over every finite or countable recorded ensemble. The same common purification gives a pure-output distance at least $`\sin a_m`$ in each branch. Orthogonal labels preserve their average distance, and a deterministic optimum attains the bound.

<a id="scope"></a>

## 8. Charge promises and the meaning of the law

The construction's residual phase is scalar within each charge sector. If the whole acted-on register is promised to occupy one fixed sector, that phase becomes global and its channel action disappears. This restricted task admits exact implementation by the constructed circuit.

The full-channel witness remains compatible with global charge conservation. Writing $`\tau=\sum_x\lambda_x|x\rangle\langle x|`$, choose the purification

```math
\lvert\Omega_\tau\rangle
=\sum_x\sqrt{\lambda_x}\,
|x\rangle_{SB}|\overline x\rangle_R.
```

The reference string is the bitwise complement, so every term has joint charge $`N`$. The target-output projector is globally invariant too. The acted-on register can have correlations across its own charge sectors while the combined register and reference have definite charge. This distinction is derived in the [invariant-witness construction](../science/randomized_optimum.md#8-a-charge-invariant-realization-of-the-lower-bound-probe).

The resource comparison therefore concerns preserving arbitrary unknown information under specified local controls. A prepared charge eigenstate provides an input subspace on which exact correctness is required; borrowed memory requires correctness throughout its Hilbert space and on its correlations. Neither resource is characterized here by a preparation-energy cost.

The exact laws quantify borrowed width. They allow arbitrary real gate angles and arbitrarily long finite circuits. The imported reachability theorem establishes existence of the necessary sector operations, without an efficient compiler for this family. The [interpretation](../science/interpretation.md) and [related-work comparison](../references/RELATED_WORK.md) keep these assumptions, the prepared-helper endpoint, and the inherited synthesis ingredients explicit.
