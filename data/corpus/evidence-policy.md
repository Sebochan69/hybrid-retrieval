---
doc_id: doc-evidence-policy
title: Evidence and Abstention Policy
source_type: synthetic
version: "1.0"
domain: ai-safety
sensitivity: public
---

# Evidence and Abstention Policy

## Citation Rules

Every factual sentence in an externally visible answer must cite the retrieved chunk or chunks that support it. A citation is correct only when the cited text entails the nearby claim; a shared keyword is not enough. Source IDs and heading paths are preferred over opaque result positions.

## Support Levels

Evidence is direct when one retrieved chunk states the claim, multi-source when the claim requires all listed chunks together, and absent when no retrieved chunk supports it. The answerer may summarize direct or multi-source evidence but may not turn a related passage into a new fact.

## Abstention Gate

An answerable query may proceed only when its required evidence chunks are present and no blocking conflict is detected. An unanswerable query must abstain. If evidence is partial, stale, or contradictory, the system returns an evidence-needed response rather than filling the gap from model memory.
