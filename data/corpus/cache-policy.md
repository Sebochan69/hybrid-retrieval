---
doc_id: doc-cache-policy
title: Cache Policy
source_type: synthetic
version: "1.0"
domain: scalability
sensitivity: public
---

# Cache Policy

## Cache-Aside Reads

The catalog service uses cache-aside reads. It checks Redis first; on a miss, it reads the database, returns the value, and populates Redis with the selected key and expiry. The application, not Redis, decides which records are cacheable.

## TTL and Invalidation

Product catalog entries have a 60-second TTL. A catalog update also emits a versioned invalidation event so a changed item can be removed before its normal expiry. The invalidation event is a latency optimization; the database remains authoritative.

## Stale-Data Boundary

A cache hit can be up to 60 seconds old unless invalidation has already removed it. The platform does not cache payment status or authorization decisions because stale values in those paths can change correctness or security outcomes. A cache outage should reduce performance, not change the source-of-record result.
