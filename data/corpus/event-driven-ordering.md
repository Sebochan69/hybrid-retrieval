---
doc_id: doc-event-driven-ordering
title: Order Event Workflow
source_type: synthetic
version: "1.0"
domain: architecture
sensitivity: public
---

# Order Event Workflow

## Transactional Outbox

When the order service commits an order, it writes an outbox row in the same database transaction. A publisher later reads unpublished outbox rows and sends them to the event bus. This prevents a successful database commit from being separated from the corresponding `order.created` event by a process crash.

## Downstream Workflow

The `order.created` event fans out to inventory reservation, notification, and analytics consumers. Inventory and notification are eventually consistent with the order write; the order response does not wait for email delivery. Each consumer reports its own processing status.

## Ordering and Duplicates

Events for one order use `order_id` as their partition key, but the system does not promise a global order across all orders. Consumers must tolerate duplicates and retry safely. The workflow therefore combines the outbox for publication reliability with idempotent consumers for delivery reliability.
