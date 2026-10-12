#!/usr/bin/env python3
"""Reproduce the paper's corpus-derived counts from corpus/corpus.csv and
check the coding for internal consistency against the codebook.

Usage:  python3 validation/check_corpus.py [--write]
        --write  also writes validation/VALIDATION_REPORT.md

Every number the paper states about the corpus should be derivable from the
CSV. If a check fails, either the CSV or the paper is wrong; the report says
which claim and which rows.
"""
import csv, sys, re, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CORPUS = os.path.join(ROOT, "corpus", "corpus.csv")
BIB = os.path.join(ROOT, "references.bib")
MATRIX = os.path.join(ROOT, "elicitation", "stride_linddun_matrix.csv")
LOG = os.path.join(ROOT, "codebook", "screening_log.csv")
CVSS = os.path.join(ROOT, "corpus", "cvss_snapshot.csv")

ARCHETYPE_TB = {  # codebook Sec. 5 (paper Sec. 3-A)
    "A1": {"TB-5", "TB-6", "TB-7"},
    "A2": {"TB-3", "TB-4", "MCP srv."},
    "A3": {"TB-1", "TB-4", "TB-8"},
}
ANCHORS_PB_FOCAL = {"ASCII Smuggling", "ChatGPT Custom GPT SSRF", "Slack AI",
                    "OpenAI Codex token theft via branch names", "Gemini memory", "Notion AI"}

