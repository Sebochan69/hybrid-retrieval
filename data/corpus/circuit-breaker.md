---
doc_id: doc-circuit-breaker
title: Downstream Circuit Breaker Policy
source_type: synthetic
version: "1.0"
domain: reliability
sensitivity: public
---

# Downstream Circuit Breaker Policy

## Circuit States

A closed circuit sends normal traffic and records failures. An open circuit fails fast without calling the dependency. After a cool-down, a half-open circuit permits a small probe; success closes it and failure opens it again. The breaker is per dependency and route, not one global switch.

## Trip Thresholds

The initial policy opens after five consecutive failures or a 50% failure rate across a rolling window of 20 requests, whichever is reached first. It stays open for 10 seconds before a probe. These values are starting policy parameters and must be measured against false trips and missed failures.

## Fallbacks

Catalog reads may use the last known cache value when its dependency is unavailable. Payment requests fail fast with a clear retryable error; they do not fabricate a success from a cache. A circuit breaker limits blast radius but does not replace timeouts, idempotency, or safe retry rules.
