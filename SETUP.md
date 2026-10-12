# Releasing the supplement and getting the DOI

1. Resolve the provisional items listed in `README.md` (archetype conflicts, ingestion TBDs). Re-run `python3 validation/check_corpus.py --write` until it reports all checks pass.
2. Create the GitHub repository (public) and push:
   ```
   cd seam-threat-model-supplement
   git init && git add . && git commit -m "Supplement v1.0.0: corpus, codebook, matrix, controls"
   gh repo create seam-threat-model-supplement --public --source=. --push
   ```
3. Enable the repository on Zenodo (zenodo.org, GitHub integration), then create a GitHub release tagged `v1.0.0`. Zenodo mints a DOI for that release and a concept DOI for all versions.
4. Put the concept DOI in:
   - `references.bib` entry `dunne2026supplement` in the Overleaf package (done: `10.5281/zenodo.23320544`);
   - `CITATION.cff` (`identifiers:` block) and `README.md`.
5. In `Master_Main.tex`, no `\AUTH{}` or `\tp{}` uses remain in the body (2026-10-08); the macro definitions can stay or be deleted.
6. After camera-ready, add the accepted manuscript as `paper/IPCCC2026_short_paper.pdf` and tag `v1.0.1`.
