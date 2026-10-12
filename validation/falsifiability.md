# Falsification conditions

The paper commits to two claims that evidence could overturn. This file states each as a checkable condition, says what would count, and says where to look.

## F1. The modal pattern ("leak data, not poison data")

**Claim.** Within the corpus, multi-mode incidents pair privilege drift with delegated-agent exfiltration (six of seven), and strict write-back appears in two incidents only.

**Condition that refutes it.** A publicly disclosed vulnerability in an MCP-canonical implementation (reference servers, major clients, the Inspector, mcp-remote and peers) that instantiates strict write-back injection (attacker-influenced output persisted into a store later read back as trusted input) **without** co-occurring drift or exfiltration. One such case would show that the corpus had not yet recorded MCP-side persistence; a growing record of them would overturn the pattern.

**What does not refute it.** Write-back in adjacent ecosystems (the two existing anchors already sit there); transient rendering of attacker content (broad ingestion, which the paper reports as near-universal: seven of the eight agent-mediated incidents, all but the Custom GPT SSRF); write-back that co-occurs with drift or exfiltration (which the pattern already accommodates, as Notion AI shows).

**Where to look.** NVD records tagged to MCP components; vendor advisories from Anthropic, Cursor, and IDE vendors; practitioner disclosures that document a persistence step with a later trusted read.

## F2. The boundary enumeration

**Claim.** The eight trust boundaries enumerate every arc of the reference DFD at which principal, domain, or trust assumption changes, and every federated AI-agent compromise of the target deployment class attaches to at least one.

**Condition that refutes it.** A documented compromise of a federated AI-agent deployment (shared IdP, two platforms, delegated agent) whose exploited trust transition is not an arc of the reference DFD and cannot be placed at TB-1 through TB-8 without redrawing the diagram.

**What does not refute it.** An incident that attaches to a boundary the corpus has not yet populated (TB-2, for example): that fills a cell rather than breaking the enumeration. A single-domain flaw (fails C5): outside the model's scope by design.

**Where to look.** The screening log: a candidate meeting C1, C2, C3, and C5 but excluded at C4 is exactly this evidence. Its absence from the log is the only corpus-based support for the claim, which is why the log must record exclusions and not only inclusions.

## Reporting

Either condition, if met, should be recorded as a new row in `codebook/screening_log.csv` with the outcome and the boundary or mode at issue, and `validation/check_corpus.py` re-run. The paper's claims are stated so that this is the whole procedure.