def main(write=False):
    rows = list(csv.DictReader(open(CORPUS, newline="")))
    out = []
    ok_all = True
    def check(name, cond, detail=""):
        nonlocal ok_all
        ok_all &= bool(cond)
        out.append(f"| {name} | {'PASS' if cond else 'FAIL'} | {detail} |")

    modes = {r["id"]: set(r["modes"].split(";")) for r in rows}
    subset = Counter(r["subset"] for r in rows)

    # --- Paper claims (Sec. 1, 3-D, 6-B, Table I) ---
    check("21 incidents", len(rows) == 21, f"{len(rows)} rows")
    check("Subsets 6 MCP / 7 antecedent / 8 focal",
          subset == Counter(MCP=6, ANT=7, FOCAL=8), dict(subset))
    yrs = [int(r["year"]) for r in rows]
    check("All years within 2022-2026 (C2)", all(2022 <= y <= 2026 for y in yrs), f"{min(yrs)}-{max(yrs)}")
    multi = [i for i, m in modes.items() if len(m) > 1]
    check("Seven multi-mode incidents", len(multi) == 7, ", ".join(sorted(multi)))
    exact = [i for i, m in modes.items() if m == {"Drift", "Exf"}]
    check("Six exact Drift+Exf pairings", len(exact) == 6, ", ".join(sorted(exact)))
    triple = [i for i, m in modes.items() if m == {"Drift", "WB-S", "Exf"}]
    check("One triple-mode incident (Notion AI)", triple == ["I20"], ", ".join(triple))
    wbs = [i for i, m in modes.items() if "WB-S" in m]
    check("WB-S appears in exactly two incidents", len(wbs) == 2, ", ".join(wbs))
    sc = [i for i, m in modes.items() if "SC" in m]
    check("Two supply-chain precondition rows", len(sc) == 2, ", ".join(sc))
    exf_only = [i for i, m in modes.items() if m == {"Exf"}]
    check("One single-mode Exf anchor (Slack AI)", exf_only == ["I21"], ", ".join(exf_only))
    ant_modes = {r["id"]: modes[r["id"]] for r in rows if r["subset"] == "ANT"}
    check("All seven antecedents are Drift-only", all(m == {"Drift"} for m in ant_modes.values()))
    mcp_wbs = [r["id"] for r in rows if r["subset"] == "MCP" and "WB-S" in modes[r["id"]]]
    check("No WB-S in the MCP CVE cluster", not mcp_wbs, ", ".join(mcp_wbs))

    # Source-quality claims (Sec. 6-B)
    pb = [r for r in rows if r["source_code"] == "PB"]
    pb_focal = [r["incident"] for r in pb if r["subset"] == "FOCAL"]
    check("Six practitioner-blog anchors in the focal set", set(pb_focal) == ANCHORS_PB_FOCAL, ", ".join(pb_focal))
    check("Seventh PB row is CVE-2025-55241 (CVE-indexed)", [r["id"] for r in pb if r["subset"] != "FOCAL"] == ["I08"])
    six_src = Counter(next(r for r in rows if r["id"] == i)["source_code"] for i in exact)
    check("Six-of-seven pattern attested across PB, VEN, and NVD sources",
          {"PB", "VEN", "NVD"} <= set(six_src), dict(six_src))

    # Boundary placement claims (Sec. 4-B)
    tb5 = [i for i in exact if next(r for r in rows if r["id"] == i)["primary_tb"] == "TB-5"]
    check("Five of the six Drift+Exf rows at TB-5, one at TB-4 (mcp-server-git)",
          len(tb5) == 5 and next(r for r in rows if r["id"] == "I03")["primary_tb"] == "TB-4")
    check("WB-S anchors at TB-6 (Gemini) and TB-7 (Notion)",
          next(r for r in rows if r["id"] == "I19")["primary_tb"] == "TB-6" and
          next(r for r in rows if r["id"] == "I20")["primary_tb"] == "TB-7")
    check("Every row has a primary boundary or component (C4, by construction)",
          all(r["primary_tb"] for r in rows))

    # --- Internal consistency (codebook) ---
    bad_arch = [(r["id"], r["archetype"], r["primary_tb"]) for r in rows
                if r["primary_tb"] not in ARCHETYPE_TB.get(r["archetype"], set()) and r["primary_tb"] != "LLM"]
    check("Archetype matches the paper's boundary attachment (A1: TB-5..7; A2: TB-3/4; A3: TB-1/4/8)",
          not bad_arch, "; ".join(f"{i} {a}@{t}" for i, a, t in bad_arch) or "all consistent")
    ant_ing = [r["id"] for r in rows if r["subset"] == "ANT" and r["ingestion_broad"] != "N"]
    foc_ing = [r["id"] for r in rows if r["subset"] == "FOCAL" and r["ingestion_broad"] != "Y"]
    check("Broad ingestion: N for all antecedents, Y for all focal rows", not ant_ing and not foc_ing)
    tbd = [r["id"] for r in rows if r["ingestion_broad"] == "TBD"]
    out_notes = [f"- Broad-ingestion coding still TBD for {len(tbd)} MCP-cluster rows: {', '.join(tbd)}."]
    draft = [r["id"] for r in rows if r["archetype_status"] == "draft"]
    out_notes.append(f"- Archetype assigned for this supplement (not named in the paper) on {len(draft)} rows: {', '.join(draft)}.")
    verify = [r["id"] for r in rows if r["verify_notes"].strip()]
    out_notes.append(f"- Rows carrying a verify note: {len(verify)} ({', '.join(verify)}).")

    # CVSS snapshot (paper Sec. 1 and 3-B; basis: CVSS v3.1 as recorded on 21 Aug. 2026,
    # NVD score where NVD has one, otherwise the CNA score marked C; MCP Inspector v4.0 only)
    if os.path.exists(CVSS):
        cv = list(csv.DictReader(open(CVSS, newline="")))
        paper_scores = {"CVE-2025-49596": "9.4", "CVE-2025-54136": "8.8", "CVE-2025-68143": "8.8",
                        "CVE-2025-68144": "7.1", "CVE-2025-68145": "9.1", "CVE-2025-6514": "9.6",
                        "CVE-2025-8217": "4.0", "CVE-2026-4269": "7.5"}
        got = {r["cve"]: r["score"] for r in cv}
        check("CVSS snapshot holds the eight MCP-cluster records with the paper's scores",
              got == paper_scores, "; ".join(f"{k} {v}" for k, v in sorted(got.items())))
        crit_high = [r["cve"] for r in cv if r["severity"] in ("Critical", "High")]
        check("Seven of eight CVE records rated Critical or High (Sec. 1)", len(crit_high) == 7,
              f"{len(crit_high)} Critical/High; Medium: " + ", ".join(r["cve"] for r in cv if r["severity"] == "Medium"))
        c_marked = sorted(r["cve"] for r in cv if r["marked_c_in_paper"] == "yes")
        out_notes_cvss = f"- CVSS snapshot: {len(cv)} records as of 2026-08-21; CNA-scored (marked C in the paper): {', '.join(c_marked)}."
    else:
        out_notes_cvss = None

    # Citation keys exist in the bib
    if os.path.exists(BIB):
        bib = open(BIB).read()
        keys = set(re.findall(r"@\w+\{([^,]+),", bib))
        missing = [(r["id"], k) for r in rows for k in r["citation_keys"].split(";") if k not in keys]
        check("Every citation key exists in references.bib", not missing, "; ".join(f"{i}:{k}" for i, k in missing) or "all found")

    # Matrix and screening log status
    if os.path.exists(MATRIX):
        mx = list(csv.DictReader(open(MATRIX, newline="")))
        filled = sum(1 for m in mx if m["category"])
        out_notes.append(f"- Elicitation matrix: {filled} of {len(mx)} rows populated (8 published in the paper).")
    if os.path.exists(LOG):
        lg = list(csv.DictReader(open(LOG, newline="")))
        exc = [l for l in lg if l["outcome"] == "excluded" and not l["candidate"].startswith("(")]
        c4only = [l for l in exc if l["excluded_at"] == "C4"]
        out_notes.append(f"- Screening log: {len(exc)} excluded candidates recorded; {len(c4only)} excluded at C4 alone. "
                         "Excluded candidates carry the reason recorded at assembly.")

    if out_notes_cvss:
        out_notes.append(out_notes_cvss)
    report = ["# Corpus validation report", "",
              "Generated by `validation/check_corpus.py` from `corpus/corpus.csv`. Re-run after any change to the corpus.", "",
              "## Paper claims and codebook consistency", "", "| Check | Result | Detail |", "|---|---|---|"] + out + \
             ["", f"**Overall: {'all checks pass' if ok_all else 'one or more checks FAIL'}.**", "",
              "## Status notes", ""] + out_notes
    text = "\n".join(report) + "\n"
    print(text)
    if write:
        open(os.path.join(HERE, "VALIDATION_REPORT.md"), "w").write(text)
    return 0 if ok_all else 1

if __name__ == "__main__":
    sys.exit(main("--write" in sys.argv))
