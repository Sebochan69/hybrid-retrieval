---
doc_id: doc-database-indexing
title: Transactional Database Indexing
source_type: synthetic
version: "1.0"
domain: data
sensitivity: public
---

# Transactional Database Indexing

## Order Query Index

The recent-orders query filters by `tenant_id`, sorts by `created_at DESC`, and uses `order_id` as a stable tie-breaker. Its supporting composite index is `(tenant_id, created_at DESC, order_id)`. The tenant column comes first so one tenant's recent orders can be found without scanning another tenant's rows.

## Write Cost

Each additional index speeds some reads but adds storage, page maintenance, and write work. Atlas does not index every column by default. An index is retained when an observed query shape and its measured improvement justify the write and storage cost.

## Search Boundary

Full-text search is not simulated by adding a collection of `LIKE` predicates to the transactional schema. Search text is maintained in the separate FTS5 retrieval index, while PostgreSQL indexes support transactional lookup and ordering. The two indexes can be rebuilt from their source records.
