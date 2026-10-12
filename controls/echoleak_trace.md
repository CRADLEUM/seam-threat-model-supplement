# Worked trace: EchoLeak (CVE-2025-32711) across the seam

EchoLeak is coded Drift+Exf at TB-5 (corpus row I16). The trace below is the paper's Sec. 5-A in tabular form, with each step tied to the boundary it crosses, the archetype, and the control that interdicts it. The narrative stays within the public NVD record and the Aim Labs disclosure, which the paper's Sec. 5-A follows.

| Step | What happens | Boundary | Mode | Control that addresses it | Without that control |
|---|---|---|---|---|---|
| (i) | An A1 adversary mails the victim a message whose embedded instructions read as if addressed to the human reader. Delivery is legitimate; no boundary is violated, but instruction-bearing content now sits in a store the agent retrieves from. | none violated | (precondition) | AC-16(11) marks the message as external, unauthenticated lineage at ingestion | Content enters the retrieval corpus with no lineage |
| (ii) | The user asks the copilot a routine question; retrieval pulls the crafted message into model context. It crosses as data and arrives as instructions. | TB-1 (request), TB-6 (retrieval) | ingestion (broad) | AC-16(11): lineage travels with the content into context | The PEP later cannot recognize A1-origin content in the flow |
| (iii) | The injected instructions execute under the agent's delegated identity. The authority exercised for the external author is the union of the victim's scopes (mail, files, chat). Neither platform's review records any grant to that author. | TB-5 | Drift | AC-6(11): a token scoped to the user's question does not carry the breadth the instructions harvested | Composed privilege stands |
| (iv) | The instructions direct the agent to embed sensitive retrieved content in a rendered image reference whose automatic fetch reaches an attacker-observable endpoint through an allow-listed domain. No user click. | TB-5 | Exf | SC-7(30): the seam PEP refuses a High-confidentiality release whose lineage includes A1 content | The fetch leaves |

## A legitimate request passes the same checks

If the user instead asks the copilot to summarize that email, the task-scoped token covers the read, the summary carries the message's external lineage, and no High-confidentiality release crosses the seam, so the PEP admits it. The controls interdict the exfiltration chain, not ordinary use of the retrieved content (paper Sec. 5-A; IPCCC Reviewer 2, major 3).

## What the trace does and does not show

It shows the model's mechanics on one documented incident and why each of the three controls is needed for this chain. It is not an empirical evaluation of the controls: this paper reports no implementation, and the trace does not establish that the trio is sufficient against variants (for example, an exfiltration channel the PEP does not sit on).

## Validation path

Ongoing thesis work implements the trio and evaluates it across models, environments, and control regimes. That work, not this trace, is where the controls' effectiveness will be tested.
