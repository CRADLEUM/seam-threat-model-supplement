# Eight candidate, non-normative SP 800-53 Rev 5 control enhancements

None of these is in the published NIST SP 800-53 Rev 5 catalog. They are proposed for standards-track review as sequentially numbered candidates under existing controls. Numbering is provisional and would be assigned by NIST if adopted.

Blocks follow the temporal layering of the corpus: Block I (drift-universal) is justified by the seven pre-agentic antecedents alone; Block II (AI-agent-bounded) by the fourteen agent-mediated incidents; Block III (bridging) applies regardless of carrier.

| Candidate | Block | Mode(s) | Mechanism | Corpus evidence anchor |
|---|---|---|---|---|
| AC-3(16) Cross-Domain Composition | I | Drift | Cross-PEP record of composed privilege, reconciled against the authorizing official's baseline | Salesloft Drift, CircleCI, Okta, GitHub-Heroku-Travis |
| AC-6(11) Agent-Level Least Privilege | I | Drift | Per-task capability tokens; expire on completion; the agent audited as its own subject | AgentFlayer |
| IA-13(4) IdP/Integrator Resilience | I | Drift | Anomalous-issuance monitoring; tenant-of-origin validation | Storm-0558, Entra Actor token, Salesloft Drift |
| AC-4(33) AI-Mediated Information Flow | II | WB-S, Exf | Signed provenance on every LLM-mediated flow; reject if unverified | Notion AI (WB-S), EchoLeak (Exf) |
| AC-16(11) AI Content Provenance Attributes | II | WB-S | Runtime-bound signed provenance manifest (PROV-DM) verified at flow points | Gemini memory |
| SI-7(18) Corpus and Memory Integrity | II | WB-S, SC | Provenance validation on retrieval; anomalous-write detection; rollback | AgentPoison (literature), Gemini memory |
| SI-10(7) AI System Input Validation | II | Exf | Channel separation; pattern filtering; capability-based effect limits | AgentFlayer, EchoLeak |
| SC-7(30) Logical Integration Boundary | III | all | Logical policy enforcement point at the seam that parses capability and provenance bindings | EchoLeak, AgentFlayer, mcp-server-git |

Anchor counts: AC-16(11) rests on one corpus anchor; AC-4(33) on one anchor per mode it covers. Generalization beyond the corpus leans on the provenance (PROV-DM, C2PA) and RAG-poisoning (Morris II, AgentPoison) literature.

## The binding-and-parsing trio

Any cross-domain agent write or release must (1) establish what authority it rides, (2) establish where its content originated, and (3) pass an enforcement point that reads both. These obligations map one-to-one onto AC-6(11), AC-16(11), and SC-7(30). Within this decomposition no pairwise subset suffices:

| Subset | Gap | What the gap leaves open |
|---|---|---|
| AC-6(11) + AC-16(11), no SC-7(30) | Two verifiable bindings that nothing at the seam is obligated to parse | Step (iv): the outbound fetch still leaves |
| AC-6(11) + SC-7(30), no AC-16(11) | The PEP confirms an authorized agent but has no lineage by which to recognize external content in the flow | The check at step (iv) is lost; where the write itself is authorized, as in Notion AI, attacker-influenced content enters the system of record as genuine |
| AC-16(11) + SC-7(30), no AC-6(11) | Lineage is checked but the authority the content rides was never bound to a task | Step (iii): composed privilege stands |

**Assumptions.** The agent runtime can mint task-scoped credentials; ingestion points can attach signed lineage that survives retrieval; every cross-domain flow traverses a PEP. The argument is a decomposition argument under these assumptions, not a formal proof. The claim is joint necessity within the decomposition, not sufficiency for secure composition.

## Standards readiness

AC-16(11) builds on W3C PROV-DM and the C2PA signed-manifest pattern and is the lowest-barrier pilot. AC-6(11) and SC-7(30) depend on capability-mediation patterns (CaMeL, IsolateGPT) that have not reached production at federation scale; authorizing officials adopting them must accept implementation-pattern compliance until standardization.
