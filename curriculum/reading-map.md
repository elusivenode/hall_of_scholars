# Reading map

Status: **proposal for the curriculum director.** Reading assignments are Claude Code's selection from the sources verified in [bibliography.md](../references/bibliography.md); the director decides what the student actually reads.

Each Schedules sub-heading has a reading-map entry `RM-<course>-<nn>`; every register item points to one ([coverage.yaml](coverage.yaml)). **Chapter and section pointers appear only where a real contents list was read**; otherwise the entry says so and gives none. An entry never contains an exercise identifier: those belong in session records once an exercise has actually been set.

Roles: *Primary* is the proposed main text. *Also* lists supplements, course-matched free notes, and the Faculty example sheets for practice. Cambridge example sheets are for independent work and assessment, with no model solutions available.

## Proposed primary text per course

| Course | Proposed primary | Verification | Supplements and free notes |
|---|---|---|---|
| Numbers and Sets | BIB-001 Allenby | partially verified | BIB-003 Hammack (free); BIB-002 Davenport |
| Groups | BIB-004 Beardon | partially verified | BIB-005 Judson (free) |
| Vectors and Matrices | BIB-004 Beardon, with BIB-007 Cowley notes as the course-matched spine | partially verified / verified | BIB-006 Axler (owned, free); BIB-016 Bourne and Kendall |
| Differential Equations | BIB-011 Robinson | partially verified | BIB-020 Allanach and Evans (calculus) |
| Analysis I | BIB-008 Burkill (access risk) | partially verified; contents unverified | BIB-009 Lebl (free); BIB-010 Garling |
| Probability | BIB-012 Grimmett and Welsh | unverified | BIB-014 Weber and BIB-015 Norris (free) |
| Vector Calculus | BIB-016 Bourne and Kendall | partially verified | BIB-019 Tong (free, all six blocks); BIB-018 Baxandall and Liebeck (owned) |
| Dynamics and Relativity | BIB-021 O'Donnell | verified | BIB-022 Gregory; BIB-024 Tong (free) |

## Notes on the student's own texts

**Axler, *Linear Algebra Done Right* (BIB-006) and Vectors and Matrices.** Not suitable as the primary. The 4th edition is open access and was read in full-text form. It is an excellent treatment of abstract vector spaces, linear maps, eigenvalues, the spectral theorem and determinants (determinants arrive late, in 9C, via alternating multilinear forms), so it fits the conceptual spine of the course and the Harvard enrichment. It contains nothing on the cross product, triple products, suffix notation and the summation convention, Lorentz transformations, or the classification of conics, and only passing mentions of Gaussian elimination. Those parts of Vectors and Matrices need Cowley's notes (BIB-007) or Beardon (BIB-004). The student's printed edition was not seen; the free 4th edition was.

**Baxandall and Liebeck, *Vector Calculus* (BIB-018) and Vector Calculus.** Not proposed as the primary. Edition facts and the publisher's description were verified; only one chapter title was. It is a rigorous companion for curves, parametrisation, the inverse and implicit function theorems, and the integration theorems (blocks RM-VC-01, 02 and 04). No source seen confirms Cartesian tensors, the Laplace/Poisson uniqueness theorems and maximum principle, the Maxwell's equations context, or curvilinear coordinates, which are the distinctive parts of the Cambridge course. The student should check the physical copy's contents page.

**The Princeton Companion (BIB-034).** Unverified: the title in the sources found is *The Princeton Companion to Mathematics*, not "to Pure Mathematics". It is orientation reading and is not assigned to any syllabus block. The student has offered to provide the title and contents pages.

## Reading by syllabus heading

### RM-NS-01 Introduction to number systems and logic
- Items: IA-NS-001 to IA-NS-002
- Primary: BIB-001 Allenby: contents titles "The need for proof", "Statements and connectives", "True or false?" (chapter numbers not shown).
- Also: BIB-003 Hammack: Ch 2 Logic (2.1 to 2.12), Ch 6 Proof by Contradiction, Ch 9 Disproof. BIB-026 Faculty sheets.

