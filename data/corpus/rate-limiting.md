---
doc_id: doc-rate-limiting
title: Tenant Rate Limiting
source_type: synthetic
version: "1.0"
domain: reliability
sensitivity: public
---

# Tenant Rate Limiting

## Token-Bucket Policy

Atlas uses a token bucket per tenant and route group. The default bucket holds 120 requests and refills at 2 requests per second. A request consumes one token; a burst is allowed while tokens remain. The values are policy defaults, not a guarantee that every route has identical capacity.

## Tenant Isolation

The limiter key includes the tenant ID and route group rather than only the source IP. This prevents a busy tenant from consuming another tenant's budget and makes noisy-neighbor behavior visible. Internal operator traffic uses a separately named policy rather than bypassing the limiter globally.

## Over-Limit Behavior

A request with an empty bucket is rejected immediately with 429 and `Retry-After`; it is not queued for later execution. The gateway records accepted, rejected, and remaining-token metrics by tenant. Repeated rejects are an operational signal, not proof that the downstream service is unhealthy.
