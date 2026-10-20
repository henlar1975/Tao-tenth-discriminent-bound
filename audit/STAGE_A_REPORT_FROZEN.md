# STAGE A — FROZEN INDEPENDENT BLIND MATHEMATICAL AUDIT

**Object:** `TAO_TENTH_DISCRIMINANT_ZERO_GAP_TO_CLASSNO1_ELEMENTARY_BRIDGE_INDEPENDENT_FINITE_FORMS_2026_10_20_v1_0.zip`.
**Date:** 2026-10-20. **Status:** WORKING / NONCANONICAL; not submitted, not authorized for promotion. **Protocol:** Read only the first local-entry README, the four-page mathematical PDF/TeX, and the mathematical external-theorem source ledger. I did *not* open, decompress, read or execute ANY producer `EXACT` script, producer JSON, or producer CSV before freezing this report. The blind checker named below is *new, independently authored* and located outside `EXACT`.

## Summary of blind verdict

**The proposed cutoff and all nine values are independently VERIFIED AS A CORRECT CONDITIONAL CONSEQUENCE of the stated external zero-gap inputs and classical analytic/class-number/form-reduction facts.** This is *not* verification of the truth of Banks's zero-gap proof or independent repetition of Lu–Zaman–Zhao's large computation. The limited theorem, the displayed Dirichlet-hyperbola estimate, the meromorphic identity, the rational numerical inequalities, and the complete finite reduced-form census withstand the blind reconstruction below. There is no claim to mathematical priority, a new proof of the zero-gap theorem, or a direct Tao–Green explicit prime bound.

## (A) Banks theorem scope — VERIFIED AS A SOURCE-STATEMENT; underlying proof NOT REPROVED

Checked original arXiv HTML `https://arxiv.org/html/2610.15483`, Theorem 1.1 (§1.2), not merely the packet's paraphrase. For **primitive real Dirichlet** characters of conductor `q >= 10^10`, **every real zero beta in (0,1)** satisfies `(1-beta) log q >= 3/1000`. This implies no real zero in `(1-(3/1000)/log q,1)`. Equality *at* the left endpoint remains possible but is harmless for the sign lemma. There is no odd/even restriction. The `q` is the conductor, not an arbitrary imprimitive modulus or the squarefree radicand. **The source statement's scope is independently VERIFIED; correctness of Banks's determinant proof as an external theorem remains UNRESOLVED by this limited audit.** Treat it as an explicitly assumed theorem, not as newly certified mathematical truth.

## (B) LZZ theorem scope — VERIFIED AS A SOURCE-STATEMENT; underlying computation NOT REPROVED

Checked original `https://arxiv.org/html/2602.03626`, Theorem 1.1 (§1), and paper's §2.1, §3. The original statement is: for `q <= 10^10` and quadratic Dirichlet character modulo `q`, `L(sigma,chi) != 0` on the real axis for `sigma >= 1 - 1/(5 log q)`. This includes the **left endpoint** and `q=10^10`, and is not restricted to odd characters (the discussion contrasts an earlier odd-only Watkins computation). The relevant `chi_D` is primitive and quadratic, so ambiguities about imprimitive characters cannot invalidate this application. For negative **fundamental** `D`, conductor `q=|D|` exactly; nonfundamental radicands are not substituted for q. This proof uses only real-axis exclusion; it does not require a complex zero-free rectangle. **The original assertion and applicability are VERIFIED; LZZ's original large-scale computation is an EXTERNAL ASSUMPTION, independently UNRESOLVED here.**

## (C) Hyperbola estimate — VERIFIED

Let `a=1*chi`, `A(t)=sum_{n<=t}a(n)`, `y=floor(sqrt(t))`, `S(v)=sum_{n<=v}chi(n)`, `L1=L(1,chi)`. For a nonprincipal primitive character modulo `q`, full periods cancel, so `|S(v)|<=q`; summation by parts gives the deliberately loose but valid bound `|L1-sum_{d<=y}chi(d)/d|<=2q/y`. Partition the pairs `(m,d)` with `md<=t` into `m<=y` or `d<=y`, subtract the double-counted `y S(y)`, obtaining exactly

`A(t)=sum_{d<=y}chi(d)floor(t/d)+sum_{m<=y}S(t/m)-y S(y)`.

The floor error is at most `y`, and the other two terms are bounded by `2 q y`. Thus

`|A(t)-tL1| <= y+2qt/y+2qy <= (1+6q)*sqrt(t) <=7q sqrt(t)` for **every real t>=1**; the middle step follows from `sqrt(t)/2<=y<=sqrt(t)`. No integer-t restriction, parity condition, or hidden asymptotic constant occurs. The interface is independently VERIFIED.

## (D) Continuation identity and sign — VERIFIED

