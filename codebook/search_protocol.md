# Search and screening protocol

**Status: reconstructed from the corpus's own sources; the author must confirm or correct each item before the supplement is released.** Reviewer 2 (IPCCC 2026) asked for the search process, exclusions, and coding rules to be documented. The coding rules are in `CODEBOOK.md`; this file covers search and screening.

## Sources searched

| Source class | What was searched | Window |
|---|---|---|
| NVD / CVE | Records for MCP clients and servers, IDE agent extensions, copilot products, OAuth integrators, and identity-provider components | 2022-01 to 2026-MM (author: fill end month) |
| Vendor advisories and incident reports | Microsoft, Google, Anthropic, OpenAI, Amazon, Salesforce/Salesloft, Okta, CircleCI, GitHub security blogs and advisories | same |
| Standards-body and government reports | CSRB, NIST, CISA | same |
| Practitioner disclosures | Embrace The Red (Rehberger), PromptArmor, Zenity Labs, Aim Labs, BeyondTrust Phantom Labs, Outsider Security, Oligo, JFrog, Check Point Research, independent researcher posts | same |
| Peer-reviewed | AISec, USENIX Security, NDSS, arXiv preprints later published | same |

Author: list the actual query strings used, if recorded (for example, NVD keyword queries such as `"Model Context Protocol"`, `MCP server`, `Copilot`, `prompt injection`, `OAuth token`), and whether any alerting service or feed was used.

## Screening

The corpus was collected in two stages, a bibliography review and a later AI-assisted search with its own topical, recency, source-quality, and verification rules, and admitted under the paper's criteria C1-C5, which restate the four admission rules used during assembly.

`screening_log.csv` holds one row per candidate. The 21 admitted incidents carry their C1-C5 coding. Candidates excluded during assembly are itemized with the reason actually recorded at the time. Their C1-C5 columns are blank because they were excluded under the search's own rules or by author decision, not assessed against C1-C5. One exclusion, ChatGPT plugin OAuth (Salt Labs, 2024), was an author decision to keep the seven-incident antecedent set and reference list stable, not a failure of any criterion.

## What this protocol is not

The corpus is a screened set, not a sample. Counts derived from it (the six-of-seven pattern, the two WB-S anchors) describe the corpus and are not prevalence estimates. Disclosure bias is a known alternative explanation for the exfiltration-over-persistence asymmetry: exfiltration is easier to demonstrate and publish than persistence into a system of record.
