# Dependencies and proposed study sequence

Status: **proposal for the curriculum director.** A rigid timetable is deliberately not imposed. A
personal plan follows the diagnostic assessment that ChatGPT runs.

## 1. How dependencies are recorded

Item-level prerequisites are in [coverage.yaml](coverage.yaml) (`prerequisites`) and are shown as `needs:` in
[syllabus.md](syllabus.md). Each item with prerequisites carries a `prereq_basis`:

- **cambridge-stated** - Cambridge explicitly links the two in a document cited. Only 9 items carry this
  basis: Probability (IA-PR-001, IA-PR-002, IA-PR-014, IA-PR-017, IA-PR-019: the combinatorics, difference
  equation and calculus links the Guide names) and Dynamics and Relativity (IA-DR-001, IA-DR-002, IA-DR-004,
  IA-DR-005: the Mechanics assumption and the Differential Equations link).
- **librarian-judgement** - Claude Code's reading of the mathematics (144 items). This includes
  dependencies that the Schedules' wording *indicates* by listing the same topic in two courses, which is
  evidence of overlap but not a declared prerequisite. These are proposals; the director should confirm or
  amend them.

The register has 153 items with at least one prerequisite and no cycles (checked by `scripts/validate.py`).
This page summarises the structure at course level.

## 2. Course-level dependencies

"Stated" means Cambridge says the link explicitly in the document cited (Schedules 2026-27 or Guide 2026-27);
"indicated" means the Schedules' text lists the same topic in both courses, so the overlap is Cambridge's but the
direction is not declared; "judged" means Claude Code's judgement.

| From | To | Why | Basis |
|---|---|---|---|
| Numbers and Sets | Analysis I | Guide: Numbers and Sets moves to "rational, real and complex numbers where we lay the logical foundations for analysis"; least upper bounds and sequences are taught there first. | stated (Guide) |
| Numbers and Sets | every pure course | Guide: its skills "will form the basis for the later courses, particularly those devoted to Pure Mathematics". | stated (Guide) |
| Numbers and Sets | Groups | Equivalence relations (cosets) and modular arithmetic (the Groups schedule lists "Fermat-Euler theorem from the group-theoretic point of view"). | indicated (Schedules) for Fermat-Euler; judged for equivalence relations |
| Numbers and Sets | Probability | Guide: "the elementary combinatorics of Numbers and Sets". | stated (Guide) |
| Vectors and Matrices | Groups | Matrix groups (GL, SL, O, SO) and "Basis change as an example of conjugation". The dependency also runs the other way: V&M's last block treats rotation matrices and Lorentz transformations "as transformation groups". | indicated (Schedules, both ways); direction judged |
| Vectors and Matrices | Differential Equations | "Coupled first order systems ... solution by matrix methods"; Hessian classification. | indicated (Schedules) |
| Vectors and Matrices | Vector Calculus | Suffix notation, tensors, and "Revision of principal axes and diagonalization". | indicated (Schedules) |
| Vectors and Matrices | Dynamics and Relativity | Vector methods; Lorentz transformations. Guide: the approach "relies heavily on vector methods". | stated (Guide) |
| Differential Equations | Analysis I | Guide: Analysis puts "a firm foundation for techniques you already know, such as basic differentiation and integration". | stated (Guide) |
| Differential Equations | Vector Calculus | Partial derivatives, gradient and directional derivative are taught first in Differential Equations. | judged (the gradient appears in both schedules) |
| Differential Equations | Probability | Guide: "the difference equations of Differential Equations". | stated (Guide) |
| Differential Equations | Dynamics and Relativity | Guide: motion in a gravitational field uses "techniques from this course and the Differential Equations course". | stated (Guide) |
| Mechanics (non-examinable) | Dynamics and Relativity | Schedules: "Familiarity with the topics covered in the non-examinable Mechanics course is assumed." | stated (Schedules) |
| Analysis I, Vector Calculus | Probability | Guide: links with "calculus of Vector Calculus and Analysis" (continuous variables, Jacobians). | stated (Guide) |
| Vector Calculus | Dynamics and Relativity | Gradient and potentials in conservative forces. | judged |

There is no Part IA prerequisite into Groups other than the above, and none out of Groups.

The Guide also says Vector Calculus is "an 'applied' course, meaning that you are expected to be able to apply
techniques, but not necessarily to prove rigorously that they work" and that the rigour "will come in future
analysis courses". The register therefore does not make
Analysis I a prerequisite of Vector Calculus.

## 3. The Cambridge order, for reference