Partial summation in `Re(s)>1` gives

`F(s)=zeta(s)L(s,chi)=sum_{n<=X}a(n)n^(-s)-A(X)X^(-s)+s int_X^infty A(t)t^(-s-1)dt`.

Writing `A(t)=L1 t+E(t)`, and integrating the `L1` term, yields exactly

`F(s)=sum_{n<=X}a(n)n^(-s)+L1 X^(1-s)/(s-1)-E(X)X^(-s)+s int_X^infty E(t)t^(-s-1)dt`.

Because `E(t)=O(q sqrt(t))`, the last integral converges absolutely, locally uniformly in `Re(s)>1/2`; both sides give the same meromorphic continuation off the pole at 1. In particular **the pole term carries the PLUS sign before `1/(s-1)`**, which is a NEGATIVE contribution at real `s=sigma<1`. Both boundary and integral errors have independent absolute-value bounds.

Put `delta=c/log q`, `sigma=1-delta`, `X=q^3`. For `q>=50000`, `0<c<=1/5`, we have `3/4<sigma<1`; then `1+sigma/(sigma-1/2)<=4` and

`|error| <= 28 q X^(1/2-sigma) = 28 e^(3c)/sqrt(q)`.

For `chi_D` from negative fundamental D, `L1>0` by the classical analytic class-number formula; the absence of a zero in `(sigma,1)` implies by continuity `L(sigma,chi_D)>=0`, even if there is a zero at sigma. Since `zeta(sigma)<0` for `0<sigma<1`, it follows `F(sigma)<=0`. The logical sign step is sound. For a general primitive real character the same sign step uses the standard `L(1,chi)>0`; restricting to the actual negative quadratic application is sufficient. **VERIFIED.**

## (E) Coefficients and 50-square lower mass — VERIFIED

At each prime `p`, the coefficient at `p^r` of `1*chi` is `1+chi(p)+...+chi(p)^r`, nonnegative for `chi(p)=-1,0,+1`. At `r=2j`, it is respectively `1,1,2j+1`, so `a(m^2)>=1` by multiplicativity. For `X=q^3>=50^2`, `sigma<1`,

`sum_{n<=X}a(n)/n^sigma >= sum_{m=1}^{50}1/m^(2sigma) >= sum_{m=1}^{50}1/m^2 > 13/8`.

Independent exact `Fraction` arithmetic gives

`sum_{m=1}^{50} 1/m^2 - 13/8 = 254956780065141618804430838740674349709 / 1920815367859463099600511526151929560192000 > 0`.

Consequently

`sqrt(q)L1 >= (c/log q) * ((13/8)*exp(-3c)*sqrt(q)-28)`.

**VERIFIED.**

## (F) Rational comparison and monotonicity — VERIFIED, with small-margin warning

Set `K=(13/8)e^(-3c)>0`, `f_c(q)=(K sqrt(q)-28)/log q`. Direct differentiation gives `f'_c(q)=[K sqrt(q)((log q)/2-1)+28]/[q (log q)^2]`, positive whenever `q>e^2`. Thus each lower estimate attains its minimum at the left endpoint.

Independent *rational*, NOT floating-point, arithmetic (see `blind/INDEPENDENT_BLIND_RECONSTRUCTION.py`, run before any `EXACT` access):

- `exp(3/5) < sum_{k=0}^4 (3/5)^k/k! + ((3/5)^5/5!)/(1-(3/5)/6) = 45553/25000 < 183/100`, hence `exp(-3/5)>100/183`.
- `exp(10)>22000` via its positive Taylor polynomial through degree 21; `exp(83/100)>25/11` via its positive Taylor polynomial through degree 4; their product is above 50000, hence `log(50000)<1083/100`.
- `(447/2)^2<50000`, hence `sqrt(50000)>447/2`.
- `exp(12/5)>10` by its positive degree-5 Taylor polynomial, giving `log(10)<12/5` and `log(10^10)<24`.
- `exp(-9/1000)>991/1000` follows from `exp(-x)>1-x` for positive x.
- The classical strict rational bound `pi<22/7` is used (e.g. positive-integral Archimedean proof); no floating pi enters the certificate.

For `50000<=q<=10^10`, `c=1/5` gives the **exact reduced rational lower bound**

`h(-q)>1455755/1453386 = 1 + 2369/1453386 >1`.

For `q>=10^10`, `c=3/1000` gives

`h(-q)>2254133/352000>1`.

Both regime computations, including strict inequalities and endpoint overlap, are VERIFIED independently. **Caution:** the first estimate exceeds one by only about 0.00163; changing any coefficient, primitive-conductor identification or rounding could destroy the proof. Here the exact arithmetic closes the gap.

## (G) Fundamental discriminants, proper form convention — VERIFIED in blind enumeration

