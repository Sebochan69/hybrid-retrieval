---
doc_id: doc-incident-failover
title: Primary Failover Runbook
source_type: synthetic
version: "1.0"
domain: operations
sensitivity: public
---

# Primary Failover Runbook

## Failover Timeline

When the primary becomes unhealthy, the operator confirms the failure, selects the most current replica, and promotes it. Because replication is asynchronous, the promoted replica can be missing the last few seconds of committed writes. The runbook records the observed replication position before reopening writes.

## Mitigation

During promotion, writes are paused or returned as retryable so two primaries are not created. Read traffic can continue from a known replica, but operators communicate that recent data may be temporarily incomplete. After promotion, clients receive fresh primary-read tokens for writes and consistency-sensitive reads.

## Monitored Signals

The runbook requires primary health, replica lag, replication position, restore checkpoint, error rate, and request latency. A successful promotion does not by itself prove that the RPO target was met; the observed lag and recovered position must be recorded in the incident report.
