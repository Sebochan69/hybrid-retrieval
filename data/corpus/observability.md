---
doc_id: doc-observability
title: Platform Observability Signals
source_type: synthetic
version: "1.0"
domain: operations
sensitivity: public
---

# Platform Observability Signals

## Retrieval Metrics

The search experiment records Recall@k, MRR, nDCG@k, candidate counts, reranker score, citation correctness, unsupported-claim rate, and abstention outcome. It keeps per-query results so an aggregate improvement cannot hide a regression on a safety-critical question.

## Request Tracing

A request ID is created at the gateway and a trace ID is propagated through services, database calls, cache lookups, queue publication, and answer generation. Timings distinguish model load, index access, candidate fusion, reranking, and answer generation.

## Operational Alerts

Initial alerts cover API p95 latency, error rate, cache hit rate, replica lag, queue lag, and evidence-gate abstentions. An alert is a signal to inspect; it is not itself proof of a root cause. Dashboards retain the relevant model, corpus, and index versions.
