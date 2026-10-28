# Learning Quantum Borrowed Ancilla Cost

The project asks how much unknown quantum workspace can replace a helper supplied in a known state. Every elementary gate must conserve excitation number, and the implementation must preserve the borrowed information together with its correlations. The precision cost depends on whether the implementation uses one circuit or a classical mixture whose choice record is discarded.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the reading version used here. Section and statement numbers refer to the author's pre-publication manuscript in its standard layout.

## Reading route

Start with the [30-milestone map](MILESTONES.md) to see the question each part of the project answers. Read the [Watrous bridge](WATROUS_BRIDGE.md) alongside the relevant milestones. It translates notation, supplies the symmetry-specific connections, and develops a complete example with three qubits. Follow the source links to the canonical statements and proofs when a step needs more detail.

| Milestones | Place in the scientific story |
|---|---|
| [M01–M04](MILESTONES.md#m01) | Registers, gates, charge sectors, and the operator quantities used in the proofs. |
| [M05–M09](MILESTONES.md#m05) | Unknown information, native conservation, channels, and reference-assisted accuracy. |
| [M10–M12](MILESTONES.md#m10) | Classical randomization, imported reachability, and the complete optimization problem. |
| [M13–M17](MILESTONES.md#m13) | From one embedded local gate to the universal deterministic lower bound. |
| [M18–M21](MILESTONES.md#m18) | The native quadratic phase, determinant correction, attainment at every width, and a six-gate example. |
| [M22–M24](MILESTONES.md#m22) | A common weighted input and one measurement against every randomized implementation. |
| [M25–M27](MILESTONES.md#m25) | The inverse circuit pair, its exact channel error, and the borrowed-qubit costs. |
| [M28–M30](MILESTONES.md#m28) | The classical record, charge promises, and the complete resource comparison. |

The **12 background/preliminaries milestones** integrate the objects and assumptions into one operational problem. The **18 narrative/innovation milestones** then build the proof mechanisms into the exact result and its physical interpretation. Each phase progresses from its individual ingredients to a complete account.

## Source roles

Watrous supplies the language of states, purifications, channels, and discrimination. The bridge identifies the targeted sections needed here. The conserving gate group, the determinant constraint, and the borrowed-workspace optimization are developed in the project. The independent special-unitary control of charge sectors is an imported research theorem, with its exact scope and attribution in [Related work](../references/RELATED_WORK.md).

The [scientific overview](../science/README.md) gives specialists a direct route through the model, proofs, examples, and interpretation. The [verification guide](../verification/README.md) explains what the finite computations check. The full claim includes arbitrary reference correlations and permits unrestricted finite circuit length; it does not establish an efficient general compiler.
