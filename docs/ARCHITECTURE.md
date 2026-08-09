# Architecture

**Status:** MVP stack approved; retrieval implementation does not exist yet.

## Approved retrieval flow

```text
Original query
  → query planner/rewriter (preserve and log original)
  → lexical retrieval + dense retrieval
  → rank fusion
  → rerank top candidates
  → evidence/abstention gate
  → answer generation (only after retrieval evaluation)
```

The evaluation path measures each retrieval variant before trusting an answer:

```text
query set → baseline/retrieval variants → relevance metrics → human review
```

## Approved MVP stack

- Python 3.12 CLI/library first; add an HTTP API only after the pipeline is measured.
- SQLite 3.45.1 FTS5 for lexical retrieval and metadata.
- `sentence-transformers/all-MiniLM-L6-v2` with normalized vectors and exact NumPy cosine comparison.
- `cross-encoder/ms-marco-MiniLM-L-6-v2` for local reranking of the fused top 20.
- Reciprocal Rank Fusion with fixed `k=60`.
- JSONL for corpus metadata, golden queries, judgments, and experiment results.
- Human-authored rewrites first; no external LLM call in the initial benchmark.

The vector database, ANN index, PostgreSQL/pgvector, or OpenSearch remain migration options when measured corpus size or latency requires them.

## Domains and entry points

| Domain | Owns | Entry points | Related docs |
|---|---|---|---|
| Ingestion | Markdown documents, stable chunk IDs, and later PDF experiments | `data/corpus/` | `PROJECT.md`, `../data/README.md` |
| Retrieval | Lexical, dense, fusion, and reranking | `UNKNOWN` (not implemented) | `system-design/TOPICS.md`, `decisions/ADR-002-approved-mvp-stack-and-evaluation-data.md` |
| Evaluation | Golden queries, qrels, metrics, and experiment comparisons | `data/golden/` and `scripts/validate_data.py` | `EVALUATION.md` |
| Answering | Evidence-gated response generation | `UNKNOWN` (deferred) | `SECURITY.md`, `EVALUATION.md` |

## Boundaries and invariants

- The original query is preserved; rewrites are experimental inputs, not replacements.
- Retrieved evidence remains distinguishable from generated answers.
- Retrieval quality and answer quality are measured separately.
- An answer may synthesize multiple cited sources but may not invent unsupported facts.
- No architecture component is selected without a stated constraint and evidence.

## Design register

| Topic | Status | Reason/evidence | Decision |
|---|---|---|---|
| Query rewriting | `selected` | Core project goal; compare against original-query baseline | ADR-002 |
| Hybrid retrieval | `selected` | Core project goal; compare lexical and dense baselines | ADR-002 |
| Reranking | `selected` | Core project goal; evaluate quality/latency trade-off | ADR-002 |
| Answer generation | `deferred` | Must follow retrieval evaluation and evidence gating | EVALUATION.md |
| Semantic caching | `unknown` | Depends on repeated-query and freshness measurements | `UNKNOWN` |
| Multi-agent workflow | `deferred` | No need before the single retrieval loop is measured | `UNKNOWN` |
