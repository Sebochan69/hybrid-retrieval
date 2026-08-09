---
doc_id: doc-query-planning
title: Query Planning and Rewrite Policy
source_type: synthetic
version: "1.0"
domain: ai-retrieval
sensitivity: public
---

# Query Planning and Rewrite Policy

## Rewrite Goal

A query rewrite may expand an abbreviation, expose an implied technical term, or make a constraint explicit. It must preserve the entities, polarity, time range, and user intent of the original. It is a retrieval hypothesis, not a new answer.

## Example Rewrite

The original question `How do we stop checkout from hanging on a bad dependency?` can be tested with the rewrite `checkout dependency failure timeout and circuit-breaker behavior`. The rewrite exposes likely retrieval vocabulary, while the original remains in the experiment record and is still evaluated.

## Rewrite Safety

A rewrite is rejected when it invents a service, changes a negation, drops a required condition, or adds an unsupported numeric value. The evaluator must retain the rewrite text, method, and intent label so an apparent retrieval lift can be traced to the transformation rather than accepted blindly.
