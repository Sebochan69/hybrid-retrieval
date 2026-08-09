# ADR-001: Retrieval-First Research MVP

- **Status:** accepted
- **Date:** 2026-08-08

## Requirement

Study and demonstrate hybrid retrieval with query rewriting, reranking, and retrieval-quality measurement before trusting generated answers.

## Assumptions

- One learner is the initial user.
- The first corpus is synthetic enterprise-like documents and/or public PDFs.
- The first phase is a local research prototype.
- Corpus size and latency targets will be measured rather than guessed.

## Alternatives

1. Build an answer-generating chatbot first.
2. Start with a production vector database and API service.
3. Build a retrieval-first local pipeline with explicit baselines and evaluation.

## Proposed decision

Choose option 3:

```text
original query
  → logged query rewrite/planner
  → lexical + dense retrieval
  → rank fusion
  → cross-encoder reranking
  → evidence/abstention gate
  → answer generation after retrieval passes
```

Start with a lightweight local implementation:

- Python library/CLI before FastAPI;
- SQLite FTS5 for lexical retrieval and metadata;
- local embeddings and exact similarity for the small corpus;
- a cross-encoder reranker via `sentence-transformers` or FlagEmbedding;
- JSONL judgments and experiment results.

Use Markdown/text documents first to isolate retrieval quality. Add PDF extraction as a separate ingestion experiment, then consider PostgreSQL/pgvector, an ANN index, or OpenSearch only when measurements justify the operational cost.

## Trade-offs

- More transparent and educational than hiding the pipeline behind a vector database.
- Slower and less scalable than ANN/distributed retrieval.
- Query rewriting may improve recall but can also introduce drift, so the original query must remain the baseline.
- Human labels cost time but are necessary before trusting an LLM judge.

## Evidence required before acceptance

Compare:

- lexical-only;
- dense-only;
- hybrid fusion;
- hybrid plus reranking;
- rewritten-query variants.

Report Recall@k, MRR, nDCG@k, latency, citation correctness, unsupported-claim rate, and abstention behavior on a held-out set.

## Failure mode

A fluent answer can look correct even when retrieval missed the required evidence. The answerer must not be the first quality gate.

## Revisit trigger

Revisit the storage, model, and serving choices when corpus size, query volume, latency, multi-user permissions, or provider dependence becomes measurable.