For `q=|D|`, a negative fundamental discriminant `D=-q` is exactly one of (i) `D≡1 (mod 4)` and squarefree, (ii) `D=4m`, `m≡2 or 3 (mod 4)` and squarefree. No count of arbitrary negative integers or of nonprimitive characters may replace this. Positive definite **primitive** integral binary quadratic forms `(a,b,c)` obey `D=b^2-4ac<0`, `|b|<=a<=c`, `gcd(a,b,c)=1`, and the standard single-representative tie convention `b>=0` if `|b|=a` or `a=c`. Crucially, `b` and `-b` in the interior need NOT be identified: we count **proper** SL_2(Z)-classes, not GL_2(Z) improper equivalence. Since `q=4ac-b^2>=3a^2`, it is sufficient to enumerate `a<=floor(sqrt(q/3))`.

Two **new independent blind** implementations, created from scratch without opening the packet `EXACT`, were executed: (I) all possible primitive reduced triples `(a,b,c)` with `3<=4ac-b^2<50000`, then filter discriminants; (II) all fundamental `q`, then for each `a,b` solve the congruence and derive `c=(b^2+q)/(4a)` exactly. A squarefree sieve enumerates the q independently of both form loops. They agreed **on all 15,195 class-number counts**, and the unique `h=1` absolute discriminants were exactly

`3,4,7,8,11,19,43,67,163`.

The complete blind independent census is saved as `blind/blind_independent_census.csv`, with SHA-256

`a024d84a1747466f44b15a2641e71c90eadefee87e9feffa0fdcdf815da28066`.

The independent code and detailed rational/enumeration receipt are `blind/INDEPENDENT_BLIND_RECONSTRUCTION.py` and `blind/blind_independent_receipt.json`. Executing source-code enumeration is not a formalized Lean proof or an independent proof of the classical proper-form/ideal-class correspondence. **Finite counting, scope and conventions VERIFIED; formal proof of the classical correspondence accepted as external standard mathematics.**

## (H) Completeness of nine-field result — VERIFIED CONDITIONALLY

With the **Banks/LZZ statements assumed** and the **classical analytic class-number and reduced-form-to-proper-ideal-class theorems accepted**, part (F) shows no negative fundamental D with `|D|>=50000` has `h(D)=1`, while part (G) covers *every* negative fundamental discriminant `3<=|D|<50000`, including -3 and -4 where the special unit factors make the general large-q class-number formula inapplicable. The small cases are handled solely by direct form enumeration. The radical-field notation is `Q(sqrt(-d))` for `d=3,1,7,2,11,19,43,67,163` corresponding to fundamental absolute discriminants `3,4,7,8,11,19,43,67,163`. This is a complete **conditional** nine-field classification, not a proof of Banks/LZZ and not a claim of historical priority. **VERIFIED CONDITIONALLY.**

## Falsification checklist / unresolved dependencies

- No false identity, missing endpoint, reversed pole sign, unjustified convergence, parity omission, bad boundary convention, or failed rational comparison was found in the mathematical text. **No FALSE subclaim found in (C)–(H)** at this first pass.
- **UNRESOLVED externally:** independent verification of Banks's interpolation-determinant theorem; replication or independent validation of LZZ's computer-assisted certification; formalization of the standard binary-quadratic-form/ideal-class correspondence. These are genuine assumptions, not re-proved by the package.
- **NOT CLAIMED / NOT ESTABLISHED:** a new explicit single-scale Tao–Green prime nonresidue inequality; new originality/priority; publication, canonical promotion, communication with Tao; a complete first-principles proof of all invoked foundational classical results.
- Stage B must compare against the producer's exact scripts and CSVs, independently execute both, assess completeness of verification, and preserve this Stage-A report byte-for-byte.

## Stage-A source and evidence log

- README read by first ZIP local header and unbuffered I/O. The PDF and TeX and scope ledger were extracted without decompressing any packet `EXACT` entry. PDF is four pages (`pdfinfo`); TeX and `pdftotext` mathematical text agree in inspected identities.
- Original external source statements: https://arxiv.org/html/2610.15483 (§1.2, Theorem 1.1); https://arxiv.org/html/2602.03626 (§1, Theorem 1.1 and §§2–3). These were read for theorem scope, NOT to reprove or replicate their theorem proofs.
- Exact rational and form-count evidence: `blind/INDEPENDENT_BLIND_RECONSTRUCTION.py`, `blind/blind_independent_receipt.json`, `blind/blind_independent_census.csv`, authored/executed blind. All arithmetic uses Python `int` / `Fraction` and `isqrt`/`gcd`, not external rational computation or producer verifiers.

**END OF COMPLETE FROZEN STAGE A REPORT — DO NOT MODIFY AFTER HASHING.**
