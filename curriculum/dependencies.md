# Dependencies and proposed study sequence

Status: **the relationships and the sequence are the curriculum librarian's recommendations for the director; none carries director approval yet.**
The sequence is a **teaching recommendation, not an inflexible algorithm** (director decision D-17). A detailed personal plan follows the
diagnostic assessment (D-08).

## 1. The relationship model

Cambridge teaches several courses concurrently, and this repository supports similar flexibility. Each item lists the earlier items it
**builds on** (`builds_on` in [coverage.yaml](coverage.yaml)), and each link has a **type** and, separately, a **provenance**.

| Type | Meaning | Effect on teaching order |
|---|---|---|
| `required` | Mathematically necessary for the intended treatment | Strongly suggests an order; the need can be met by prior study, not only by this repository's items |
| `recommended` | Helpful preparation, not strictly necessary | A weak preference; the topics can run concurrently or in either order |
| `connection` | Related material; the topics illuminate each other | **No ordering constraint** |

| Provenance | Meaning |
|---|---|
| `cambridge-stated` | Cambridge says the link in the Schedules or the Guide |
| `inferred-from-cambridge` | Follows from Cambridge's wording (for example the same topic listed in two courses) but is not declared as a prerequisite |
| `librarian-judgement` | The librarian's reading of the mathematics |
| `director-approved` | Confirmed by the curriculum director (**none yet**) |

**A prerequisite never means "mastery must be recorded first".** Nothing in the repository requires a predecessor's mastery before a topic is
begun or assessed. The validator checks only that links are well formed, type and provenance are valid, and that the `required` and `recommended`
links contain no ordering cycle.

## 2. What the register contains

252 links across the 173 non-note items:

| | Required | Recommended | Connection | All |
|---|---|---|---|---|
| Within a course | 149 | 42 | 0 | 191 |
| Across courses | 18 | 33 | 10 | 61 |
| All | 167 | 75 | 10 | 252 |

By provenance: 219 librarian judgement, 27 inferred from Cambridge, **6 stated by Cambridge**, 0 director-approved. The v1 baseline recorded every
link as a flat prerequisite (247 links, 9 items marked Cambridge-stated); the typed model replaces that. Two links were corrected in the process: the
Probability link for Jacobians pointed at line integrals (now surface and volume integrals, IA-VC-003), and the Dynamics link for "vector methods"
pointed at suffix notation (now vector algebra, IA-VM-003).

## 3. The five relationships reviewed

### 3.1 Numbers and Sets and Groups

Two links, both **recommended**: cosets from equivalence relations (IA-GP-004 from IA-NS-006, judgement) and the Fermat-Euler theorem from modular arithmetic
(IA-GP-006 from IA-NS-012, inferred from Cambridge: the Groups schedule re-derives Fermat-Euler "from the group-theoretic point of view", which presupposes the
arithmetic version). **No required link.** Cosets can be introduced as equivalence classes inside Groups, and the two courses run in parallel at Cambridge. Groups
can be started before Numbers and Sets is finished. In v1 these were undifferentiated prerequisites.

### 3.2 Groups and Vectors and Matrices

The dependence is genuinely two-way and is now stated that way. **Required** (matrices underlie matrix groups): IA-GP-003 from IA-VM-001 (the Mobius group
acts on the complex plane), IA-GP-011 from IA-VM-009 (matrix algebra and determinants) and IA-GP-012 from IA-VM-012 (orthogonal matrices), the last two inferred from the
schedules; **recommended**: IA-GP-013 from IA-VM-015 (change of basis as conjugation). In the other direction the last Vectors and Matrices item names rotations and Lorentz
transformations "as groups", but it needs no group theory: that link (IA-VM-018 from IA-GP-001) is now a **connection**, where v1 had made it a prerequisite. So the early Groups
items (axioms, permutations, Lagrange, actions, quotient groups) are independent of Vectors and Matrices, and only the matrix-group items need it.

### 3.3 Differential Equations and Analysis I

**Connection only** (IA-AN-007, IA-AN-011 and IA-AN-016 are connected to IA-DE-001, inferred from the Guide). Differential Equations uses calculus informally;
Analysis I rebuilds it rigorously, and the Guide describes Analysis as the firm foundation for techniques already used. Neither is required by the other, so they can be
taken in either order or together. The informal-first order is a pedagogical preference, not a constraint.

### 3.4 Analysis I and Vector Calculus

**Connection only** (IA-VC-001 to IA-VC-003 connected to IA-AN-007 and IA-AN-016). The Guide calls Vector Calculus an applied course in which techniques are used without rigorous
proof, "that will come in future analysis courses". Nothing in Vector Calculus requires Analysis I, and nothing in Analysis I requires Vector Calculus. Vector Calculus can precede,
follow or accompany Analysis I.

### 3.5 Mechanics and Dynamics and Relativity

Six links from the non-examinable Mechanics lectures: **five required** and one recommended (IA-DR-007 from IA-MC-004), all **inferred from Cambridge**. The Schedules say familiarity
with the Mechanics topics "is assumed" for Dynamics and Relativity, which is stated at course level; which Mechanics lecture supports which Dynamics item is the librarian's mapping, hence
`inferred-from-cambridge` and not `cambridge-stated`. "Required" here means **assumed knowledge**: it can be satisfied by prior study (A-level mechanics) and should be established by the
diagnostic assessment, not by working through the ten lectures. The student may skip Mechanics if the diagnostic shows the material is secure.

