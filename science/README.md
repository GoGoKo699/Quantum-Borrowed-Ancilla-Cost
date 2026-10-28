# Scientific account

The question is whether arbitrary unknown workspace can replace an initialized helper for a conserving CCZ gate, and how the answer depends on accuracy. The complete result concerns one fixed target, conserving one- and two-qubit gates, and identity return of the borrowed information within the full channel error.

Read the pages in this order:

1. [Model and exact precision law](model.md): registers, native gates, complete return condition, error normalization, both optima, and the integer qubit costs.
2. [Determinant obstruction](deterministic_bound.md): the invariant of every allowed circuit and the deterministic lower bound.
3. [Attaining construction](construction.md): an allowed quadratic charge phase, exact sector corrections, and the finite cases completing all borrowed widths.
4. [Randomized optimum](randomized_optimum.md): one fixed probe against every mixture, an attaining two-circuit mixture, and the role of a retained classical record.
5. [Finite examples](examples.md): error and qubit-count tables, plus an explicit six-gate circuit with no borrowed qubits.
6. [Resource interpretation](interpretation.md): why initialization helps, why unknown memory has a precision cost, and what a fixed-charge input promise changes.

The [related-work account](../references/RELATED_WORK.md) identifies the inherited locality constraints, sector reachability, initialized-helper synthesis, and probabilistic-error reduction. The [verification record](../verification/README.md) distinguishes finite computations from the analytical proofs.
