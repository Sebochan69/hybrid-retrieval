---
doc_id: doc-api-gateway
title: API Gateway Policy
source_type: synthetic
version: "1.0"
domain: api
sensitivity: public
---

# API Gateway Policy

## Gateway Responsibilities

The gateway terminates TLS, authenticates the caller, attaches the tenant and trace context, applies request-size and rate policies, assigns a request ID, and routes to a service. It does not own order or payment business rules. A gateway route is selected from the method and path; service-level authorization remains mandatory.

## Idempotency and Retries

Clients must send an idempotency key for payment and order-creation requests. The gateway may retry a safe GET after a connection reset, but it does not blindly retry a non-idempotent payment POST. The billing service stores the idempotency key with the result so a client retry cannot create a second charge.

## Rate-Limit Response

When a tenant exceeds its request budget, the gateway returns HTTP 429 and a `Retry-After` header. The response includes the request ID so the client and operator can correlate the rejection. The gateway does not place over-limit requests into an unbounded waiting queue.
