# Reproduce the finite checks

The universal optima are established in the [deterministic converse](../science/deterministic_bound.md), [attaining construction](../science/construction.md), and [randomized proof](../science/randomized_optimum.md). The program here checks finite algebraic identities and explicit matrices that those arguments use. It does not replace the analytical proofs or synthesize the general determinant-one circuit.

## Run

Use Python 3.11 or later. Install the pinned numerical dependency, then run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The program also runs from another working directory when given its absolute path. It exits with an assertion error if a check fails and prints a JSON report when all checks pass. To save a new report:

```bash
python verification/run_all.py --write-results verification/results.json
```

The committed [results.json](results.json) records an executed run using Python 3.12.14 and NumPy 2.3.5. The pseudorandom seed is fixed at 20261028. Floating residuals can vary slightly across numerical libraries; the assertions use explicit tolerances and do not require bitwise reproduction of those residuals.

## What is checked

| Check | Domain | Purpose |
|---|---|---|
| Exact sector phases and determinant congruences | Every $`N=3,\ldots,100`$, using rational arithmetic | Catch sign, modular-wrap, and normalization errors in the construction |
| Literal small-register phase rows | $`N=3,\ldots,7`$ | Verify the finite cases used with the analytical large-$`N`$ bound |
| Local-gate character exponents and global-phase balance | Every $`N=3,\ldots,100`$ | Check the combinatorial identities underlying the converse |
| Direct target-basis enumeration | $`N=3,\ldots,10`$ | Independently count negative CCZ eigenvalues in each charge sector |
| Six diagonal gates without borrowed qubits | All eight basis states | Verify the elementary circuit in the examples |
| Explicit products of conserving pair gates | 24 circuits on $`N=3,4,5,6`$, 24 gates each | Check the character and common-probe bound on full matrices |
| Randomized error matrices | 328 probability distributions across eight register sizes | Check the one-positive-eigenvalue property, norm upper bound, and endpoint saturation |
| Integer precision thresholds | Four stated tolerances | Verify both attainment and failure with one fewer borrowed qubit |

The executed run passed. The largest local-circuit character residual was approximately $`3.01\times10^{-15}`$; the largest numerical excess over the randomized upper bound was approximately $`2.43\times10^{-17}`$. The corresponding tolerances are $`10^{-10}`$ and $`10^{-12}`$.

For the randomized check, the residual phase is constant within each charge sector. The tested probabilities therefore range over sector weights, and the resulting matrix represents the output difference for a pure input with those weights. Finite sampling checks the calculation; the proof for every input and every reference is analytical.

## Evidential limits

The program does not establish novelty, efficient compilation, the imported semi-universality theorem, or a universal lower bound by enumeration. It does not introduce an extra initialized helper into the construction. The exact rational checks and the full-matrix checks serve different purposes: the former verify the prescribed attaining phases, while the latter evaluate unrelated allowed circuits directly.
