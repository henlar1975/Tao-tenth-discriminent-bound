# STAGE B — EXACT REVEAL, EXECUTION AND HOSTILE CODE REVIEW

**Date:** 2026-10-20. **Status:** SECOND PASS COMPLETED / WORKING-NONCANONICAL MATHEMATICS. **Stage-A report remains frozen.**

## Physical/logical read barrier receipt

The first pass extracted only the first ZIP-entry README and the allowed TeX/PDF mathematical proof plus external scope ledger. Producer `EXACT/` payloads were skipped, not decompressed, inspected or executed. The complete 12,519-byte `STAGE_A_REPORT_FROZEN.md` was written before Stage-B reveal and independently verified twice:

```
$ sha256sum -c STAGE_A_REPORT_FROZEN.md.sha256
STAGE_A_REPORT_FROZEN.md: OK

$ python3 -c '... hashlib.sha256(Path("STAGE_A_REPORT_FROZEN.md").read_bytes()) ...'
3da12760a0a98ae9ac19a256a923da271659a1ea9c9df67a854516dcc09ce191
```

The same digest was checked AFTER revealing and executing Stage B. The report has not been modified.

## Producer archive integrity and original material

The outer ZIP has **17 entries**; `ZipFile.testzip()` returned `None` (all CRCs agree). The root `MANIFEST_SHA256.txt` validated **all 16 individually listed files** with `sha256sum -c`, including both producers' scripts, both census CSVs, the rational verifier, JSON receipts and original four-page PDF/TeX. This checks internal byte consistency; it is not by itself mathematical proof.

Before looking at the exact scripts, independent blind code already obtained 15,195 negative fundamental discriminants and the claimed nine `h=1` values. Thus the exact-stage agreement is not just the producer comparing two scripts of its own.

## Producer script audit

1. **`EXACT/check_analytic_rational_certificate.py` — VERIFIED within declared scope.** All inequalities used in the strict cutoff are implemented using `Fraction` and positive exponential Taylor truncations / a rigorously geometrically dominated tail. The two `float` conversions are only *post-proof reporting*, not used for acceptance. Independently established:

   - `exp(3/5) < 45553/25000 < 183/100`, so `exp(-3/5)>100/183`;
   - `exp(10)>22000`, `exp(83/100)>25/11`, `exp(12/5)>10` from finite rational Taylor sums;
   - `sum_{m=1}^{50}1/m^2 >13/8`, `sqrt(50000)>447/2`, `exp(-9/1000)>991/1000`;
   - the **exact** lower fractions `1455755/1453386 > 1` and `2254133/352000 > 1`.

   Additional independent rational proof for the classical bound `pi<22/7`: the *positive* integral
   `int_0^1 x^4(1-x)^4/(1+x^2) dx = int_0^1 (x^6-4x^5+5x^4-4x^2+4-4/(1+x^2)) dx =22/7-pi>0`.
   Thus the integer/rational cutoff has no unverified floating or π approximation. The script explicitly *does not claim to verify* Banks/LZZ or analytic continuation.

2. **`EXACT/enumerate_discriminants_first.py` — VERIFIED.** It marks integers divisible by any square `j*j>1` as nonsquarefree (iterating all `j` rather than only primes is redundant, not wrong). Its two fundamental-discriminant cases correctly test `D=-q`, including the negative modular residues. The reduced-form generator enforces exactly `|b|<=a<=c`, integrality `4ac-b²=q`, primitivity by `gcd`, proper boundary sign and `a<=floor(sqrt(q/3))`. Its `q` range includes every `3<=q<50000`. It is exhaustive, not sampling.

3. **`EXACT/enumerate_forms_first.py` — VERIFIED.** Its independent `sqfree()` performs integer trial division over the required range; it does not import the other enumerator. It traverses all reduced `a,b,c` with `c>=a`, `q=4ac-b²<50000`, excludes negative `b` on the standard two boundary edges, and enforces primitivity. The `cmax` bound is correct. Filtering by exact fundamentalness is complete. The script's structure genuinely reverses the two principal enumeration loops relative to method A. It is not a new external source, just a second implementation of the same mathematics.

4. **`EXACT/crosscheck_independent_enumerators.py` — VERIFIED WITH AN EXTRA HARDENING CHECK.** It converts each CSV to a dict and checks `len(a)==len(b)==15195` plus equality. A dict-only parser could conceivably conceal duplicate raw lines. The independently written `exact/INDEPENDENT_STAGE_B_COMPARATOR.py` also verifies **15,195 physical data rows in each CSV, no duplicate keys, strictly sorted unique `q`, positive class numbers, complete equality with the pre-reveal blind census**. All these additional tests PASS.

## Independent replay

