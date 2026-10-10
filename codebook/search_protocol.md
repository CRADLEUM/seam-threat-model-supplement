# Search and screening protocol

Reviewer 2 (IPCCC 2026) asked for the search process, exclusions, and coding rules to be documented. The coding rules are in `CODEBOOK.md`; this file covers search and screening. It is transcribed from the authors' assembly records: the earlier bibliography review and the log of the AI-assisted search session of 2026-05-06.

## Two collection stages

| Stage | What it was | Incidents it supplied |
|---|---|---|
| 1. Bibliography review | The author's earlier 84-source literature review for the same threat model, compiled before the 2026-05-06 search | 7: EchoLeak, Salesloft Drift, CVE-2025-55241 Entra Actor token, Storm-0558, CVE-2023-36019, Slack AI, Gemini memory |
| 2. AI-assisted search (session of 2026-05-06) | A systematic-review-style scan run with an AI research assistant (Claude Opus 4.7, Anthropic) under the author's direction, with a single screener. It applied its own rules: topical fit, novelty against the bibliography, recency (disclosures dated 2022-04-01 to 2026-05-06), source quality (peer-reviewed venue, standard, primary vendor advisory plus NVD record, or named-attribution incident report), and verification of every retained item against its primary publisher URL | 14: the six MCP CVE-cluster rows (MCP Inspector, Cursor, mcp-server-git, mcp-remote, Amazon Q Developer, Bedrock AgentCore), CircleCI, Okta, GitHub-Heroku-Travis, ASCII Smuggling, AgentFlayer, Custom GPT SSRF, OpenAI Codex, Notion AI |

No incident was added after the AI-assisted stage. The matrix row T-10 (mcp-server-git at TB-4), added on 2026-07-19, was a coding change for an incident already in the corpus, not an addition.

## Sources queried in the AI-assisted stage

| Source class | Databases and sites queried | Window |
|---|---|---|
| Peer-reviewed and preprint | arXiv, IEEE Xplore, ACM Digital Library, USENIX, NDSS Symposium, OpenReview, ACL Anthology, Springer LNCS, Semantic Scholar | disclosures dated 2022-04-01 to 2026-05-06 |
| Vulnerability records | NVD | same |
| Standards and government | NIST CSRC; CSRB and CISA reports reached through it and through web search | same |
| Vendor advisories and incident reports | MSRC, AWS Security Bulletins, Mandiant / Google Cloud Threat Intelligence blog, and the security-advisory pages of Atlassian, Notion, Slack, OpenAI (Bugcrowd), Anthropic, and Microsoft Copilot Studio | same |
| Practitioner disclosures | Reached through web search on Google's index followed by a direct fetch of the publisher's page (Embrace The Red, PromptArmor, Zenity Labs, Aim Labs, BeyondTrust Phantom Labs, Outsider Security, Oligo, JFrog, Check Point Research, and independent researcher posts) | same |

The bibliography-review stage drew on the same source classes; its items were re-verified against their primary URLs during the 2026-05-06 session.

## Query strings (incident lane, as logged)

The session log records the following strings for the incident and CVE lane; the literature lanes (defenses, RAG poisoning, non-human identity) are omitted here because they did not supply corpus rows.

- `CircleCI January 2023 incident report security breach session token customer environment`
- `Okta support system breach October 2023 BeyondTrust Cloudflare 1Password session token`
- `GitHub OAuth tokens stolen April 2022 Heroku Travis CI npm incident report`
- `"ASCII smuggling" Microsoft Copilot prompt injection invisible characters disclosure 2024`
- `Bargury "Copilot Studio" agent hijacking DEF CON 33 2025 vulnerability disclosure`
- `"MCP" Model Context Protocol CVE vulnerability 2025 server tool`
- `"Model Context Protocol" MCP security analysis 2025 attack tool poisoning`
- `"mcp-remote" CVE OAuth proxy`; `"MCP Inspector" RCE`; `"Cursor" CVE MCP config`
- `"ChatGPT" "GPT Actions" OR "Custom GPT" vulnerability OAuth disclosure 2024 2025`
- `"AWS Bedrock" OR "AWS Q Business" agent prompt injection vulnerability CVE 2024 2025`; `"AWS Q Developer" CVE-2025-8217`; `"AWS Bedrock AgentCore" CVE 2026`
- `"Slack AI" OR "Slack Lists" prompt injection vulnerability 2024 2025 disclosure`
- `"Notion AI" OR "Linear" OR "ClickUp" AI agent vulnerability disclosure 2024 2025`
- `"Atlassian" Rovo OR Confluence AI vulnerability CVE 2024 2025 advisory`
- `Salt Labs ChatGPT plugin OAuth`

For each CVE the session fetched the NVD record and the vendor advisory and noted NVD-versus-CNA score differences; for each incident report it fetched the primary writeup. No alerting service or feed is recorded in the session log.

## Screening

The corpus was collected in two stages, a bibliography review and a later AI-assisted search with its own topical, recency, source-quality, and verification rules, and admitted under the paper's criteria C1-C5, which restate the four admission rules used during assembly (public documentation, window, codability, seam relevance).

`screening_log.csv` holds one row per candidate. The 21 admitted incidents carry their C1-C5 coding. Candidates excluded during assembly are itemized with the reason actually recorded at the time. Their C1-C5 columns are blank because they were excluded under the search's own rules or by author decision, not assessed against C1-C5. One exclusion, ChatGPT plugin OAuth (Salt Labs, 2024), was an author decision to keep the seven-incident antecedent set and reference list stable, not a failure of any criterion.

The AI-assisted stage's own screen had a single screener; the author made every admission decision. The paper discloses the AI assistance in Section 3-D and through the venue's submission form.

## What this protocol is not

The corpus is a screened set, not a sample. Counts derived from it (the six-of-seven pattern, the two WB-S anchors) describe the corpus and are not prevalence estimates. Disclosure bias is a known alternative explanation for the exfiltration-over-persistence asymmetry: exfiltration is easier to demonstrate and publish than persistence into a system of record.
