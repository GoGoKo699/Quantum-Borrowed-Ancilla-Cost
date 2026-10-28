# Borrowed workspace and the exact precision law

An initialized helper qubit and a borrowed qubit provide different resources. The first comes in a specified state. The second may contain unknown information and must be returned without disturbing that information or its correlations. This distinction matters even for a fixed three-qubit gate when every elementary interaction conserves excitation number.

The target is controlled-controlled-Z, abbreviated CCZ. It changes the sign of the computational basis vector $`|111\rangle`$ and leaves the other seven basis vectors unchanged. CCZ itself conserves excitation number. Its implementation by conserving one- and two-qubit gates nevertheless encounters the locality constraints identified by [Marvian](../references/RELATED_WORK.md#marvian2022). A prepared helper removes that obstruction. The question here is how accurately arbitrary borrowed workspace can replace the prepared helper.

## Registers and native gates

Let $`S`$ contain the three data qubits and let $`B`$ contain $`m\geq0`$ borrowed qubits. Write $`N=m+3`$. Every qubit has the same charge operator

```math
n_j=|1\rangle\langle1|_j,
\qquad Q=\sum_{j=1}^{N}n_j.
```

For identical qubit energy gaps, conserving $`Q`$ is equivalent to conserving the total noninteracting energy, up to an additive constant and the common gap. Let $`\mathcal H_k`$ be the charge-$`k`$ subspace and $`\Pi_k`$ its projector. Then

```math
\mathcal H_{SB}=\bigoplus_{k=0}^{N}\mathcal H_k,
\qquad d_k=\dim\mathcal H_k=\binom Nk.
```

An allowed elementary gate acts on one or two qubits and commutes with the sum of their charges. The set $`G_N`$ consists of all finite products of these gates. Angles are arbitrary real numbers; the model does not restrict gates to a discrete alphabet. Every $`W\in G_N`$ is block diagonal,

```math
W=\bigoplus_{k=0}^{N}W_k,
\qquad W_k\in U(\mathcal H_k).
```

Any pair of qubits may interact. Restricting pairs to the edges of a connected graph gives the same reachable group because conserving SWAP gates can route qubits and undo the routing. This observation concerns reachability; it does not bound the number of routing gates or the depth.

No additional initialized quantum register, measurement, reset, postselection, or discarded quantum workspace is supplied. Circuit length and control precision are unrestricted in this width optimization. The randomized model below additionally permits an input-independent classical choice of circuit.

## Target and return condition

The ideal unitary on the complete acted-on register is

```math
T=\mathrm{CCZ}_{S}\otimes I_B,
\qquad
\mathrm{CCZ}=I_S-2|111\rangle\langle111|_S.
```

For a unitary $`V`$, write $`\mathcal V(X)=VXV^\dagger`$. Thus $`\mathcal T=\mathcal{CCZ}\otimes\mathrm{id}_B`$. The approximation error is

```math
\delta(\mathcal E,\mathcal T)
=\frac12\|\mathcal E-\mathcal T\|_\diamond.
```

The diamond norm optimizes over all inputs $`\rho_{SBR}`$, including inputs with correlations between the data, borrowed qubits, and an untouched reference $`R`$. Explicitly,

```math
\delta(\mathcal E,\mathcal T)
=\sup_{\rho_{SBR}}
\frac12\left\|
(\mathcal E\otimes\mathrm{id}_R)(\rho_{SBR})
-(T\otimes I_R)\rho_{SBR}(T^\dagger\otimes I_R)
\right\|_1.
```

A reference of dimension $`2^N`$ suffices. The maximum error is one. This normalization is used throughout the account.

The ideal borrowed-register action is the identity channel. At nonzero error, restoration and all correlations are approximated jointly with the data gate. The construction is not claimed to return an unknown borrowed register exactly at positive error. A condition that checks only the final borrowed marginal, or only one chosen borrowed input state, defines a different task.

## Deterministic and randomized optimization

For a deterministic circuit, define

```math
\delta_{\mathrm{det}}^*(m)
=\inf_{W\in G_N}\delta(\mathcal W,\mathcal T).
```

For classical probabilities $`p_j`$ independent of the input, an averaged randomized implementation has channel

```math
\mathcal E_p=\sum_jp_j\mathcal W_j,
\qquad W_j\in G_N,
\quad p_j\geq0,
\quad \sum_jp_j=1.
```

Its optimum is

```math
\delta_{\mathrm{rand}}^*(m)
=\inf_{p,\{W_j\}}\delta(\mathcal E_p,\mathcal T).
```

The random-choice record is discarded from the scored output. The random variable does not supply an initialized quantum helper or permission to measure the input. The lower bound also covers probability measures over arbitrary allowed circuits; a two-element distribution attains the optimum. If the classical record is retained and its correlations with the output are scored, the [recorded-coin result](randomized_optimum.md) gives a different optimum.

## The exact theorem

**Theorem 1.** Under the above gate and return conditions, for every integer $`m\geq0`$,

```math
\boxed{\displaystyle
\delta_{\mathrm{det}}^*(m)
=\sin a_m,
\qquad
\delta_{\mathrm{rand}}^*(m)
=\sin^2 a_m,
\qquad
a_m=\frac{\pi}{4(m+2)}.}
```

Both optima are attained by finite circuits. The randomized optimum uses an equal mixture of a constructed circuit and its inverse. The circuit realizing the deterministic optimum can be chosen as

```math
W=T\exp(i\Theta),
\qquad
\Theta=\sum_{k=0}^{N}\theta_k\Pi_k,
\qquad -a_m\leq\theta_k\leq a_m,
```

with both endpoints among the phases. The [construction](construction.md) gives every $`\theta_k`$ and proves that $`W`$ belongs to $`G_N`$, using established exact synthesis of determinant-one operations within charge sectors.

The [deterministic converse](deterministic_bound.md) uses a determinant identity satisfied by every allowed gate. The [randomized converse](randomized_optimum.md) turns the same identity into one common input test for every circuit. This common test is needed because a lower bound obtained from a different worst-case input for each circuit would not automatically survive averaging.

## Required number of borrowed qubits

For $`0<\epsilon\leq1`$, let $`m_x(\epsilon)`$ be the smallest nonnegative integer whose optimum error is at most $`\epsilon`$, with $`x\in\{\mathrm{det},\mathrm{rand}\}`$. Monotonicity of the sine on the relevant interval gives

```math
\begin{aligned}
m_{\mathrm{det}}(\epsilon)
&=\max\!\left\{0,
\left\lceil\frac{\pi}{4\arcsin\epsilon}-2\right\rceil
\right\},\\
m_{\mathrm{rand}}(\epsilon)
&=\max\!\left\{0,
\left\lceil\frac{\pi}{4\arcsin\sqrt\epsilon}-2\right\rceil
\right\}.
\end{aligned}
```

In particular,

```math
m_{\mathrm{det}}(\epsilon)
=\frac{\pi}{4\epsilon}+O(1),
\qquad
m_{\mathrm{rand}}(\epsilon)
=\frac{\pi}{4\sqrt\epsilon}+O(1)
\qquad(\epsilon\downarrow0).
```

No finite borrowed register achieves zero error, even with classical randomization. By contrast, one helper initialized in $`|0\rangle`$ permits exact CCZ and is returned to $`|0\rangle`$, by the established [initialized-ancilla synthesis result](../references/RELATED_WORK.md#bai2024). The circuits need only satisfy that specified-input condition; they are not required to act as the identity on an arbitrary state of the helper.

## Scope of the conclusion

The theorem fixes the data gate and optimizes borrowed qubit count as accuracy changes. It does not establish an efficient classical compiler, short gate sequence, low depth, or a resource law for every conserving target gate. The common qubit charge representation, exact conservation of each elementary gate, full input domain, and full return error are part of the result.

If the acted-on register is promised to occupy one fixed total-charge sector, the residual phase $`e^{i\theta_k}`$ is global and the constructed channel is exact on that sector. The full-channel obstruction nevertheless has a [globally charge-invariant reference-assisted witness](randomized_optimum.md): it does not require an asymmetric external phase-reference state. The [interpretation](interpretation.md) explains these two statements together.

Continue to the [determinant obstruction](deterministic_bound.md), the [attaining circuit](construction.md), and the [randomized optimum](randomized_optimum.md). [Examples](examples.md) show the finite costs and a direct zero-borrowed-qubit circuit.
