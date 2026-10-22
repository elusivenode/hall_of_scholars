# Part IA syllabus (readable view of the register)

This page renders [coverage.yaml](coverage.yaml), which is the authoritative register. If they disagree, the YAML is right and this page is stale.

**Source:** *Schedules of Lecture Courses and Form of Examinations for the Mathematical Tripos 2026-27*, revised 19 August 2026, Part IA (printed pp.8 to 12); see [references/source-register.md](../references/source-register.md). The syllabus statements below are the curriculum librarian's **own summaries**, not Cambridge's wording: the Cambridge text is copyright and this repository is public. Each item is tied to its exact Schedules location (page, heading, paragraph, position) and carries a fingerprint so it can be audited against a local copy of the PDF. All summaries are currently `librarian-draft`: **none has yet been compared with the source by the director or the independent reviewer**, and a passing fingerprint audit does not prove a summary is faithful. Superscripts and subscripts are written with `^` and `_` in the summaries (R^3, S_n).

**Reading the entries.** `Lectures [n]` is the Schedules' count for the whole source paragraph, shared by its items, not a per-item figure. *Starred* means the Schedules put the topic between asterisks: the lecturer must cover it but examiners cannot set questions on it. Tags such as `statement-only` or `informal-treatment` record scope qualifiers present in the source wording. Relations are typed: **requires** (mathematically necessary for the intended treatment), **recommended** (helpful preparation), **connected** (related; no ordering constraint). Provenance letters: **C** Cambridge states it, **I** inferred from Cambridge's wording, **J** librarian's judgement, **D** director-approved. A prerequisite can be met by prior study; it never means mastery must be recorded first.

## Summary

