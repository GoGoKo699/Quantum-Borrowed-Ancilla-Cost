# Related work and contribution

## The task being compared

The [model and exact theorem](../science/model.md#the-exact-theorem) concern three system qubits and $`m\geq 0`$ borrowed qubits, with $`N=m+3`$. Write $`B`$ for the $`m`$-qubit borrowed register. Every elementary gate acts on at most two qubits and commutes with their total excitation number. Circuit length is unrestricted. The target on the complete register is

```math
T=\mathrm{CCZ}\otimes I_B.
```

Error is one half of the diamond norm distance from the target channel. Thus correctness includes arbitrary borrowed inputs and their correlations with an inaccessible reference. At nonzero error, the borrowed register is returned approximately in this joint metric. There is no promise that it starts in a known state, and no additional prepared ancilla is available.

Writing $`a_m=\pi/[4(m+2)]`$, the optimal errors are

```math
\delta_{\mathrm{det}}^*(m)=\sin a_m,
\qquad
\delta_{\mathrm{rand}}^*(m)=\sin^2 a_m.
```

The second optimization permits arbitrary classical mixtures of admissible circuits and discards the branch record. These are exact width versus precision laws for every integer $`m\geq0`$. They do not optimize gate count, depth, control time, or compilation time.

## What the result adds

Symmetry and locality already impose determinant constraints, and a single prepared qubit already removes the relevant obstruction. The present question is the precision cost of replacing that prepared resource with an arbitrary borrowed register whose full quantum information must be preserved. The [deterministic proof](../science/deterministic_bound.md) extracts a sharp metric obstruction from four charge sectors. The [construction](../science/construction.md) saturates it by choosing sector phases within the established reachable group. The [randomized proof](../science/randomized_optimum.md) gives both an attaining mixture and a single reference-assisted probe that bounds every admissible circuit, hence every mixture. The resulting quadratic improvement is an exact optimum for this task.

The distinction from the cited work is therefore the resource-constrained, fixed-target optimization over all circuits and their convex mixtures. Determinant normalization, independent special-unitary control within charge sectors, prepared-ancilla catalysis, and cancellation of coherent errors by mixing are imported ingredients. Neither a new universality principle nor a new general principle of randomized synthesis is claimed. The full input domain is essential: the theorem does not obstruct a computation promised to remain in one fixed total-charge sector of the acted-on register. The [interpretation](../science/interpretation.md) explains that scope and the realization of the lower-bound witness with a globally charge-invariant reference.

The numbered source statements below refer to the specified versions. Journal publication details and BibTeX keys are collected in [references.bib](references.bib).

## marvian2022

**Iman Marvian, “Restrictions on realizable unitary operations imposed by symmetry and locality.”** *Nature Physics* **18**, 283–289 (2022). [DOI: 10.1038/s41567-021-01464-0](https://doi.org/10.1038/s41567-021-01464-0). Numbering: [arXiv:2003.05524v3](https://arxiv.org/html/2003.05524v3), 14 August 2024.

This paper establishes the locality obstruction for symmetric circuits. Supplementary Note D develops the charge-sector determinant constraints. In particular, Eq. (130) already removes each block determinant by a scalar phase, and the text following Eq. (131) identifies the resulting determinant-one unitary as reachable. The phase lifts are defined modulo $`2\pi`$, exactly the freedom used in the present construction. This normalization is prior work; the contribution here is its optimization in the borrowed-register channel metric, together with a matching lower bound. Figure 3 and Supplementary Note E also explain how an invariant reference experiment can access relative charge-sector phases.

## marvian2024

**Iman Marvian, “Theory of Quantum Circuits with Abelian Symmetries.”** *Physical Review Research* **6**, 043292 (2024). [DOI: 10.1103/PhysRevResearch.6.043292](https://doi.org/10.1103/PhysRevResearch.6.043292). Numbering: [arXiv:2302.12466v3](https://arxiv.org/html/2302.12466v3), 23 December 2024.

Theorem 3, Eqs. (10)–(11), gives independent special-unitary transformations on the irreducible invariant subspaces. For identical qubits with excitation-number symmetry and unrestricted pairwise gates, these are the total-charge sectors. This supplies the reachability input for the attaining construction.

Section VI, Lemma 7, implements any diagonal target using one ancilla in a fixed state of definite charge and returns that state exactly. CCZ is such a target. Its promise concerns inputs $`\lvert\psi\rangle\otimes\lvert0\rangle`$; it does not require the same action for arbitrary ancilla inputs. The prepared endpoint used in the comparison is therefore established, while the borrowed-register optimization has a stronger input requirement.

## bai2024

**Ge Bai and Iman Marvian, “Synthesis of energy-conserving quantum circuits with XY interaction.”** *Quantum Science and Technology* **9**, 045049 (2024). [DOI: 10.1088/2058-9565/ad53fa](https://doi.org/10.1088/2058-9565/ad53fa). Numbering: [arXiv:2309.11051v3](https://arxiv.org/pdf/2309.11051v3), 23 September 2024.

This work explicitly identifies CCZ among the energy-conserving gates whose synthesis requires ancillary resources. Proposition 13 constructs any unitary with determinant one in each excitation sector using $`O(4^n n^{3/2})`$ elementary gates without ancillas. Section V, Eqs. (79)–(80), implements a basis-state phase with an ancilla prepared in $`\lvert0\rangle`$, which remains available for reuse; the construction extends to general energy-conserving targets.

These results substantiate exact finite-circuit reachability and the prepared-ancilla comparison. Their synthesis guarantees concern different resources from the present minimum borrowed width at a specified joint channel error. The width optimum does not assert a polynomial-size implementation of its attaining unitary.

## campbell2017

**Earl Campbell, “Shorter gate sequences for quantum computing by mixing unitaries.”** *Physical Review A* **95**, 042306 (2017). [DOI: 10.1103/PhysRevA.95.042306](https://doi.org/10.1103/PhysRevA.95.042306). Numbering: [arXiv:1612.02689v3](https://arxiv.org/pdf/1612.02689v3), 5 April 2017.

Section III, Lemma 1, bounds the diamond norm error of a unitary mixture by a quadratic term in the individual operator errors plus a term measuring the error of their average. It supplies the established mechanism by which mixing cancels leading coherent errors. The two-branch construction here uses that mechanism. Its additional content is the exact error at every borrowed width and an optimality proof against all admissible mixtures, rather than the existence of quadratic cancellation alone.

## hastings2017

**Matthew B. Hastings, “Turning gate synthesis errors into incoherent errors.”** *Quantum Information and Computation* **17**(5–6), 488–494 (2017). [DOI: 10.26421/QIC17.5-6-7](https://doi.org/10.26421/QIC17.5-6-7). Numbering: [published article](https://www.rintonpress.com/xxqic17/qic-17-56/0488-0494.pdf); [arXiv:1612.01011v1](https://arxiv.org/abs/1612.01011v1), 3 December 2016.

Section 2, Lemma 1 and Eq. (3), independently bound the error of a mixture using its mean unitary approximation and a second-order fluctuation term. Lemma 2 controls accumulated error under independent random choices. This is another direct antecedent of the cancellation used in the randomized upper bound. It does not provide the charge-constrained borrowed-width optimum or the common probe that proves its converse.

## akibue2024

**Seiseki Akibue, Go Kato, and Seiichiro Tani, “Probabilistic Unitary Synthesis with Optimal Accuracy.”** *ACM Transactions on Quantum Computing* **5**(3), Article 17 (2024). [DOI: 10.1145/3663576](https://doi.org/10.1145/3663576). Numbering: [arXiv:2301.06307v2](https://arxiv.org/html/2301.06307v2), 2 May 2024.

For a finite candidate family on dimension $`d`$, Theorem 4.3 distinguishes the best deterministic error $`\epsilon_U`$ at a fixed target from the covering error $`\epsilon_{\mathrm{cov}}`$ maximized over all unitary targets. Its bounds are

```math
\frac{4\eta_U}{d}\left(1-\frac{\eta_U}{d}\right)
\leq \epsilon_U^{\mathrm{mix}}
\leq \epsilon_{\mathrm{cov}}^2,
\qquad
\eta_U=1-\sqrt{1-\epsilon_U^2}.
```

The upper bound is not a pointwise statement $`\epsilon_U^{\mathrm{mix}}\leq\epsilon_U^2`$. The lower bound behaves as $`2\epsilon_U^2/d`$, as also stated in Appendix D, Eq. (101). Here the physical dimension is $`d=2^{m+3}`$, so that dependence would not establish the dimension-independent optimum $`\sin^2 a_m`$. The present weighted probe proves the stronger task-specific converse. The general use of convex optimization and channel-discrimination witnesses remains prior methodology.
