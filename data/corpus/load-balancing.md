---
doc_id: doc-load-balancing
title: Stateless API Load Balancing
source_type: synthetic
version: "1.0"
domain: scalability
sensitivity: public
---

# Stateless API Load Balancing

## Routing Policy

The API fleet uses weighted least-outstanding-requests routing. A healthy instance with fewer active requests receives more traffic, while a configured weight accounts for different instance sizes. The policy is appropriate because the API tier keeps session state outside the process.

## Health Checks

A liveness check answers whether a process is running; a readiness check answers whether it can accept traffic. The load balancer removes an instance after failed readiness checks, but a liveness failure is also recorded for diagnosis. Health checks do not run business transactions.

## Failure Recovery

Routing is zone-aware and keeps a small amount of spare capacity in each zone. After an instance recovers, it is gradually reintroduced instead of receiving a full share immediately. Consistent hashing is not required for this stateless API path because requests do not depend on local session state.