Michaelmas: Vectors and Matrices, Differential Equations, Groups, Numbers and Sets (and the optional
10-lecture Mechanics). Lent: Analysis I, Probability, Vector Calculus, Dynamics and Relativity. Easter:
Computational Projects introduction and optional Part IB preview courses. Cambridge runs four courses in
parallel each term. It is a useful reference, not necessarily the best order for independent study.

## 4. Proposed sequence

Work on **one or two threads at a time**, not four. Phases overlap; an item is started when its
prerequisites are at least at `understanding` (the assessor's call). Id ranges are from the register.

| Phase | Items | Why here | Computational exploration | Harvard enrichment (optional, after the phase) |
|---|---|---|---|---|
| **A. The language of proof** | Numbers and Sets: logic, sets, relations, integers and induction, elementary number theory (IA-NS-001 to IA-NS-014). In parallel: Vectors and Matrices complex numbers and vectors (IA-VM-001 to IA-VM-008). | Proof construction is the stated priority; Groups and Analysis I rest on it. | Euclid's algorithm, modular exponentiation, a toy RSA | none needed; the 2018 discrete mathematics page is optional extra practice |
| **B. Linear algebra and structure** | Vectors and Matrices matrices, systems, eigenvalues, quadratic forms (IA-VM-009 to IA-VM-018); then Groups (IA-GP-001 to IA-GP-016). | Groups needs the equivalence relations and modular arithmetic from A, and V&M for matrix groups. | permutation and symmetry-group computations; matrix group checks | Axler (owned) after V&M; Artin and 55a lectures L1-L4, L21-L22 after Groups |
| **C. Calculus as modelling** | Differential Equations (IA-DE-001 to IA-DE-020). | Needs the matrix methods and eigenvalues from B for coupled systems. Keeps applied mathematics in the programme from the start. | logistic map, phase portraits, numerical ODE solvers | none |
| **D. Rigorous analysis** | Numbers and Sets real numbers and countability (IA-NS-015 to IA-NS-022), then Analysis I (IA-AN-001 to IA-AN-020). | Needs least upper bounds and series from the real-numbers block and the calculus from C. | convergence experiments (illustrations only, never proofs) | Rudin; 55b lectures L19-L20 |
| **E. Probability** | Probability (IA-PR-001 to IA-PR-027). | Needs counting (A), series and integrals (D), difference equations (C). | Monte Carlo, random walks and gambler's ruin, branching processes, Box-Muller, CLT demonstrations | none |
| **F. Vector calculus** | Vector Calculus (IA-VC-001 to IA-VC-014). | Needs suffix notation (A/B) and partial derivatives and gradient (C). | numerical line and surface integrals; testing Stokes and the divergence theorem | none |
| **G. Dynamics and relativity** | Mechanics if needed (IA-MC-001 to IA-MC-010), then Dynamics and Relativity (IA-DR-001 to IA-DR-024). | Needs differential equations, vector methods, Lorentz transformations from V&M, and potentials from F. | orbit integration, the rocket equation, Lorentz boosts | none |

Ancillary items: Computational Projects (IA-CP-001, IA-CP-002) are Easter-term preparation for Part IB and
sit outside the sequence; the director may bring them forward. Starred items (IA-AN-015, IA-DR-010) are
lectured but not examinable.

Differences from the Cambridge order, and why:

1. Numbers and Sets first, so proof technique is in place before Groups and Analysis I.
2. Analysis I after the real-numbers block and after Differential Equations, because Cambridge itself
   treats Analysis I as the rigorous version of Differential Equations' calculus.
3. Probability after Analysis I (series, convergence, integrals) instead of in parallel.
4. Dynamics and Relativity last, because it draws on Differential Equations, vector methods and potentials.

## 5. Coverage is complete

Every one of the 161 examinable-course items appears in exactly one phase above, and all eight courses
are scheduled, so applied mathematics is preserved in full. The sequence does not drop or defer any
Cambridge-required item.

## 6. Decisions for the director

1. Confirm or amend the `librarian-judgement` prerequisites, especially Groups to Vectors and Matrices.
2. Whether Analysis I should start earlier (the Cambridge approach) or stay after Differential Equations.
3. Whether the non-examinable Mechanics items and Computational Projects belong in the plan.
4. How the 2025 papers (edition note in [assessments/tripos-papers/index.md](../assessments/tripos-papers/index.md))
   are used against the 2026-27 syllabus.
5. Whether and when to include Part IB previews (Groups, Rings and Modules in Lent is the one the Guide
   mentions); none are in this baseline.
