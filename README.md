# Quantum Borrowed Ancilla Cost

**How much unknown, reusable quantum workspace can replace one initialized helper qubit under excitation-conserving elementary gates?**

The target is a CCZ gate on three data qubits. Every elementary gate acts on at most two qubits and conserves their total excitation number. There are $`m`$ borrowed qubits in arbitrary unknown states. The target acts as the identity on those qubits, including their correlations with the data and any untouched reference.

The error is half the diamond distance on the complete data-plus-borrowed register. For every integer $`m\geq0`$, the exact optima are

```math
\boxed{\displaystyle
\delta_{\mathrm{det}}^*(m)
=\sin\!\left(\frac{\pi}{4(m+2)}\right),
\qquad
\delta_{\mathrm{rand}}^*(m)
=\sin^2\!\left(\frac{\pi}{4(m+2)}\right).}
```

Both are attained by finite circuits. The randomized optimum allows every input-independent classical mixture of permitted circuits, with the choice record discarded. An equal mixture of one attaining circuit and its inverse suffices.

| Auxiliary resource | Precision consequence |
|---|---|
| One initialized charge-eigenstate helper | Exact CCZ is possible by [established synthesis](references/RELATED_WORK.md#bai2024). |
| Arbitrary borrowed qubits, deterministic circuit | Required number grows as $`\Theta(\epsilon^{-1})`$. |
| Arbitrary borrowed qubits, averaged randomized channel | Required number grows as $`\Theta(\epsilon^{-1/2})`$. |
| Borrowed qubits with the classical choice record retained and scored | The optimum is the deterministic value. |

No finite borrowed register attains zero error. At positive error, the identity return of borrowed information is approximated jointly with the data operation. The result permits arbitrarily long circuits and does not assert efficient compilation.

## Why the bound holds

Excitation conservation decomposes the register into charge sectors. A specific combination of their determinants equals one for every allowed local circuit and minus one for CCZ tensored with the borrowed identity. Its phase constraint gives the coherent error lower bound.

An allowed quadratic function of total charge, together with established determinant-one synthesis within sectors, attains that bound. A fixed reference-assisted input witnesses the corresponding squared error for every random mixture. This common witness supplies the all-mixture converse; cancellation of coherent errors by randomization is itself [established prior work](references/RELATED_WORK.md#campbell2017).

## Read the science

Start with the [scientific overview](science/README.md) or go directly to the [model and exact theorem](science/model.md).

| Question | Authoritative page |
|---|---|
| What is borrowed, what is allowed, and how is error scored? | [Model and precision law](science/model.md) |
| Why must every coherent circuit have nonzero error? | [Determinant obstruction](science/deterministic_bound.md) |
| How is the optimal error attained? | [Matching construction](science/construction.md) |
| Why can no random mixture improve the squared law? | [Randomized optimum](science/randomized_optimum.md) |
| What happens when the coin record is retained? | [Recorded-coin proposition](science/randomized_optimum.md#7-the-optimum-when-the-coin-record-is-scored) |
| What are the actual qubit counts and simplest circuit? | [Finite examples](science/examples.md) |
| How do initialization, unknown memory, and charge promises differ? | [Resource interpretation](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| What do the computations verify? | [Verification](verification/README.md) |

For one-percent error, the optimal borrowed counts are 77 deterministically and six for an averaged randomized channel. These are width costs in the stated exact native-gate model, not total hardware costs.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) points to the relevant sections of the author's available manuscript, translates its notation, and connects channel discrimination to the conserving-gate problem. A complete three-qubit example shows how discarding a classical choice record changes the error.

The [30-milestone map](learning/MILESTONES.md) has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. It follows the argument from registers, charge sectors, and borrowed information through the determinant obstruction, attaining construction, common-probe converse, and exact randomized law. Each milestone gives an understanding target, earlier dependencies, conceptual connections, and scientific sources.

Start with the [learning route](learning/README.md), use the bridge alongside the map, or follow the direct scientific route above. The [LLM reading guide](llms.txt) maps questions to the authoritative pages.

## Reproduce the finite checks

With Python 3.11 or later, run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The checks use exact rational arithmetic for the sector phases, full matrices for finite conserving circuits, and numerical error matrices for the randomized construction. The [recorded outputs](verification/results.json) and [verification scope](verification/README.md) distinguish these finite checks from the analytical universal proofs.

## Scope

All qubits carry the same charge representation, every elementary gate conserves charge exactly, and no additional initialized quantum workspace, measurements, or resets are supplied. The averaged randomized result discards its independent classical choice record.

The full-channel input domain is essential. If the acted-on register is promised to occupy one fixed charge sector, the residual phase is global and the constructed channel is exact on that sector. The full-channel lower bound nevertheless has a [globally charge-invariant witness](science/randomized_optimum.md#8-a-charge-invariant-realization-of-the-lower-bound-probe), using an untouched reference with complementary charge.

The exact formulas concern CCZ and borrowed-qubit width. Efficient gate synthesis, control time, and a classification of other target gates are outside the stated result.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

See [LICENSE](LICENSE).
