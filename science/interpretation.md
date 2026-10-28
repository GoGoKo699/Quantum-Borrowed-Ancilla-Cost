# What initialization, borrowed memory, and randomness provide

The same conserving native gates behave differently depending on the auxiliary resource. A helper prepared in a known charge eigenstate provides a subspace on which the implementation has to be correct. Borrowed qubits provide more Hilbert-space dimension, but their unknown information must survive. Classical randomness provides a mixture of circuit channels. The [exact theorem](model.md) quantifies the distinction for CCZ.

## Why a prepared qubit helps

The initialized-ancilla condition is

```math
\widetilde W\bigl(|\psi\rangle_S\otimes|0\rangle_A\bigr)
=(\mathrm{CCZ}|\psi\rangle_S)\otimes|0\rangle_A
\quad\text{for every }|\psi\rangle_S.
```

Only the input subspace with ancillary state $`|0\rangle_A`$ is specified. The action on the orthogonal ancillary branch can compensate the sector-determinant phases required by locality. [Bai and Marvian's construction](../references/RELATED_WORK.md#bai2024) makes this compensation explicit. The helper returns unchanged on its specified input, so it can be reused.

For CCZ, a four-qubit example makes this freedom visible. Order the bits as the three data qubits followed by the helper, and define

```math
\widetilde W
=I-2|1110\rangle\langle1110|-2|1101\rangle\langle1101|.
```

Both flipped basis vectors have charge three, so every charge-sector determinant of $`\widetilde W`$ equals one. The imported [sectorwise reachability theorem](construction.md#1-exact-reachability-inside-the-charge-sectors) therefore places this unitary in $`G_4`$. On inputs with helper state $`|0\rangle`$, it gives exactly CCZ and restores the helper. On the other helper branch it flips $`|110\rangle_S`$ instead. That branch is available for compensation under initialization and is incompatible with the borrowed identity contract. This example illustrates the established initialized-ancilla mechanism.

A borrowed helper has no unused branch with this freedom. Its initial state may be $`|0\rangle`$, $`|1\rangle`$, a superposition, or part of an entangled state. The target $`\mathrm{CCZ}\otimes I_B`$ specifies the action on all those possibilities simultaneously. Increasing $`m`$ increases the available dimension but leaves the [determinant character](deterministic_bound.md) incompatible with the target for every finite $`m`$.

The prepared state is a charge eigenstate and has no coherence between different charges. The resource distinction here therefore does not require a symmetry-breaking phase reference. It concerns the specified input subspace made available by initialization, together with the stronger restoration promise imposed on borrowed information. The theorem does not assign a preparation-energy or entropy-production cost to that initialization.

## How more borrowed qubits reduce the error

The character constraint involves the four charge sectors $`0,1,N-1,N`$. Their dimensions are $`1,N,N,1`$. Its total absolute eigenphase weight is $`4(N-1)`$. A target character phase of $`\pi`$ must therefore leave a residual eigenphase half-width of at least

```math
a_m=\frac{\pi}{4(N-1)}.
```

The construction spreads this unavoidable phase mismatch across the relevant sectors. A quadratic function of total charge supplies an allowed correction, while determinant-one operations within each sector implement the remaining target action. The bulk sectors have larger dimensions, so their determinant corrections fit within the same phase interval. This produces a coherent error proportional to $`1/m`$ at large $`m`$.

Borrowed qubits are not being erased or assigned known states. Their original information remains within the jointly approximated operation. The increasing dimension allows a smaller distributed residual phase under the unchanged full-channel contract.

## Why a discarded classical coin changes the exponent

For the attaining circuit $`W=T e^{i\Theta}`$, CCZ satisfies $`T=T^\dagger`$ and $`T^2=I`$, and $`T`$ commutes with the sector phase $`\Theta`$. Consequently, $`W^\dagger=T e^{-i\Theta}`$ is another allowed implementation. Choosing between them with equal probability gives

```math
\frac12(\mathcal W+\mathcal W^{-1})
=\mathcal T\circ\Psi,
\qquad
\Psi(X)=\frac12\left(e^{i\Theta}Xe^{-i\Theta}
+e^{-i\Theta}Xe^{i\Theta}\right).
```

Opposite first-order phase errors cancel in the averaged channel. Such cancellation is an established principle of [probabilistic synthesis](../references/RELATED_WORK.md#campbell2017). Here the exact channel distance is $`\sin^2a_m`$. The additional optimality statement is that no distribution over any allowed circuits can improve it. A single weighted reference-assisted input proves that lower bound for every mixture.

The distinction is operational. If the random-choice label remains part of the scored output, its correlations reveal the two opposite coherent errors. The [recorded-coin proposition](randomized_optimum.md) gives optimum $`\sin a_m`$ in that case. The quadratic improvement concerns the averaged quantum channel, with the classical record outside the output being compared to the target.

## Charge conservation and the input domain

The residual phase $`\theta_k`$ is constant within each sector. For an input supported entirely on $`\mathcal H_k`$, conjugation by $`e^{i\theta_k}`$ has no effect. The same construction therefore implements the target exactly when the entire acted-on register is promised to remain in one fixed total-charge sector. It also agrees with the target on input states that are block diagonal in that register's charge, including their reference operators.

This does not make the full-channel lower bound unphysical under charge conservation. Let the marginal used in the converse be diagonal in the computational basis,

```math
\tau=\sum_x\lambda_x|x\rangle\langle x|.
```

Give the untouched reference $`N`$ qubits with the same charge convention and prepare

```math
|\Omega_\tau\rangle
=\sum_x\sqrt{\lambda_x}\,|x\rangle_{SB}|\overline x\rangle_R,
```

where $`\overline x`$ is the bitwise complement of $`x`$. Every term has the same joint charge $`N`$. The target output and its rank-one projector lie in this fixed joint-charge sector as well. The distinguishing experiment can therefore use globally invariant states and measurements. What must be preserved is the correlation between the acted-on register's charge and the untouched reference, rather than coherence relative to an asymmetric external clock.

Native-gate conservation and a fixed-charge promise on the acted-on register are different assumptions. The theorem applies to the first with the full reference-assisted input domain. Encoded computations confined to a known charge sector can use the second and are outside the claimed obstruction.

## Reachability, precision, and circuit cost

The exact width law permits arbitrarily long finite circuits and arbitrary real gate angles. The imported semi-universality theorem guarantees that the determinant-one part of the construction is attainable without another helper. It does not make that part short. No efficient compilation theorem, practical memory saving, or fault-tolerant gate-count advantage is inferred from the width optimum.

Similarly, the result assumes exact conservation at every elementary gate. Nonconserving controls, extra initialized helpers, resets, input measurements, alternative local charge representations, or a weaker borrowed-return requirement change the admissible operations or the task. Their costs cannot be inferred by applying the displayed formulas unchanged.

The physical statement that remains is precise: under the stated native gates, one prepared helper gives exact CCZ; arbitrary borrowed quantum memory has an unavoidable precision-dependent width; and a discarded classical coin reduces that optimal width from order $`\epsilon^{-1}`$ to order $`\epsilon^{-1/2}`$.
