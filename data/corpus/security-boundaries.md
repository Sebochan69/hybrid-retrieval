---
doc_id: doc-security-boundaries
title: Security and Retrieved Content Boundaries
source_type: synthetic
version: "1.0"
domain: security
sensitivity: public
---

# Security and Retrieved Content Boundaries

## Tenant Access

The authenticated tenant context is a required filter on every order and document lookup. A retrieved chunk without a matching tenant authorization decision is not evidence the answerer may use. Search relevance does not override access control.

## Retrieved Text Is Untrusted

Document text is data, not an instruction to the retrieval or answer pipeline. A passage that says `ignore the system policy` must be treated as content and may be cited only for the fact that the passage contains those words. Retrieval and generation prompts keep control instructions separate from retrieved text.

## Secrets and Logs

Credentials, tokens, and private keys must never be placed in indexed documents or experiment logs. Request IDs and hashed document identifiers are acceptable correlation fields. If a source contains a secret-shaped value, ingestion must quarantine it rather than embedding or citing it.
