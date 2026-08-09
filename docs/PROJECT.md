# Project Definition

## Goal

Build a research prototype for hybrid search with reranking. The system should rewrite or plan a query before retrieval, measure retrieval quality, and gate answer generation until the evidence is trustworthy.

## Primary user

The project owner, initially as a learning and interview-preparation project.

## Phase

Research prototype.

## Approved MVP

- An 18-document synthetic English Atlas corpus split into 54 stable heading chunks.
- A 44-query golden-set draft: 28 development and 16 held-out test queries, including 12 intentionally unanswerable cases; owner review is pending.
- Keyword and semantic retrieval, rank fusion, and cross-encoder reranking.
- Human-authored query rewrites evaluated alongside the preserved original query.
- Evidence-first answers with abstention when required evidence is insufficient.

PDF ingestion is a later experiment. Clean Markdown/text is the first boundary so retrieval quality is not confused with PDF extraction quality.

## In scope

- Retrieval pipeline and experiments.
- Retrieval-quality measurement before answer generation.
- Source citations and groundedness checks.
- Comparisons between lexical-only, dense-only, hybrid, reranked, and rewritten-query retrieval.

## Out of scope for the MVP

- Production multi-tenancy.
- Autonomous external actions.
- Multi-agent orchestration.
- Production-scale distributed infrastructure.

## Current constraints and unknowns

- Stack: approved in ADR-002; runtime dependencies and model weights still need setup.
- Corpus size and latency target: retrieval latency remains to be measured, not guessed.
- Data: 18 synthetic English Markdown documents; no private enterprise data; PDF ingestion is deferred.
- Privacy: local-first, with no runtime external provider in the initial benchmark.

## Success criteria

- Hybrid retrieval is compared fairly against lexical-only and dense-only baselines.
- Reranking improves held-out retrieval quality without unacceptable latency.
- Query rewriting is evaluated against the original-query baseline rather than trusted automatically.
- Every accepted answer is supported by retrieved evidence; unsupported questions produce abstention.
- Human labels establish the initial answer-quality and judge-calibration baseline.
