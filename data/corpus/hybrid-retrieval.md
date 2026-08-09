---
doc_id: doc-hybrid-retrieval
title: Atlas Search Retrieval Pipeline
source_type: synthetic
version: "1.0"
domain: ai-retrieval
sensitivity: public
---

# Atlas Search Retrieval Pipeline

## Candidate Generation

The search service generates a lexical candidate list with SQLite FTS5 BM25 ranking and a dense candidate list with normalized embedding cosine similarity. The initial experiment takes the top 20 from each list and removes duplicate chunk IDs before fusion.

## Rank Fusion and Reranking

The first hybrid path uses Reciprocal Rank Fusion with a fixed `k=60`; it does not compare raw BM25 scores with cosine scores directly. A cross-encoder then reranks the fused top-20 candidates. Candidate generation and reranking latency are recorded separately.

## Query Inputs and Provenance

The original user query is always stored and retrieved as the baseline. A rewrite is an additional experiment input and never silently replaces the original. Each returned chunk carries a stable source ID and heading so an answer can cite the evidence that was actually retrieved.
