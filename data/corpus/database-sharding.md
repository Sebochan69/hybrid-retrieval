---
doc_id: doc-database-sharding
title: Database Sharding Policy
source_type: synthetic
version: "1.0"
domain: data
sensitivity: public
---

# Database Sharding Policy

## Shard Key

The proposed shard key is a stable hash of `tenant_id`. Every tenant's transactional rows stay on one shard, which keeps the common tenant-scoped order query local. Cross-tenant joins are not a supported fast path and must be handled as an explicit application workflow.

## Resharding

Shard routing uses virtual buckets so a bucket can move without changing every tenant's hash. During a move, the router sends writes through the migration coordinator and verifies a checksum before declaring the bucket complete. The experiment does not assume that resharding is free or invisible.

## Hot-Tenant Handling

A single very large tenant can still create a hot bucket even with a good hash. The first response is to measure and isolate that tenant's workload; splitting a tenant across shards is a separate data-model decision. Sharding is not selected for the research MVP merely because the topic exists.
