# ADR-002: Approved MVP Stack and Evaluation Data

- **Status:** accepted
- **Date:** 2026-08-08

## Requirement

Run a local, reproducible retrieval experiment for one learner before trusting answer generation. The experiment must compare lexical, dense, hybrid, reranked, and rewritten-query paths while preserving the original query.

## Assumptions

- The first corpus is English-only and synthetic; this isolates retrieval behavior from language and licensing variables.
- The initial corpus is small enough for exact dense similarity.
- Model weights are downloaded or provisioned once, then loaded locally; runtime inference does not call an external provider.
- The assistant can draft a complete qrel/claim set, but the project owner must review it before any LLM judge is introduced.

## Alternatives

1. Use an external hosted embedding/reranking or rewriting API.
2. Start with a vector database and ANN index.
3. Use a local Python pipeline with transparent indexes and a fixed evaluation set.

## Decision

Use the following MVP stack:

- Python 3.12 (the project environment was verified on Python 3.12.3).
- SQLite 3.45.1 FTS5 with the built-in `unicode61` tokenizer for lexical retrieval and metadata.
- `sentence-transformers/all-MiniLM-L6-v2` for the first local dense baseline; normalize vectors and compare them with an exact NumPy cosine scan.
- `cross-encoder/ms-marco-MiniLM-L-6-v2` for local reranking of a fixed top-20 candidate pool.
- Reciprocal Rank Fusion with a fixed `k=60` for the initial hybrid path; do not tune it on the held-out split.
- JSONL for the corpus manifest, golden queries, judgments, and experiment results.
- `pytest` for the eventual automated checks; PyMuPDF is optional and isolated to the later PDF-ingestion experiment.
- No external LLM query rewriting in the initial benchmark. The golden set contains human-authored rewrite hypotheses; a local or hosted rewrite model may be evaluated later only as a separately versioned experiment.

The initial data set is 18 synthetic English Markdown documents, split by heading into 54 stable chunks, and 44 query drafts: 28 development queries and 16 held-out test queries. Twelve queries are intentionally unanswerable. Human review is still required before this is called a frozen golden set.

## Evaluation invariants

- Every run stores `original_query` even when a rewrite is used.
- Original-query retrieval is the baseline. A rewrite is an additional input, never a replacement.
- Retrieval variants are evaluated on the same query IDs and qrels.
- The answerer receives retrieved evidence only after the evidence gate passes. Otherwise the result is abstention.
- Citation correctness and unsupported-claim labels remain pending human review until a judge is calibrated against them.

## Trade-offs

- MiniLM models are small and easy to run locally, but an English-only baseline does not establish Taglish or multilingual quality.
- Exact NumPy comparison is transparent and sufficient for this corpus, but it will not scale indefinitely.
- Manual rewrite hypotheses make the first comparison reproducible, but they do not measure the behavior of an LLM rewriter.
- Synthetic documents avoid privacy and licensing risk, but results do not establish enterprise-domain performance.

## Evidence

- Python 3.12.3 and SQLite FTS5 were present in the working environment on 2026-08-08.
- The corpus and draft golden-set contracts are stored in `data/README.md` and `data/golden/golden_queries.jsonl`.
- No source implementation or benchmark has run yet; model quality and latency remain unverified until the evaluation runner exists.

## Failure mode

A rewrite can introduce a new entity, polarity, or unsupported term and appear to improve retrieval on a small sample. The original query and a human-reviewed held-out set prevent silently accepting that regression.

## Revisit trigger

Revisit the embedding model, reranker, fusion constant, language policy, or storage when held-out quality, p95 latency, corpus size, repeated-query rate, or provider dependence supplies measurable evidence.
