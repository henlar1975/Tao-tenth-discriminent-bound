# An explicit class-number-one cutoff from recent real-zero gaps

**Henric Larsson** · Independent researcher · [ORCID 0009-0007-8688-5733](https://orcid.org/0009-0007-8688-5733)

A short, AI-assisted response to [Terence Tao's 2026 tenth-discriminant challenge](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/).

## Mathematical statement

Assume the *published statements* of the explicit real-zero exclusions of [Banks (2026)](https://arxiv.org/abs/2610.15483) for primitive real Dirichlet characters of conductor `q >= 10^10`, and [Lu–Zaman–Zhao (2026)](https://arxiv.org/abs/2602.03626) for quadratic conductors `q <= 10^10`. Then the elementary argument in [`paper.pdf`](paper.pdf) shows that an imaginary quadratic field of class number one has absolute fundamental discriminant `|D| < 50,000`. An exact finite enumeration returns precisely

`|D| = 3, 4, 7, 8, 11, 19, 43, 67, 163`.

This is **not** a new Siegel-zero theorem, an improvement of the best known discriminant cutoff, or a human-peer-reviewed proof. In particular, [Bennett–Martin–O'Bryant–Rechnitzer (2018), Proposition 1.10](https://arxiv.org/abs/1802.00085) already yields a better bound of `|D| <= 6677` for class number one by a different method. [Kimura (2026)](https://arxiv.org/abs/2610.21511) gives much broader class-number results. The purpose of this note is a compact quantitative extraction from the specified Banks/Lu–Zaman–Zhao inputs, in the comparative spirit of Tao's challenge.

## Read the mathematics

- [`paper.pdf`](paper.pdf) — four-page note including full elementary bridge, explicit rational bounds, source attributions, and AI disclosure.
- [`paper.tex`](paper.tex) — complete LaTeX source.

## Reproduce the exact calculations

Python 3 standard library suffices; no external packages and no precomputed class-number tables are needed.

```bash
python3 verification/check_analytic_rational_certificate.py
python3 verification/enumerate_discriminants_first.py
python3 verification/enumerate_forms_first.py
python3 verification/crosscheck_independent_enumerators.py
```

These scripts regenerate the corresponding JSON and CSV certificates in `verification/`. The two enumerations use different traversal strategies and agree on every one of the 15,195 negative fundamental discriminants below 50,000. Their agreement checks a finite calculation, **not** the validity of the external zero-free theorems.

For public-data integrity, hashes of the files in this release are in [`CHECKSUMS_SHA256.txt`](CHECKSUMS_SHA256.txt). They are not mathematical proof certificates for the analytic inputs.

## Independent AI audit

An independently prompted fresh GPT-Pro model performed a blind-first mathematical reconstruction followed by exact-code replay; the final verdict was **VERIFIED CONDITIONALLY**, conditional on the cited Banks and Lu–Zaman–Zhao theorem statements and standard classical class-number facts. The audit did not re-prove the external theorems or repeat LZZ's large numerical computation. This constitutes independent **AI review**, not human peer review.

A readable audit summary and its preserved reports are in [`audit/`](audit/). The original comprehensive audit ZIP, not included in this compact repository snapshot, had SHA-256 `6506f69927213594b94d583bcd9a479343f58a55d8717f4d9bb1e51aeea2671b`.

## AI contribution and scope

This human-directed investigation used GPT-6 Extra High for mathematical derivation, coding and exposition, and a separate fresh GPT-Pro model for independent verification. All work relying on Banks and Lu–Zaman–Zhao is attributed to those authors. We make no claim to be first to prove the classical nine-discriminant classification or to discover the underlying standard analytic techniques.

## Publication state and licensing

The mathematical note is the reviewed **v0.3 candidate dated 20 October 2026**. It was prepared for release in connection with Tao's challenge; it has not been independently human-peer-reviewed. The author should add an explicit reuse license before inviting derivatives (e.g. CC BY 4.0 for the note and MIT for original code), if desired. No reuse license has been assigned in this prepared package.
