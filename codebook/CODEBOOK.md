# Codebook: corpus inclusion and coding rules

This is the written rule set under which the 21-incident corpus in `corpus/corpus.csv` was coded. The definitions are those of the paper (Sections 1, 3, and 4). The decision rules under each definition state how the definition was applied to a candidate incident. Anyone re-coding the corpus should apply these rules without reference to the coding already recorded, then compare against `corpus/corpus.csv`.

Coding was performed by a single analyst (the first author). See `validation/single_coder_statement.md` for what that design can and cannot claim.

## 1. Inclusion criteria

An incident enters the corpus only if it satisfies all five criteria.

| ID | Criterion | Decision rule |
|---|---|---|
| C1 | Citable public record | At least one of: NVD/CVE record, vendor advisory or incident report, standards-body or government report, peer-reviewed publication, or a practitioner disclosure with a stable URL. Rumor, social-media-only claims, and paywalled-only coverage do not satisfy C1. |
| C2 | Date in the 2022--2026 window | Date of the primary disclosure or incident report, not the date of the underlying activity if different. |
| C3 | Instantiates at least one failure mode or the supply-chain precondition | Apply the mode decision rules in Section 3 below. An incident that fits none is excluded. |
| C4 | Attaches to at least one of the eight reference trust boundaries | Apply the boundary rules in Section 4 below. An incident whose exploited trust transition is not an arc of the reference DFD is excluded. **Because C4 is an inclusion criterion, "every corpus incident attaches to a boundary" is true by construction and is not evidence that the eight boundaries are complete.** The screening log should record any candidate excluded by C4 alone; such exclusions are the only corpus-based signal about boundary completeness. |
| C5 | Federated or cross-domain authority relationship | The incident exercises authority across at least two authorization domains (tenants, platforms, integrator and customer, IdP and relying party), or across a delegated-agent boundary within a federated deployment. Single-domain flaws (a bug inside one application with no delegated or federated authority involved) are excluded. C5 is deliberately broader than the paper's target topology; see Section 6 (topology codes). |

Pre-agentic incidents (no AI agent in the chain) are admitted under C5 by design, to test whether privilege drift depends on an AI-agent carrier.

## 2. Source-quality codes

One code per incident, recording the **primary** source on which the coding rests.

