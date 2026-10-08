# Supplement: A Bidirectional Threat Model for AI-Agent Integration Across Federated Identity Boundaries

Jerad Dunne and Suleyman Uludag, Department of Computer Science, University of Michigan-Flint.

Companion material for the short paper accepted at IEEE IPCCC 2026 (Austin, TX, November 2026). It holds everything the six-page limit could not: the full 21-incident corpus with per-incident coding, the codebook, the search and screening protocol, the 31-row STRIDE/LINDDUN elicitation matrix, the control specifications, the EchoLeak trace, and a script that reproduces the paper's corpus counts from the data file.

**Status: pre-release.** Items marked provisional in the table below are awaiting author confirmation. Do not cite a DOI until the first release is tagged.

## How to read this repository

Start with `codebook/CODEBOOK.md`, then `corpus/corpus.csv`. To check that the paper's numbers follow from the data, run:

```
python3 validation/check_corpus.py
```

To re-code the corpus independently: apply the codebook to each row's cited sources without looking at the recorded coding, then diff against `corpus/corpus.csv`. Disagreements are welcome as issues; please cite the rule and the source.

## Layout

| Path | Contents |
|---|---|
| `references.bib` | The paper's bibliography (the citation keys used in `corpus/corpus.csv`) |
| `corpus/corpus.csv` | 21 incidents: year, subset, source quality, citation keys, modes, primary boundary, archetype, broad-ingestion flag, verify notes |
| `codebook/CODEBOOK.md` | Inclusion criteria C1 to C5 as decision rules; mode definitions and rules; boundary and archetype rules; coding procedure |
| `codebook/search_protocol.md` | Sources searched, window, screening procedure |
| `codebook/screening_log.csv` | One row per candidate: the 21 admitted incidents and the 9 candidates excluded at assembly, with the recorded reason |
| `elicitation/dfd.md` | DFD elements, arcs, boundaries, FIPS 199 asset ratings |
| `elicitation/stride_linddun_matrix.csv` | The full 31-row threat matrix (8 rows published in the paper, same IDs) |
| `controls/candidate_enhancements.md` | The eight candidate SP 800-53 enhancements; the binding-and-parsing trio; token, provenance, and PEP specification |
| `controls/echoleak_trace.md` | Step-by-step trace with boundary, mode, and control per step |
| `validation/check_corpus.py` | Reproduces the paper's counts and checks codebook consistency |
| `validation/VALIDATION_REPORT.md` | Latest output of the script |
| `validation/single_coder_statement.md` | Why single-coder, mitigations, what the claims rest on, what is deferred |
| `validation/falsifiability.md` | The two conditions that would overturn the paper's claims |

## What is settled and what is provisional

| Item | Status |
|---|---|
| Incident list, years, modes, primary boundaries, source codes | As published in the paper's Table I |
| Archetypes for the 12 incidents the paper names under A1/A2/A3 | As published |
| Archetypes for the other 9 incidents | Provisional; two conflict with the paper's attachment statement (see validation report) |
| Broad-ingestion flag for the 6 MCP-cluster rows | TBD |
| Search protocol, excluded candidates | Recorded from the authors' assembly records |
| Full 31-row matrix | From the authors' working matrix (row T-10 added 2026-07-19) |

## Citing

Paper (short version, IPCCC 2026): see `CITATION.cff`. This supplement: cite the Zenodo DOI once the first release is tagged (see `SETUP.md`). Repository: https://github.com/jeraddunne/seam-threat-model-supplement

## License

Everything in this repository is released under CC BY 4.0 (see `LICENSE`). The paper itself is not included here; the accepted manuscript will be added under `paper/` after the IEEE camera-ready, subject to IEEE's author-posting policy.
