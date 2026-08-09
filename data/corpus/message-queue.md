---
doc_id: doc-message-queue
title: Durable Message Queue Policy
source_type: synthetic
version: "1.0"
domain: reliability
sensitivity: public
---

# Durable Message Queue Policy

## Delivery Semantics

The event bus provides durable at-least-once delivery. A producer can publish an event more than once after a timeout, and a consumer can receive a message again after a visibility or acknowledgement failure. The partition key is `order_id`, so events for one order are ordered within a partition rather than globally.

## Consumer Idempotency

Consumers store the event ID in an inbox table with a uniqueness constraint before applying a side effect. A repeated event finds the existing ID and is acknowledged without applying the side effect a second time. This protects email, inventory reservation, and billing handlers from duplicate delivery.

## Backpressure

Operators alert when consumer lag exceeds 30 seconds. Consumers scale out within the partition limit, and a message that fails five times is moved to a dead-letter queue for inspection. The queue is a buffer, not permission to accumulate unbounded work.
