# Plan 001: Retrieval-First MVP

## Objective

Build a small, measurable hybrid-retrieval pipeline before adding trusted answer generation.

## Scope

1. Create a synthetic enterprise-like Markdown corpus; evaluate PDF ingestion separately later.
2. Draft and human-review 30–50 labeled queries, including answerable and unanswerable cases.
3. Implement lexical-only and dense-only baselines.
4. Fuse candidates with a transparent rank-fusion method.
5. Add top-k reranking.
6. Add query rewriting as an experiment while preserving the original query.
7. Measure retrieval quality and latency.
8. Return evidence and abstention decisions before adding an answerer.

## Out of scope

- Production deployment.
- Multi-tenancy and document-level authorization.
- Multi-agent orchestration.
- Distributed databases, queues, sharding, and CDN infrastructure.
- Automatic LLM judging without human calibration.

## Approved implementation

- Python 3.12 CLI/library; add FastAPI only after the core is measured.
- SQLite 3.45.1 FTS5 for lexical retrieval and metadata.
- `sentence-transformers/all-MiniLM-L6-v2` for normalized dense vectors and exact NumPy similarity.
- `cross-encoder/ms-marco-MiniLM-L-6-v2` for local reranking of the fused top 20.
- Reciprocal Rank Fusion with fixed `k=60`.
- PyMuPDF only for the later PDF-ingestion experiment.
- JSONL for corpus metadata, queries, judgments, and results.
- Human-authored rewrites first; no external LLM call in the initial benchmark.

## Provisional evaluation envelope

Use this as a test envelope, not a permanent requirement:

- one user;
- roughly 100–500 documents;
- roughly 5,000–50,000 chunks;
- local batch indexing;
- warm-query latency measured at p50/p95, with model-load time reported separately.

Increase the envelope until the simple exact-scan implementation becomes the measured bottleneck.

## Verification path

Compare lexical-only, dense-only, hybrid, reranked, and rewritten-query variants using Recall@k, MRR, nDCG@k, latency, and human-reviewed evidence quality.

## Risks and blockers

- Runtime dependencies and model weights are not installed or loaded yet.
- PDF extraction noise may be mistaken for retrieval failure.
- A query rewrite may introduce unsupported terms or lower recall.
- Human judgment set must be created before an LLM judge is trusted.

## Progress

- [x] Project harness initialized.
- [x] Project goal and phase recorded.
- [x] Retrieval-first MVP proposed.
- [x] Intake and next-session handoff recorded.
- [x] Approve stack and initial model.
- [x] Create corpus and query-set draft.
- [ ] Human-review and freeze qrels, claims, and abstention labels.
- [ ] Implement baseline retrieval.

## Open decisions

- Exact warm-query latency distribution after the first implementation.
- Whether a second embedding/reranker model is justified by measured results.
- Whether to add a local or hosted rewrite model after the manual-rewrite benchmark.

## Next action

Implement ingestion and the SQLite FTS5 lexical baseline, then add the smallest runnable retrieval check.
