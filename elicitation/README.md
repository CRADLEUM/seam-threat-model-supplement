# STRIDE-per-element and LINDDUN elicitation

`stride_linddun_matrix.csv` is the full 31-row threat matrix the paper summarizes in Table II (eight exemplar rows). Reviewer 3 asked for the full matrix; this file is where it lives.

**Contents.** All 31 rows come from the authors' working matrix (the 30 rows of the first-pass elicitation plus T-10, mcp-server-git at TB-4, added 2026-07-19 to match the corpus coding of that incident). The eight rows published in the paper are T-02, T-06, T-11, T-14, T-16, T-18, T-22, and T-28, with the same IDs here. Rows marked *analogue* in `structural_argument` are retained on a structural argument with no direct corpus incident.

No row attaches to TB-1 or the host-application process: no incident in the 21-incident corpus anchors a cell there, and no structural argument was retained at those elements in the first-pass elicitation.

## Method (paper, Sec. 4-A)

For each (DFD element, STRIDE category) pair, the analyst asked whether a corpus incident instantiates the threat. Cells with an incident or a structural argument were retained; the rest were dropped. LINDDUN was applied in scope-bounded form: Linkability, Identifiability, Disclosure of information, and Detectability attach to the seam; Non-repudiation, Unawareness, and Non-compliance are covered by single-platform LINDDUN work and were not elicited here.

Coverage statements the full matrix must be consistent with (paper, Sec. 4-C):

- Spoofing, Tampering, Information disclosure, and Elevation of privilege populate densely.
- Repudiation populates only at the system-of-record and agent-memory rows.
- Denial of service does not populate from the corpus (no incident shows a DoS outcome at the seam).
- Row selection for Table II was constrained so that every Section 5 enhancement appears at least once and every mode class (Drift, WB-S, Exf, SC, LINDDUN-L) is represented.

## Columns

| Column | Meaning |
|---|---|
| id | T-01 to T-31 |
| element_or_boundary | TB-1 to TB-8, or a component name (MCP srv., LLM, Agent memory, System of record) |
| category | STRIDE letter (S, T, R, I, E; D does not populate) or LINDDUN category (L-Link. = Linkability, L-Ident. = Identifiability, L-Disc. = Disclosure of information, L-Det. = Detectability) |
| modes | Failure mode(s) the row instantiates |
| primary_controls | Candidate SP 800-53 enhancement(s) the row justifies |
| anchor_incident | Corpus incident(s) that instantiate the threat; for analogue rows, the incident the structural argument extends |
| structural_argument | "analogue" when the row rests on a structural argument rather than a direct corpus incident |
| status | published in paper Table II, or in the authors' matrix only |
