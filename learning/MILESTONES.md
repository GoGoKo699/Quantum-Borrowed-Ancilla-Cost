# Thirty milestones for Quantum Borrowed Ancilla Cost

This map follows the scientific question from individual qubits to the exact cost of replacing initialized workspace by unknown borrowed qubits. It gives a common set of understanding targets, dependencies, conceptual connections, and source pointers.

There are **12 background/preliminaries milestones, M01–M12**, and **18 narrative/innovation milestones, M13–M30**. The background assembles the register, conservation law, return condition, and channel metric into the full task. The narrative develops the coherent optimum, the common-probe randomized converse, and the attaining mixture before integrating their physical meaning and limits.

The randomized converse receives its own sequence because a different worst input for each circuit does not automatically give one test for a mixture. The final milestones address the classical choice record and charge promises, which determine what the resource comparison means. Detailed synthesis algorithms and intermediate calculations remain in the canonical scientific account.

Use the [Watrous bridge](WATROUS_BRIDGE.md) for explanations and notation translation, and the [scientific overview](../science/README.md) for the direct proof route.

## Single educational anchor and source conventions

The sole educational anchor is **John Watrous, The Theory of Quantum Information, the 2018 author-hosted pre-publication manuscript**. Section numbering was checked against the author's contents and chapter PDFs:

- [Author's book page](https://cs.uwaterloo.ca/~watrous/TQI/).
- [Author's front matter and contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf).
- [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf): Sections 1.1.1–1.1.3 and Sections 1.2.1–1.2.2.
- [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf): Sections 2.1.1–2.1.3, Sections 2.2.1–2.2.3, and Sections 2.3.1–2.3.2.
- [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf): Section 3.1.1, Section 3.2.1, and Sections 3.3.1–3.3.3.
- [Chapter 4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.4.pdf): Sections 4.1.1 and 4.1.3.

Every anchor pointer below refers to these exact sections of that manuscript. They are targeted support, not a requirement to read entire chapters. Watrous supplies the operator, state, channel, discrimination, convexity, and Schur-channel framework. The charge-sector invariant, native conserving gate model, semi-universality theorem, initialized-helper mechanism, and sharp CCZ formulas require the project's own bridge and its explicitly cited research papers.

Two notation translations are essential: the book's completely bounded trace norm is the diamond norm used here, and the project's error includes a factor of one half. The book's fidelity convention is unsquared; the output acceptance probabilities in the project involve squared overlaps.

The project links below identify the canonical statements and proofs. Research-paper pointers remain primary scientific dependencies, not additional educational anchors.

## Phase I: background/preliminaries, M01–M12

<a id="m01"></a>

### M01. Registers, basis labels, and quantum information

- **Phase:** Background/preliminaries.
- **Central question:** What information-bearing object is represented by a qubit register and its computational basis?
- **Understanding target:** Relate a qubit's two basis states, a multi-qubit bit-string basis, complex amplitudes, and the dimension of the corresponding state space. Recognize the data register, borrowed register, and external reference as separately identified physical systems.
- **Dependencies and story role:** No earlier milestone. Establishes the local objects and labels from which the full register is built.
- **Conceptual connection:** Translates the book's standard basis vectors into the project's Dirac notation and gives meaning to the data-plus-workspace task.
- **Anchor sections:** Watrous Sections 1.1.1, 2.1.1–2.1.2.
- **Project source pointers:** [Model: Registers and native gates](../science/model.md#registers-and-native-gates); [Model: Target and return condition](../science/model.md#target-and-return-condition).

<a id="m02"></a>

### M02. Reversible gates and relative phase

- **Phase:** Background/preliminaries.
- **Central question:** How can a gate change quantum information while leaving every computational-basis population unchanged?
- **Understanding target:** Explain unitary action, adjoints and inverses, the distinction between global and relative phase, and the action of CCZ on the three-qubit basis. Distinguish a unitary matrix from its physically equivalent global-phase choices.
- **Dependencies and story role:** [M01](#m01). Introduces operations on the previously defined information-bearing objects.
- **Conceptual connection:** Makes a diagonal phase gate an operational target and prepares the later use of phase mismatch as a measurable error.
- **Anchor sections:** Watrous Sections 1.1.2, 2.2.3.
- **Project source pointers:** [Model: Target and return condition](../science/model.md#target-and-return-condition); [Examples: No borrowed qubits: six diagonal gates suffice](../science/examples.md#no-borrowed-qubits-six-diagonal-gates-suffice).

<a id="m03"></a>

### M03. Subsystems and charge sectors

- **Phase:** Background/preliminaries.
- **Central question:** How does a division into physical qubits differ from a division into total-charge sectors?
- **Understanding target:** Distinguish the tensor product of data and borrowed subsystems from the direct sum over excitation number. Explain $`n_j`$, $`Q`$, $`\Pi_k`$, and $`d_k=\binom Nk`$, including the sector dimensions $`1,N,N,1`$ at the four edges.
- **Dependencies and story role:** [M01](#m01)–[M02](#m02). Organizes the local qubits into the symmetry structure used throughout both proofs.
- **Conceptual connection:** Connects the book's tensor products, direct sums, and projectors to the project's physically conserved quantity.
- **Anchor sections:** Watrous Sections 1.1.1–1.1.2.
- **Project source pointers:** [Model: Registers and native gates](../science/model.md#registers-and-native-gates); [Determinant obstruction: 1. A determinant character on four charge sectors](../science/deterministic_bound.md#1-a-determinant-character-on-four-charge-sectors).

<a id="m04"></a>

### M04. Spectra, traces, determinants, and norms

- **Phase:** Background/preliminaries.
- **Central question:** Which features of an operator are recorded by its eigenvalues, trace, determinant, and trace norm?
- **Understanding target:** Distinguish sums of eigenvalues, products of eigenvalues, and sums of singular values. Explain how a scalar phase changes a block determinant according to its dimension, and how direct sums combine traces and trace norms.
- **Dependencies and story role:** [M02](#m02)–[M03](#m03). Supplies the operator tools before they are used to compare complete operations.
- **Conceptual connection:** Joins the phase description of a gate to the algebraic invariant and to the later distinguishability bounds.
- **Anchor sections:** Watrous Sections 1.1.2–1.1.3.
- **Project source pointers:** [Determinant obstruction: 1. A determinant character on four charge sectors](../science/deterministic_bound.md#1-a-determinant-character-on-four-charge-sectors); [Randomized optimum: 2. A determinant-constrained trace bound](../science/randomized_optimum.md#2-a-determinant-constrained-trace-bound); [Randomized optimum: 7. The optimum when the coin record is scored](../science/randomized_optimum.md#7-the-optimum-when-the-coin-record-is-scored).

<a id="m05"></a>

### M05. Unknown information and inaccessible references

- **Phase:** Background/preliminaries.
- **Central question:** Why does returning a subsystem's density operator fail to guarantee that its quantum information has been preserved?
- **Understanding target:** Explain density operators, reductions, purification, and correlations with other registers. Distinguish a promise about one specified helper state, equality of a final marginal, and identity action on an arbitrary borrowed input including its reference correlations.
- **Dependencies and story role:** [M01](#m01)–[M04](#m04). Extends the account from isolated register states to the joint information the task must preserve.
- **Conceptual connection:** Connects the book's purification framework to the strong borrowed-workspace return condition.
- **Anchor sections:** Watrous Sections 2.1.2–2.1.3.
- **Project source pointers:** [Model: Target and return condition](../science/model.md#target-and-return-condition); [Interpretation: Why a prepared qubit helps](../science/interpretation.md#why-a-prepared-qubit-helps).

<a id="m06"></a>

### M06. Native conservation at every gate

- **Phase:** Background/preliminaries.
- **Central question:** Why is a conserving target not automatically realizable by conserving one- and two-qubit gates?
- **Understanding target:** State the distinction between a target commuting with $`Q`$ and a finite sequence whose every primitive conserves charge on its support. Identify the allowed group $`G_N`$, its inverse operations, arbitrary gate angles, pair connectivity, and the absence of extra initialized or discarded quantum workspace.
- **Dependencies and story role:** [M02](#m02)–[M04](#m04). Adds the physical implementation restriction to the operator framework.
- **Conceptual connection:** Places operator composition inside a specified resource model; charge conservation and interaction locality are separate restrictions.
- **Anchor sections:** Watrous Sections 1.1.2, 2.2.1, 2.2.3, for operators and channel composition. The specific conserving circuit group is supplied locally.
- **Project source pointers:** [Model: Registers and native gates](../science/model.md#registers-and-native-gates); [Construction: 1. Exact reachability inside the charge sectors](../science/construction.md#1-exact-reachability-inside-the-charge-sectors).

<a id="m07"></a>

### M07. The operation as a quantum channel

- **Phase:** Background/preliminaries.
- **Central question:** What mathematical object describes correctness for every possible input rather than for a chosen state?
- **Understanding target:** Read $`\mathrm{Ad}_W`$ as a channel, understand composition and tensoring with an identity channel, and explain why global unitary phases disappear at channel level. State the target as an operation on the entire data-plus-borrowed register.
- **Dependencies and story role:** [M02](#m02), [M05](#m05)–[M06](#m06). Converts the local gate description into the global input-output object that will be optimized.
- **Conceptual connection:** Links reversible circuits to the book's general channel language without adding measurements or resets to the allowed implementation.
- **Anchor sections:** Watrous Sections 2.2.1–2.2.3.
- **Project source pointers:** [Model: Target and return condition](../science/model.md#target-and-return-condition); [Model: Deterministic and randomized optimization](../science/model.md#deterministic-and-randomized-optimization).

<a id="m08"></a>

### M08. Distinguishability as physical error

- **Phase:** Background/preliminaries.
- **Central question:** How does a difference between two output states become an observable error?
- **Understanding target:** Explain a binary measurement, half-trace distance, and a fixed projector as a discrimination test. Relate pure-state overlap to trace distance, while keeping the book's unsquared fidelity distinct from squared overlap probabilities.
- **Dependencies and story role:** [M04](#m04)–[M05](#m05), [M07](#m07). Gives operational meaning to the norms that will quantify gate accuracy.
- **Conceptual connection:** Connects linear-algebraic distances to a concrete distinguishing experiment and its success probabilities.
- **Anchor sections:** Watrous Sections 2.3.1–2.3.2, 3.1.1, 3.2.1.
- **Project source pointers:** [Determinant obstruction: 2. Diamond error controls the spectral arc](../science/deterministic_bound.md#2-diamond-error-controls-the-spectral-arc); [Randomized optimum: 4. Lower bound for arbitrary mixtures](../science/randomized_optimum.md#4-lower-bound-for-arbitrary-mixtures).

<a id="m09"></a>

### M09. Accuracy on the complete register

- **Phase:** Background/preliminaries.
- **Central question:** Why is the diamond distance the relevant accuracy requirement when unknown workspace may be entangled with a reference?
- **Understanding target:** Explain optimization over joint inputs and untouched references, the half-diamond normalization, and the distinction between data-only error and complete return error. Translate the book's completely bounded trace norm into the project's notation.
- **Dependencies and story role:** [M05](#m05), [M07](#m07)–[M08](#m08). Integrates states, channels, and discrimination into the task's full operational metric.
- **Conceptual connection:** Makes reference preservation part of implementation accuracy rather than a separate marginal-return check.
- **Anchor sections:** Watrous Sections 3.3.1–3.3.3.
- **Project source pointers:** [Model: Target and return condition](../science/model.md#target-and-return-condition); [Determinant obstruction: Model and statement](../science/deterministic_bound.md#model-and-statement).

<a id="m10"></a>

### M10. Classical mixtures and the choice record

- **Phase:** Background/preliminaries.
- **Central question:** What changes when a classical random variable chooses the circuit?
- **Understanding target:** Distinguish a convex mixture of unitary channels from an average of unitary matrices. Explain input-independent probabilities, a discarded choice record, and an output that retains that record. Recognize that an input optimized separately for each branch need not provide one common test for the mixture.
- **Dependencies and story role:** [M07](#m07)–[M09](#m09). Adds the second implementation model while preserving the same quantum input and return contract.
- **Conceptual connection:** Connects convex channel geometry to the quantifier issue that makes the randomized converse substantive.
- **Anchor sections:** Watrous Sections 1.2.1–1.2.2, 4.1.1; Section 2.1.1 for the classical label register.
- **Project source pointers:** [Model: Deterministic and randomized optimization](../science/model.md#deterministic-and-randomized-optimization); [Randomized optimum: 1. Model and inputs from the deterministic analysis](../science/randomized_optimum.md#1-model-and-inputs-from-the-deterministic-analysis); [Randomized optimum: 7. The optimum when the coin record is scored](../science/randomized_optimum.md#7-the-optimum-when-the-coin-record-is-scored).

<a id="m11"></a>

### M11. Reachability and a prepared input subspace

- **Phase:** Background/preliminaries.
- **Central question:** What does established sectorwise synthesis provide, and why can one initialized helper change the task?
- **Understanding target:** State the imported ability to realize independent determinant-one unitaries in every charge sector by finite conserving circuits on the existing register. Explain the initialized-helper promise using the four-qubit example and its unconstrained orthogonal input branch. Distinguish exact reachability from an efficient compiler.
- **Dependencies and story role:** [M03](#m03)–[M06](#m06), [M09](#m09). Adds the research-level background needed to judge an attaining construction and the prepared-resource comparison.
- **Conceptual connection:** Connects block-operator algebra to semi-universality and to the operational freedom supplied by a known input state.
- **Anchor sections:** Watrous Sections 1.1.2–1.1.3, 2.2.3, for the operator and channel framework. The reachability theorem is an explicitly imported research dependency.
- **Project source pointers:** [Construction: 1. Exact reachability inside the charge sectors](../science/construction.md#1-exact-reachability-inside-the-charge-sectors); [Interpretation: Why a prepared qubit helps](../science/interpretation.md#why-a-prepared-qubit-helps); [Related work: marvian2024](../references/RELATED_WORK.md#marvian2024); [Related work: bai2024](../references/RELATED_WORK.md#bai2024).

<a id="m12"></a>

### M12. The full optimization problem

- **Phase:** Background/preliminaries.
- **Central question:** Which resources, inputs, errors, and quantifiers define the borrowed-qubit cost question?
- **Understanding target:** Assemble $`N=m+3`$, the same-representation qubits, $`G_N`$, the fixed CCZ target, full reference-assisted return, and the deterministic and averaged randomized optima into one model. Explain why gate count, preparation cost, and a fixed-charge input promise are different optimization questions.
- **Dependencies and story role:** [M03](#m03), [M05](#m05)–[M11](#m11). Completes the background phase by integrating its objects and operational distinctions into the precise scientific task.
- **Conceptual connection:** Turns the textbook channel framework and the local physical constraints into the project's global resource question.
- **Anchor sections:** Watrous Sections 2.2.1, 3.3.3, 4.1.1.
- **Project source pointers:** [Model: Registers and native gates](../science/model.md#registers-and-native-gates); [Model: Target and return condition](../science/model.md#target-and-return-condition); [Model: Deterministic and randomized optimization](../science/model.md#deterministic-and-randomized-optimization); [Model: Scope of the conclusion](../science/model.md#scope-of-the-conclusion).

## Phase II: narrative/innovation, M13–M30

<a id="m13"></a>

### M13. A local gate viewed through the whole register

- **Phase:** Narrative/innovation.
- **Central question:** How does a two-qubit gate contribute to determinants in different total-charge sectors?
- **Understanding target:** Explain how the gate's local charge blocks are repeated according to the spectator register's charge multiplicities. Read the binomial determinant formula and its four-edge specialization as the result of embedding the same primitive in a larger register.
- **Dependencies and story role:** [M03](#m03)–[M04](#m04), [M06](#m06), [M12](#m12). Starts the narrative with the local action from which the circuit-wide obstruction will be assembled.
- **Conceptual connection:** Connects local tensor factors to global charge-sector algebra without introducing a prepared spectator state.
- **Anchor sections:** Watrous Sections 1.1.1–1.1.2.
- **Project source pointers:** [Determinant obstruction: Every allowed gate has character one](../science/deterministic_bound.md#every-allowed-gate-has-character-one).

<a id="m14"></a>

### M14. A phase identity preserved by every circuit

- **Phase:** Narrative/innovation.
- **Central question:** Which combination of sector determinants survives arbitrary composition of the allowed gates?
- **Understanding target:** Explain why $`\chi_N`$ is multiplicative, why the local determinant factors cancel, and why its global-phase weights balance. Understand that the invariant applies to every finite allowed circuit and is well-defined for its unitary channel.
- **Dependencies and story role:** [M04](#m04), [M13](#m13). Elevates the primitive calculation into a constraint on the entire reachable group.
- **Conceptual connection:** Converts local conservation and multiplicativity into an obstruction that arbitrary circuit length cannot remove.
- **Anchor sections:** Watrous Section 1.1.2, especially the trace and determinant framework.
- **Project source pointers:** [Determinant obstruction: 1. A determinant character on four charge sectors](../science/deterministic_bound.md#1-a-determinant-character-on-four-charge-sectors); [Determinant obstruction: Every allowed gate has character one](../science/deterministic_bound.md#every-allowed-gate-has-character-one).

<a id="m15"></a>

### M15. The target mismatch persists as workspace grows

- **Phase:** Narrative/innovation.
- **Central question:** Why does adding any finite number of unknown qubits leave exact CCZ outside the allowed group?
- **Understanding target:** Relate the number of sign-flipped target basis states in each charge sector to $`\det T_k`$, and explain why $`\chi_N(T)=-1`$ for every $`m`$. Distinguish this exact exclusion from the quantitative finite-error conclusion still to be proved.
- **Dependencies and story role:** [M03](#m03), [M14](#m14). Applies the circuit invariant to the fixed target and establishes the qualitative problem.
- **Conceptual connection:** Shows why additional unknown Hilbert-space dimension differs from the specified input subspace of an initialized helper.
- **Anchor sections:** Watrous Sections 1.1.2–1.1.3, for determinants and spectral descriptions.
- **Project source pointers:** [Determinant obstruction: The target has character minus one](../science/deterministic_bound.md#the-target-has-character-minus-one); [Interpretation: Why a prepared qubit helps](../science/interpretation.md#why-a-prepared-qubit-helps).

<a id="m16"></a>

### M16. Turning eigenphase spread into channel error

- **Phase:** Narrative/innovation.
- **Central question:** How does the spectrum of the target-relative unitary determine coherent implementation error?
- **Understanding target:** Explain the convex hull of eigenvalues, its distance from the origin, and the shortest containing arc when the channel error is below one. Relate the arc half-width $`\alpha`$ to $`\delta=\sin\alpha`$ and account for global phase freedom.
- **Dependencies and story role:** [M04](#m04), [M08](#m08)–[M09](#m09), [M15](#m15). Connects the algebraic obstruction to the project's operational metric.
- **Conceptual connection:** Joins convex geometry, purified-state overlap, and unitary-channel discrimination.
- **Anchor sections:** Watrous Sections 1.2.1, 3.2.1, 3.3.3.
- **Project source pointers:** [Determinant obstruction: 2. Diamond error controls the spectral arc](../science/deterministic_bound.md#2-diamond-error-controls-the-spectral-arc).

<a id="m17"></a>

### M17. The unavoidable phase budget

- **Phase:** Narrative/innovation.
- **Central question:** Why does the target's sign mismatch force an error of order the reciprocal of register size?
- **Understanding target:** Explain why the character angle is an odd multiple of $`\pi`$ and why the weighted sum of sector eigenangles is at most $`4(N-1)\alpha`$. Combine this budget with the spectral-arc relation to obtain the coherent lower bound, including its uniformity over all circuits.
- **Dependencies and story role:** [M14](#m14)–[M16](#m16). Completes the converse by turning the qualitative obstruction into a sharp candidate precision scale.
- **Conceptual connection:** Makes sector dimension the mechanism controlling how finely the forbidden determinant phase can be distributed.
- **Anchor sections:** Watrous Sections 1.1.2–1.1.3, 3.3.3, for the operator and metric ingredients; the phase budget is supplied by the project.
- **Project source pointers:** [Determinant obstruction: 3. The character requires a finite phase budget](../science/deterministic_bound.md#3-the-character-requires-a-finite-phase-budget); [Interpretation: How more borrowed qubits reduce the error](../science/interpretation.md#how-more-borrowed-qubits-reduce-the-error).

<a id="m18"></a>

### M18. A quadratic phase made from native gates

- **Phase:** Narrative/innovation.
- **Central question:** How can a function of total charge be implemented while every primitive still acts on at most two qubits?
- **Understanding target:** Explain the identity for $`Q^2`$ in terms of number operators and pair products, and why the chosen quadratic phase $`p(Q)`$ factors into commuting conserving gates. Relate its four edge values to the phase budget rather than treating it as an arbitrary formal correction.
- **Dependencies and story role:** [M03](#m03), [M06](#m06), [M11](#m11), [M17](#m17). Begins the matching upper bound with a manifestly allowed operation.
- **Conceptual connection:** Connects a collective charge polynomial to local physical interactions under the exact same native-gate model.
- **Anchor sections:** Watrous Sections 1.1.2–1.1.3, 2.2.3, for functions of operators and unitary action.
- **Project source pointers:** [Construction: 2. An allowed quadratic phase](../science/construction.md#2-an-allowed-quadratic-phase).

<a id="m19"></a>

### M19. Matching determinants without a hidden CCZ primitive

- **Phase:** Narrative/innovation.
- **Central question:** How can the target matrix help specify an allowed approximant without assuming the target gate is already available?
- **Understanding target:** Explain the wrapped sector phases, determinant equality with the quadratic phase, and the factorization into an allowed phase and sectorwise determinant-one unitary. Keep the wrapping interval $`[-\pi,\pi)`$, the existing-register synthesis, and the role of the imported reachability theorem explicit.
- **Dependencies and story role:** [M04](#m04), [M11](#m11), [M15](#m15), [M18](#m18). Converts the desired approximating matrix into a valid finite-circuit existence proof.
- **Conceptual connection:** Uses modulo-phase freedom to bridge the target's determinant pattern and the known reachable subgroup.
- **Anchor sections:** Watrous Sections 1.1.2–1.1.3. Watrous supports the operator manipulations; the symmetry-specific synthesis is a primary-paper dependency.
- **Project source pointers:** [Construction: 3. Correcting the target determinants](../science/construction.md#3-correcting-the-target-determinants); [Construction: 1. Exact reachability inside the charge sectors](../science/construction.md#1-exact-reachability-inside-the-charge-sectors); [Related work: marvian2024](../references/RELATED_WORK.md#marvian2024); [Related work: bai2024](../references/RELATED_WORK.md#bai2024).

<a id="m20"></a>

### M20. Attainment at every borrowed width

- **Phase:** Narrative/innovation.
- **Central question:** What makes the construction saturate the converse for every integer $`m\geq0`$?
- **Understanding target:** Explain the exact edge phases, the large-sector dimension bound for $`N\geq8`$, and the five rational small-register cases. Use the presence of both phase endpoints to conclude exact equality of the constructed error and the converse.
- **Dependencies and story role:** [M16](#m16)–[M17](#m17), [M19](#m19). Closes the coherent optimization globally, including the finite widths excluded by the bulk estimate alone.
- **Conceptual connection:** Joins an analytical uniform bound with a finite exact boundary check, while keeping reachability separate from gate efficiency.
- **Anchor sections:** Watrous Sections 1.1.3, 3.3.3.
- **Project source pointers:** [Construction: 4. Bounding every correction phase](../science/construction.md#4-bounding-every-correction-phase); [Construction: The five smaller registers](../science/construction.md#the-five-smaller-registers); [Construction: 5. Exact channel error](../science/construction.md#5-exact-channel-error).

<a id="m21"></a>

### M21. The complete argument in a three-qubit circuit

- **Phase:** Narrative/innovation.
- **Central question:** What does the optimum look like when no borrowed qubits are supplied?
- **Understanding target:** Connect the explicit six diagonal gates to the quadratic-charge construction and its even-versus-odd residual phase. Explain why its error is $`\sin(\pi/8)`$ and why the universal converse certifies its optimality.
- **Dependencies and story role:** [M02](#m02), [M06](#m06), [M18](#m18), [M20](#m20). Consolidates the full coherent mechanism in the smallest complete worked example before introducing the randomized proof.
- **Conceptual connection:** Links the abstract determinant argument to a directly specified conserving circuit without treating that small example as a general synthesis algorithm.
- **Anchor sections:** Watrous Sections 1.1.2, 2.2.3, 3.3.3.
- **Project source pointers:** [Examples: No borrowed qubits: six diagonal gates suffice](../science/examples.md#no-borrowed-qubits-six-diagonal-gates-suffice); [Determinant obstruction: 3. The character requires a finite phase budget](../science/deterministic_bound.md#3-the-character-requires-a-finite-phase-budget).

<a id="m22"></a>

### M22. A trace constraint suitable for averaging

- **Phase:** Narrative/innovation.
- **Central question:** What kind of consequence of the determinant obstruction can support one common test against every mixture?
- **Understanding target:** Explain why the coherent converse alone, with a potentially circuit-dependent worst input, is insufficient. Understand the determinant-minus-one trace bound for $`r\geq5`$ and how cosine concavity limits a unitary's real trace.
- **Dependencies and story role:** [M04](#m04), [M10](#m10), [M14](#m14)–[M17](#m17). Opens the randomized converse with an algebraic statement designed to control a common overlap.
- **Conceptual connection:** Connects the conserved determinant phase to a linear quantity that can later be evaluated on the same input for every circuit.
- **Anchor sections:** Watrous Sections 1.1.3, 1.2.1, for spectral decomposition and convexity; the determinant-constrained trace inequality is proved locally.
- **Project source pointers:** [Randomized optimum: 2. A determinant-constrained trace bound](../science/randomized_optimum.md#2-a-determinant-constrained-trace-bound); [Model: The exact theorem](../science/model.md#the-exact-theorem).

<a id="m23"></a>

### M23. One weighted input for the entire allowed group

- **Phase:** Narrative/innovation.
- **Central question:** How is the same density operator chosen to witness an error for every allowed circuit?
- **Understanding target:** Explain the four-sector weights and normalization of $`\tau`$, the algebraic auxiliary matrix of dimension $`r=4(N-1)`$, and the bound $`|\mathrm{Tr}(\tau T^\dagger W)|\leq\cos a`$ for every $`W`$. Distinguish proof-only direct sums and rephasing from physical resources available to the implementation.
- **Dependencies and story role:** [M03](#m03)–[M05](#m05), [M14](#m14), [M22](#m22). Converts the trace inequality into a circuit-independent physical input marginal.
- **Conceptual connection:** Turns the signed character weights into positive input probabilities while preserving the determinant constraint through adjointed blocks.
- **Anchor sections:** Watrous Sections 1.1.2–1.1.3, 2.1.2–2.1.3.
- **Project source pointers:** [Randomized optimum: 3. One fixed probe bounds every allowed circuit](../science/randomized_optimum.md#3-one-fixed-probe-bounds-every-allowed-circuit); [Examples: A symmetry-respecting distinguishing experiment](../science/examples.md#a-symmetry-respecting-distinguishing-experiment).

<a id="m24"></a>

### M24. A lower bound that survives every mixture

- **Phase:** Narrative/innovation.
- **Central question:** Why can arbitrary randomization, including far-away circuits, not beat the squared lower bound?
- **Understanding target:** Purify the same $`\tau`$ and use the same ideal-output projector for every circuit. Explain how linearity bounds its acceptance probability after averaging, and how this one test implies half-diamond error at least $`\sin^2a`$ for every allowed probability distribution.
- **Dependencies and story role:** [M08](#m08)–[M10](#m10), [M23](#m23). Completes the global randomized converse without interchanging circuit-dependent optimizations with an average.
- **Conceptual connection:** Links a fixed overlap constraint to a common operational witness and then to the channel norm.
- **Anchor sections:** Watrous Sections 2.3.1–2.3.2, 3.1.1, 3.2.1, 3.3.3.
- **Project source pointers:** [Randomized optimum: 4. Lower bound for arbitrary mixtures](../science/randomized_optimum.md#4-lower-bound-for-arbitrary-mixtures).

<a id="m25"></a>

### M25. Opposite coherent errors from an allowed inverse pair

- **Phase:** Narrative/innovation.
- **Central question:** Why does choosing between the attaining circuit and its inverse suppress the leading phase error?
- **Understanding target:** Use the involution property of CCZ, commutation with the sector correction, and closure of the gate set under inverses to obtain the two allowed branches. Explain cancellation in the averaged channel while retaining the same unknown inputs and borrowed-return requirement.
- **Dependencies and story role:** [M07](#m07), [M10](#m10), [M19](#m19)–[M20](#m20). Begins the randomized upper bound with an explicit admissible ensemble.
- **Conceptual connection:** Applies established coherent-error cancellation to the particular inverse pair supplied by the symmetry-constrained construction.
- **Anchor sections:** Watrous Sections 2.2.3, 4.1.1.
- **Project source pointers:** [Randomized optimum: 6. Achievability and the exact resource law](../science/randomized_optimum.md#6-achievability-and-the-exact-resource-law); [Interpretation: Why a discarded classical coin changes the exponent](../science/interpretation.md#why-a-discarded-classical-coin-changes-the-exponent); [Related work: campbell2017](../references/RELATED_WORK.md#campbell2017).

<a id="m26"></a>

### M26. Exact error of the two-branch channel

- **Phase:** Narrative/innovation.
- **Central question:** Why is the inverse pair's diamond error exactly $`\sin^2a`$, including arbitrary references?
- **Understanding target:** Recognize the phase-damping channel as a Schur multiplier and reduce a pure joint input to its error matrix. Explain the one-positive-eigenvalue structure, the nonnegative Rayleigh maximizer, and the bound from the phase interval. Understand why both endpoints give equality for $`0\leq a\leq\pi/2`$.
- **Dependencies and story role:** [M04](#m04), [M09](#m09), [M16](#m16), [M25](#m25). Replaces a small-error cancellation heuristic with an exact channel-norm calculation.
- **Conceptual connection:** Connects Schur-channel structure and spectral geometry to a reference-uniform bound. The matrix inequality and maximizing-vector argument are supplied locally.
- **Anchor sections:** Watrous Sections 1.1.3, 3.3.2–3.3.3, 4.1.3.
- **Project source pointers:** [Randomized optimum: 5. Exact diamond error of a symmetric two-branch mixture](../science/randomized_optimum.md#5-exact-diamond-error-of-a-symmetric-two-branch-mixture).

<a id="m27"></a>

### M27. The exact randomized law and finite width costs

- **Phase:** Narrative/innovation.
- **Central question:** What complete resource law follows when the randomized lower and upper bounds meet?
- **Understanding target:** Combine the two bounds to obtain the exact squared relation between randomized and deterministic errors for all $`m\geq0`$. Explain the inverse-error and inverse-square-root-error width laws, the integer threshold formulas, and the distinction between numerical examples and the universal theorem.
- **Dependencies and story role:** [M12](#m12), [M20](#m20), [M24](#m24)–[M26](#m26). Integrates the two proof branches into the operational width-versus-accuracy result.
- **Conceptual connection:** Converts a channel optimization into an exact statement about how much unknown quantum workspace is required.
- **Anchor sections:** Watrous Sections 3.3.3, 4.1.1, for the channel metric and mixture framework; the width optimization is the project result.
- **Project source pointers:** [Randomized optimum: 6. Achievability and the exact resource law](../science/randomized_optimum.md#6-achievability-and-the-exact-resource-law); [Model: Required number of borrowed qubits](../science/model.md#required-number-of-borrowed-qubits); [Examples: Borrowed qubits at fixed precision](../science/examples.md#borrowed-qubits-at-fixed-precision).

<a id="m28"></a>

### M28. The meaning of retaining the random-choice record

- **Phase:** Narrative/innovation.
- **Central question:** Why does scoring the classical record restore the coherent optimum?
- **Understanding target:** State the recorded target with the same input-independent coin distribution. Explain the additivity of trace norm across orthogonal classical labels and why the common probe gives a $`\sin a`$ lower bound for every finite or countable recorded ensemble. Relate discarding the label to the improved averaged-channel task.
- **Dependencies and story role:** [M05](#m05), [M08](#m08), [M10](#m10), [M23](#m23), [M27](#m27). Tests the operational boundary of the randomness advantage within the same scientific model.
- **Conceptual connection:** Connects classical information retained at the output to distinguishability of branchwise coherent errors.
- **Anchor sections:** Watrous Sections 1.1.3, 2.1.1, 3.3.3, 4.1.1.
- **Project source pointers:** [Randomized optimum: 7. The optimum when the coin record is scored](../science/randomized_optimum.md#7-the-optimum-when-the-coin-record-is-scored); [Interpretation: Why a discarded classical coin changes the exponent](../science/interpretation.md#why-a-discarded-classical-coin-changes-the-exponent).

<a id="m29"></a>

### M29. Charge-invariant certification and a restricted input promise

- **Phase:** Narrative/innovation.
- **Central question:** How can the lower bound have a globally charge-invariant witness while disappearing on a fixed-charge input sector?
- **Understanding target:** Explain the complementary-charge purification and invariant target-output measurement. Distinguish fixed total charge of register plus reference from fixed charge of the acted-on register alone. Explain why sectorwise scalar corrections vanish under the latter promise without weakening the full-channel theorem.
- **Dependencies and story role:** [M03](#m03), [M05](#m05), [M09](#m09), [M20](#m20), [M23](#m23)–[M24](#m24). Integrates the symmetry, reference, and input-domain assumptions into a physically interpretable boundary.
- **Conceptual connection:** Shows that the relevant resource is preservation of joint correlations across the acted-on register's sectors, without supplying an asymmetric external phase-reference state.
- **Anchor sections:** Watrous Sections 2.1.3, 2.3.1, 3.3.1.
- **Project source pointers:** [Randomized optimum: 8. A charge-invariant realization of the lower-bound probe](../science/randomized_optimum.md#8-a-charge-invariant-realization-of-the-lower-bound-probe); [Interpretation: Charge conservation and the input domain](../science/interpretation.md#charge-conservation-and-the-input-domain); [Examples: A symmetry-respecting distinguishing experiment](../science/examples.md#a-symmetry-respecting-distinguishing-experiment).

<a id="m30"></a>

### M30. The complete resource separation and its limits

- **Phase:** Narrative/innovation.
- **Central question:** What does the whole result establish about initialization, borrowed quantum memory, and classical randomness?
- **Understanding target:** Give one coherent account of the prepared-helper endpoint, both exact borrowed-width optima, the retained-record boundary, and the invariant reference witness. Identify the inherited research ingredients and the matching resource optimization established here. Preserve the finite-circuit, arbitrary-angle, same-charge, complete-return assumptions and distinguish analytical proof from finite verification and from gate-efficiency claims.
- **Dependencies and story role:** [M11](#m11)–[M12](#m12), [M17](#m17), [M20](#m20)–[M21](#m21), [M24](#m24), [M26](#m26)–[M29](#m29). Ends the phase by integrating the mechanism, theorem, physical meaning, attribution, and limitations.
- **Conceptual connection:** Connects the single-anchor channel framework to the full project contribution while explaining what changes when its operational assumptions change.
- **Anchor sections:** Watrous Sections 3.3.3, 4.1.1, 4.1.3 as the integrated channel-and-mixture framework. The exact symmetry-constrained resource theorem remains a project result.
- **Project source pointers:** [Model: The exact theorem](../science/model.md#the-exact-theorem); [Model: Scope of the conclusion](../science/model.md#scope-of-the-conclusion); [Interpretation: Reachability, precision, and circuit cost](../science/interpretation.md#reachability-precision-and-circuit-cost); [Related work: What the result adds](../references/RELATED_WORK.md#what-the-result-adds); [Verification](../verification/README.md).

