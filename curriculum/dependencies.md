# Dependencies and proposed study sequence

Status: **the relationships and the sequence are the curriculum librarian's recommendations. Five links carry the director's approval (section 3); every other link is provisional.**
The sequence is a **teaching recommendation, not an inflexible algorithm** (director decision D-17). A detailed personal plan follows the diagnostic assessment (D-08).

## 1. The relationship model

Cambridge teaches several courses concurrently, and this repository supports similar flexibility. Each item lists the earlier items it **builds on** (`builds_on` in
[coverage.yaml](coverage.yaml)), and each link carries a **type**, a **provenance** and an **approval**, kept separate.

| Type | Meaning | Effect on teaching order |
|---|---|---|
| `required` | Mathematically necessary for the intended treatment | Strongly suggests an order |
| `assumed` | Prior knowledge the programme takes for granted; the diagnostic or earlier study can establish it | None within the programme: it is checked at the start, not taught first |
| `recommended` | Helpful preparation, not strictly necessary | A weak preference; topics can run concurrently or in either order |
| `connection` | Related material; the topics illuminate each other | **No ordering constraint** |

| Provenance (where the link comes from) | Meaning |
|---|---|
| `cambridge-stated` | Cambridge states this item-to-item link itself (none at present) |
| `cambridge-course-level` | Cambridge states a dependence or link between the two **courses** in the Schedules or Guide; which items it joins is the librarian's mapping |
| `inferred-from-cambridge` | Follows from Cambridge's wording (for example the same topic in two courses) but Cambridge states no dependence |
| `librarian-judgement` | The librarian's reading of the mathematics |

| Approval | Meaning |
|---|---|
| `provisional` | Not yet reviewed by the director |
| `director-approved` | Accepted by the director |

Provenance says where a link comes from; approval says whether the director has accepted it. They are independent: a `librarian-judgement` link can be approved, and a
`cambridge-course-level` link can still be provisional.

**A prerequisite never means "mastery must be recorded first".** Nothing in the repository requires a predecessor's mastery before a topic is begun or assessed, and a valid diagnostic
can establish competence before a topic is formally covered ([assessment-standard.md](../governance/assessment-standard.md)). The validator checks that links are well formed and that the
`required` links contain no ordering cycle; recommended and connection links may run both ways.

## 2. What the register contains

256 links across the 173 non-note items:

| | Required | Assumed | Recommended | Connection | All |
|---|---|---|---|---|---|
| Within a course | 149 | 0 | 41 | 2 | 192 |
| Across courses | 8 | 10 | 33 | 13 | 64 |
| All | 157 | 10 | 74 | 15 | 256 |

By provenance: 221 librarian judgement, 19 inferred from Cambridge, 16 Cambridge course-level, 0 Cambridge item-level. By approval: **5 director-approved, 251 provisional**.

Changes since the first remediation: the Mechanics links, and the links to revision-level school knowledge (complex numbers, vector algebra), are now `assumed` instead of `required`; Cambridge's
course-level statements are labelled as such and not as item-level statements; and approval is a separate field, not a provenance value.

## 3. Links the director has approved

| Link | Type | Provenance | Why |
|---|---|---|---|
| IA-VC-011 builds on IA-VM-012 | required | librarian judgement | Tensor transformation laws use orthogonal transformations, which are the orthogonal matrices of IA-VM-012 |
| IA-VC-011 and IA-VM-018 | connection | librarian judgement | Rotation matrices as a group is a conceptual connection, not a requirement |
| IA-VC-014 and IA-DR-014 | connection | inferred from Cambridge | The inertia tensor (Vector Calculus) and moments of inertia (Dynamics) are the same idea in two courses |
| IA-GP-012 and IA-VM-018 | connection | inferred from Cambridge | Orthogonal groups and rotation matrices as transformation groups |
| IA-DR-019 and IA-VM-018 | connection | inferred from Cambridge | The Guide describes the symmetry group of special relativity in the Vectors and Matrices course; the Lorentz link is retained |

All other links, including the 8 required cross-course links in section 4, are provisional.

## 4. The only required cross-course links

Of 64 cross-course links, 8 are `required` (all provisional):

| Item | Needs | Why |
|---|---|---|
| IA-AN-002, IA-AN-016 | IA-NS-015 | the least upper bound axiom underlies Bolzano-Weierstrass and the Riemann integral |
| IA-DE-018 | IA-VM-016 | coupled systems solved by diagonalisation |
| IA-GP-011 | IA-VM-009 | matrix groups need matrix algebra and determinants |
| IA-GP-012 | IA-VM-012 | orthogonal groups need orthogonal matrices |
| IA-VC-011 | IA-VM-006, IA-VM-012 | tensors use suffix notation and orthogonal transformations |
| IA-DR-007 | IA-VM-007 | angular momentum uses the vector product |

Ten further cross-course links are `assumed` school-level or Mechanics knowledge: complex numbers (IA-VM-001) for IA-AN-001, IA-AN-012, IA-DE-011 and IA-GP-003; vector algebra (IA-VM-003) for
IA-DR-005; and the Mechanics lectures for IA-DR-001, 002, 004, 006 and 011. The diagnostic assessment should establish these. Everything else across courses is a recommendation or a connection.

