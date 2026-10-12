# Reference data-flow diagram

Rendered in the paper as Fig. 1 (TikZ source: `dfd_figure.tex` in the paper's LaTeX).

## Elements

| Kind | Element | Notes |
|---|---|---|
| External entity | User | Delegating principal |
| External entity | External system | The second platform; reached through the MCP server under federated identity |
| Process | Host application | IDE, chat surface, or agent runtime |
| Process | MCP client | Instantiated by the host |
| Process | MCP server | Exposes tools, resources, prompts; executes against the external system |
| Process | LLM (in host context) | Receives tool results as new input |
| Data store | Agent memory | Persistent per-user or per-agent memory |
| Data store | Retrieval corpus | Documents, mail, chat retrieved into context |
| Data store | System of record | Authoritative store the agent can write to and later read from |
| Data store | IdP / token store | Shared identity provider and the tokens it issues |

## Arcs and the boundaries that cross them

| Arc | Direction | Boundary | Why the trust assumption changes |
|---|---|---|---|
| User to Host app | one-way | TB-1 | Delegation: the user's authority becomes the host's |
| Host app to MCP client | one-way | TB-2 | Host hands authority to a component that talks to servers |
| MCP client to MCP server | bidirectional | TB-3 | Results return as new model input; a server can act on the client |
| MCP server to External system | one-way | TB-4 | Server exercises federated credentials against another domain |
| MCP client to LLM | bidirectional | TB-5 | Model output becomes tool dispatch under the delegated identity |
| Agent memory and Retrieval corpus with LLM | memory: two-way (read and write); corpus: one-way retrieval | TB-6 | Stored content enters context as if trusted; model output written to memory is read back later as trusted (Gemini memory) |
| LLM to System of record | one-way | TB-7 | Model output persists into an authoritative store |
| IdP to MCP server; IdP to External system | one-way | TB-8 (IdP to external system) | Token trust across the federation; the IdP-to-server arc is inside the host's domain and carries no separate boundary |

Arcs internal to one trust domain carry no boundary. The enumeration is structural (every arc where principal, domain, or trust assumption changes), not derived from the corpus; its completeness is a falsifiable claim (`validation/falsifiability.md`).

## FIPS 199 asset ratings

Moved here from the regular-paper manuscript (Sec. 4-B) to meet the short-paper limit. C/I/A = confidentiality, integrity, availability; H = High.

| Asset | Rating | Role in the model |
|---|---|---|
| Agent memory | I-H | A1 ingestion surface; SI-7(18) target |
| Retrieval corpus | I-H | A1 ingestion surface; SI-7(18) target |
| System of record | C-H, I-H | TB-7 write-back endpoint; AC-16(11) target |
| IdP / token store | C-H, I-H, A-H | A3 target; IA-13(4) scope |
| LLM context window | C-H, I-H (in session) | A1 surface across TB-5 through TB-7 |

No asset rates Low on all three dimensions.