All four producer scripts were run in the distinct `exact/replay` copy, not in the immutable extracted producer material:

```
python3 EXACT/check_analytic_rational_certificate.py
python3 EXACT/enumerate_discriminants_first.py
python3 EXACT/enumerate_forms_first.py
python3 EXACT/crosscheck_independent_enumerators.py
```

All four commands exited normally and produced six outputs **byte-identical** to those in the source ZIP. The original producer root passed `sha256sum -c MANIFEST_SHA256.txt` for every listed file. Exact SHA-256 source/replay pairs:

| Output | Producer and replay SHA-256 |
|---|---|
| `analytic_rational_certificate.json` | `d3334ce8e3356df4b4d6839bd9fd104d14800e56e013b303d511be84c2d00831` |
| `enum_crosscheck.json` | `ed1dd3b6704d962510963cda219ad325ab43659df264788f56f817ba5845a320` |
| `enum_discriminants_first.json` | `51dd8b292caa63372548e5a272b835c42ae56ec14f4d20b54802de9da3b78354` |
| `enum_forms_first.json` | `36fd37901fdc149102895764df40f8a46c65d582953374ea0dae58002ea69df9` |
| `full_fundamental_discriminant_classnumbers_under_50000.csv` | `3f0ab4721daeca3afc53353fe57dc4c8eecb7137c2a521caf690bd4889389b06` |
| `independent_forms_first_classnumbers.csv` | `70896897a71b27833e8182d23a8abb80378dbd66bae31feb820b3ded2d517956` |

The pre-reveal independent checker produced another, structurally separate 15,195-row CSV SHA-256 `a024d84a1747466f44b15a2641e71c90eadefee87e9feffa0fdcdf815da28066`. All THREE per-discriminant count dictionaries coincide; canonical sorted `q:h` records have semantic SHA-256 `6fde7912b4e1f00bcc3783c36b48754d841bd249e649009140965699fddc5595`. There are zero mismatches, missing discriminants or duplicate keys. The maximum class number in the finite range is 357.

The independent B receipt `exact/INDEPENDENT_STAGE_B_RECEIPT.json` is generated from independently parsed data, not by reading the producer's `passed` flags. Sanity cases cover `D=-3,-4,-15,-20,-23,-163`, which catch special units and proper-versus-improper form-count pitfalls: counts 1,1,2,2,3,1 respectively.

## Final A–H adjudication after reveal

| Interface | Verdict and scope |
|---|---|
| **A Banks** | **VERIFIED theorem statement and correct character/conductor/endpoint application; UNRESOLVED external correctness of its determinant proof.** |
| **B LZZ** | **VERIFIED original theorem statement, q≤10¹⁰ inclusive, left boundary inclusive, both parities, primitive χ_D applicability; UNRESOLVED external computation.** |
| **C Uniform hyperbola** | **VERIFIED** with explicit derivation for every real t≥1, exact constant 7. |
| **D Partial summation/sign** | **VERIFIED**, including meromorphic continuation to Re(s)>1/2, s≠1, error constant 28 and harmless endpoint zero at σ. |
| **E Square mass** | **VERIFIED**, with coefficient Euler factors and independently computed exact positive margin above 13/8. |
| **F Rational regimes** | **VERIFIED** by independent exact arithmetic and derivative, with strict inequalities and π upper bound. |
| **G Class census** | **VERIFIED** as finite exhaustive computation under the standard proper-form correspondence: three independently produced 15,195-row count dictionaries match. |
| **H Complete nine-field list** | **VERIFIED CONDITIONALLY** on A/B as external zero-free inputs and classical class-number / proper-form correspondence. |

**FALSE mathematical claims detected within the intended conditional statement: NONE.** Do NOT convert the verification of theorem *statements* (A/B) into independent certification of the external proofs or computations. No new direct Tao–Green explicit prime inequality is obtained or claimed, and mathematical priority is expressly not claimed. The packet remains **WORKING / NONCANONICAL**, with no promotion/publication/submission authorization.

## Residual audit limitations

This review does not reproduce Banks's interpolation determinant machinery, independently recompute the LZZ 10¹⁰-modulus zero-exclusion experiment, formally check proofs in Lean, or establish the general reduced form/ideal class correspondence from first principles. It treats all these as explicitly identified external input or classical facts. The exact replay and separate blind census substantially reduce risk of a local integer/enumeration error, but do not replace formal verification or independent external-theorem review.

**Stage-B conclusion:** `VERIFIED AS A CONDITIONAL PROOF-EXTRACTION PACKAGE; EXTERNAL ZERO-FREE INPUTS NOT INDEPENDENTLY VERIFIED`. No need for discovery continuation; not cleared for publication or canonical promotion.