## 5. The relationships reviewed

- **Numbers and Sets and Groups:** two recommended links only (cosets from equivalence relations; the Fermat-Euler theorem from modular arithmetic). Groups can start before Numbers and Sets is finished.
- **Groups and Vectors and Matrices:** two-way. Matrix-group items require matrices (IA-GP-011, IA-GP-012) and assume complex numbers (IA-GP-003). The Vectors and Matrices item that names groups needs no group theory, so IA-VM-018 is a connection, and IA-GP-012 and IA-VM-018 are also connected (approved).
- **Differential Equations and Analysis I:** connection only; neither is required by the other. The Guide frames Analysis as the foundation for techniques already used informally.
- **Analysis I and Vector Calculus:** connection only; Vector Calculus is applied and imposes no analysis requirement.
- **Mechanics and Dynamics and Relativity:** `assumed`. Cambridge's Schedules say familiarity with Mechanics is assumed, so these are knowledge to establish, not lectures to complete first. The student may skip Mechanics if the diagnostic shows the material is secure.
- **Probability and Vectors and Matrices:** the Guide says Probability links with Vectors and Matrices "in particular" but does not say which topics. **No link has been added**, to avoid inventing one; this is an unresolved matter for the director.

## 6. Cambridge order, for reference

Michaelmas: Vectors and Matrices, Differential Equations, Groups, Numbers and Sets (and the optional Mechanics). Lent: Analysis I, Probability, Vector Calculus, Dynamics and Relativity.
Easter: Computational Projects introduction and optional Part IB previews. Cambridge runs four courses at once; it is a reference, not necessarily the best order for independent study.

## 7. Proposed sequence (a recommendation)

Work on **one or two threads at a time**. Phases overlap, and with so few hard constraints the order within and between phases can change freely. An item is started when the student and
tutor judge the preparation adequate, not when a predecessor has been recorded at some level.

| Phase | Items | Why here | Computational exploration | Harvard enrichment (optional; [enrichment.md](enrichment.md)) |
|---|---|---|---|---|
| **A. The language of proof** | Numbers and Sets: logic, sets, induction, number theory (IA-NS-001 to IA-NS-014). In parallel: Vectors and Matrices complex numbers and vectors (IA-VM-001 to IA-VM-008) | Proof construction is the stated priority; the Vectors and Matrices items it feeds are assumed or required elsewhere | Euclid's algorithm, modular exponentiation, a toy RSA | none needed |
| **B. Linear algebra and structure** | Vectors and Matrices (IA-VM-009 to IA-VM-018); Groups (IA-GP-001 to IA-GP-016); Groups can start in phase A | Matrix groups need matrices; the rest of Groups does not | permutation and symmetry-group computations | Axler (owned); Artin-style group material after Groups |
| **C. Calculus as modelling** | Differential Equations (IA-DE-001 to IA-DE-020) | Coupled systems need eigenvalues; keeps applied mathematics in view from the start | logistic map, phase portraits, numerical ODE | none |
| **D. Rigorous analysis** | Numbers and Sets reals and countability (IA-NS-015 to IA-NS-022), then Analysis I (IA-AN-001 to IA-AN-020) | The least upper bound axiom is a required input | convergence experiments (illustrations, never proofs) | Rudin; 55b lectures 19 and 20 |
| **E. Probability** | Probability (IA-PR-001 to IA-PR-027) | Counting (A), series and integrals (D), difference equations (C) help but are recommendations | Monte Carlo, random walks, branching processes, Box-Muller, CLT demonstrations | none |
| **F. Vector calculus** | Vector Calculus (IA-VC-001 to IA-VC-014) | Tensors need suffix notation and orthogonal transformations; no analysis requirement | numerical line and surface integrals; testing Stokes and divergence theorems | none |
| **G. Dynamics and relativity** | Mechanics if the diagnostic shows a gap (IA-MC-001 to IA-MC-010), then Dynamics and Relativity (IA-DR-001 to IA-DR-024) | Assumed Mechanics and vector algebra; recommended differential equations | orbit integration, the rocket equation, Lorentz boosts | none |

Every one of the 161 core-course items (159 examinable and 2 wholly starred, IA-AN-015 and IA-DR-010) appears in exactly one phase above, so applied mathematics is preserved in full. Computational Projects
(IA-CP-001, IA-CP-002) are Easter-term preparation for Part IB and sit outside the sequence. Starred items are lectured but not examinable and are tracked separately (D-05).

**Equally reasonable alternatives**, because the links allow them: a Cambridge-style concurrent start; Analysis I earlier, immediately after the real numbers block; Vector Calculus before Analysis I; Dynamics
and Relativity earlier if Mechanics is secure. The diagnostic assessment should decide.

## 8. Questions for the director

1. Review the provisional links, especially the 8 required cross-course links in section 4, and mark approved those you accept.
2. Whether to map the Guide's Probability and Vectors and Matrices link to specific items, and which.
3. Whether the sequence in section 7 or a Cambridge-style concurrent start suits the student better once the diagnostic is done.
4. Whether any Part IB previews (Groups, Rings and Modules in the Lent Term is the one the Guide mentions) belong in the plan; none are in this baseline.