| Course | Code | Term | Paper | Items | Starred | Lectures |
|---|---|---|---|---|---|---|
| [Numbers and Sets](#numbers-and-sets) | IA-NS | Michaelmas | Paper 4 | 22 | 0 | 24 |
| [Groups](#groups) | IA-GP | Michaelmas | Paper 3 | 16 | 0 | 24 |
| [Vectors and Matrices](#vectors-and-matrices) | IA-VM | Michaelmas | Paper 1 | 18 | 0 | 24 |
| [Differential Equations](#differential-equations) | IA-DE | Michaelmas | Paper 2 | 20 | 0 | 24 |
| [Analysis I](#analysis-i) | IA-AN | Lent | Paper 1 | 20 | 1 | 24 |
| [Probability](#probability) | IA-PR | Lent | Paper 2 | 27 | 0 | 24 |
| [Vector Calculus](#vector-calculus) | IA-VC | Lent | Paper 3 | 14 | 0 | 24 |
| [Dynamics and Relativity](#dynamics-and-relativity) | IA-DR | Lent | Paper 4 | 24 | 1 | 24 |
| Ancillary: Mechanics (non-examinable) | IA-MC | Michaelmas | none | 10 | 0 | 10 |
| Ancillary: Computational Projects | IA-CP | Easter (Part IA); examined in Part IB | none | 2 | 0 | 8 |

Total: **161 items** across the eight examinable courses, plus 12 ancillary items.

## Numbers and Sets

24 lectures, Michaelmas Term. Examined on Paper 4.

- **IA-NS-N01** (course note): Course note: this course does not form part of Option (b), Mathematics with Physics.


### Introduction to number systems and logic

Reading map: RM-NS-01

- **IA-NS-001**: A survey of the number systems (naturals, integers, rationals, reals, with irrational, algebraic and transcendental numbers); a brief look at the complex numbers, with the Fundamental Theorem of Algebra stated only. `statement-only`, `brief`  
  <sub>NS-B01, item 1 of 2; Schedules printed p.9. Lectures [2].</sub>
- **IA-NS-002**: What an axiomatic system and a proof are, why proof is needed, and the role of counterexamples; elementary logic (implication, negation of compound statements); proof by contradiction.  
  <sub>NS-B01, item 2 of 2; Schedules printed p.9. Lectures [2].</sub>

### Sets, relations and functions

Reading map: RM-NS-02

- **IA-NS-003**: Union, intersection and equality of sets.  
  <sub>NS-B02, item 1 of 5; Schedules printed p.9. Lectures [4]. recommended IA-NS-002(J).</sub>
- **IA-NS-004**: Indicator (characteristic) functions and their use in proving set identities.  
  <sub>NS-B02, item 2 of 5; Schedules printed p.9. Lectures [4]. requires IA-NS-003(J).</sub>
- **IA-NS-005**: Functions, and the notions of injection, surjection and bijection.  
  <sub>NS-B02, item 3 of 5; Schedules printed p.9. Lectures [4]. requires IA-NS-003(J).</sub>
- **IA-NS-006**: Relations in general and equivalence relations in particular.  
  <sub>NS-B02, item 4 of 5; Schedules printed p.9. Lectures [4]. requires IA-NS-003(J).</sub>
- **IA-NS-007**: Counting arrangements and selections from a set; the Inclusion-Exclusion Principle.  
  <sub>NS-B02, item 5 of 5; Schedules printed p.9. Lectures [4]. recommended IA-NS-005(J).</sub>

### The integers

Reading map: RM-NS-03

- **IA-NS-008**: Mathematical induction and the well-ordering principle for the natural numbers, with examples including the Binomial Theorem.  
  <sub>NS-B03, item 1 of 1; Schedules printed p.9. Lectures [2]. recommended IA-NS-002(J), IA-NS-003(J).</sub>

### Elementary number theory

Reading map: RM-NS-04

- **IA-NS-009**: Existence and uniqueness of prime factorisation; hcf and lcm.  
  <sub>NS-B04, item 1 of 6; Schedules printed p.9. Lectures [8]. requires IA-NS-008(J).</sub>
- **IA-NS-010**: Euclid's proof that there are infinitely many primes.  
  <sub>NS-B04, item 2 of 6; Schedules printed p.9. Lectures [8]. requires IA-NS-009(J).</sub>
- **IA-NS-011**: Euclid's algorithm, and solving ax + by = c in integers.  
  <sub>NS-B04, item 3 of 6; Schedules printed p.9. Lectures [8]. requires IA-NS-009(J).</sub>
- **IA-NS-012**: Modular arithmetic (congruences) and the units modulo n.  
  <sub>NS-B04, item 4 of 6; Schedules printed p.9. Lectures [8]. requires IA-NS-011(J); recommended IA-NS-006(J).</sub>
- **IA-NS-013**: The Chinese Remainder Theorem, Wilson's Theorem and the Fermat-Euler Theorem.  
  <sub>NS-B04, item 5 of 6; Schedules printed p.9. Lectures [8]. requires IA-NS-012(J).</sub>
- **IA-NS-014**: Public-key cryptography and the RSA algorithm.  
  <sub>NS-B04, item 6 of 6; Schedules printed p.9. Lectures [8]. requires IA-NS-013(J).</sub>

### The real numbers

Reading map: RM-NS-05

- **IA-NS-015**: Least upper bounds with simple examples, and the least upper bound axiom for the reals.  
  <sub>NS-B05, item 1 of 4; Schedules printed p.9. Lectures [4]. recommended IA-NS-001(J), IA-NS-003(J).</sub>
- **IA-NS-016**: Sequences and series, including convergence of bounded monotonic sequences.  
  <sub>NS-B05, item 2 of 4; Schedules printed p.9. Lectures [4]. requires IA-NS-015(J).</sub>
- **IA-NS-017**: Irrationality of the square root of 2 and of e; decimal expansions.  
  <sub>NS-B05, item 3 of 4; Schedules printed p.9. Lectures [4]. requires IA-NS-016(J); recommended IA-NS-009(J).</sub>
- **IA-NS-018**: Constructing an explicit transcendental number.  
  <sub>NS-B05, item 4 of 4; Schedules printed p.9. Lectures [4]. recommended IA-NS-017(J).</sub>

### Countability and uncountability

Reading map: RM-NS-06

- **IA-NS-019**: What it means for a set to be finite, infinite, countable or uncountable.  
  <sub>NS-B06, item 1 of 4; Schedules printed p.9. Lectures [4]. requires IA-NS-005(J).</sub>
- **IA-NS-020**: The union of countably many countable sets is again countable.  
  <sub>NS-B06, item 2 of 4; Schedules printed p.9. Lectures [4]. requires IA-NS-019(J).</sub>
- **IA-NS-021**: R is uncountable, and no set admits a bijection onto its power set.  
  <sub>NS-B06, item 3 of 4; Schedules printed p.9. Lectures [4]. requires IA-NS-019(J); recommended IA-NS-017(J).</sub>
- **IA-NS-022**: An indirect (non-constructive) proof that transcendental numbers exist.  
  <sub>NS-B06, item 4 of 4; Schedules printed p.9. Lectures [4]. requires IA-NS-020(J), IA-NS-021(J); recommended IA-NS-001(J).</sub>

## Groups

24 lectures, Michaelmas Term. Examined on Paper 3.



### Examples of groups

Reading map: RM-GP-01

- **IA-GP-001**: The group axioms, with examples drawn from geometry: the symmetry groups of regular polygons, the cube and the tetrahedron.  
  <sub>GP-B01, item 1 of 3; Schedules printed p.8. Lectures [4].</sub>
- **IA-GP-002**: Permutations of a set and the symmetric group; subgroups and homomorphisms; a symmetry group seen as a subgroup of a permutation group.  
  <sub>GP-B01, item 2 of 3; Schedules printed p.8. Lectures [4]. requires IA-GP-001(J).</sub>
- **IA-GP-003**: The Mobius group of transformations of the extended plane: cross-ratio, how circles are preserved, the point at infinity; conjugation, and the fixed points of Mobius maps with the behaviour of their iterates.  
  <sub>GP-B01, item 3 of 3; Schedules printed p.8. Lectures [4]. requires IA-VM-001(J); recommended IA-GP-002(J).</sub>

### Lagrange's theorem

Reading map: RM-GP-02

- **IA-GP-004**: Cosets of a subgroup, leading to Lagrange's theorem.  
  <sub>GP-B02, item 1 of 3; Schedules printed p.8. Lectures [5]. requires IA-GP-002(J); recommended IA-NS-006(J).</sub>
- **IA-GP-005**: Classification of the groups of small order (up to order 8); the quaternion group.  
  <sub>GP-B02, item 2 of 3; Schedules printed p.8. Lectures [5]. requires IA-GP-004(J).</sub>
- **IA-GP-006**: The Fermat-Euler theorem re-derived using group theory.  
  <sub>GP-B02, item 3 of 3; Schedules printed p.8. Lectures [5]. requires IA-GP-004(J); recommended IA-NS-012(I).</sub>

### Group actions

Reading map: RM-GP-03

- **IA-GP-007**: Group actions on a set: orbits and stabilisers, and the orbit-stabiliser theorem.  
  <sub>GP-B03, item 1 of 3; Schedules printed p.8. Lectures [4]. requires IA-GP-002(J), IA-GP-004(J).</sub>
- **IA-GP-008**: Cayley's theorem: every group embeds as a subgroup of a permutation group.  
  <sub>GP-B03, item 2 of 3; Schedules printed p.8. Lectures [4]. requires IA-GP-007(J).</sub>
- **IA-GP-009**: Conjugacy classes in a group; Cauchy's theorem.  
  <sub>GP-B03, item 3 of 3; Schedules printed p.8. Lectures [4]. requires IA-GP-007(J).</sub>

### Quotient groups

Reading map: RM-GP-04

- **IA-GP-010**: Normal subgroups and quotient groups, with the isomorphism theorem.  
  <sub>GP-B04, item 1 of 1; Schedules printed p.8. Lectures [4]. requires IA-GP-004(J), IA-GP-002(J).</sub>

### Matrix groups

Reading map: RM-GP-05

- **IA-GP-011**: The general linear and special linear groups, and how they relate to the Mobius group.  
  <sub>GP-B05, item 1 of 3; Schedules printed p.8. Lectures [3]. requires IA-GP-001(J), IA-VM-009(I).</sub>
- **IA-GP-012**: The orthogonal and special orthogonal groups; a proof, in R^3, that every orthogonal transformation is a product of reflections and every rotation has an axis. `proof-given`  
  <sub>GP-B05, item 2 of 3; Schedules printed p.8. Lectures [3]. requires IA-VM-012(I); recommended IA-GP-011(J).</sub>
- **IA-GP-013**: A change of basis viewed as an instance of conjugation.  
  <sub>GP-B05, item 3 of 3; Schedules printed p.8. Lectures [3]. recommended IA-GP-003(J), IA-VM-015(I).</sub>

### Permutations

Reading map: RM-GP-06

- **IA-GP-014**: Permutations written as cycles and as products of transpositions; the sign of a permutation.  
  <sub>GP-B06, item 1 of 3; Schedules printed p.8. Lectures [4]. requires IA-GP-002(J).</sub>
- **IA-GP-015**: When two permutations are conjugate in S_n, and in A_n.  
  <sub>GP-B06, item 2 of 3; Schedules printed p.8. Lectures [4]. requires IA-GP-014(J), IA-GP-009(J).</sub>
- **IA-GP-016**: Simple groups, including a proof that A_5 is simple.  
  <sub>GP-B06, item 3 of 3; Schedules printed p.8. Lectures [4]. requires IA-GP-010(J), IA-GP-015(J).</sub>

## Vectors and Matrices

24 lectures, Michaelmas Term. Examined on Paper 1.



### Complex numbers

Reading map: RM-VM-01

- **IA-VM-001**: Revision of complex numbers: conjugate, inverse, modulus, argument and the Argand diagram. `revision`  
  <sub>VM-B01, item 1 of 2; Schedules printed p.8. Lectures [2].</sub>
- **IA-VM-002**: Informal treatment of complex logarithms, n-th roots and powers, and de Moivre's theorem. `informal-treatment`  
  <sub>VM-B01, item 2 of 2; Schedules printed p.8. Lectures [2]. requires IA-VM-001(J).</sub>

### Vectors

Reading map: RM-VM-02

- **IA-VM-003**: Revision of the elementary algebra of vectors in R^3, including the scalar product. `revision`  
  <sub>VM-B02, item 1 of 6; Schedules printed p.8. Lectures [5].</sub>
- **IA-VM-004**: A brief look at vectors in R^n and C^n, with the scalar product and the Cauchy-Schwarz inequality. `brief`  
  <sub>VM-B02, item 2 of 6; Schedules printed p.8. Lectures [5]. requires IA-VM-003(J), IA-VM-001(J).</sub>
- **IA-VM-005**: The ideas of linear span, linear independence, subspace, basis and dimension.  
  <sub>VM-B02, item 3 of 6; Schedules printed p.8. Lectures [5]. recommended IA-VM-004(J).</sub>
- **IA-VM-006**: Suffix (index) notation: the summation convention and the symbols delta_ij and epsilon_ijk.  
  <sub>VM-B02, item 4 of 6; Schedules printed p.8. Lectures [5]. requires IA-VM-003(J).</sub>
- **IA-VM-007**: The vector product and triple product, their definitions and geometric meaning; solving linear equations in vectors.  
  <sub>VM-B02, item 5 of 6; Schedules printed p.8. Lectures [5]. recommended IA-VM-006(J).</sub>
- **IA-VM-008**: Geometric applications of vectors, including the equations of lines, planes and spheres.  
  <sub>VM-B02, item 6 of 6; Schedules printed p.8. Lectures [5]. requires IA-VM-007(J).</sub>

### Matrices

Reading map: RM-VM-03

- **IA-VM-009**: Arithmetic of 3 x 3 matrices and their determinants, extended to n x n complex matrices; trace, invertibility and inverse matrices.  
  <sub>VM-B03, item 1 of 2; Schedules printed p.8. Lectures [4].</sub>
- **IA-VM-010**: Matrices as linear maps, with geometric examples (rotations, reflections, dilations, shears); kernel and image; the rank-nullity theorem is stated only, not proved. `statement-only`  
  <sub>VM-B03, item 2 of 2; Schedules printed p.8. Lectures [4]. requires IA-VM-009(J), IA-VM-005(J).</sub>
- **IA-VM-011**: Systems of linear equations in matrix form: when solutions exist and are unique, the geometric picture, and Gaussian elimination.  
  <sub>VM-B04, item 1 of 1; Schedules printed p.8. Lectures [3]. requires IA-VM-009(J); recommended IA-VM-010(J).</sub>
- **IA-VM-012**: Special classes of matrix (symmetric, antisymmetric, orthogonal, hermitian, unitary), and writing any matrix as a sum of an isotropic part, a symmetric trace-free part and an antisymmetric part.  
  <sub>VM-B05, item 1 of 1; Schedules printed p.8. Lectures [1]. requires IA-VM-009(J).</sub>

### Eigenvalues and Eigenvectors

Reading map: RM-VM-04

- **IA-VM-013**: Eigenvalues and eigenvectors and their geometric meaning.  
  <sub>VM-B06, item 1 of 1; Schedules printed p.8. Lectures [2]. requires IA-VM-010(J), IA-VM-011(J).</sub>
- **IA-VM-014**: Proof that hermitian matrices have real eigenvalues and that eigenvectors for different eigenvalues are orthogonal, which gives an orthogonal basis of eigenvectors. `proof-given`  
  <sub>VM-B07, item 1 of 3; Schedules printed p.8. Lectures [5]. requires IA-VM-013(J), IA-VM-012(J), IA-VM-004(J).</sub>
- **IA-VM-015**: How a matrix changes under an arbitrary change of basis (similarity transformations).  
  <sub>VM-B07, item 2 of 3; Schedules printed p.8. Lectures [5]. requires IA-VM-005(J); recommended IA-VM-013(J).</sub>
- **IA-VM-016**: When a general matrix can be diagonalised (sufficient conditions), examples where it cannot, and canonical forms for 2 x 2 matrices.  
  <sub>VM-B07, item 3 of 3; Schedules printed p.8. Lectures [5]. requires IA-VM-015(J).</sub>
- **IA-VM-017**: Quadratic forms, including how they change under a change of basis; classification of conics in Cartesian and polar form.  
  <sub>VM-B08, item 1 of 1; Schedules printed p.8. Lectures [1]. requires IA-VM-014(J); recommended IA-VM-015(J).</sub>
- **IA-VM-018**: Rotation matrices and Lorentz transformations presented as groups of transformations.  
  <sub>VM-B09, item 1 of 1; Schedules printed p.8. Lectures [1]. requires IA-VM-010(J), IA-VM-012(J); connected IA-GP-001(J).</sub>

## Differential Equations

24 lectures, Michaelmas Term. Examined on Paper 2.



### Basic calculus

Reading map: RM-DE-01

- **IA-DE-001**: A working (non-rigorous) review of single-variable calculus: derivative as a limit, chain rule, Leibniz's rule, Taylor series, big-O and little-o notation and l'Hopital's rule treated informally; integral as area, the fundamental theorem, and integration by substitution and by parts. `informal-treatment`  
  <sub>DE-B01, item 1 of 1; Schedules printed p.9. Lectures [3].</sub>
- **IA-DE-002**: Partial derivatives introduced informally with their geometric meaning; the equality of mixed partials is stated only; chain rule and implicit differentiation. `statement-only`, `informal-treatment`  
  <sub>DE-B02, item 1 of 3; Schedules printed p.9. Lectures [2]. requires IA-DE-001(J).</sub>
- **IA-DE-003**: Differentials, treated informally, including exact differentials. `informal-treatment`  
  <sub>DE-B02, item 2 of 3; Schedules printed p.9. Lectures [2]. requires IA-DE-002(J).</sub>
- **IA-DE-004**: Differentiating an integral with respect to a parameter.  
  <sub>DE-B02, item 3 of 3; Schedules printed p.9. Lectures [2]. requires IA-DE-002(J).</sub>

### First-order linear differential equations

Reading map: RM-DE-02

- **IA-DE-005**: First-order linear equations with constant coefficients: exponential growth, the comparison with discrete (difference) equations, series solutions, and modelling examples such as radioactive decay.  
  <sub>DE-B03, item 1 of 2; Schedules printed p.9. Lectures [2]. requires IA-DE-001(J).</sub>
- **IA-DE-006**: First-order linear equations with variable coefficients, solved with an integrating factor.  
  <sub>DE-B03, item 2 of 2; Schedules printed p.9. Lectures [2]. recommended IA-DE-005(J).</sub>

### Nonlinear first-order equations

Reading map: RM-DE-03

- **IA-DE-007**: Separable equations and exact equations.  
  <sub>DE-B04, item 1 of 3; Schedules printed p.9. Lectures [4]. recommended IA-DE-006(J).</sub>
- **IA-DE-008**: Sketching solution curves; equilibria and their stability by perturbation, with examples including the logistic equation and chemical kinetics.  
  <sub>DE-B04, item 2 of 3; Schedules printed p.9. Lectures [4]. recommended IA-DE-007(J).</sub>
- **IA-DE-009**: Discrete (difference) equations: equilibria and stability, with examples including the logistic map.  
  <sub>DE-B04, item 3 of 3; Schedules printed p.9. Lectures [4]. requires IA-DE-008(J); recommended IA-DE-005(J).</sub>

### Higher-order linear differential equations

Reading map: RM-DE-04

- **IA-DE-010**: Linear equations of higher order: complementary function plus particular integral, linear independence, the Wronskian for second-order equations, and Abel's theorem.  
  <sub>DE-B05, item 1 of 5; Schedules printed p.9. Lectures [8]. requires IA-DE-005(J); recommended IA-VM-005(J).</sub>
- **IA-DE-011**: Higher-order linear equations with constant coefficients and their examples (including radioactive decay chains), a comparison with difference equations in simple cases, reduction of order, resonance, transients and damping.  
  <sub>DE-B05, item 2 of 5; Schedules printed p.9. Lectures [8]. requires IA-DE-010(J), IA-VM-001(J).</sub>
- **IA-DE-012**: Homogeneous (equidimensional) equations.  
  <sub>DE-B05, item 3 of 5; Schedules printed p.9. Lectures [8]. recommended IA-DE-011(J).</sub>
- **IA-DE-013**: How a system responds to step and impulse inputs, introducing the Heaviside step function and the Dirac delta.  
  <sub>DE-B05, item 4 of 5; Schedules printed p.9. Lectures [8]. requires IA-DE-011(J).</sub>
- **IA-DE-014**: Series solutions of linear equations; it is only stated, not shown in detail, that a logarithmic solution can be needed. `statement-only`  
  <sub>DE-B05, item 5 of 5; Schedules printed p.9. Lectures [8]. requires IA-DE-010(J).</sub>

### Multivariate functions: applications

Reading map: RM-DE-05

- **IA-DE-015**: Directional derivatives and the gradient vector.  
  <sub>DE-B06, item 1 of 6; Schedules printed p.9. Lectures [5]. requires IA-DE-002(J).</sub>
- **IA-DE-016**: The Taylor series for functions of several variables, stated only. `statement-only`  
  <sub>DE-B06, item 2 of 6; Schedules printed p.9. Lectures [5]. requires IA-DE-002(J), IA-DE-001(J).</sub>
- **IA-DE-017**: Local extrema of functions of several variables, classified by the Hessian matrix.  
  <sub>DE-B06, item 3 of 6; Schedules printed p.9. Lectures [5]. requires IA-DE-016(J); recommended IA-VM-014(J).</sub>
- **IA-DE-018**: Coupled first-order systems: equivalence with a single higher-order equation, and solution by matrix methods.  
  <sub>DE-B06, item 4 of 6; Schedules printed p.9. Lectures [5]. requires IA-DE-011(J), IA-VM-016(I).</sub>
- **IA-DE-019**: Phase portraits near non-degenerate equilibrium points, and stability.  
  <sub>DE-B06, item 5 of 6; Schedules printed p.9. Lectures [5]. requires IA-DE-018(J); recommended IA-DE-008(J).</sub>
- **IA-DE-020**: Simple first- and second-order partial differential equations, including the wave equation solved in the form f(x+ct) + g(x-ct).  
  <sub>DE-B06, item 6 of 6; Schedules printed p.9. Lectures [5]. requires IA-DE-002(J).</sub>

## Analysis I

24 lectures, Lent Term. Examined on Paper 1.



### Limits and convergence

Reading map: RM-AN-01

- **IA-AN-001**: Sequences and series in R and C: limits of sums, products and quotients; absolute convergence implies convergence.  
  <sub>AN-B01, item 1 of 3; Schedules printed p.10. Lectures [6]. requires IA-VM-001(J); recommended IA-NS-016(I), IA-NS-015(I).</sub>
- **IA-AN-002**: The Bolzano-Weierstrass theorem and its applications, including the General Principle of Convergence.  
  <sub>AN-B01, item 2 of 3; Schedules printed p.10. Lectures [6]. requires IA-AN-001(J), IA-NS-015(J).</sub>
- **IA-AN-003**: Convergence tests for series: comparison, ratio and alternating series.  
  <sub>AN-B01, item 3 of 3; Schedules printed p.10. Lectures [6]. requires IA-AN-001(J).</sub>

### Continuity

Reading map: RM-AN-02

- **IA-AN-004**: Continuity of real- or complex-valued functions on subsets of R or C.  
  <sub>AN-B02, item 1 of 3; Schedules printed p.10. Lectures [3]. requires IA-AN-001(J).</sub>
- **IA-AN-005**: The intermediate value theorem.  
  <sub>AN-B02, item 2 of 3; Schedules printed p.10. Lectures [3]. requires IA-AN-004(J); recommended IA-AN-002(J).</sub>
- **IA-AN-006**: A continuous function on a closed interval is bounded and achieves its upper and lower bounds.  
  <sub>AN-B02, item 3 of 3; Schedules printed p.10. Lectures [3]. requires IA-AN-004(J), IA-AN-002(J).</sub>

### Differentiability

Reading map: RM-AN-03

- **IA-AN-007**: Differentiability of functions from R to R.  
  <sub>AN-B03, item 1 of 6; Schedules printed p.10. Lectures [5]. requires IA-AN-004(J); connected IA-DE-001(I).</sub>
- **IA-AN-008**: The derivative of sums and products, the chain rule, and the derivative of an inverse function.  
  <sub>AN-B03, item 2 of 6; Schedules printed p.10. Lectures [5]. requires IA-AN-007(J).</sub>
- **IA-AN-009**: Rolle's theorem and the mean value theorem.  
  <sub>AN-B03, item 3 of 6; Schedules printed p.10. Lectures [5]. requires IA-AN-006(J); recommended IA-AN-008(J).</sub>
- **IA-AN-010**: The one-variable inverse function theorem.  
  <sub>AN-B03, item 4 of 6; Schedules printed p.10. Lectures [5]. requires IA-AN-009(J), IA-AN-005(J).</sub>
- **IA-AN-011**: Taylor's theorem for functions from R to R, with Lagrange's form of the remainder.  
  <sub>AN-B03, item 5 of 6; Schedules printed p.10. Lectures [5]. requires IA-AN-009(J); connected IA-DE-001(I).</sub>
- **IA-AN-012**: Differentiation of functions of a complex variable.  
  <sub>AN-B03, item 6 of 6; Schedules printed p.10. Lectures [5]. requires IA-AN-007(J), IA-VM-001(J).</sub>

### Power series

Reading map: RM-AN-04

- **IA-AN-013**: Complex power series and the radius of convergence.  
  <sub>AN-B04, item 1 of 3; Schedules printed p.10. Lectures [4]. requires IA-AN-003(J).</sub>
- **IA-AN-014**: The exponential, trigonometric and hyperbolic functions and the relations among them.  
  <sub>AN-B04, item 2 of 3; Schedules printed p.10. Lectures [4]. requires IA-AN-013(J); recommended IA-VM-002(J).</sub>
- **IA-AN-015** (*starred*): Starred (lectured but not examinable): a direct proof that a power series is differentiable inside its circle of convergence. `proof-given`  
  <sub>AN-B04, item 3 of 3; Schedules printed p.10. Lectures [4]. requires IA-AN-013(J); recommended IA-AN-008(J).</sub>

### Integration

Reading map: RM-AN-05

- **IA-AN-016**: The definition of the Riemann integral and its basic properties.  
  <sub>AN-B05, item 1 of 5; Schedules printed p.10. Lectures [6]. requires IA-NS-015(J), IA-AN-006(J); connected IA-DE-001(I).</sub>
- **IA-AN-017**: A function that is not integrable; monotonic functions and piecewise-continuous functions are integrable.  
  <sub>AN-B05, item 2 of 5; Schedules printed p.10. Lectures [6]. requires IA-AN-016(J).</sub>
- **IA-AN-018**: The fundamental theorem of calculus, and differentiation of indefinite integrals.  
  <sub>AN-B05, item 3 of 5; Schedules printed p.10. Lectures [6]. requires IA-AN-016(J), IA-AN-009(J).</sub>
- **IA-AN-019**: Integration by parts; the Taylor remainder written as an integral.  
  <sub>AN-B05, item 4 of 5; Schedules printed p.10. Lectures [6]. requires IA-AN-018(J), IA-AN-011(J).</sub>
- **IA-AN-020**: Improper integrals.  
  <sub>AN-B05, item 5 of 5; Schedules printed p.10. Lectures [6]. requires IA-AN-016(J), IA-AN-001(J).</sub>

## Probability

24 lectures, Lent Term. Examined on Paper 2.



### Basic concepts

Reading map: RM-PR-01

- **IA-PR-001**: Classical probability with equally likely outcomes.  
  <sub>PR-B01, item 1 of 3; Schedules printed p.10. Lectures [3]. recommended IA-NS-007(C).</sub>
- **IA-PR-002**: Combinatorial analysis: permutations and combinations.  
  <sub>PR-B01, item 2 of 3; Schedules printed p.10. Lectures [3]. recommended IA-NS-007(C).</sub>
- **IA-PR-003**: Stirling's formula, with the asymptotics of log n! proved. `proof-given`  
  <sub>PR-B01, item 3 of 3; Schedules printed p.10. Lectures [3]. recommended IA-PR-002(J), IA-AN-001(J).</sub>

### Axiomatic approach

Reading map: RM-PR-02

- **IA-PR-004**: The axioms of probability in the countable case; probability spaces.  
  <sub>PR-B02, item 1 of 5; Schedules printed p.10. Lectures [5]. recommended IA-PR-001(J), IA-NS-003(J).</sub>
- **IA-PR-005**: Inclusion-exclusion; continuity and subadditivity properties of a probability measure.  
  <sub>PR-B02, item 2 of 5; Schedules printed p.10. Lectures [5]. requires IA-PR-004(J); recommended IA-NS-007(J).</sub>
- **IA-PR-006**: Independence of events.  
  <sub>PR-B02, item 3 of 5; Schedules printed p.10. Lectures [5]. requires IA-PR-004(J).</sub>
- **IA-PR-007**: The binomial, Poisson and geometric distributions, and how the Poisson distribution arises from the binomial.  
  <sub>PR-B02, item 4 of 5; Schedules printed p.10. Lectures [5]. requires IA-PR-006(J); recommended IA-PR-002(J).</sub>
- **IA-PR-008**: Conditional probability and Bayes's formula, with examples including Simpson's paradox.  
  <sub>PR-B02, item 5 of 5; Schedules printed p.10. Lectures [5]. requires IA-PR-004(J).</sub>

### Discrete random variables

Reading map: RM-PR-03

- **IA-PR-009**: Expectation of a discrete random variable.  
  <sub>PR-B03, item 1 of 8; Schedules printed p.10. Lectures [7]. recommended IA-PR-007(J).</sub>
- **IA-PR-010**: Functions of a random variable, indicator functions, variance and standard deviation.  
  <sub>PR-B03, item 2 of 8; Schedules printed p.10. Lectures [7]. requires IA-PR-009(J).</sub>
- **IA-PR-011**: Covariance and independence of random variables.  
  <sub>PR-B03, item 3 of 8; Schedules printed p.10. Lectures [7]. requires IA-PR-010(J), IA-PR-006(J).</sub>
- **IA-PR-012**: Generating functions: sums of independent random variables, the random sum formula and moments.  
  <sub>PR-B03, item 4 of 8; Schedules printed p.10. Lectures [7]. requires IA-PR-011(J); recommended IA-AN-013(J).</sub>
- **IA-PR-013**: Conditional expectation.  
  <sub>PR-B03, item 5 of 8; Schedules printed p.10. Lectures [7]. requires IA-PR-009(J), IA-PR-008(J).</sub>
- **IA-PR-014**: Random walks: gambler's ruin and recurrence relations, solving difference equations, and the mean time to absorption.  
  <sub>PR-B03, item 6 of 8; Schedules printed p.10. Lectures [7]. recommended IA-PR-013(J); connected IA-DE-011(C).</sub>
- **IA-PR-015**: Branching processes: generating functions and the probability of extinction.  
  <sub>PR-B03, item 7 of 8; Schedules printed p.10. Lectures [7]. requires IA-PR-012(J), IA-PR-013(J).</sub>
- **IA-PR-016**: Combinatorial applications of generating functions.  
  <sub>PR-B03, item 8 of 8; Schedules printed p.10. Lectures [7]. requires IA-PR-012(J).</sub>

### Continuous random variables

Reading map: RM-PR-04

- **IA-PR-017**: Distributions and density functions of continuous random variables; expectations, including of a function of a random variable.  
  <sub>PR-B04, item 1 of 6; Schedules printed p.10. Lectures [6]. recommended IA-PR-009(J), IA-DE-001(I), IA-AN-020(I).</sub>
- **IA-PR-018**: The uniform, normal and exponential distributions, and the memoryless property of the exponential.  
  <sub>PR-B04, item 2 of 6; Schedules printed p.10. Lectures [6]. requires IA-PR-017(J).</sub>
- **IA-PR-019**: Joint distributions and transformations of random variables, including Jacobians, with examples.  
  <sub>PR-B04, item 3 of 6; Schedules printed p.10. Lectures [6]. requires IA-PR-017(J); recommended IA-DE-002(I), IA-VC-003(I).</sub>
- **IA-PR-020**: Simulation of continuous random variables: the Box-Muller transform and rejection sampling.  
  <sub>PR-B04, item 4 of 6; Schedules printed p.10. Lectures [6]. requires IA-PR-018(J); recommended IA-PR-019(J).</sub>
- **IA-PR-021**: Geometrical probability: Bertrand's paradox and Buffon's needle.  
  <sub>PR-B04, item 5 of 6; Schedules printed p.10. Lectures [6]. requires IA-PR-017(J).</sub>
- **IA-PR-022**: The correlation coefficient and bivariate normal random variables.  
  <sub>PR-B04, item 6 of 6; Schedules printed p.10. Lectures [6]. requires IA-PR-019(J), IA-PR-011(J).</sub>

### Inequalities and limits

Reading map: RM-PR-05

- **IA-PR-023**: Markov's inequality and Chebyshev's inequality.  
  <sub>PR-B05, item 1 of 5; Schedules printed p.10. Lectures [3]. requires IA-PR-009(J), IA-PR-010(J).</sub>
- **IA-PR-024**: The weak law of large numbers.  
  <sub>PR-B05, item 2 of 5; Schedules printed p.10. Lectures [3]. requires IA-PR-023(J), IA-PR-011(J).</sub>
- **IA-PR-025**: Convex functions, Jensen's inequality for arbitrary random variables, and the AM-GM inequality.  
  <sub>PR-B05, item 3 of 5; Schedules printed p.10. Lectures [3]. requires IA-PR-009(J).</sub>
- **IA-PR-026**: Moment generating functions; the continuity theorem is stated without proof. `statement-only`  
  <sub>PR-B05, item 4 of 5; Schedules printed p.10. Lectures [3]. requires IA-PR-017(J); recommended IA-PR-012(J).</sub>
- **IA-PR-027**: The central limit theorem is stated and its proof sketched; examples, including sampling. `statement-only`, `proof-sketch`  
  <sub>PR-B05, item 5 of 5; Schedules printed p.10. Lectures [3]. requires IA-PR-026(J), IA-PR-018(J); recommended IA-PR-024(J).</sub>

## Vector Calculus

24 lectures, Lent Term. Examined on Paper 3.



### Curves in R3

Reading map: RM-VC-01

- **IA-VC-001**: Parametrised curves in R^3: arc length, tangent and normal vectors, curvature and torsion.  
  <sub>VC-B01, item 1 of 1; Schedules printed p.11. Lectures [1]. recommended IA-DE-001(J), IA-VM-007(J); connected IA-AN-007(I).</sub>

### Integration in R2 and R3

Reading map: RM-VC-02

- **IA-VC-002**: Line integrals.  
  <sub>VC-B02, item 1 of 2; Schedules printed p.11. Lectures [4]. requires IA-VC-001(J); recommended IA-DE-002(J); connected IA-AN-016(I).</sub>
- **IA-VC-003**: Surface and volume integrals: definitions, examples in Cartesian, cylindrical and spherical coordinates, and change of variables.  
  <sub>VC-B02, item 2 of 2; Schedules printed p.11. Lectures [4]. recommended IA-VC-002(J), IA-VM-007(J); connected IA-AN-016(I).</sub>

### Vector operators

Reading map: RM-VC-03

- **IA-VC-004**: Directional derivatives and the gradient of a scalar function: its definition, its role as a normal to level surfaces, and examples in cylindrical and spherical coordinates. Use of general orthogonal curvilinear coordinates is a starred part (lectured, not examinable).  
  <sub>VC-B03, item 1 of 4; Schedules printed p.11. Lectures [5]. Starred part: general orthogonal curvilinear coordinates. recommended IA-DE-015(I), IA-VM-006(J).</sub>
- **IA-VC-005**: Divergence, curl and the Laplacian in Cartesian coordinates, with examples; the corresponding formulae in cylindrical and spherical coordinates are quoted without derivation. The general orthogonal curvilinear case is a starred part (lectured, not examinable). `statement-only`  
  <sub>VC-B03, item 2 of 4; Schedules printed p.11. Lectures [5]. Starred part: general orthogonal curvilinear coordinates. requires IA-VC-004(J); recommended IA-VM-006(J).</sub>
- **IA-VC-006**: Solenoidal, irrotational and conservative fields, and scalar potentials.  
  <sub>VC-B03, item 3 of 4; Schedules printed p.11. Lectures [5]. requires IA-VC-005(J).</sub>
- **IA-VC-007**: Identities between vector derivative operators.  
  <sub>VC-B03, item 4 of 4; Schedules printed p.11. Lectures [5]. requires IA-VC-005(J); recommended IA-VM-006(J).</sub>

### Integration theorems

Reading map: RM-VC-04

- **IA-VC-008**: The divergence theorem, Green's theorem, Stokes's theorem and Green's second theorem: statements, informal proofs and examples, with applications to fluid dynamics and to electromagnetism (Maxwell's equations are stated). `informal-proof`  
  <sub>VC-B04, item 1 of 1; Schedules printed p.11. Lectures [5]. requires IA-VC-003(J), IA-VC-005(J).</sub>

### Laplace's equation

Reading map: RM-VC-05

- **IA-VC-009**: Laplace's equation in R^2 and R^3: the uniqueness theorem and the maximum principle.  
  <sub>VC-B05, item 1 of 2; Schedules printed p.11. Lectures [4]. requires IA-VC-008(J), IA-VC-005(J).</sub>
- **IA-VC-010**: Solving Poisson's equation: Gauss's method when the symmetry is spherical or cylindrical, and a general integral solution.  
  <sub>VC-B05, item 2 of 2; Schedules printed p.11. Lectures [4]. requires IA-VC-008(J); recommended IA-VC-009(J).</sub>

### Cartesian tensors in R3

Reading map: RM-VC-06

- **IA-VC-011**: How tensor components transform under change of axes; adding, multiplying and contracting tensors, with emphasis on second-rank tensors.  
  <sub>VC-B06, item 1 of 4; Schedules printed p.11. Lectures [5]. requires IA-VM-006(I), IA-VM-018(I).</sub>
- **IA-VC-012**: Isotropic tensors of second and third rank.  
  <sub>VC-B06, item 2 of 4; Schedules printed p.11. Lectures [5]. requires IA-VC-011(J).</sub>
- **IA-VC-013**: Symmetric and antisymmetric tensors; a revision of principal axes and diagonalisation. `revision`  
  <sub>VC-B06, item 3 of 4; Schedules printed p.11. Lectures [5]. requires IA-VC-011(J); recommended IA-VM-014(I).</sub>
- **IA-VC-014**: The quotient theorem, with examples such as the inertia tensor and conductivity.  
  <sub>VC-B06, item 4 of 4; Schedules printed p.11. Lectures [5]. requires IA-VC-011(J).</sub>

## Dynamics and Relativity

24 lectures, Lent Term. Examined on Paper 4.

- **IA-DR-N01** (course note): Course note: this course does not form part of Option (b), Mathematics with Physics.
- **IA-DR-N02** (course note): Course note: familiarity with the non-examinable Mechanics course is assumed.


### Basic concepts

Reading map: RM-DR-01

- **IA-DR-001**: Space, time and frames of reference; Galilean transformations.  
  <sub>DR-B01, item 1 of 4; Schedules printed p.11. Lectures [4]. requires IA-MC-002(I).</sub>
- **IA-DR-002**: Newton's laws of motion.  
  <sub>DR-B01, item 2 of 4; Schedules printed p.11. Lectures [4]. requires IA-MC-005(I).</sub>
- **IA-DR-003**: Dimensional analysis.  
  <sub>DR-B01, item 3 of 4; Schedules printed p.11. Lectures [4].</sub>
- **IA-DR-004**: Examples of forces: gravity, friction and the Lorentz force.  
  <sub>DR-B01, item 4 of 4; Schedules printed p.11. Lectures [4]. requires IA-MC-003(I).</sub>

### Newtonian dynamics of a single particle

Reading map: RM-DR-02

- **IA-DR-005**: Equations of motion in Cartesian and plane polar coordinates.  
  <sub>DR-B02, item 1 of 6; Schedules printed p.11. Lectures [8]. requires IA-DR-002(J), IA-VM-003(C); recommended IA-DE-011(C).</sub>
- **IA-DR-006**: Work, conservative forces and potential energy; what the shape of a potential energy curve says about motion; stable equilibria and small oscillations; the effect of damping.  
  <sub>DR-B02, item 2 of 6; Schedules printed p.11. Lectures [8]. requires IA-DR-005(J), IA-MC-007(I); connected IA-VC-004(J).</sub>
- **IA-DR-007**: Angular velocity, angular momentum and torque.  
  <sub>DR-B02, item 3 of 6; Schedules printed p.11. Lectures [8]. requires IA-VM-007(J); recommended IA-MC-004(I).</sub>
- **IA-DR-008**: Orbits in a central force: the u(theta) equation, escape velocity, Kepler's laws, whether orbits are stable, and scattering from a repulsive potential (Rutherford).  
  <sub>DR-B02, item 4 of 6; Schedules printed p.11. Lectures [8]. requires IA-DR-007(J), IA-DR-006(J); recommended IA-DE-011(C).</sub>
- **IA-DR-009**: Rotating frames: the centrifugal and Coriolis forces.  
  <sub>DR-B02, item 5 of 6; Schedules printed p.11. Lectures [8]. requires IA-DR-007(J); recommended IA-VM-007(J).</sub>
- **IA-DR-010** (*starred*): Starred (lectured but not examinable): a brief discussion of the Foucault pendulum. `brief`  
  <sub>DR-B02, item 6 of 6; Schedules printed p.11. Lectures [8]. requires IA-DR-009(J).</sub>

### Newtonian dynamics of systems of particles

Reading map: RM-DR-03

- **IA-DR-011**: Momentum, angular momentum and energy for a system of particles.  
  <sub>DR-B03, item 1 of 3; Schedules printed p.11. Lectures [2]. requires IA-MC-008(I); recommended IA-DR-007(J).</sub>
- **IA-DR-012**: The centre-of-mass frame and the two-body problem.  
  <sub>DR-B03, item 2 of 3; Schedules printed p.11. Lectures [2]. requires IA-DR-011(J).</sub>
- **IA-DR-013**: Problems with variable mass, including the rocket equation.  
  <sub>DR-B03, item 3 of 3; Schedules printed p.11. Lectures [2]. requires IA-DR-011(J).</sub>

### Rigid bodies

Reading map: RM-DR-04

- **IA-DR-014**: Moments of inertia, and the angular momentum and energy of a rigid body.  
  <sub>DR-B04, item 1 of 3; Schedules printed p.11. Lectures [3]. requires IA-DR-011(J).</sub>
- **IA-DR-015**: The parallel axis theorem.  
  <sub>DR-B04, item 2 of 3; Schedules printed p.11. Lectures [3]. requires IA-DR-014(J).</sub>
- **IA-DR-016**: Simple motions combining rotation and translation, such as rolling.  
  <sub>DR-B04, item 3 of 3; Schedules printed p.11. Lectures [3]. requires IA-DR-014(J); recommended IA-DR-015(J).</sub>

### Special relativity

Reading map: RM-DR-05

- **IA-DR-017**: The principle of relativity, and the relativity of simultaneity.  
  <sub>DR-B05, item 1 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-001(J).</sub>
- **IA-DR-018**: The invariant interval.  
  <sub>DR-B05, item 2 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-017(J).</sub>
- **IA-DR-019**: Lorentz transformations in one space and one time dimension; time dilation and length contraction.  
  <sub>DR-B05, item 3 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-018(J); connected IA-VM-018(J).</sub>
- **IA-DR-020**: The Minkowski metric for one space and one time dimension.  
  <sub>DR-B05, item 4 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-019(J).</sub>
- **IA-DR-021**: Lorentz transformations in three space dimensions plus time.  
  <sub>DR-B05, item 5 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-019(J); recommended IA-VM-018(J).</sub>
- **IA-DR-022**: Four-vectors and Lorentz invariants; proper time.  
  <sub>DR-B05, item 6 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-021(J); recommended IA-VM-006(J).</sub>
- **IA-DR-023**: Four-velocity and four-momentum.  
  <sub>DR-B05, item 7 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-022(J).</sub>
- **IA-DR-024**: Conservation of four-momentum in particle decay and collisions; the Newtonian limit.  
  <sub>DR-B05, item 8 of 8; Schedules printed p.11. Lectures [7]. requires IA-DR-023(J); recommended IA-DR-011(J).</sub>

## Ancillary: Mechanics (non-examinable)

10 lectures, Michaelmas Term. The Schedules state that this material is assumed by Dynamics and Relativity.

- **IA-MC-N01** (course note): Course note: ten lectures for students with limited A-level mechanics; Dynamics and Relativity builds on them.


### Lectures

Reading map: RM-MC-01

- **IA-MC-001**: Lecture 1: a brief introduction to the course. `brief`  
  <sub>MC-B01, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-002**: Lecture 2: kinematics of one particle (position, velocity, speed, acceleration), with uniform acceleration in a line and projectile motion in a plane.  
  <sub>MC-B02, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-003**: Lecture 3: equilibrium of a single particle - forces as vectors and their addition; examples (gravity, string tension, normal reaction with Newton's third law, friction); conditions for equilibrium.  
  <sub>MC-B03, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-004**: Lecture 4: equilibrium of a rigid body: combining forces, couples and moments, and the conditions for equilibrium.  
  <sub>MC-B04, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-005**: Lecture 5: particle dynamics through Newton's second law, with pulleys and slopes as examples.  
  <sub>MC-B05, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-006**: Lecture 6: more particle dynamics, for instance a projectile subject to air resistance.  
  <sub>MC-B06, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-007**: Lecture 7: work and energy - kinetic energy, gravitational potential energy in a uniform field, and conservation of energy.  
  <sub>MC-B07, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-008**: Lecture 8: momentum - momentum as a vector and its conservation, collisions, coefficient of restitution, impulse.  
  <sub>MC-B08, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-009**: Lecture 9: springs, strings and simple harmonic motion - Hooke's law, oscillations of a particle on a spring or hanging on a string, SHM for small displacements.  
  <sub>MC-B09, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>
- **IA-MC-010**: Lecture 10: motion in a circle - the central acceleration for circular motion, the simple pendulum, and a particle sliding on a cylinder.  
  <sub>MC-B10, item 1 of 1; Schedules printed p.12. Lectures [1].</sub>

## Ancillary: Computational Projects

8 lectures in the Easter Term of Part IA; examined in Part IB.



### Introductory lectures

Reading map: RM-CP-01

- **IA-CP-001**: Introductory lectures in the Easter Term of Part IA on algorithms and aspects of the Matlab language. The course itself is examined in Part IB.  
  <sub>CP-B01, item 1 of 2; Schedules printed p.12. Lectures [8].</sub>

### Projects and manual

Reading map: RM-CP-02

- **IA-CP-002**: The Faculty publishes a projects manual around the end of July or start of August after Part IA. Full credit needs two core projects and two further projects, which may be done once the manual is out and are submitted by deadlines early in the Lent Term (core) and Easter Term (additional) of Part IB. The manual lists suitable books.  
  <sub>CP-B01, item 2 of 2; Schedules printed p.12.</sub>