### RM-NS-02 Sets, relations and functions
- Items: IA-NS-003 to IA-NS-007
- Primary: BIB-001 Allenby: "Sets, negations, notations and functions" (chapter number not shown).
- Also: BIB-003 Hammack: Ch 1 Sets; Ch 3 Counting (3.7 The Inclusion-Exclusion Principle); Ch 11 Relations (11.3 Equivalence Relations); Ch 12 Functions (12.2 Injective and Surjective). BIB-026.

### RM-NS-03 The integers
- Items: IA-NS-008
- Primary: BIB-001 Allenby: "The principle of mathematical induction"; "The integers and rational numbers" (numbers not shown).
- Also: BIB-003 Hammack: Ch 10 Mathematical Induction (10.1 to 10.4); 3.6 Pascal's Triangle and the Binomial Theorem. BIB-026.
- Note: The Binomial Theorem is the syllabus's worked example of induction.

### RM-NS-04 Elementary number theory
- Items: IA-NS-009 to IA-NS-014
- Primary: BIB-002 Davenport: I Factorization and the Primes; II Congruences (verified chapter titles).
- Also: BIB-003 Hammack: 5.2 Congruence of Integers; 10.4 Fundamental Theorem of Arithmetic; 11.5 The Integers Modulo n. BIB-001 Allenby: "The integers and rational numbers" (modular content not confirmed). BIB-026.
- Note: RSA: Davenport's chapter VIII "Computers and Number Theory" is the likely place; not confirmed. Euclid's algorithm, the Chinese Remainder Theorem and RSA are not in Hammack's contents.

### RM-NS-05 The real numbers
- Items: IA-NS-015 to IA-NS-018
- Primary: BIB-001 Allenby: "The rational numbers and the real numbers"; "Real numbers and complex numbers" (numbers not shown).
- Also: BIB-026 Faculty sheets. BIB-025 Chua notes (unofficial): a section on real numbers.
- Note: Least upper bounds and the least upper bound axiom are the content here; no verified source covers them closely. R.P. Burn's Numbers and Functions is Cambridge-listed for this end of the course but was not evaluated. Open question for the director.

### RM-NS-06 Countability and uncountability
- Items: IA-NS-019 to IA-NS-022
- Primary: BIB-003 Hammack: Ch 14 Cardinality of Sets (14.1 to 14.4, including 14.2 Countable and Uncountable Sets).
- Also: BIB-026 Faculty sheets.
- Note: Allenby's contents titles do not show countability.

### RM-GP-01 Examples of groups
- Items: IA-GP-001 to IA-GP-003
- Primary: BIB-004 Beardon: Ch 1 Groups and permutations; Ch 6 Quaternions and isometries; Ch 13 Mobius transformations (chapter titles verified; sections not seen).
- Also: BIB-005 Judson: Ch 3 Groups (3.2 Definitions and Examples; 3.3 Subgroups); Ch 4 Cyclic Groups; 5.2 Dihedral Groups; Ch 9 Isomorphisms. BIB-007 Cowley 1.9 Mobius Transformations. BIB-027.
- Note: Judson's contents (as read) have no Mobius groups or quaternions.

### RM-GP-02 Lagrange's theorem
- Items: IA-GP-004 to IA-GP-006
- Primary: BIB-004 Beardon: placement not visible from chapter titles (Ch 1 or Ch 12 plausible, unverified).
- Also: BIB-005 Judson: Ch 6 Cosets and Lagrange's Theorem (6.1 to 6.3; 6.3 Fermat's and Euler's Theorems). BIB-027.

### RM-GP-03 Group actions
- Items: IA-GP-007 to IA-GP-009
- Primary: BIB-004 Beardon: Ch 14 Group actions.
- Also: BIB-005 Judson: Ch 14 Group Actions (14.1 Groups Acting on Sets; 14.2 The Class Equation). BIB-027.

