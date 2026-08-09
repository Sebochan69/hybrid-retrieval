---
doc_id: doc-capacity-plan
title: Capacity and Migration Triggers
source_type: synthetic
version: "1.0"
domain: scalability
sensitivity: public
---

# Capacity and Migration Triggers

## Baseline Envelope

The local research envelope is one learner, batch indexing, roughly 100 to 500 documents, and roughly 5,000 to 50,000 chunks. Warm-query latency is measured with model-load time reported separately. These numbers are an experiment envelope, not a production sizing promise.

## Scale Triggers

The dense baseline remains an exact NumPy scan while it fits the measured envelope. An ANN index becomes worth testing only when exact scanning creates a measured p95 regression, initially defined as more than 100 ms at the target corpus size. A vector database is a migration option, not a prerequisite.

## Growth Boundaries

Database sharding, queues, and an API service are deferred until corpus size, write rate, concurrent users, or operational requirements make the simpler local path insufficient. A topic is not a requirement merely because it appears in a system-design checklist. Any migration must reproduce the golden evaluation before it is accepted.
