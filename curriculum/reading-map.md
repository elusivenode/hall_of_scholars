# Reading map

Status: **proposal for the curriculum director.** Reading assignments are Claude Code's selection from the sources verified in [bibliography.md](../references/bibliography.md) and compared item by item in [reading-alignment.md](reading-alignment.md). The director decides what the student actually reads. Resources are chosen on mathematical quality, **syllabus alignment** and **practical accessibility** to the student, and each carries four separate statuses (bibliographic, contents, alignment, availability) so that nothing is claimed beyond what was seen.

Each Schedules sub-heading has an entry `RM-<course>-<nn>`; every register item points to one ([coverage.yaml](coverage.yaml)). **Chapter and section pointers appear only where a real contents list was read**; otherwise the entry says so. An entry never contains an exercise identifier: those belong in session records once an exercise has actually been set. Do not delay study until every later reference is verified: the outstanding checks are listed and prioritised in [verification-tasks.md](../references/verification-tasks.md), with the first study phase (Numbers and Sets, Vectors and Matrices, Groups) first.

## Working resources by course

| Course | Working primary and companions | Verification | Notes and open points |
|---|---|---|---|
| Numbers and Sets | Logic, sets, induction (IA-NS-001 to IA-NS-008): BIB-001 Allenby with BIB-003 Hammack. Number theory (009 to 014): BIB-002 Davenport. Reals and countability (015 to 022): BIB-009 Lebl | Allenby: bibliographic verified, contents partial; Hammack, Lebl, Davenport: verified | Allenby does not name the reals or countability and needs a companion; Lebl is free but has gaps (017 e, 018, 020); Burn and Hamilton need a library check |
| Groups | BIB-004 Beardon | bibliographic partial; contents partial (chapter titles) | BIB-005 Judson (free; verified; no Mobius groups or quaternions) |
| Vectors and Matrices | BIB-007 Cowley notes (the course-matched spine; covers all 18 items); BIB-006 Axler for the conceptual development | Cowley and Axler: verified | Beardon (chapter titles); nine items need Cowley or Beardon because Axler does not cover them |
| Differential Equations | BIB-011 Robinson (provisional) | bibliographic partial; contents partial (Part titles) | Unconfirmed against the schedule; Priority B verification |
| Analysis I | BIB-009 Lebl (working primary), with BIB-025 Chua/Gowers notes for the complex material | Lebl and Chua notes: verified | Burkill (Cambridge dagger; access risk; omits Bolzano-Weierstrass); Garling (real only; contents gated) |
| Probability | BIB-015 Norris notes (working primary), with BIB-014 Weber notes | verified | BIB-012 Grimmett and Welsh as the companion book (contents verified; does not show four items) |
| Vector Calculus | BIB-019 Tong notes (working primary; names all 14 items) | verified | BIB-018 Baxandall and Liebeck as a rigorous companion for the calculus core (contents UNVERIFIED); BIB-016 Bourne and Kendall for tensors; BIB-017 Riley et al |
| Dynamics and Relativity | BIB-021 O'Donnell (provisional primary) | verified; 3 items not named, several partial | BIB-024 Tong notes for dimensional analysis and moments of inertia |

## Axler's role in Vectors and Matrices

