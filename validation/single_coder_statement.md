# Single-coder design: what it supports and what it does not

The corpus was coded by one analyst (the first author). Three independent reviewers across two venues raised this. This statement sets out why the design is retained, what mitigations are in place, what the paper's claims therefore rest on, and what is deferred to future work. It is written so that a reader can judge the claims without taking the coder's word for the coding.

## Why single-coder

The corpus is a screened evidence set assembled to test whether a structural model (eight boundaries, three modes) can express documented incidents and to report what pattern the screened set shows. It is not a sample from which population rates are estimated. For that purpose, the controlling question is whether each coding decision is traceable to a public source and a written rule, so that any reader can re-derive or dispute it. Inter-rater agreement would add evidence that the rules are applied consistently by people other than their author; it would not change what any individual incident shows. The authors chose to spend the available effort on the audit trail rather than on a second coding pass, and to carry second-pass coding into the thesis work that extends this corpus.

## Mitigations in place

1. **Written codebook.** `codebook/CODEBOOK.md` states each criterion and mode as a decision rule, including the negative cases (what does not count as WB-S; why antecedents are never coded Exf; why Gemini memory and Slack AI are single-mode).
2. **Per-incident source.** Every row in `corpus/corpus.csv` carries the citation keys of its primary sources, so each mode and boundary coding can be checked against the public record.
3. **Reproducible counts.** `validation/check_corpus.py` derives every corpus number the paper states (21; 6/7/8; seven multi-mode; six exact Drift+Exf; two WB-S; five PB anchors; TB-5 placement) from the CSV and fails if any disagrees. The paper's numbers are therefore a function of the data file, not of the prose.
4. **Internal consistency checks.** The same script tests the coding against the codebook's own structural statements (archetype-to-boundary attachment; ingestion coding by subset) and reports violations rather than hiding them. Two rows currently fail the archetype check and are listed for resolution.
5. **Dual coding of the contested construct.** The strict-versus-broad reading of "poisoning" is coded as two columns (WB-S and ingestion_broad) so the headline asymmetry can be read either way.
6. **Circularity stated, not buried.** C4 makes boundary fit an inclusion criterion; the paper and the codebook say so, and the screening log is the place where any C4-only exclusion would appear.
7. **Falsification conditions.** `validation/falsifiability.md` states what evidence would overturn the modal pattern and the boundary enumeration.

## What the claims rest on

- *The model can express each of the 21 incidents.* Rests on the per-row coding; auditable row by row.
- *Six of seven multi-mode incidents pair drift with exfiltration.* Rests on seven rows; the paper calls it an observation about the corpus, not a prevalence estimate, and names disclosure bias as a live alternative explanation.
- *Drift predates AI agents.* Rests on seven antecedents with no agent in the chain; each is a well-documented incident whose drift coding is unlikely to be contested.
- *The eight boundaries are complete.* Rests on the structural enumeration of DFD arcs, not on the corpus (which cannot test it); stated as falsifiable.

## What is deferred

- **Second-pass coding and inter-rater agreement** (Cohen's kappa on mode and primary boundary) on the extended corpus assembled for the first author's thesis.
- **Resolution of the two archetype inconsistencies** and the six TBD broad-ingestion codes, recorded in `VALIDATION_REPORT.md`.
- **Completion of the screening log** with excluded candidates, which is what would let the C4 exclusion statement be made.
- **Empirical evaluation of the controls** in simulation across models, environments, and control regimes (ongoing thesis work).
