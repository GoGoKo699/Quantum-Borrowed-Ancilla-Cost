# Finite costs and a direct circuit

The [exact theorem](model.md#the-exact-theorem) applies at every nonnegative borrowed-qubit count. These examples use half the diamond distance on the complete data-plus-borrowed register. They illustrate a width optimum with unrestricted finite circuit length.

## Errors at fixed borrowed width

| Borrowed qubits $`m`$ | Deterministic optimum | Averaged randomized optimum |
|---:|---:|---:|
| 0 | 0.3826834324 | 0.1464466094 |
| 1 | 0.2588190451 | 0.0669872981 |
| 2 | 0.1950903220 | 0.0380602337 |
| 3 | 0.1564344650 | 0.0244717419 |
| 4 | 0.1305261922 | 0.0170370869 |
| 5 | 0.1119644761 | 0.0125360439 |
| 9 | 0.0713391832 | 0.0050892791 |

The second column is $`\sin[\pi/(4(m+2))]`$ and the third is its square. A single borrowed qubit therefore has a strictly positive optimum error. A single initialized helper, under its specified-input contract, gives exact implementation by [established synthesis](../references/RELATED_WORK.md#bai2024).

## Borrowed qubits at fixed precision

The integer formulas in the [model](model.md#required-number-of-borrowed-qubits) give:

| Error tolerance $`\epsilon`$ | Deterministic borrowed qubits | Averaged randomized borrowed qubits |
|---:|---:|---:|
| $`10^{-1}`$ | 6 | 1 |
| $`10^{-2}`$ | 77 | 6 |
| $`10^{-3}`$ | 784 | 23 |
| $`10^{-4}`$ | 7852 | 77 |

For example, six borrowed qubits attain randomized error approximately $`0.00960736`$. Five give approximately $`0.01253604`$, so six is the minimum at one-percent error. The deterministic minimum at that tolerance is 77. These numbers count borrowed qubits in the exact native-gate model. They do not estimate a hardware implementation's total cost.

## No borrowed qubits: six diagonal gates suffice

The case $`m=0`$ has a particularly direct realization. For three qubits define

```math
W_0=e^{i\pi/8}
\prod_{j=1}^{3}e^{-i\pi n_j/4}
\prod_{1\leq j<\ell\leq3}e^{i\pi n_jn_\ell/2}.
```

Apart from an irrelevant global phase, this uses three one-qubit phase gates and three two-qubit controlled-phase gates. All gates are diagonal and conserve excitation number; they commute, so their displayed order is immaterial.

On a bit string $`x=(x_1,x_2,x_3)`$, the phase of $`W_0`$ in units of $`\pi`$ is

```math
\frac18-\frac14\sum_jx_j
+\frac12\sum_{j<\ell}x_jx_\ell.
```

Using

```math
(-1)^{x_1+x_2+x_3}
=1-2\sum_jx_j+4\sum_{j<\ell}x_jx_\ell
-8x_1x_2x_3,
```

the circuit has the exact form

```math
W_0=T\exp\!\left[\frac{i\pi}{8}(-1)^Q\right].
```

Its residual phases are $`+\pi/8`$ on even charge and $`-\pi/8`$ on odd charge. A superposition between these classes witnesses coherent half-diamond error $`\sin(\pi/8)`$. The [universal lower bound](deterministic_bound.md) proves that no other allowed circuit improves it.

An equal classical choice between $`W_0`$ and $`W_0^\dagger`$ gives averaged error $`\sin^2(\pi/8)`$. The six-gate example is a finite illustration; no comparable efficient gate-count assertion is made for the general-$`m`$ construction.

## A symmetry-respecting distinguishing experiment

For $`N=m+3`$, the converse uses the diagonal marginal

```math
\tau=\frac{\Pi_1+\Pi_{N-1}+(N-2)(\Pi_0+\Pi_N)}{4(N-1)}.
```

It places comparable total probability near the four edges of the charge spectrum, rather than uniformly across all $`2^N`$ basis vectors. This is why the witness avoids the dimension loss in a generic maximally entangled trace test. A complementary-charge purification gives a fixed-total-charge experiment; its construction and the exact error test appear in the [randomized proof](randomized_optimum.md).

The [verification program](../verification/README.md) reproduces the numerical tables, checks the six-gate identity on all eight basis states, and verifies the exact rational sector phases used by the general construction.
