# System Design Topics

These are design choices, not mandatory features. Select them only when project constraints justify them.

| Topic | Status | Why it matters | Evidence/decision | Revisit trigger |
|---|---|---|---|---|
| Load balancing | not-applicable | No deployed service in the local MVP | ADR-002; local CLI/library | A network service is measured |
| Caching | unknown | Depends on repetition, latency, and freshness | `UNKNOWN` | `UNKNOWN` |
| Database replication | not-applicable | Corpus/index rebuild is local and single-writer | ADR-002; SQLite FTS5 | Index availability needs redundancy |
| Database sharding | not-applicable | Research MVP has no distributed database requirement | Proposed MVP scope | Corpus/write scale requires it |
| Message queue | not-applicable | Batch ingestion is sufficient initially | Proposed MVP scope | Ingestion must be asynchronous or burst-tolerant |
| Event-driven architecture | not-applicable | No event-driven product workflow yet | Proposed MVP scope | Multiple independently owned consumers appear |
| API gateway | not-applicable | Start with a local CLI/library | Proposed MVP scope | A network API and multiple edge policies are needed |
| Circuit breaker | not-applicable | Initial runtime has no external provider call | ADR-002; local inference | A provider becomes part of the runtime path |
| Rate limiting | not-applicable | No external API or multi-user service in the MVP | ADR-002; local CLI/library | External API exposure is added |
| Consistent hashing | not-applicable | No distributed key routing requirement | Proposed MVP scope | Sharded retrieval/cache layer is introduced |
| CDN | not-applicable | No geographic content delivery requirement | Proposed MVP scope | Hosted user-facing content is added |
| Database indexing | selected | Retrieval needs lexical indexing and metadata lookup | ADR-002; SQLite FTS5 | Query/corpus size exceeds local index envelope |
| CAP/distributed-systems trade-offs | deferred | Useful for later scale-out, not an MVP constraint | Proposed MVP scope | Replication or multi-node storage is selected |
| Query rewriting | selected | Core goal: transform/plan queries before index access | ADR-002; manual rewrite hypotheses | Rewrite harms held-out retrieval quality |
| Hybrid search with reranking | selected | Core project goal | ADR-002; fixed RRF and local reranker | Retrieval quality/latency evidence changes the design |
| Enterprise retrieval | selected | Target problem shape; start with synthetic data | ADR-002; synthetic Atlas corpus | Permissions and tenancy become real requirements |
| Multi-agent research assistant | deferred | No need before the single retrieval loop is measured | Project intake | A bounded multi-role workflow has a measured benefit |
| LLM-as-judge with human calibration | deferred | Human labels must establish the first baseline | EVALUATION.md; ADR-002 | Evaluation volume justifies calibrated assistance |
| Semantic caching for LLM APIs | unknown | Depends on repeated queries, cost, and freshness | `UNKNOWN` | Answer generation becomes a measured bottleneck |
| Guardrails and hallucination detection | selected | Answers must be evidence-gated and abstain when unsupported | EVALUATION.md; SECURITY.md | Production threat/evaluation scope expands |