| Code | Meaning | Rule when several sources exist |
|---|---|---|
| PR | Peer-reviewed publication | Use only if the peer-reviewed source is the primary disclosure or independently reproduces the finding. A secondary review article that merely summarizes a practitioner disclosure does not earn PR (Slack AI was recoded PR to PB on 2026-10-09 for this reason; no corpus row now carries PR). |
| STD | Standards body or government report | For example, a CSRB report. |
| NVD | NVD/CVE record | Use when the CVE record is the primary citable artifact, even if a vendor or researcher write-up is also cited. |
| VEN | Vendor advisory, incident report, or vendor-presented research | Includes vendor-published conference research (for example, a Black Hat talk by a vendor's researchers). |
| PB | Practitioner disclosure (blog, independent research post) | Includes CVE-indexed practitioner disclosures where the blog is the primary source (flag these, as the paper does for CVE-2025-55241). |

## 3. Failure modes and the precondition class

An incident may carry more than one mode. Code every mode the evidence supports; do not stop at the first match. The "exact" two-mode signature used in the paper's modal-pattern count means Drift and Exf with no third mode.

### Drift (privilege drift)

**Definition (paper, Sec. 1).** Accumulation of effective authority across the seam between two authorization domains under a delegated identity, such that no single platform's access review granted the composed authority and no single platform's review surface can recover it.

**Decision rule.** Code Drift when all of the following hold:
1. Authority from at least two authorization domains, or from a delegating principal and a delegate, is composed in one actor (an agent, an integrator, a token holder).
2. The composed authority was exercised, or was demonstrably exercisable, for an effect no single domain's review had approved.
3. The composition is not visible to any one domain's role or scope review.

Token, session, or signing-key theft that lets a third party exercise another domain's authority satisfies the rule (the antecedent set). A consent that silently widens into unreviewed capabilities also satisfies it (the MCP cluster). An attack that stays inside one authorization domain with no delegation does not (compare Gemini memory, coded WB-S only, and Slack AI, coded Exf only).

### WB-S (write-back injection, strict)

**Definition (paper, Sec. 1).** Writing of attacker-influenced AI output into a system of record: an authoritative store whose contents a later agent action reads back as trusted input. Content rendered only into transient surfaces (chat output, browser markdown, a summarized response) does not qualify.

**Decision rule.** Code WB-S only when all three hold:
1. The AI output written was attacker-influenced.
2. The destination is an authoritative store (page, record, memory, knowledge base, configuration that an agent later reads).
3. The persisted content was, or by the platform's design would be, read back by a later agent action as trusted input.

If the attacker's content merely passed through the model's context and was rendered (the broad "poisoning" reading), code `ingestion_broad = Y` but not WB-S.

### Exf (delegated-agent exfiltration)

**Definition (paper, Sec. 1).** Data transiting out of the authorized domain through an AI-agent-mediated channel under the agent's delegated identity; the carrier is the tool-call surface, generated content, or rendered output.

**Decision rule.** Code Exf when data left the scope the victim had authorized and the channel was the agent's tool call, generated content, or rendered output. For pre-agentic incidents (no agent), do not code Exf even if data was stolen: the paper's Exf is agent-mediated by definition, and the antecedents are coded Drift only.

### SC (supply-chain compromise, precondition class)

**Definition (paper, Sec. 1).** Compromise of the integrator release pipeline, dependency store, or build process. Its downstream effect is one or more of the three modes.

**Decision rule.** Code SC when the root cause is a compromised release, dependency, or build artifact reaching downstream tenants. Code SC alone when the disclosure documents the precondition but not a realized downstream mode.

### Ingestion (broad reading)

Recorded in `ingestion_broad` to support the paper's strict-vs-broad discussion (Sec. 3-D). Code Y when the agent ingested attacker-controlled content as instruction-bearing at runtime, whether or not anything persisted. Code N when no agent ingestion step exists (the antecedents). The six MCP CVE-cluster rows are TBD pending the author's decision on whether client-side ingestion of server-returned content and supply-chain-delivered prompts count.

## 4. Reference DFD and trust boundaries

Elements: two external entities (User, External system), four processes (Host application, MCP client, MCP server, LLM-in-host-context), four data stores (Agent memory, Retrieval corpus, System of record, IdP/token store). The eight boundaries enumerate every arc where the principal, domain, or trust assumption changes. See `elicitation/dfd.md`.

| TB | Arc | Code here when the exploited trust transition is... |
|---|---|---|
| TB-1 | User to host (delegation) | the user's delegation to the host application |
| TB-2 | Host to MCP client | the host's handoff of authority to the client |
| TB-3 | MCP client to server (bidirectional) | the client-server channel, including server-returned content acting on the client |
| TB-4 | MCP server to external system (federation) | the server's or integrator's exercise of authority against an external system under delegated or stolen credentials |
| TB-5 | LLM to tool-call dispatch (capability) | the model's instruction-driven invocation of tools under the delegated identity |
| TB-6 | Memory and corpus retrieval into LLM | retrieval of stored content into model context, or writes into memory read back as context |
| TB-7 | LLM write-back to system of record | the model's write into an authoritative store |
| TB-8 | IdP to external system (federation) | token or assertion trust between the identity provider and a relying system |

**Primary boundary rule.** Record one primary boundary: the arc at which the first unauthorized crossing occurs. Where an incident spans several arcs (EchoLeak crosses TB-1, TB-6, and TB-5), the primary is the arc at which the composed authority is exercised for the attacker's effect (TB-5 for EchoLeak). Incidents whose locus is a component rather than an arc (the MCP server for supply-chain rows; the LLM for Slack AI) record the component name.

## 5. Adversary archetypes

| Code | Archetype | Paper's boundary attachment |
|---|---|---|
| A1 | External content author: publishes content the agent ingests as instruction-bearing | TB-5, TB-6, TB-7 |
| A2 | Integrator-side compromise: ships malicious code, configuration, or OAuth-app behavior through the connector, extension, or MCP-server supply chain | TB-3, TB-4 |
| A3 | IdP-side compromise: forges, replays, or abuses assertions or tokens at the federation seam | TB-1, TB-4, TB-8 |

A2 and A3 overlap at TB-4. Code the archetype from the **adversary's position**, not from the vulnerable component. `corpus/corpus.csv` records `archetype_status = paper` where the paper names the incident under an archetype and `draft` where the code was assigned for this supplement. `validation/check_corpus.py` flags any row whose archetype and primary boundary do not match the attachment table above; two rows currently do (see `validation/VALIDATION_REPORT.md`).

## 6. Coding procedure (as performed)

1. Candidate identified from the sources in `codebook/search_protocol.md` and entered in `codebook/screening_log.csv`.
2. C1 and C2 checked from the record's metadata.
3. C3: each mode's decision rule applied in the order Drift, WB-S, Exf, SC; every mode that fits is recorded.
4. C4: the exploited trust transition located on the reference DFD; primary boundary recorded.
5. C5: the cross-domain authority relationship confirmed from the cited sources.
6. Any doubt recorded in `verify_notes` rather than resolved silently.
7. Source-quality code assigned from the primary source.

Steps 1 and 2 were performed when the corpus was assembled. The archetype for rows the paper does not name and the broad-ingestion flag were written for this supplement and are marked for verification in `corpus/corpus.csv`.
