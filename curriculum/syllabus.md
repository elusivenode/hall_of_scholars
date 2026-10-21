# Part IA syllabus (human-readable view of the register)

This page is a readable rendering of [coverage.yaml](coverage.yaml), which is the authoritative register. If the two disagree, the YAML is right and this page is stale.

**Source:** *Schedules of Lecture Courses and Form of Examinations for the Mathematical Tripos 2026-27*, revised 19 August 2026, Part IA (printed pp.8 to 12). Syllabus statements are quoted as extracted from the PDF text; see [references/source-register.md](../references/source-register.md) for the normalisation applied and for the open question on redistribution of this text. Superscripts and subscripts are flattened by text extraction (`R3` is R^3, `Sn` is S_n, `∇2` is ∇^2); check the PDF when the distinction matters.

**Reading the entries.** `Lectures [n]` is the number the Schedules give for the whole source paragraph, shared by every item from that paragraph. *Starred* means the Schedules put the topic between asterisks: the lecturer must cover it but examiners cannot set questions on it. `needs:` lists prerequisite items (**[C]** stated by Cambridge, **[J]** the librarian's judgement, for the director to confirm).

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

- **IA-NS-N01** (course note): [Note that this course is omitted from Option (b) of Part IA.]


### Introduction to number systems and logic

Reading map: RM-NS-01

- **IA-NS-001**: Overview of the natural numbers, integers, real numbers, rational and irrational numbers, algebraic and transcendental numbers. Brief discussion of complex numbers; statement of the Fundamental Theorem of Algebra.  
  <sub>NS-B01. Lectures [2].</sub>
- **IA-NS-002**: Ideas of axiomatic systems and proof within mathematics; the need for proof; the role of counter-examples in mathematics. Elementary logic; implication and negation; examples of negation of compound statements. Proof by contradiction.  
  <sub>NS-B01. Lectures [2].</sub>

### Sets, relations and functions

Reading map: RM-NS-02

- **IA-NS-003**: Union, intersection and equality of sets.  
  <sub>NS-B02. Lectures [4]. needs[J]: IA-NS-002.</sub>
- **IA-NS-004**: Indicator (characteristic) functions; their use in establishing set identities.  
  <sub>NS-B02. Lectures [4]. needs[J]: IA-NS-003.</sub>
- **IA-NS-005**: Functions; injections, surjections and bijections.  
  <sub>NS-B02. Lectures [4]. needs[J]: IA-NS-003.</sub>
- **IA-NS-006**: Relations, and equivalence relations.  
  <sub>NS-B02. Lectures [4]. needs[J]: IA-NS-003.</sub>
- **IA-NS-007**: Counting the combinations or permutations of a set. The Inclusion-Exclusion Principle.  
  <sub>NS-B02. Lectures [4]. needs[J]: IA-NS-005.</sub>

### The integers

Reading map: RM-NS-03

- **IA-NS-008**: The natural numbers: mathematical induction and the well-ordering principle. Examples, including the Binomial Theorem.  
  <sub>NS-B03. Lectures [2]. needs[J]: IA-NS-002, IA-NS-003.</sub>

### Elementary number theory

Reading map: RM-NS-04

- **IA-NS-009**: Prime numbers: existence and uniqueness of prime factorisation into primes; highest common factors and least common multiples.  
  <sub>NS-B04. Lectures [8]. needs[J]: IA-NS-008.</sub>
- **IA-NS-010**: Euclid's proof of the infinity of primes.  
  <sub>NS-B04. Lectures [8]. needs[J]: IA-NS-009.</sub>
- **IA-NS-011**: Euclid's algorithm. Solution in integers of ax+by = c.  
  <sub>NS-B04. Lectures [8]. needs[J]: IA-NS-009.</sub>
- **IA-NS-012**: Modular arithmetic (congruences). Units modulo n.  
  <sub>NS-B04. Lectures [8]. needs[J]: IA-NS-011, IA-NS-006.</sub>
- **IA-NS-013**: Chinese Remainder Theorem. Wilson's Theorem; the Fermat-Euler Theorem.  
  <sub>NS-B04. Lectures [8]. needs[J]: IA-NS-012.</sub>
- **IA-NS-014**: Public key cryptography and the RSA algorithm.  
  <sub>NS-B04. Lectures [8]. needs[J]: IA-NS-013.</sub>

### The real numbers

Reading map: RM-NS-05

- **IA-NS-015**: Least upper bounds; simple examples. Least upper bound axiom.  
  <sub>NS-B05. Lectures [4]. needs[J]: IA-NS-001, IA-NS-003.</sub>
- **IA-NS-016**: Sequences and series; convergence of bounded monotonic sequences.  
  <sub>NS-B05. Lectures [4]. needs[J]: IA-NS-015.</sub>
- **IA-NS-017**: Irrationality of √2 and e. Decimal expansions.  
  <sub>NS-B05. Lectures [4]. needs[J]: IA-NS-009, IA-NS-016.</sub>
- **IA-NS-018**: Construction of a transcendental number.  
  <sub>NS-B05. Lectures [4]. needs[J]: IA-NS-017.</sub>

### Countability and uncountability

Reading map: RM-NS-06

- **IA-NS-019**: Definitions of finite, infinite, countable and uncountable sets.  
  <sub>NS-B06. Lectures [4]. needs[J]: IA-NS-005.</sub>
- **IA-NS-020**: A countable union of countable sets is countable.  
  <sub>NS-B06. Lectures [4]. needs[J]: IA-NS-019.</sub>
- **IA-NS-021**: Uncountability of R. Non-existence of a bijection from a set to its power set.  
  <sub>NS-B06. Lectures [4]. needs[J]: IA-NS-019, IA-NS-017.</sub>
- **IA-NS-022**: Indirect proof of existence of transcendental numbers.  
  <sub>NS-B06. Lectures [4]. needs[J]: IA-NS-020, IA-NS-021, IA-NS-001.</sub>

## Groups

24 lectures, Michaelmas Term. Examined on Paper 3.



### Examples of groups

Reading map: RM-GP-01

- **IA-GP-001**: Axioms for groups. Examples from geometry: symmetry groups of regular polygons, cube, tetrahedron.  
  <sub>GP-B01. Lectures [4].</sub>
- **IA-GP-002**: Permutations on a set; the symmetric group. Subgroups and homomorphisms. Symmetry groups as subgroups of general permutation groups.  
  <sub>GP-B01. Lectures [4]. needs[J]: IA-GP-001.</sub>
- **IA-GP-003**: The Möbius group; cross-ratios, preservation of circles, the point at infinity. Conjugation. Fixed points of Möbius maps and iteration.  
  <sub>GP-B01. Lectures [4]. needs[J]: IA-GP-002, IA-VM-001.</sub>

### Lagrange's theorem

Reading map: RM-GP-02

- **IA-GP-004**: Cosets. Lagrange's theorem.  
  <sub>GP-B02. Lectures [5]. needs[J]: IA-GP-002, IA-NS-006.</sub>
- **IA-GP-005**: Groups of small order (up to order 8). Quaternions.  
  <sub>GP-B02. Lectures [5]. needs[J]: IA-GP-004.</sub>
- **IA-GP-006**: Fermat-Euler theorem from the group-theoretic point of view.  
  <sub>GP-B02. Lectures [5]. needs[J]: IA-GP-004, IA-NS-012.</sub>

### Group actions

Reading map: RM-GP-03

- **IA-GP-007**: Group actions; orbits and stabilizers. Orbit-stabilizer theorem.  
  <sub>GP-B03. Lectures [4]. needs[J]: IA-GP-002, IA-GP-004.</sub>
- **IA-GP-008**: Cayley's theorem (every group is isomorphic to a subgroup of a permutation group).  
  <sub>GP-B03. Lectures [4]. needs[J]: IA-GP-007.</sub>
- **IA-GP-009**: Conjugacy classes. Cauchy's theorem.  
  <sub>GP-B03. Lectures [4]. needs[J]: IA-GP-007.</sub>

### Quotient groups

Reading map: RM-GP-04

- **IA-GP-010**: Normal subgroups, quotient groups and the isomorphism theorem.  
  <sub>GP-B04. Lectures [4]. needs[J]: IA-GP-004, IA-GP-002.</sub>

### Matrix groups

Reading map: RM-GP-05

- **IA-GP-011**: The general and special linear groups; relation with the Möbius group.  
  <sub>GP-B05. Lectures [3]. needs[J]: IA-GP-001, IA-VM-009.</sub>
- **IA-GP-012**: The orthogonal and special orthogonal groups. Proof (in R3) that every element of the orthogonal group is the product of reflections and every rotation in R3 has an axis.  
  <sub>GP-B05. Lectures [3]. needs[J]: IA-GP-011, IA-VM-012.</sub>
- **IA-GP-013**: Basis change as an example of conjugation.  
  <sub>GP-B05. Lectures [3]. needs[J]: IA-GP-003, IA-VM-015.</sub>

### Permutations

Reading map: RM-GP-06

- **IA-GP-014**: Permutations, cycles and transpositions. The sign of a permutation.  
  <sub>GP-B06. Lectures [4]. needs[J]: IA-GP-002.</sub>
- **IA-GP-015**: Conjugacy in Sn and in An.  
  <sub>GP-B06. Lectures [4]. needs[J]: IA-GP-014, IA-GP-009.</sub>
- **IA-GP-016**: Simple groups; simplicity of A5.  
  <sub>GP-B06. Lectures [4]. needs[J]: IA-GP-010, IA-GP-015.</sub>

## Vectors and Matrices

24 lectures, Michaelmas Term. Examined on Paper 1.



### Complex numbers

Reading map: RM-VM-01

- **IA-VM-001**: Review of complex numbers, including complex conjugate, inverse, modulus, argument and Argand diagram.  
  <sub>VM-B01. Lectures [2].</sub>
- **IA-VM-002**: Informal treatment of complex logarithm, n-th roots and complex powers. de Moivre's theorem.  
  <sub>VM-B01. Lectures [2]. needs[J]: IA-VM-001.</sub>

### Vectors

Reading map: RM-VM-02

- **IA-VM-003**: Review of elementary algebra of vectors in R3, including scalar product.  
  <sub>VM-B02. Lectures [5].</sub>
- **IA-VM-004**: Brief discussion of vectors in Rn and Cn; scalar product and the Cauchy–Schwarz inequality.  
  <sub>VM-B02. Lectures [5]. needs[J]: IA-VM-003, IA-VM-001.</sub>
- **IA-VM-005**: Concepts of linear span, linear independence, subspaces, basis and dimension.  
  <sub>VM-B02. Lectures [5]. needs[J]: IA-VM-004.</sub>
- **IA-VM-006**: Suffix notation: including summation convention, δij and ϵijk .  
  <sub>VM-B02. Lectures [5]. needs[J]: IA-VM-003.</sub>
- **IA-VM-007**: Vector product and triple product: definition and geometrical interpretation. Solution of linear vector equations.  
  <sub>VM-B02. Lectures [5]. needs[J]: IA-VM-006.</sub>
- **IA-VM-008**: Applications of vectors to geometry, including equations of lines, planes and spheres.  
  <sub>VM-B02. Lectures [5]. needs[J]: IA-VM-007.</sub>

### Matrices

Reading map: RM-VM-03

- **IA-VM-009**: Elementary algebra of 3 × 3 matrices, including determinants. Extension to n × n complex matrices. Trace, determinant, non-singular matrices and inverses.  
  <sub>VM-B03. Lectures [4].</sub>
- **IA-VM-010**: Matrices as linear transformations; examples of geometrical actions including rotations, reflections, dilations, shears; kernel and image, rank–nullity theorem (statement only).  
  <sub>VM-B03. Lectures [4]. needs[J]: IA-VM-009, IA-VM-005.</sub>
- **IA-VM-011**: Simultaneous linear equations: matrix formulation; existence and uniqueness of solutions, geometric interpretation; Gaussian elimination.  
  <sub>VM-B04. Lectures [3]. needs[J]: IA-VM-009, IA-VM-010.</sub>
- **IA-VM-012**: Symmetric, anti-symmetric, orthogonal, hermitian and unitary matrices. Decomposition of a general matrix into isotropic, symmetric trace-free and antisymmetric parts.  
  <sub>VM-B05. Lectures [1]. needs[J]: IA-VM-009.</sub>

### Eigenvalues and Eigenvectors

Reading map: RM-VM-04

- **IA-VM-013**: Eigenvalues and eigenvectors; geometric significance.  
  <sub>VM-B06. Lectures [2]. needs[J]: IA-VM-010, IA-VM-011.</sub>
- **IA-VM-014**: Proof that eigenvalues of hermitian matrix are real, and that distinct eigenvalues give an orthogonal basis of eigenvectors.  
  <sub>VM-B07. Lectures [5]. needs[J]: IA-VM-013, IA-VM-012, IA-VM-004.</sub>
- **IA-VM-015**: The effect of a general change of basis (similarity transformations).  
  <sub>VM-B07. Lectures [5]. needs[J]: IA-VM-013, IA-VM-005.</sub>
- **IA-VM-016**: Diagonalization of general matrices: sufficient conditions; examples of matrices that cannot be diagonalized. Canonical forms for 2 × 2 matrices.  
  <sub>VM-B07. Lectures [5]. needs[J]: IA-VM-015.</sub>
- **IA-VM-017**: Discussion of quadratic forms, including change of basis. Classification of conics, cartesian and polar forms.  
  <sub>VM-B08. Lectures [1]. needs[J]: IA-VM-014, IA-VM-015.</sub>
- **IA-VM-018**: Rotation matrices and Lorentz transformations as transformation groups.  
  <sub>VM-B09. Lectures [1]. needs[J]: IA-VM-010, IA-VM-012, IA-GP-001.</sub>

## Differential Equations

24 lectures, Michaelmas Term. Examined on Paper 2.



### Basic calculus

Reading map: RM-DE-01

- **IA-DE-001**: Informal treatment of differentiation as a limit, the chain rule, Leibnitz's rule, Taylor series, informal treatment of O and o notation and l'Hôpital's rule; integration as an area, fundamental theorem of calculus, integration by substitution and parts.  
  <sub>DE-B01. Lectures [3].</sub>
- **IA-DE-002**: Informal treatment of partial derivatives, geometrical interpretation, statement (only) of symmetry of mixed partial derivatives, chain rule, implicit differentiation.  
  <sub>DE-B02. Lectures [2]. needs[J]: IA-DE-001.</sub>
- **IA-DE-003**: Informal treatment of differentials, including exact differentials.  
  <sub>DE-B02. Lectures [2]. needs[J]: IA-DE-002.</sub>
- **IA-DE-004**: Differentiation of an integral with respect to a parameter.  
  <sub>DE-B02. Lectures [2]. needs[J]: IA-DE-002.</sub>

### First-order linear differential equations

Reading map: RM-DE-02

- **IA-DE-005**: Equations with constant coefficients: exponential growth, comparison with discrete equations, series solution; modelling examples including radioactive decay.  
  <sub>DE-B03. Lectures [2]. needs[J]: IA-DE-001.</sub>
- **IA-DE-006**: Equations with non-constant coefficients: solution by integrating factor.  
  <sub>DE-B03. Lectures [2]. needs[J]: IA-DE-005.</sub>

### Nonlinear first-order equations

Reading map: RM-DE-03

- **IA-DE-007**: Separable equations. Exact equations.  
  <sub>DE-B04. Lectures [4]. needs[J]: IA-DE-006.</sub>
- **IA-DE-008**: Sketching solution trajectories. Equilibrium solutions, stability by perturbation; examples, including logistic equation and chemical kinetics.  
  <sub>DE-B04. Lectures [4]. needs[J]: IA-DE-007.</sub>
- **IA-DE-009**: Discrete equations: equilibrium solutions, stability; examples including the logistic map.  
  <sub>DE-B04. Lectures [4]. needs[J]: IA-DE-005, IA-DE-008.</sub>

### Higher-order linear differential equations

Reading map: RM-DE-04

- **IA-DE-010**: Complementary function and particular integral, linear independence, Wronskian (for second-order equations), Abel's theorem.  
  <sub>DE-B05. Lectures [8]. needs[J]: IA-DE-005, IA-VM-005.</sub>
- **IA-DE-011**: Equations with constant coefficients and examples including radioactive sequences, comparison in simple cases with difference equations, reduction of order, resonance, transients, damping.  
  <sub>DE-B05. Lectures [8]. needs[J]: IA-DE-010, IA-VM-001.</sub>
- **IA-DE-012**: Homogeneous equations.  
  <sub>DE-B05. Lectures [8]. needs[J]: IA-DE-011.</sub>
- **IA-DE-013**: Response to step and impulse function inputs; introduction to the notions of the Heaviside step-function and the Dirac delta-function.  
  <sub>DE-B05. Lectures [8]. needs[J]: IA-DE-011.</sub>
- **IA-DE-014**: Series solutions including statement only of the need for the logarithmic solution.  
  <sub>DE-B05. Lectures [8]. needs[J]: IA-DE-010.</sub>

### Multivariate functions: applications

Reading map: RM-DE-05

- **IA-DE-015**: Directional derivatives and the gradient vector.  
  <sub>DE-B06. Lectures [5]. needs[J]: IA-DE-002.</sub>
- **IA-DE-016**: Statement of Taylor series for functions on Rn.  
  <sub>DE-B06. Lectures [5]. needs[J]: IA-DE-002, IA-DE-001.</sub>
- **IA-DE-017**: Local extrema of real functions, classification using the Hessian matrix.  
  <sub>DE-B06. Lectures [5]. needs[J]: IA-DE-016, IA-VM-014.</sub>
- **IA-DE-018**: Coupled first order systems: equivalence to single higher order equations; solution by matrix methods.  
  <sub>DE-B06. Lectures [5]. needs[J]: IA-DE-011, IA-VM-016.</sub>
- **IA-DE-019**: Non-degenerate phase portraits local to equilibrium points; stability.  
  <sub>DE-B06. Lectures [5]. needs[J]: IA-DE-018, IA-DE-008.</sub>
- **IA-DE-020**: Simple examples of first- and second-order partial differential equations, solution of the wave equation in the form f (x + ct) + g(x − ct).  
  <sub>DE-B06. Lectures [5]. needs[J]: IA-DE-002.</sub>

## Analysis I

24 lectures, Lent Term. Examined on Paper 1.



### Limits and convergence

Reading map: RM-AN-01

- **IA-AN-001**: Sequences and series in R and C. Sums, products and quotients. Absolute convergence; absolute convergence implies convergence.  
  <sub>AN-B01. Lectures [6]. needs[J]: IA-NS-016, IA-NS-015, IA-VM-001.</sub>
- **IA-AN-002**: The Bolzano-Weierstrass theorem and applications (the General Principle of Convergence).  
  <sub>AN-B01. Lectures [6]. needs[J]: IA-AN-001, IA-NS-015.</sub>
- **IA-AN-003**: Comparison and ratio tests, alternating series test.  
  <sub>AN-B01. Lectures [6]. needs[J]: IA-AN-001.</sub>

### Continuity

Reading map: RM-AN-02

- **IA-AN-004**: Continuity of real- and complex-valued functions defined on subsets of R and C.  
  <sub>AN-B02. Lectures [3]. needs[J]: IA-AN-001.</sub>
- **IA-AN-005**: The intermediate value theorem.  
  <sub>AN-B02. Lectures [3]. needs[J]: IA-AN-004, IA-AN-002.</sub>
- **IA-AN-006**: A continuous function on a closed bounded interval is bounded and attains its bounds.  
  <sub>AN-B02. Lectures [3]. needs[J]: IA-AN-004, IA-AN-002.</sub>

### Differentiability

Reading map: RM-AN-03

- **IA-AN-007**: Differentiability of functions from R to R.  
  <sub>AN-B03. Lectures [5]. needs[J]: IA-AN-004, IA-DE-001.</sub>
- **IA-AN-008**: Derivative of sums and products. The chain rule. Derivative of the inverse function.  
  <sub>AN-B03. Lectures [5]. needs[J]: IA-AN-007.</sub>
- **IA-AN-009**: Rolle's theorem; the mean value theorem.  
  <sub>AN-B03. Lectures [5]. needs[J]: IA-AN-008, IA-AN-006.</sub>
- **IA-AN-010**: One-dimensional version of the inverse function theorem.  
  <sub>AN-B03. Lectures [5]. needs[J]: IA-AN-009, IA-AN-005.</sub>
- **IA-AN-011**: Taylor's theorem from R to R; Lagrange's form of the remainder.  
  <sub>AN-B03. Lectures [5]. needs[J]: IA-AN-009.</sub>
- **IA-AN-012**: Complex differentiation.  
  <sub>AN-B03. Lectures [5]. needs[J]: IA-AN-007, IA-VM-001.</sub>

### Power series

Reading map: RM-AN-04

- **IA-AN-013**: Complex power series and radius of convergence.  
  <sub>AN-B04. Lectures [4]. needs[J]: IA-AN-003.</sub>
- **IA-AN-014**: Exponential, trigonometric and hyperbolic functions, and relations between them.  
  <sub>AN-B04. Lectures [4]. needs[J]: IA-AN-013, IA-VM-002.</sub>
- **IA-AN-015** (*starred*): *Direct proof of the differentiability of a power series within its circle of convergence*.  
  <sub>AN-B04. Lectures [4]. needs[J]: IA-AN-013, IA-AN-008.</sub>

### Integration

Reading map: RM-AN-05

- **IA-AN-016**: Definition and basic properties of the Riemann integral.  
  <sub>AN-B05. Lectures [6]. needs[J]: IA-NS-015, IA-AN-006.</sub>
- **IA-AN-017**: A non-integrable function. Integrability of monotonic functions. Integrability of piecewise-continuous functions.  
  <sub>AN-B05. Lectures [6]. needs[J]: IA-AN-016.</sub>
- **IA-AN-018**: The fundamental theorem of calculus. Differentiation of indefinite integrals.  
  <sub>AN-B05. Lectures [6]. needs[J]: IA-AN-016, IA-AN-009.</sub>
- **IA-AN-019**: Integration by parts. The integral form of the remainder in Taylor's theorem.  
  <sub>AN-B05. Lectures [6]. needs[J]: IA-AN-018, IA-AN-011.</sub>
- **IA-AN-020**: Improper integrals.  
  <sub>AN-B05. Lectures [6]. needs[J]: IA-AN-016, IA-AN-001.</sub>

## Probability

24 lectures, Lent Term. Examined on Paper 2.



### Basic concepts

Reading map: RM-PR-01

- **IA-PR-001**: Classical probability, equally likely outcomes.  
  <sub>PR-B01. Lectures [3]. needs[C]: IA-NS-007.</sub>
- **IA-PR-002**: Combinatorial analysis, permutations and combinations.  
  <sub>PR-B01. Lectures [3]. needs[C]: IA-NS-007.</sub>
- **IA-PR-003**: Stirling's formula (asymptotics for log n! proved).  
  <sub>PR-B01. Lectures [3]. needs[J]: IA-PR-002, IA-AN-001.</sub>

### Axiomatic approach

Reading map: RM-PR-02

- **IA-PR-004**: Axioms (countable case). Probability spaces.  
  <sub>PR-B02. Lectures [5]. needs[J]: IA-PR-001, IA-NS-003.</sub>
- **IA-PR-005**: Inclusion-exclusion formula. Continuity and subadditivity of probability measures.  
  <sub>PR-B02. Lectures [5]. needs[J]: IA-PR-004, IA-NS-007.</sub>
- **IA-PR-006**: Independence.  
  <sub>PR-B02. Lectures [5]. needs[J]: IA-PR-004.</sub>
- **IA-PR-007**: Binomial, Poisson and geometric distributions. Relation between Poisson and binomial distributions.  
  <sub>PR-B02. Lectures [5]. needs[J]: IA-PR-006, IA-PR-002.</sub>
- **IA-PR-008**: Conditional probability, Bayes's formula. Examples, including Simpson's paradox.  
  <sub>PR-B02. Lectures [5]. needs[J]: IA-PR-004.</sub>

### Discrete random variables

Reading map: RM-PR-03

- **IA-PR-009**: Expectation.  
  <sub>PR-B03. Lectures [7]. needs[J]: IA-PR-007.</sub>
- **IA-PR-010**: Functions of a random variable, indicator function, variance, standard deviation.  
  <sub>PR-B03. Lectures [7]. needs[J]: IA-PR-009.</sub>
- **IA-PR-011**: Covariance, independence of random variables.  
  <sub>PR-B03. Lectures [7]. needs[J]: IA-PR-010, IA-PR-006.</sub>
- **IA-PR-012**: Generating functions: sums of independent random variables, random sum formula, moments.  
  <sub>PR-B03. Lectures [7]. needs[J]: IA-PR-011, IA-AN-013.</sub>
- **IA-PR-013**: Conditional expectation.  
  <sub>PR-B03. Lectures [7]. needs[J]: IA-PR-009, IA-PR-008.</sub>
- **IA-PR-014**: Random walks: gambler's ruin, recurrence relations. Difference equations and their solution. Mean time to absorption.  
  <sub>PR-B03. Lectures [7]. needs[C]: IA-PR-013, IA-DE-011.</sub>
- **IA-PR-015**: Branching processes: generating functions and extinction probability.  
  <sub>PR-B03. Lectures [7]. needs[J]: IA-PR-012, IA-PR-013.</sub>
- **IA-PR-016**: Combinatorial applications of generating functions.  
  <sub>PR-B03. Lectures [7]. needs[J]: IA-PR-012.</sub>

### Continuous random variables

Reading map: RM-PR-04

- **IA-PR-017**: Distributions and density functions. Expectations; expectation of a function of a random variable.  
  <sub>PR-B04. Lectures [6]. needs[C]: IA-PR-009, IA-DE-001, IA-AN-020.</sub>
- **IA-PR-018**: Uniform, normal and exponential random variables. Memoryless property of exponential distribution.  
  <sub>PR-B04. Lectures [6]. needs[J]: IA-PR-017.</sub>
- **IA-PR-019**: Joint distributions: transformation of random variables (including Jacobians), examples.  
  <sub>PR-B04. Lectures [6]. needs[C]: IA-PR-017, IA-DE-002, IA-VC-002.</sub>
- **IA-PR-020**: Simulation: generating continuous random variables, Box–Muller transform, rejection sampling.  
  <sub>PR-B04. Lectures [6]. needs[J]: IA-PR-018, IA-PR-019.</sub>
- **IA-PR-021**: Geometrical probability: Bertrand's paradox, Buffon's needle.  
  <sub>PR-B04. Lectures [6]. needs[J]: IA-PR-017.</sub>
- **IA-PR-022**: Correlation coefficient, bivariate normal random variables.  
  <sub>PR-B04. Lectures [6]. needs[J]: IA-PR-019, IA-PR-011.</sub>

### Inequalities and limits

Reading map: RM-PR-05

- **IA-PR-023**: Markov's inequality, Chebyshev's inequality.  
  <sub>PR-B05. Lectures [3]. needs[J]: IA-PR-009, IA-PR-010.</sub>
- **IA-PR-024**: Weak law of large numbers.  
  <sub>PR-B05. Lectures [3]. needs[J]: IA-PR-023, IA-PR-011.</sub>
- **IA-PR-025**: Convexity: Jensen's inequality for general random variables, AM/GM inequality.  
  <sub>PR-B05. Lectures [3]. needs[J]: IA-PR-009.</sub>
- **IA-PR-026**: Moment generating functions and statement (no proof) of continuity theorem.  
  <sub>PR-B05. Lectures [3]. needs[J]: IA-PR-012, IA-PR-017.</sub>
- **IA-PR-027**: Statement of central limit theorem and sketch of proof. Examples, including sampling.  
  <sub>PR-B05. Lectures [3]. needs[J]: IA-PR-026, IA-PR-018, IA-PR-024.</sub>

## Vector Calculus

24 lectures, Lent Term. Examined on Paper 3.



### Curves in R3

Reading map: RM-VC-01

- **IA-VC-001**: Parameterised curves and arc length, tangents and normals to curves in R3; curvature and torsion.  
  <sub>VC-B01. Lectures [1]. needs[J]: IA-DE-001, IA-VM-007.</sub>

### Integration in R2 and R3

Reading map: RM-VC-02

- **IA-VC-002**: Line integrals.  
  <sub>VC-B02. Lectures [4]. needs[J]: IA-VC-001, IA-DE-002.</sub>
- **IA-VC-003**: Surface and volume integrals: definitions, examples using Cartesian, cylindrical and spherical coordinates; change of variables.  
  <sub>VC-B02. Lectures [4]. needs[J]: IA-VC-002, IA-VM-007.</sub>

### Vector operators

Reading map: RM-VC-03

- **IA-VC-004**: Directional derivatives. The gradient of a real-valued function: definition; interpretation as normal to level surfaces; examples including the use of cylindrical, spherical ∗and general orthogonal curvilinear ∗ coordinates.  
  <sub>VC-B03. Lectures [5]. needs[J]: IA-DE-015, IA-VM-006.</sub>
- **IA-VC-005**: Divergence, curl and ∇2 in Cartesian coordinates, examples; formulae for these operators (statement only) in cylindrical, spherical ∗and general orthogonal curvilinear ∗ coordinates.  
  <sub>VC-B03. Lectures [5]. needs[J]: IA-VC-004, IA-VM-006.</sub>
- **IA-VC-006**: Solenoidal fields, irrotational fields and conservative fields; scalar potentials.  
  <sub>VC-B03. Lectures [5]. needs[J]: IA-VC-005.</sub>
- **IA-VC-007**: Vector derivative identities.  
  <sub>VC-B03. Lectures [5]. needs[J]: IA-VC-005, IA-VM-006.</sub>

### Integration theorems

Reading map: RM-VC-04

- **IA-VC-008**: Divergence theorem, Green's theorem, Stokes's theorem, Green's second theorem: statements; informal proofs; examples; application to fluid dynamics, and to electromagnetism including statement of Maxwell's equations.  
  <sub>VC-B04. Lectures [5]. needs[J]: IA-VC-003, IA-VC-005.</sub>

### Laplace's equation

Reading map: RM-VC-05

- **IA-VC-009**: Laplace's equation in R2 and R3: uniqueness theorem and maximum principle.  
  <sub>VC-B05. Lectures [4]. needs[J]: IA-VC-008, IA-VC-005.</sub>
- **IA-VC-010**: Solution of Poisson's equation by Gauss's method (for spherical and cylindrical symmetry) and as an integral.  
  <sub>VC-B05. Lectures [4]. needs[J]: IA-VC-009, IA-VC-008.</sub>

### Cartesian tensors in R3

Reading map: RM-VC-06

- **IA-VC-011**: Tensor transformation laws, addition, multiplication, contraction, with emphasis on tensors of second rank.  
  <sub>VC-B06. Lectures [5]. needs[J]: IA-VM-006, IA-VM-018.</sub>
- **IA-VC-012**: Isotropic second and third rank tensors.  
  <sub>VC-B06. Lectures [5]. needs[J]: IA-VC-011.</sub>
- **IA-VC-013**: Symmetric and antisymmetric tensors. Revision of principal axes and diagonalization.  
  <sub>VC-B06. Lectures [5]. needs[J]: IA-VC-011, IA-VM-014.</sub>
- **IA-VC-014**: Quotient theorem. Examples including inertia and conductivity.  
  <sub>VC-B06. Lectures [5]. needs[J]: IA-VC-011.</sub>

## Dynamics and Relativity

24 lectures, Lent Term. Examined on Paper 4.

- **IA-DR-N01** (course note): [Note that this course is omitted from Option (b) of Part IA.]
- **IA-DR-N02** (course note): Familiarity with the topics covered in the non-examinable Mechanics course is assumed.


### Basic concepts

Reading map: RM-DR-01

- **IA-DR-001**: Space and time, frames of reference, Galilean transformations.  
  <sub>DR-B01. Lectures [4]. needs[C]: IA-MC-002.</sub>
- **IA-DR-002**: Newton's laws.  
  <sub>DR-B01. Lectures [4]. needs[C]: IA-MC-005.</sub>
- **IA-DR-003**: Dimensional analysis.  
  <sub>DR-B01. Lectures [4].</sub>
- **IA-DR-004**: Examples of forces, including gravity, friction and Lorentz.  
  <sub>DR-B01. Lectures [4]. needs[C]: IA-MC-003.</sub>

### Newtonian dynamics of a single particle

Reading map: RM-DR-02

- **IA-DR-005**: Equation of motion in Cartesian and plane polar coordinates.  
  <sub>DR-B02. Lectures [8]. needs[C]: IA-DR-002, IA-DE-011, IA-VM-006.</sub>
- **IA-DR-006**: Work, conservative forces and potential energy, motion and the shape of the potential energy function; stable equilibria and small oscillations; effect of damping.  
  <sub>DR-B02. Lectures [8]. needs[J]: IA-DR-005, IA-MC-007, IA-VC-004.</sub>
- **IA-DR-007**: Angular velocity, angular momentum, torque.  
  <sub>DR-B02. Lectures [8]. needs[J]: IA-VM-007, IA-MC-004.</sub>
- **IA-DR-008**: Orbits: the u(θ) equation; escape velocity; Kepler's laws; stability of orbits; motion in a repulsive potential (Rutherford scattering).  
  <sub>DR-B02. Lectures [8]. needs[J]: IA-DR-007, IA-DR-006, IA-DE-011.</sub>
- **IA-DR-009**: Rotating frames: centrifugal and Coriolis forces.  
  <sub>DR-B02. Lectures [8]. needs[J]: IA-DR-007, IA-VM-007.</sub>
- **IA-DR-010** (*starred*): *Brief discussion of Foucault pendulum.*  
  <sub>DR-B02. Lectures [8]. needs[J]: IA-DR-009.</sub>

### Newtonian dynamics of systems of particles

Reading map: RM-DR-03

- **IA-DR-011**: Momentum, angular momentum, energy.  
  <sub>DR-B03. Lectures [2]. needs[J]: IA-DR-007, IA-MC-008.</sub>
- **IA-DR-012**: Motion relative to the centre of mass; the two body problem.  
  <sub>DR-B03. Lectures [2]. needs[J]: IA-DR-011.</sub>
- **IA-DR-013**: Variable mass problems; the rocket equation.  
  <sub>DR-B03. Lectures [2]. needs[J]: IA-DR-011.</sub>

### Rigid bodies

Reading map: RM-DR-04

- **IA-DR-014**: Moments of inertia, angular momentum and energy of a rigid body.  
  <sub>DR-B04. Lectures [3]. needs[J]: IA-DR-011.</sub>
- **IA-DR-015**: Parallel axis theorem.  
  <sub>DR-B04. Lectures [3]. needs[J]: IA-DR-014.</sub>
- **IA-DR-016**: Simple examples of motion involving both rotation and translation (e.g. rolling).  
  <sub>DR-B04. Lectures [3]. needs[J]: IA-DR-015, IA-DR-014.</sub>

### Special relativity

Reading map: RM-DR-05

- **IA-DR-017**: The principle of relativity. Relativity and simultaneity.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-001.</sub>
- **IA-DR-018**: The invariant interval.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-017.</sub>
- **IA-DR-019**: Lorentz transformations in (1 + 1)-dimensional spacetime. Time dilation and length contraction.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-018, IA-VM-018.</sub>
- **IA-DR-020**: The Minkowski metric for (1 + 1)-dimensional spacetime.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-019.</sub>
- **IA-DR-021**: Lorentz transformations in (3 + 1) dimensions.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-019, IA-VM-018.</sub>
- **IA-DR-022**: 4–vectors and Lorentz invariants. Proper time.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-021, IA-VM-006.</sub>
- **IA-DR-023**: 4–velocity and 4–momentum.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-022.</sub>
- **IA-DR-024**: Conservation of 4–momentum in particle decay. Collisions. The Newtonian limit.  
  <sub>DR-B05. Lectures [7]. needs[J]: IA-DR-023, IA-DR-011.</sub>

## Ancillary: Mechanics (non-examinable)

10 lectures, Michaelmas Term. The Schedules state this material is prerequisite for Dynamics and Relativity.

- **IA-MC-N01** (course note): This course is intended for students who have taken only a limited amount of Mechanics at A-level (or the equivalent). The material is prerequisite for Dynamics and Relativity in the Lent Term.


### Lectures

Reading map: RM-MC-01

- **IA-MC-001**: Lecture 1 Brief introduction  
  <sub>MC-B01. Lectures [1].</sub>
- **IA-MC-002**: Lecture 2: Kinematics of a single particle Position, velocity, speed, acceleration. Constant acceleration in one-dimension. Projectile motion in two-dimensions.  
  <sub>MC-B02. Lectures [1].</sub>
- **IA-MC-003**: Lecture 3: Equilibrium of a single particle The vector nature of forces, addition of forces, examples including gravity, tension in a string, normal reaction (Newton's third law), friction. Conditions for equilibrium.  
  <sub>MC-B03. Lectures [1].</sub>
- **IA-MC-004**: Lecture 4: Equilibrium of a rigid body Resultant of several forces, couple, moment of a force. Conditions for equilibrium.  
  <sub>MC-B04. Lectures [1].</sub>
- **IA-MC-005**: Lecture 5: Dynamics of particles Newton's second law. Examples of pulleys, motion on an inclined plane.  
  <sub>MC-B05. Lectures [1].</sub>
- **IA-MC-006**: Lecture 6: Dynamics of particles Further examples, including motion of a projectile with air-resistance.  
  <sub>MC-B06. Lectures [1].</sub>
- **IA-MC-007**: Lecture 7: Energy Definition of energy and work. Kinetic energy, potential energy of a particle in a uniform gravitational field. Conservation of energy.  
  <sub>MC-B07. Lectures [1].</sub>
- **IA-MC-008**: Lecture 8: Momentum Definition of momentum (as a vector), conservation of momentum, collisions, coefficient of restitution, impulse.  
  <sub>MC-B08. Lectures [1].</sub>
- **IA-MC-009**: Lecture 9: Springs, strings and SHM Force exerted by elastic springs and strings (Hooke's law). Oscillations of a particle attached to a spring, and of a particle hanging on a string. Simple harmonic motion of a particle for small displacement from equilibrium.  
  <sub>MC-B09. Lectures [1].</sub>
- **IA-MC-010**: Lecture 10: Motion in a circle Derivation of the central acceleration of a particle constrained to move on a circle. Simple pendulum; motion of a particle sliding on a cylinder.  
  <sub>MC-B10. Lectures [1].</sub>

## Ancillary: Computational Projects

8 lectures in the Easter Term of Part IA; examined in Part IB.



### Introductory lectures

Reading map: RM-CP-01

- **IA-CP-001**: The Computational Projects course is examined in Part IB. However introductory lectures are given in the Easter Full Term of the Part IA year. The lectures cover an introduction to algorithms and aspects of the Matlab programming language.  
  <sub>CP-B01. Lectures [8].</sub>

### Projects and manual

Reading map: RM-CP-02

- **IA-CP-002**: The projects that need to be completed for credit are published by the Faculty in a manual usually at the end of July or the beginning of August at the end of the Part IA year. The manual contains details of the projects and information about course administration. The manual is available on the Faculty website at https://www.maths.cam.ac.uk/undergrad/catam/. Full credit may be obtained from the submission of the two core projects and a further two additional projects. Once the manual is available, these projects may be undertaken at any time up to the submission deadlines, which are near the start of the Full Lent Term in the Part IB year for the two core projects, and near the start of the Full Easter Term in the Part IB year for the two additional projects. A list of suitable books can be found in the manual.  
  <sub>CP-B01.</sub>

