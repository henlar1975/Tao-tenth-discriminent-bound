# Independent AI audit — scoped summary

**Verdict:** VERIFIED CONDITIONALLY. A separate fresh GPT-Pro completed a blind-first mathematical reconstruction and later an exact-code replay. No local defect was found in the hyperbola lemma, analytic-continuation argument, class-number deduction, rational inequalities, or full reduced-form enumeration.

**External assumptions not verified afresh:** (a) Banks's primitive-real-character zero gap for conductor `q >= 10^10`; (b) the Lu–Zaman–Zhao zero computation for quadratic conductors `q <= 10^10`; (c) standard classical class-number/ideal-class correspondence. These theorems were checked for statement scope, not independently re-proved.

**Exact finite checks:** 15,195 negative fundamental discriminants below 50,000; two independent blind implementations and producer verifiers agree on each class number. Final producer outputs were recreated byte-for-byte.

**Frozen audit receipts:** Stage-A report SHA-256 `3da12760a0a98ae9ac19a256a923da271659a1ea9c9df67a854516dcc09ce191`; original comprehensive audit ZIP SHA-256 `6506f69927213594b94d583bcd9a479343f58a55d8717f4d9bb1e51aeea2671b`.

**Important:** This was an AI mathematical audit, not human peer review, a formal Lean proof, or a fresh verification of the external published computations.

See `FINAL_THEOREM_SPECIFIC_VERDICT.md`, `STAGE_A_REPORT_FROZEN.md` and `STAGE_B_EXACT_REPLAY_AND_HOSTILE_REVIEW.md` in this folder for the full scoped reports.
