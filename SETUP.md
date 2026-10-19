# Releasing a new version

1. Resolve the provisional items listed in `README.md` (archetype conflicts, ingestion TBDs). Re-run `python3 validation/check_corpus.py --write` until it reports all checks pass.
2. Update `version` and `date-released` in `CITATION.cff` and the status line in `README.md`.
3. Commit, push, and create a GitHub release with the new tag at https://github.com/CRADLEUM/seam-threat-model-supplement.
4. After camera-ready, add the accepted manuscript as `paper/IPCCC2026_short_paper.pdf` and tag `v1.0.2`.
