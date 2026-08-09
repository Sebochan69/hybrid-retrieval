---
doc_id: doc-database-replication
title: Database Replication Policy
source_type: synthetic
version: "1.0"
domain: data
sensitivity: public
---

# Database Replication Policy

## Topology

Atlas has one writable primary and two read replicas in separate availability zones. Replication is asynchronous. Ordinary catalog reads may use a replica, while payment and inventory writes go to the primary. Replica lag is exported as a measured signal rather than hidden behind a fixed assumption.

## Read-Your-Writes

After a successful write, the session receives a short-lived primary-read token. Reads carrying that token are routed to the primary for five seconds or until the token expires. This provides a bounded read-your-writes guarantee without requiring every read to use the primary.

## Failure Objectives

The database recovery target is an RPO below 30 seconds and an RTO of 10 minutes for the initial region. Operators monitor replica lag, primary health, and restore checkpoints. These targets are objectives for the runbook, not evidence that a particular incident met them.