## 4. The only hard cross-course constraints

Of 61 cross-course links, just 18 are `required`. They are the only places where one course really leans on another:

| Item | Needs | Why |
|---|---|---|
| IA-AN-001, IA-AN-012 | IA-VM-001 | sequences, series and differentiation over the complex numbers |
| IA-AN-002, IA-AN-016 | IA-NS-015 | the least upper bound axiom underlies Bolzano-Weierstrass and the Riemann integral |
| IA-DE-011 | IA-VM-001 | complex roots of the auxiliary equation |
| IA-DE-018 | IA-VM-016 | coupled systems solved by diagonalisation |
| IA-GP-003, IA-GP-011, IA-GP-012 | IA-VM-001, IA-VM-009, IA-VM-012 | complex maps, matrix groups, orthogonal matrices |
| IA-VC-011 | IA-VM-006, IA-VM-018 | tensors use suffix notation and rotation matrices |
| IA-DR-005, IA-DR-007 | IA-VM-003, IA-VM-007 | vector algebra and the vector product |
| IA-DR-001, 002, 004, 006, 011 | IA-MC-002, 005, 003, 007, 008 | assumed Mechanics knowledge (section 3.5) |

Everything else across courses is a recommendation or a connection.

## 5. Cambridge order, for reference

Michaelmas: Vectors and Matrices, Differential Equations, Groups, Numbers and Sets (and the optional Mechanics). Lent: Analysis I, Probability, Vector Calculus, Dynamics and Relativity.
Easter: Computational Projects introduction and optional Part IB previews. Cambridge runs four courses at once; it is a reference, not necessarily the best order for independent study.

## 6. Proposed sequence (a recommendation)

Work on **one or two threads at a time**. Phases overlap, and with so few hard constraints the order within and between phases can change freely. An item is started when the student
and tutor judge the preparation adequate, not when a predecessor has been recorded at some level.

| Phase | Items | Why here | Computational exploration | Harvard enrichment (optional; [enrichment.md](enrichment.md)) |
|---|---|---|---|---|
| **A. The language of proof** | Numbers and Sets: logic, sets, induction, number theory (IA-NS-001 to IA-NS-014). In parallel: Vectors and Matrices complex numbers and vectors (IA-VM-001 to IA-VM-008) | Proof construction is the stated priority; the Vectors and Matrices items it feeds are the hard cross-course constraints | Euclid's algorithm, modular exponentiation, a toy RSA | none needed |
| **B. Linear algebra and structure** | Vectors and Matrices (IA-VM-009 to IA-VM-018); Groups (IA-GP-001 to IA-GP-016); Groups can start in phase A | Matrix groups need matrices; the rest of Groups does not | permutation and symmetry-group computations | Axler (owned); Artin-style group material after Groups |
| **C. Calculus as modelling** | Differential Equations (IA-DE-001 to IA-DE-020) | Coupled systems need eigenvalues; keeps applied mathematics in view from the start | logistic map, phase portraits, numerical ODE | none |
| **D. Rigorous analysis** | Numbers and Sets reals and countability (IA-NS-015 to IA-NS-022), then Analysis I (IA-AN-001 to IA-AN-020) | The least upper bound axiom is a required input | convergence experiments (illustrations, never proofs) | Rudin; 55b lectures 19 and 20 |
| **E. Probability** | Probability (IA-PR-001 to IA-PR-027) | Counting (A), series and integrals (D), difference equations (C) help but are recommendations | Monte Carlo, random walks, branching processes, Box-Muller, CLT demonstrations | none |
| **F. Vector calculus** | Vector Calculus (IA-VC-001 to IA-VC-014) | Tensors need suffix notation and rotation matrices; no analysis requirement | numerical line and surface integrals; testing Stokes and divergence theorems | none |
| **G. Dynamics and relativity** | Mechanics if the diagnostic shows a gap (IA-MC-001 to IA-MC-010), then Dynamics and Relativity (IA-DR-001 to IA-DR-024) | Assumed Mechanics, vector algebra, and recommended differential equations | orbit integration, the rocket equation, Lorentz boosts | none |

Every one of the 161 examinable-course items appears in exactly one phase above, so applied mathematics is preserved in full. Computational Projects (IA-CP-001, IA-CP-002) are Easter-term preparation for Part IB and
sit outside the sequence. Starred items (IA-AN-015, IA-DR-010) are lectured but not examinable and are tracked separately (D-05).

**Equally reasonable alternatives**, because the links allow them: a Cambridge-style concurrent start (Vectors and Matrices, Numbers and Sets, Groups and Differential Equations together); Analysis I earlier,
immediately after the real numbers block; Vector Calculus before Analysis I; Dynamics and Relativity earlier if Mechanics is secure. The diagnostic assessment should decide.

## 7. Questions for the director

1. Review and, where you agree, mark the `librarian-judgement` and `inferred-from-cambridge` links `director-approved`, especially the 18 required cross-course links in section 4.
2. Whether the sequence in section 6 or a Cambridge-style concurrent start suits the student better once the diagnostic is done.
3. Whether any Part IB previews (Groups, Rings and Modules in the Lent Term is the one the Guide mentions) belong in the plan; none are in this baseline.