Axler (BIB-006, 4th edition, open access) has a substantial role: the **conceptual development** of vector spaces, linear maps, eigenvalues and inner-product spaces. Suggested reading, each tied to Cambridge items (all section names verified from the PDF's contents): 1B and 1C with 2A to 2C (IA-VM-005, subspaces, span, independence, basis, dimension); 3A to 3D (IA-VM-009 to IA-VM-010 and IA-VM-015: linear maps, null space and range, the Fundamental Theorem of Linear Maps which proves rank-nullity, matrices of linear maps, change of basis); 5A and 5D (IA-VM-013, IA-VM-016: eigenvalues and diagonalisability); 6A and 6B (IA-VM-004: inner products, Cauchy-Schwarz, orthonormal bases); 7A and 7B (IA-VM-014: self-adjoint operators and the spectral theorem); 9A (quadratic forms, IA-VM-017) and 9C (determinants, after the concrete version in Cowley). The Harvard 55a lectures use the same book ([enrichment.md](enrichment.md)).

**Cambridge requirements that must be covered outside Axler** (no hit in its contents or text): the logarithm, roots and powers of complex numbers (IA-VM-002); R^3 geometry and the scalar product in R^3 (IA-VM-003); suffix notation and the summation convention (IA-VM-006); the vector and triple products and vector equations (IA-VM-007); lines, planes and spheres (IA-VM-008); the geometric actions of matrices in IA-VM-010 and Gaussian elimination as a method (IA-VM-011, only passing mentions in Axler); the isotropic/symmetric/antisymmetric decomposition (IA-VM-012); conics (IA-VM-017); and Lorentz transformations (IA-VM-018). Cowley's notes (BIB-007) cover all of these by their section titles.

## Baxandall and Liebeck's role in Vector Calculus

Baxandall and Liebeck (BIB-018, owned) is intended as a **substantial rigorous companion**. Its coverage is **not yet verified**: no source gave a real contents list, so every alignment cell is unknown. What the publisher says (rigorous; begins with linear algebra; includes the inverse and implicit function theorems; concludes with Green, Stokes and Gauss) and what Tong says (a more careful treatment) point to the calculus core (curves, line and surface integrals, the integral theorems; IA-VC-001 to IA-VC-003 and IA-VC-008). Nothing seen confirms tensors, Laplace and Poisson uniqueness, curvilinear coordinates or the Maxwell context, so those items rest on Tong and Allanach and Evans, and on Bourne and Kendall for tensors. **To settle it**, the student can photograph the contents pages of their copy and the index entries for tensor, Laplace, Poisson, cylindrical, curvilinear and Maxwell.

## The student's other text

**The Princeton Companion (BIB-034).** Unverified: the title in the sources found is *The Princeton Companion to Mathematics*, not "to Pure Mathematics". It is orientation reading and is not assigned to any syllabus block. The student has offered to supply the title and contents pages.

## Reading by syllabus heading

### RM-NS-01 Introduction to number systems and logic
- Items: IA-NS-001 to IA-NS-002
- Primary: BIB-001 Allenby: chapter titles "The need for proof"; "Statements and connectives"; "True or false?"; "Proofs....for all"; "There exists....proofs" (numbers not printed).
- Also: BIB-003 Hammack: Ch 2 Logic; Ch 6 Proof by Contradiction; Ch 9 Disproof; 1.9 Sets That Are Number Systems. BIB-026 Faculty sheets.
- Note: No verified contents shows the algebraic/transcendental distinction or the Fundamental Theorem of Algebra statement (IA-NS-001).

### RM-NS-02 Sets, relations and functions
- Items: IA-NS-003 to IA-NS-007
- Primary: BIB-001 Allenby: "Sets, negations, notations and functions".
- Also: BIB-003 Hammack: Ch 1 Sets; Ch 3 Counting (3.7 The Inclusion-Exclusion Principle); 11.3 Equivalence Relations; 12.2 Injective and Surjective Functions. BIB-009 Lebl: 0.3 Basic set theory (0.3.3 Functions; 0.3.4 Relations and equivalence classes). BIB-026.
- Note: Indicator functions (IA-NS-004) are not named in any verified source.

### RM-NS-03 The integers
- Items: IA-NS-008
- Primary: BIB-001 Allenby: "The principle of mathematical induction".
- Also: BIB-003 Hammack: Ch 10 Mathematical Induction (10.1 to 10.4); 3.6 Pascal's Triangle and the Binomial Theorem. BIB-009 Lebl: 0.3.2 Induction. BIB-026.

### RM-NS-04 Elementary number theory
- Items: IA-NS-009 to IA-NS-014
- Primary: BIB-002 Davenport: I Factorization and the Primes (pp 1-30); II Congruences (pp 31-48); VIII Computers and Number Theory (pp 165-208, the likely place for RSA, unconfirmed).
- Also: BIB-003 Hammack: 5.2 Congruence of Integers; 10.4 Fundamental Theorem of Arithmetic; 11.5 The Integers Modulo n. BIB-001 Allenby: "The integers and rational numbers" (modular content unconfirmed). BIB-026.
- Note: Euclid's algorithm, the Chinese Remainder Theorem and Wilson's theorem are not named in any verified section list. Section-level checking of Davenport is an outstanding task.

### RM-NS-05 The real numbers
- Items: IA-NS-015 to IA-NS-018
- Primary: BIB-009 Lebl: Chapter 1 Real Numbers (1.1 Basic properties, which defines the least-upper-bound property; 1.2 The set of real numbers, incl. 1.2.3 Using supremum and infimum; 1.5 Decimal representation of the reals); 2.1.1 Monotone sequences; 2.5 Series.
- Also: BIB-040 Gowers pages: reals.html, decimals.html, roottwo.html. BIB-038 Burn: chapters titled 3 Sequences, 4 Completeness: what the rational numbers lack, 5 Series (title level only). BIB-039 Hamilton: chapter 1 Numbers (title only).
- Note: Allenby's verified titles name none of these items. Lebl assumes R as a complete ordered field and does not construct it. No verified source shows the irrationality of e, an explicit transcendental construction (IA-NS-018), or a construction of R. Library checks of Burn and Hamilton are outstanding.

### RM-NS-06 Countability and uncountability
- Items: IA-NS-019 to IA-NS-022
- Primary: BIB-009 Lebl: 0.3.5 Cardinality; 1.4 Intervals and the size of R (R is uncountable); 1.5 Decimal representation of the reals (the diagonal argument).
- Also: BIB-003 Hammack: Ch 14 Cardinality of Sets (14.1 to 14.4). BIB-040 Gowers: countability.html. BIB-039 Hamilton: chapter 2 The size of a set (title only). BIB-026.
- Note: Lebl does not state the countable-union theorem (IA-NS-020) and has the existence of transcendental numbers only as an exercise (1.4.9). Allenby's titles do not show countability.

### RM-GP-01 Examples of groups
- Items: IA-GP-001 to IA-GP-003
- Primary: BIB-004 Beardon: chapter titles 1 Groups and permutations; 6 Quaternions and isometries; 13 Mobius transformations.
- Also: BIB-005 Judson: 3.2 Definitions and Examples; 3.3 Subgroups; 4 Cyclic Groups; 5.2 Dihedral Groups; 12.2 Symmetry; Ch 9 Isomorphisms. BIB-007 Cowley: 1.9 Mobius Transformations. BIB-027.
- Note: Judson has no Mobius groups; use Beardon (chapter 13) or Cowley 1.9.

### RM-GP-02 Lagrange's theorem
- Items: IA-GP-004 to IA-GP-006
- Primary: BIB-004 Beardon: placement not visible from chapter titles.
- Also: BIB-005 Judson: Ch 6 Cosets and Lagrange's Theorem (6.3 Fermat's and Euler's Theorems). BIB-027.
- Note: Judson names neither the classification of groups of small order nor the quaternion group (IA-GP-005).

### RM-GP-03 Group actions
- Items: IA-GP-007 to IA-GP-009
- Primary: BIB-004 Beardon: Ch 14 Group actions.
- Also: BIB-005 Judson: Ch 14 Group Actions (14.1 Groups Acting on Sets; 14.2 The Class Equation). BIB-027.

### RM-GP-04 Quotient groups
- Items: IA-GP-010
- Primary: BIB-004 Beardon: placement not visible from chapter titles.
- Also: BIB-005 Judson: Ch 10 Normal Subgroups and Factor Groups (10.1); Ch 11 Homomorphisms (11.2 The Isomorphism Theorems). BIB-027.

### RM-GP-05 Matrix groups
- Items: IA-GP-011 to IA-GP-013
- Primary: BIB-004 Beardon: Ch 11 Linear maps of Euclidean space; Ch 12 Groups (titles; unconfirmed).
- Also: BIB-005 Judson: Ch 12 Matrix Groups and Symmetry (12.1 Matrix Groups). BIB-007 Cowley: Ch 6 Transformation Groups. BIB-027.

### RM-GP-06 Permutations
- Items: IA-GP-014 to IA-GP-016
- Primary: BIB-004 Beardon: Ch 1 Groups and permutations.
- Also: BIB-005 Judson: 5.1 Permutation Groups; 10.2 The Simplicity of the Alternating Group. BIB-027.

### RM-VM-01 Complex numbers
- Items: IA-VM-001 to IA-VM-002
- Primary: BIB-007 Cowley (course-matched spine): Ch 1 Complex Numbers (1.3 Polar; 1.4 Exponential Function; 1.5 Roots of Unity; 1.6 Logarithms and Complex Powers; 1.7 De Moivre's Theorem).
- Also: BIB-006 Axler: 1A Complex Numbers (basic arithmetic only; polar form, logarithms and powers are not named). BIB-004 Beardon: Ch 3 The complex plane (title). BIB-028.
- Note: IA-VM-002 must be covered outside Axler.

### RM-VM-02 Vectors
- Items: IA-VM-003 to IA-VM-008
- Primary: BIB-007 Cowley: Ch 2 Vector Algebra (2.4 Scalar Product; 2.5 Vector Product; 2.6 Triple Products; 2.7 Spanning Sets, Linear Independence, Bases; 2.10 Higher Dimensional Spaces; 2.11 Suffix Notation; 2.13 Lines, Planes and Spheres; 2.14 Subspaces).
- Also: BIB-006 Axler (conceptual development of IA-VM-004 and IA-VM-005): 1B Definition of Vector Space; 1C Subspaces; 2A Span and Linear Independence; 2B Bases; 2C Dimension; 6A Inner Products and Norms (Cauchy-Schwarz). BIB-004 Beardon: Ch 4, Ch 7 (titles). BIB-028.
- Note: Outside Axler: IA-VM-003 (R^3 geometry), IA-VM-006 (suffix notation), IA-VM-007 (vector and triple products), IA-VM-008 (lines, planes, spheres).

### RM-VM-03 Matrices
- Items: IA-VM-009 to IA-VM-012
- Primary: BIB-007 Cowley: Ch 3 (3.3 Rank, Kernel and Nullity; 3.6 Algebra of Matrices; 3.7 Determinants); Ch 4 (4.3.4 Gaussian elimination; 4.4 The Rank of a Matrix).
- Also: BIB-006 Axler: 3A Vector Space of Linear Maps; 3B Null Spaces and Ranges (Fundamental Theorem of Linear Maps = rank-nullity, proved); 3C Matrices; 3D Invertibility and Isomorphisms; 7D Isometries, Unitary Operators; 9B, 9C Determinants (abstract, late). BIB-004 Beardon: Ch 8, 9, 11 (titles). BIB-028.
- Note: Outside Axler: the geometric actions in IA-VM-010, Gaussian elimination as a method (IA-VM-011), the isotropic/symmetric/antisymmetric decomposition (IA-VM-012). Read Axler's determinants (9C) after Cowley's concrete 3 x 3 version.

### RM-VM-04 Eigenvalues and Eigenvectors
- Items: IA-VM-013 to IA-VM-018
- Primary: BIB-007 Cowley: Ch 5 (5.2 Eigenspaces, Eigenvectors, Bases; 5.3 Change of Basis; 5.5 Diagonalizable Maps; 5.7 Hermitian Matrices; 5.8 Forms; 5.9 More on Conic Sections); 6.5 Lorentz Transformations.
- Also: BIB-006 Axler: 5A Invariant Subspaces; 5D Diagonalizable Operators; 3D Change of Basis; 7A Self-Adjoint and Normal Operators; 7B Spectral Theorem; 9A Bilinear Forms and Quadratic Forms. BIB-004 Beardon: Ch 10 Eigenvectors (title). BIB-028.
- Note: Outside Axler: classification of conics (IA-VM-017) and Lorentz transformations as transformation groups (IA-VM-018). Axler's Jordan form (8C) goes beyond the schedule, which needs only canonical forms of 2 x 2 matrices.

### RM-DE-01 Basic calculus
- Items: IA-DE-001 to IA-DE-004
- Primary: BIB-011 Robinson: Appendix C Derivatives and partial derivatives (title only; depth unverified).
- Also: BIB-030 Faculty sheet A3a. BIB-020 Allanach and Evans: Ch 1 Derivatives and Coordinates.

### RM-DE-02 First-order linear differential equations
- Items: IA-DE-005 to IA-DE-006
- Primary: BIB-011 Robinson: Part I First order differential equations (chapters unverified).
- Also: BIB-030.

### RM-DE-03 Nonlinear first-order equations
- Items: IA-DE-007 to IA-DE-009
- Primary: BIB-011 Robinson: Part I; Part IV Numerical methods and difference equations is the likely match for the discrete-equation item (titles only).
- Also: BIB-030.
- Note: Coverage of the logistic equation and logistic map is unconfirmed.

### RM-DE-04 Higher-order linear differential equations
- Items: IA-DE-010 to IA-DE-014
- Primary: BIB-011 Robinson: Part II Second order linear equations with constant coefficients; Part III Linear second order equations with variable coefficients.
- Also: BIB-030.
- Note: Heaviside and Dirac responses and series solutions are not confirmed in Robinson.

### RM-DE-05 Multivariate functions: applications
- Items: IA-DE-015 to IA-DE-020
- Primary: BIB-011 Robinson: Part V Coupled linear equations; Part VI Coupled nonlinear equations; Appendix B Matrices, eigenvalues, and eigenvectors (titles suggest a match; coverage unverified).
- Also: BIB-020 Allanach and Evans: Ch 1 (partial derivatives, chain rule). BIB-030.
- Note: No source verified covers the gradient, Hessian classification or simple partial differential equations. The whole Differential Equations selection is Priority B in verification-tasks.md.

### RM-AN-01 Limits and convergence
- Items: IA-AN-001 to IA-AN-003
- Primary: BIB-009 Lebl: 2.1 Sequences and limits; 2.2; 2.3 (2.3.3 Bolzano-Weierstrass theorem); 2.4 Cauchy sequences; 2.5 Series (2.5.4 Absolute convergence; 2.5.5 Comparison test; 2.5.6 Ratio test); 2.6.2 Alternating series test.
- Also: Complex versions: BIB-025 Chua/Gowers 3.4 Complex versions; BIB-036 Korner (series in R and C). BIB-029 Faculty sheets.
- Note: Lebl is real-only for sequences and series; use the Gowers notes or Korner for the complex parts of IA-AN-001.

### RM-AN-02 Continuity
- Items: IA-AN-004 to IA-AN-006
- Primary: BIB-009 Lebl: 3.2 Continuous functions; 3.3 Extreme and intermediate value theorems (3.3.2 Bolzano's intermediate value theorem).
- Also: BIB-025 Chua/Gowers: 4 Continuous functions. BIB-036 Korner: Continuity. BIB-029.
- Note: Complex-valued continuity: use BIB-025 or BIB-036.

### RM-AN-03 Differentiability
- Items: IA-AN-007 to IA-AN-012
- Primary: BIB-009 Lebl: 4.1 The derivative (4.1.2 Chain rule); 4.2 Mean value theorem (4.2.2 Rolle's theorem); 4.3 Taylor's theorem (Lagrange form of the remainder); 4.4 Inverse function theorem.
- Also: BIB-025 Chua/Gowers: 5.2 Differentiation; 5.3 Differentiation theorems; 5.4 Complex differentiation. BIB-036 Korner: Complex variable. BIB-029.
- Note: Complex differentiation (IA-AN-012) is not in Lebl; use BIB-025 5.4 or BIB-036.

### RM-AN-04 Power series
- Items: IA-AN-013 to IA-AN-015
- Primary: BIB-009 Lebl: 2.6.5 Power series (real variable, radius of convergence).
- Also: BIB-025 Chua/Gowers: 6 Complex power series (6.1 Exponential and trigonometric functions; 6.2 Differentiating power series; 6.3 Hyperbolic trigonometric functions). BIB-036 Korner: Power series; The standard functions. BIB-029.
- Note: IA-AN-014 (trigonometric and hyperbolic functions) is not in Lebl. IA-AN-015 is starred (not examinable); the Gowers notes name it (6.2). Burkill (BIB-008) is reported to cover complex numbers and complex power series; unverified here.

### RM-AN-05 Integration
- Items: IA-AN-016 to IA-AN-020
- Primary: BIB-009 Lebl: 5.1 The Riemann integral (an example of a non-integrable function); 5.2 Properties of the integral (monotone functions are integrable); 5.3 Fundamental theorem of calculus; 5.5 Improper integrals (marked optional by the author).
- Also: BIB-025 Chua/Gowers: 7.1 Riemann Integral; 7.2 Improper integrals. BIB-036 Korner: The Riemann integral; Some properties of the integral; Infinite integrals. BIB-029.
- Note: Lebl has integration by parts only as an exercise and does not give the integral form of the Taylor remainder (IA-AN-019); piecewise-continuous integrability (IA-AN-017) is not a named result in Lebl.

### RM-PR-01 Basic concepts
- Items: IA-PR-001 to IA-PR-003
- Primary: BIB-015 Norris: 1.2 Equally likely outcomes; 2.1 to 2.5 counting; 3 Stirling's formula (3.1 Statement; 3.2 Asymptotics for log(n!); 3.3 Proof, non-examinable).
- Also: BIB-014 Weber: 1.2 Classical probability; 2.1 to 2.4; 3.2 Stirling's formula. BIB-012 Grimmett and Welsh: Appendix A Elements of combinatorics (Stirling's formula not shown). BIB-031.

### RM-PR-02 Axiomatic approach
- Items: IA-PR-004 to IA-PR-008
- Primary: BIB-015 Norris: 1.1 A general definition; 4.1 Countable subadditivity; 4.2 Continuity; 4.3 Inclusion-exclusion; 6.1 to 6.3 Independence; 7.2 Binomial; 7.4 Geometric; 7.5 Poisson; 8.1 to 8.3 Conditional probability; 8.6 Simpson's paradox.
- Also: BIB-014 Weber: 4.1 to 4.3; 5.2 to 5.5; 6.1 to 6.5 (6.5 Simpson's paradox). BIB-012 Grimmett and Welsh: 1.3 Probabilities; 1.4 Probability spaces; 1.6 Conditional probabilities; 1.7 Independent events; 1.8 The partition theorem; 1.9 Probability measures are continuous. BIB-031.

### RM-PR-03 Discrete random variables
- Items: IA-PR-009 to IA-PR-016
- Primary: BIB-015 Norris: 10.1 to 10.4 Expectation, variance and covariance; 10.6 Conditional expectation; 12.1 to 12.3 Random walks (12.3 Mean time to absorption); 13.1 to 13.6 Generating functions (13.6 Counting with generating functions); 14.1 to 14.6 Branching processes.
- Also: BIB-014 Weber: 7.3, 7.4, 8.2, 8.3, 9.1, 9.2, 10.4; 12.1, 12.2; 13.1 to 13.3; 14.1 to 14.3; 15.1 to 15.4. BIB-012 Grimmett and Welsh: 2.3 to 2.5; 4.1 to 4.4; 9.3, 9.5; 10.1, 10.4; Appendix B Difference equations. BIB-031.
- Note: Grimmett and Welsh does not show combinatorial applications of generating functions (IA-PR-016).

### RM-PR-04 Continuous random variables
- Items: IA-PR-017 to IA-PR-022
- Primary: BIB-015 Norris: 15 to 18 (17.2 Memoryless property; 18.1 to 18.5 multivariate densities and transformations); 19.1 to 19.3 Simulation (19.2 Box-Muller transform; 19.3 Rejection sampling); 21.5 Bivariate normals; 23.1 Bertrand's paradox; 23.2 Buffon's needle.
- Also: BIB-014 Weber: 16 to 20 (18.3 to 18.5 geometric probability; 20.1 Transformation; Appendix C The Jacobian; 22.4, 22.5 normals). BIB-012 Grimmett and Welsh: 5.3 to 5.7; 6.2 to 6.5; 6.8 Bivariate normal distribution. BIB-031.
- Note: Simulation (IA-PR-020) is in Norris only, not in Weber or Grimmett and Welsh.

### RM-PR-05 Inequalities and limits
- Items: IA-PR-023 to IA-PR-027
- Primary: BIB-015 Norris: 11 Inequalities (Markov, Chebyshev, Jensen, AM-GM); 20 Moment generating functions (20.3 Uniqueness and the continuity theorem); 22 Limits of sums of independent random variables (22.1 weak law; 22.3 central limit theorem; 22.4 Sampling error via the CLT).
- Also: BIB-014 Weber: 10, 11, 21.3, 23.1, 23.2. BIB-012 Grimmett and Welsh: 7.4, 7.5, 8.2, 8.3. BIB-031.

### RM-VC-01 Curves in R3
- Items: IA-VC-001
- Primary: BIB-019 Tong: 1.1 (incl. 1.1.3 Curvature and Torsion).
- Also: BIB-020 Allanach and Evans: 5.1 (torsion is marked non-examinable there). BIB-016 Bourne and Kendall: chapter on differential geometry of curves. BIB-017 Riley et al: 10.3 Space curves. BIB-018 Baxandall and Liebeck (companion; contents unverified). BIB-032.

### RM-VC-02 Integration in R2 and R3
- Items: IA-VC-002 to IA-VC-003
- Primary: BIB-019 Tong: 1.2 Line Integrals; 2.1.2 Changing Coordinates; 2.1.3 Volume Integrals; 2.1.4 Spherical Polar and Cylindrical Polar Coordinates; 2.2 Surface Integrals.
- Also: BIB-020 Allanach and Evans: Ch 2, 3, 4. BIB-016: line, surface and volume integrals chapter. BIB-017: Ch 11. BIB-018 Baxandall and Liebeck (line and surface integrals per the publisher; contents unverified). BIB-032.

### RM-VC-03 Vector operators
- Items: IA-VC-004 to IA-VC-007
- Primary: BIB-019 Tong: 3.1 The Gradient; 3.2 Div and Curl (3.2.2 Conservative is Irrotational; 3.2.3 Solenoidal Fields; 3.2.4 The Laplacian); 3.3 Orthogonal Curvilinear Coordinates.
- Also: BIB-020 Allanach and Evans: 6.1; 6.2 Leibniz Properties; 6.3 Second Order Derivatives (the vector identities, IA-VC-007); 8.2; 9. BIB-016: Scalar and vector fields chapter. BIB-017: 10.7 to 10.10. BIB-032.
- Note: Tong has no titled section for the vector identities (IA-VC-007).

### RM-VC-04 Integration theorems
- Items: IA-VC-008
- Primary: BIB-019 Tong: 4.1 The Divergence Theorem; 4.3 Green's Theorem in the Plane; 4.4 Stokes' Theorem (4.4.3 An Application: Magnetic Fields); 4.2 conservation laws; 3.2.5 Some Vector Calculus Equations in Physics (Maxwell's equations).
- Also: BIB-020 Allanach and Evans: Ch 7; 12 Maxwell's Equations. BIB-016: Integral theorems chapter. BIB-017: 11.3, 11.8, 11.9. BIB-018 Baxandall and Liebeck: the publisher says it concludes with the Green, Stokes and Gauss theorems; contents unverified.

### RM-VC-05 Laplace's equation
- Items: IA-VC-009 to IA-VC-010
- Primary: BIB-019 Tong: 5.1.1 Gauss' Law; 5.2.1 Isotropic Solutions; 5.2.2 Some General Results (uniqueness and the maximum principle); 5.2.3 Integral Solutions.
- Also: BIB-020 Allanach and Evans: Ch 10; 11.1 Uniqueness Theorems; 11.2.2 The Maximum Principle; 11.3 Integral Solution of Poisson's Equation.
- Note: No verified BOOK source shows the uniqueness theorem, the maximum principle or Gauss's method; only the two sets of notes do.

### RM-VC-06 Cartesian tensors in R3
- Items: IA-VC-011 to IA-VC-014
- Primary: BIB-019 Tong: 6.1 What it Takes to Make a Tensor (6.1.2 Tensor Operations; 6.1.3 Invariant Tensors); 6.2.1 Electric Fields in Matter; 6.2.2 The Inertia Tensor.
- Also: BIB-020 Allanach and Evans: Ch 13 (13.3.2 The quotient rule); 14.2 The Inertia Tensor; 14.3; Ch 15 Invariant and Isotropic Tensors. BIB-016 Bourne and Kendall: Cartesian tensors chapter (isotropic tensors; tensor fields). BIB-017 Riley et al: 26.3 Cartesian tensors; 26.7 The quotient law; 26.9 Isotropic tensors; 26.12 Physical applications. BIB-032.

### RM-DR-01 Basic concepts
- Items: IA-DR-001 to IA-DR-004
- Primary: BIB-021 O'Donnell: "The Galileo-Newton Formulation of Dynamics" (Galilean relativity; Newton's dynamical laws; Gravitational and inertial mass); Friction; "Charged particles in an electromagnetic field" (the Lorentz force).
- Also: BIB-024 Tong: 1 Newtonian Mechanics; 2 Forces; 3 Interlude: Dimensional Analysis. BIB-033.
- Note: Dimensional analysis (IA-DR-003) is not named in O'Donnell; use Tong chapter 3.

### RM-DR-02 Newtonian dynamics of a single particle
- Items: IA-DR-005 to IA-DR-010
- Primary: BIB-021 O'Donnell: Particle Dynamics in One Dimension (Potential energy diagrams); Oscillations (Simple harmonic motion; Damped simple harmonic motion); Particle Dynamics in Two and Three Dimensions; Central Forces and Orbits (Orbital equation; Perturbed orbits; Kepler's laws; Rutherford scattering); Rotating Reference Frames (Centrifugal force; Coriolis force).
- Also: BIB-024 Tong: 4 Central Forces; 6 Non-Inertial Frames. BIB-022 Gregory (chapter titles). BIB-033.
- Note: The Foucault pendulum (IA-DR-010, starred) is not named in O'Donnell.

### RM-DR-03 Newtonian dynamics of systems of particles
- Items: IA-DR-011 to IA-DR-013
- Primary: BIB-021 O'Donnell: Multi-Particle Systems (Conservation of linear momentum; Conservation of angular momentum; The centre of mass frame; The two-body problem; Variable mass problems).
- Also: BIB-024 Tong: 5 Systems of Particles (5.1 centre of mass; 5.2 Collisions; 5.3 Variable Mass Problems). BIB-033.

### RM-DR-04 Rigid bodies
- Items: IA-DR-014 to IA-DR-016
- Primary: BIB-021 O'Donnell: Rigid Bodies (Rotation of a rigid body about a fixed axis; Planar motion of a rigid body).
- Also: BIB-024 Tong: 5.4 Rigid Bodies (the moment of inertia; the inertia tensor). BIB-022 Gregory: chapters on rigid body kinematics, the inertia tensor and rigid body dynamics (titles). BIB-033.
- Note: The parallel axis theorem (IA-DR-015) is not named in O'Donnell; moments of inertia are not named by title.

### RM-DR-05 Special relativity
- Items: IA-DR-017 to IA-DR-024
- Primary: BIB-021 O'Donnell: Special Relativity (Einstein's postulates; Lorentz transformations; Minkowski diagrams; Relativistic kinematics); Space-Time (The light cone; Proper time; The four-component vector formalism); Relativistic Mechanics (4-momentum; Relativistic energy; Particle collisions).
- Also: BIB-024 Tong: 7 Special Relativity (7.1 Lorentz Transformations; 7.4 Relativistic Kinematics). BIB-023 Rindler (Cambridge dagger; unverified). BIB-007 Cowley 6.5 Lorentz Transformations. BIB-033.

### RM-MC-01 Mechanics (non-examinable lectures)
- Items: IA-MC-001 to IA-MC-010
- Primary: BIB-021 O'Donnell: the opening dynamics chapters (The Galileo-Newton Formulation of Dynamics; Particle Dynamics in One Dimension; Oscillations; Particle Dynamics in Two and Three Dimensions) fit by title.
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