### RM-GP-04 Quotient groups
- Items: IA-GP-010
- Primary: BIB-004 Beardon: placement not visible from chapter titles (Ch 12 plausible, unverified).
- Also: BIB-005 Judson: Ch 10 Normal Subgroups and Factor Groups (10.1); Ch 11 Homomorphisms (11.2 The Isomorphism Theorems). BIB-027.

### RM-GP-05 Matrix groups
- Items: IA-GP-011 to IA-GP-013
- Primary: BIB-004 Beardon: Ch 11 Linear maps of Euclidean space; Ch 12 Groups (plausible, unverified).
- Also: BIB-005 Judson: Ch 12 Matrix Groups and Symmetry (12.1 Matrix Groups). BIB-007 Cowley Ch 6 Transformation Groups. BIB-027.

### RM-GP-06 Permutations
- Items: IA-GP-014 to IA-GP-016
- Primary: BIB-004 Beardon: Ch 1 Groups and permutations.
- Also: BIB-005 Judson: 5.1 Permutation Groups; 10.2 The Simplicity of the Alternating Group. BIB-027.

### RM-VM-01 Complex numbers
- Items: IA-VM-001 to IA-VM-002
- Primary: BIB-004 Beardon: Ch 3 The complex plane (title).
- Also: BIB-007 Cowley: Ch 1 Complex Numbers (1.3 Polar Representation; 1.4 Exponential Function; 1.5 Roots of Unity; 1.6 Logarithms and Complex Powers; 1.7 De Moivre's Theorem). BIB-006 Axler 1A (basic only). BIB-028.

### RM-VM-02 Vectors
- Items: IA-VM-003 to IA-VM-008
- Primary: BIB-004 Beardon: Ch 4 Vectors in three-dimensional space; Ch 7 Vector spaces (titles).
- Also: BIB-007 Cowley: Ch 2 Vector Algebra (2.4 Scalar Product; 2.5 Vector Product; 2.6 Triple Products; 2.7 Spanning Sets, Linear Independence, Bases; 2.10 Higher Dimensional Spaces; 2.11 Suffix Notation; 2.13 Lines, Planes and Spheres). BIB-006 Axler 1B, 1C, 2A to 2C (abstract; no cross product or suffix notation). BIB-028.
- Note: Suffix notation is not in Axler or (visibly) Beardon; use Cowley or Bourne and Kendall (BIB-016, contents unverified).

### RM-VM-03 Matrices
- Items: IA-VM-009 to IA-VM-012
- Primary: BIB-004 Beardon: Ch 8 Linear equations; Ch 9 Matrices; Ch 11 Linear maps of Euclidean space (titles).
- Also: BIB-007 Cowley: Ch 3 (3.3 Rank, Kernel and Nullity; 3.6 Algebra of Matrices; 3.7 Determinants); Ch 4 (4.3.4 Gaussian elimination; 4.4 The Rank of a Matrix). BIB-006 Axler 3A to 3D, 9B, 9C (determinants arrive late, via alternating multilinear forms). BIB-028.

### RM-VM-04 Eigenvalues and Eigenvectors
- Items: IA-VM-013 to IA-VM-018
- Primary: BIB-004 Beardon: Ch 10 Eigenvectors (title).
- Also: BIB-007 Cowley: Ch 5 (5.2 Eigenspaces; 5.3 Change of Basis; 5.5 Diagonalizable Maps; 5.7 Hermitian Matrices; 5.8 Forms; 5.9 More on Conic Sections); 6.5 Lorentz Transformations. BIB-006 Axler 5A to 5D, 6A, 6B, 7A, 7B, 9A (quadratic forms); no conics, no Lorentz. BIB-028.
- Note: Axler's Jordan form (Ch 8) is beyond the schedule, which needs only canonical forms of 2 x 2 matrices.

### RM-DE-01 Basic calculus
- Items: IA-DE-001 to IA-DE-004
- Primary: BIB-011 Robinson: Appendix C Derivatives and partial derivatives (title verified; depth unverified).
- Also: BIB-030 Faculty sheet A3a (derivatives, Leibniz rule, Taylor series). BIB-020 Allanach and Evans Ch 1 Derivatives and Coordinates (1.2.2 chain rule; 1.2.3 inverse functions).

### RM-DE-02 First-order linear differential equations
- Items: IA-DE-005 to IA-DE-006
- Primary: BIB-011 Robinson: Part I First order differential equations (chapters unverified).
- Also: BIB-030.

### RM-DE-03 Nonlinear first-order equations
- Items: IA-DE-007 to IA-DE-009
- Primary: BIB-011 Robinson: Part I (which chapters not seen); Part IV Numerical methods and difference equations is the likely match for the discrete-equation item (title only).
- Also: BIB-030.
- Note: Coverage of the logistic equation and logistic map against the schedule is unconfirmed.

### RM-DE-04 Higher-order linear differential equations
- Items: IA-DE-010 to IA-DE-014
- Primary: BIB-011 Robinson: Part II Second order linear equations with constant coefficients; Part III Linear second order equations with variable coefficients.
- Also: BIB-030.
- Note: Heaviside and Dirac delta responses and series solutions are not confirmed in Robinson.

### RM-DE-05 Multivariate functions: applications
- Items: IA-DE-015 to IA-DE-020
- Primary: BIB-011 Robinson: Part V Coupled linear equations; Part VI Coupled nonlinear equations; Appendix B Matrices, eigenvalues, and eigenvectors (titles suggest a match; coverage unverified).
- Also: BIB-020 Allanach and Evans Ch 1 (partial derivatives, chain rule). BIB-030.
- Note: No source verified covers gradient, Hessian classification and simple partial differential equations. Open question for the director.

### RM-AN-01 Limits and convergence
- Items: IA-AN-001 to IA-AN-003
- Primary: BIB-008 Burkill: contents not verified, so no chapters are given.
- Also: BIB-009 Lebl: Ch 1 Real Numbers; Ch 2 Sequences and Series. BIB-025 Chua/Gowers notes (unofficial): 2 Convergence of sequences; 3 Convergence of infinite sums (3.2 Absolute convergence; 3.3 Convergence tests; 3.4 Complex versions). BIB-029.

### RM-AN-02 Continuity
- Items: IA-AN-004 to IA-AN-006
- Primary: BIB-008 Burkill: contents not verified.
- Also: BIB-009 Lebl: Ch 3 Continuous Functions. BIB-025: 4 Continuous functions. BIB-029.

### RM-AN-03 Differentiability
- Items: IA-AN-007 to IA-AN-012
- Primary: BIB-008 Burkill: contents not verified.
- Also: BIB-009 Lebl: Ch 4 The Derivative. BIB-025: 5 Differentiability (5.3 Differentiation theorems; 5.4 Complex differentiation). BIB-029.

### RM-AN-04 Power series
- Items: IA-AN-013 to IA-AN-015
- Primary: BIB-008 Burkill: contents not verified.
- Also: BIB-025: 6 Complex power series (6.1 Exponential and trigonometric functions; 6.2 Differentiating power series; 6.3 Hyperbolic functions). BIB-029.
- Note: Lebl has no complex power series in its chapter titles. IA-AN-015 is starred (not examinable).

### RM-AN-05 Integration
- Items: IA-AN-016 to IA-AN-020
- Primary: BIB-008 Burkill: contents not verified.
- Also: BIB-009 Lebl: Ch 5 The Riemann Integral. BIB-025: 7 The Riemann Integral (7.1; 7.2 Improper integrals). BIB-029.

### RM-PR-01 Basic concepts
- Items: IA-PR-001 to IA-PR-003
- Primary: BIB-012 Grimmett and Welsh: unverified, no chapters given.
- Also: BIB-014 Weber: 1 Classical probability; 2 Combinatorial analysis; 3 Stirling's formula. BIB-015 Norris: 1 to 3. BIB-031.

### RM-PR-02 Axiomatic approach
- Items: IA-PR-004 to IA-PR-008
- Primary: BIB-012: unverified.
- Also: BIB-014 Weber: 4 Axiomatic approach; 5 Independence; 6 Conditional probability. BIB-015 Norris: 4 to 8. BIB-031.

### RM-PR-03 Discrete random variables
- Items: IA-PR-009 to IA-PR-016
- Primary: BIB-012: unverified.
- Also: BIB-014 Weber: 7, 8, 9, 12 Probability generating functions, 13 Conditional expectation, 14 Branching processes, 15 Random walk and gambler's ruin. BIB-015 Norris: 9, 10, 12, 13, 14. BIB-031.

### RM-PR-04 Continuous random variables
- Items: IA-PR-017 to IA-PR-022
- Primary: BIB-012: unverified.
- Also: BIB-014 Weber: 16 to 20. BIB-015 Norris: 15 to 19, 21, 23 (19 Simulation of random variables; 23 Geometric probability). BIB-031.

### RM-PR-05 Inequalities and limits
- Items: IA-PR-023 to IA-PR-027
- Primary: BIB-012: unverified.
- Also: BIB-014 Weber: 10 Inequalities; 11 Weak law of large numbers; 21 Moment generating functions (the central limit theorem chapter is listed on the course web page, not in the contents lines read). BIB-015 Norris: 11 Inequalities; 20 Moment generating functions; 22 Limits of sums of independent random variables. BIB-031.

### RM-VC-01 Curves in R3
- Items: IA-VC-001
- Primary: BIB-016 Bourne and Kendall: a chapter on curves exists per a paraphrased contents list; numbers unverified.
- Also: BIB-019 Tong: Ch 1 Curves (1.1.3 Curvature and Torsion). BIB-018 Baxandall and Liebeck (parametrisations of curves; owned). BIB-032.

### RM-VC-02 Integration in R2 and R3
- Items: IA-VC-002 to IA-VC-003
- Primary: BIB-016: line, surface and volume integrals chapter per a paraphrased contents list; numbers unverified.
- Also: BIB-019 Tong: Ch 2 (2.1 Multiple Integrals; 2.1.2 Changing Coordinates; 2.1.4 Spherical Polar and Cylindrical Polar Coordinates; 2.2 Surface Integrals); 1.2 Line Integrals. BIB-020 Allanach and Evans Ch 2, 3. BIB-018 (owned; line and surface integrals). BIB-032.

### RM-VC-03 Vector operators
- Items: IA-VC-004 to IA-VC-007
- Primary: BIB-016: scalar and vector fields including curvilinear coordinates, per a paraphrased contents list.
- Also: BIB-019 Tong: Ch 3 Grad, Div and Curl (3.3 Orthogonal Curvilinear Coordinates). BIB-020 Allanach and Evans Ch 9. BIB-032 (suffix notation).
- Note: Baxandall and Liebeck (BIB-018): no verified source confirms curvilinear coordinates.

### RM-VC-04 Integration theorems
- Items: IA-VC-008
- Primary: BIB-016: integral theorems per a paraphrased contents list.
- Also: BIB-019 Tong: Ch 4 The Integral Theorems (4.1 Divergence Theorem; 4.3 Green's Theorem in the Plane; 4.4 Stokes' Theorem); 3.2.5 Some Vector Calculus Equations in Physics (Maxwell's equations are displayed there). BIB-018 Baxandall and Liebeck: concludes with the integration theorems of Green, Stokes and Gauss (publisher description).

### RM-VC-05 Laplace's equation
- Items: IA-VC-009 to IA-VC-010
- Primary: BIB-016: potential theory chapter per a paraphrased contents list.
- Also: BIB-019 Tong: Ch 5 The Poisson and Laplace Equations (5.2.2 Some General Results; states uniqueness and the maximum principle). BIB-020 Allanach and Evans Ch 11 (11.1 Uniqueness Theorems; 11.2 Laplace's Equation and Harmonic Functions).
- Note: Not confirmed in Baxandall and Liebeck.

### RM-VC-06 Cartesian tensors in R3
- Items: IA-VC-011 to IA-VC-014
- Primary: BIB-016 Bourne and Kendall: a chapter on Cartesian tensors per a paraphrased contents list; number unverified.
- Also: BIB-019 Tong: Ch 6 Tensors (6.1 What it Takes to Make a Tensor; 6.1.3 Invariant Tensors). BIB-032.
- Note: Not confirmed in Baxandall and Liebeck.

### RM-DR-01 Basic concepts
- Items: IA-DR-001 to IA-DR-004
- Primary: BIB-021 O'Donnell: Ch 1 The Galileo-Newton Formulation of Dynamics.
- Also: BIB-022 Gregory: Ch 1, 2. BIB-024 Tong: 1 Newtonian Mechanics; 2 Forces; 3 Interlude: Dimensional Analysis. BIB-033.

### RM-DR-02 Newtonian dynamics of a single particle
- Items: IA-DR-005 to IA-DR-010
- Primary: BIB-021 O'Donnell: Ch 2 Particle Dynamics in One Dimension; 3 Oscillations; 4 Particle Dynamics in Two and Three Dimensions; 5 Central Forces and Orbits; 8 Rotating Reference Frames.
- Also: BIB-022 Gregory: 3 to 7, 17 Rotating reference frames. BIB-024 Tong: 4 Central Forces; 6 Non-Inertial Frames. BIB-033.

### RM-DR-03 Newtonian dynamics of systems of particles
- Items: IA-DR-011 to IA-DR-013
- Primary: BIB-021 O'Donnell: Ch 6 Multi-Particle Systems.
- Also: BIB-022 Gregory: 9, 10, 11. BIB-024 Tong: 5 Systems of Particles (5.1 centre of mass; 5.2 Collisions; 5.3 Variable Mass Problems). BIB-033.

### RM-DR-04 Rigid bodies
- Items: IA-DR-014 to IA-DR-016
- Primary: BIB-021 O'Donnell: Ch 7 Rigid Bodies.
- Also: BIB-022 Gregory: 16, 18, 19. BIB-024 Tong: 5.4 Rigid Bodies. BIB-033.

### RM-DR-05 Special relativity
- Items: IA-DR-017 to IA-DR-024
- Primary: BIB-021 O'Donnell: Ch 9 Special Relativity; 10 Space-Time; 11 Relativistic Mechanics.
- Also: BIB-024 Tong: 7 Special Relativity (7.1 Lorentz Transformations; 7.4 Relativistic Kinematics). BIB-023 Rindler (Cambridge dagger; unverified). BIB-007 Cowley 6.5 Lorentz Transformations (as transformation groups). BIB-033.

### RM-MC-01 Mechanics (non-examinable lectures)
- Items: IA-MC-001 to IA-MC-010
- Primary: BIB-021 O'Donnell: Ch 1 to 4 (titles fit kinematics, forces, energy, oscillations and motion in two and three dimensions).
- Also: BIB-024 Tong: 1 Newtonian Mechanics; 2 Forces (university level). Hebborn and Littlewood (Cambridge-listed A-level text) was not evaluated.
- Note: No free A-level mechanics resource was verified.

### RM-CP-01 Computational Projects: introductory lectures
- Items: IA-CP-001
- Primary: No text proposed. The Schedules refer to the Faculty's Computational Projects manual (https://www.maths.cam.ac.uk/undergrad/catam/), which was not opened here.
- Note: Unverified; listed for the director.

### RM-CP-02 Computational Projects: projects and manual
- Items: IA-CP-002
- Primary: The Faculty manual, published each late July or early August; not opened here.
- Note: Unverified; listed for the director.

