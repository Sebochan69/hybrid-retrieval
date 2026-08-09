---
doc_id: doc-platform-overview
title: Atlas Platform Overview
source_type: synthetic
version: "1.0"
domain: platform
sensitivity: public
---

# Atlas Platform Overview

## System Boundaries

Atlas is a fictional commerce platform used for retrieval experiments. The web client reaches the API gateway, which routes requests to the order, billing, catalog, and search services. PostgreSQL is the system of record for transactional data, Redis serves selected read caches, and the event bus carries asynchronous domain events. The gateway and services are in the synchronous request path; notifications and analytics are asynchronous.

## Service-Level Objectives

The initial service objectives are 99.9% monthly availability for the public API and a 250 ms p95 target for ordinary catalog reads. The order service prioritizes correctness over latency for payment and inventory writes. The platform does not promise global read-after-write consistency; it provides a short session-level guarantee after a write.

## Request Lifecycle

The gateway authenticates the request, assigns a traceable request ID, and forwards the tenant context. A service validates the request and performs its database transaction. If the transaction emits a domain event, the event is published after the transaction through the outbox workflow. The request ID and trace ID are propagated to database, cache, queue, and downstream-service logs.
