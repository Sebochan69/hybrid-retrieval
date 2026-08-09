# Build Log

## 2026-08-08 — Project harness initialized

- Goal: create the initial agent-readable project contract.
- Changed: added root instructions and core project documentation.
- Verified: project directory is empty of implementation; no Git repository exists.
- Decision/blocker: Graphify deferred until meaningful source or documentation exists; project intake is still required.
- Next: define purpose, users, stack, data policy, scope, and acceptance metrics.

## 2026-08-08 — Project intake recorded

- Goal: define the research prototype direction.
- Changed: recorded hybrid search, query rewriting, reranking, retrieval-first evaluation, and interview-learning context.
- Proposed: start with a clean synthetic enterprise-like corpus, add PDFs after the retrieval baseline, and use a lightweight local stack before a vector database or API service.
- Verified: user goal, initial user, and research-prototype phase are known; stack, corpus size, and latency remain open.
- Next: approve the active MVP plan and choose the first model/dependency set.

## 2026-08-08 — Session handoff prepared

- Completed: project contract, intake, proposed retrieval-first architecture, ADR-001, and Plan 001.
- Checks: documentation inspected; no source implementation or automated checks exist.
- Open: corpus language/format, embedding/reranker models, external query-rewrite policy, and Git initialization.
- Next: approve the stack, create the corpus and labeled query set, then implement lexical and dense baselines.

## 2026-08-08 — MVP stack and evaluation data approved

- Goal: remove the initial design blockers and create a reproducible retrieval target.
- Changed: initialized Git on `main`; accepted ADR-001; added ADR-002 and `docs/EVALUATION.md`; approved Python 3.12, SQLite FTS5, MiniLM dense/reranker models, exact NumPy similarity, fixed RRF `k=60`, and manual rewrites.
- Changed: added 18 synthetic Atlas Markdown documents, 54 stable heading chunks, 44 assistant-drafted golden queries, and `scripts/validate_data.py`.
- Verified: `python3 scripts/validate_data.py` passed with 18 documents, 54 chunks, 44 queries, 32 answerable cases, and 12 abstention cases; human review is still pending.
- Decision/blocker: English-only synthetic text is the first boundary; PDF ingestion, external rewriting, LLM judging, Graphify, and answer generation remain deferred.
- Next: review and freeze the query labels, then implement ingestion and the SQLite FTS5 lexical baseline.

## 2026-08-08 — Study-oriented delivery backlog added

- Goal: make the project usable, teachable, and ready to publish as a GitHub project.
- Changed: added `docs/plans/active/002-study-oriented-ticket-backlog.md` with ordered tickets covering the full retrieval system, evaluation, evidence gating, CLI use, and GitHub quality.
- Verified: project data validator still passes; no application implementation has been added.
- Next: publish the initial repository state, then start HRT-002 and HRT-003 before implementation.

## 2026-08-08 — HRT-002 assistant pre-review

- Goal: review the draft golden set before human approval.
- Changed: added `docs/reviews/HRT-002-golden-set-review.md` with source-backed findings and owner decisions; no query labels were changed.
- Verified: all 44 rows cross-reference valid corpus chunks; structural validation passed; eight rows need owner decisions before freezing.
- Blocked: human approval is still required; HRT-002 remains open.
- Next: owner decides the flagged q005, q010, q018, q026, q029, q030, q031, and q036 changes.

## 2026-08-08 — HRT-002 golden set frozen

- Goal: apply the approved review corrections and freeze the benchmark labels.
- Changed: corrected query wording, rewrite scope, required evidence, and the golden-set metadata; strengthened `scripts/validate_data.py` to enforce evidence consistency.
- Verified: `python3 scripts/validate_data.py` passed with 18 documents, 54 chunks, and 44 owner-approved `golden-v2` queries.
- Completed: HRT-002 is closed; no retrieval or answer-generation implementation was added.
- Next: start HRT-003 reproducible environment setup.

## 2026-08-08 — HRT-002 study guide documented

- Goal: make the ticket’s reasoning reusable for future study sessions and interview preparation.
- Changed: added the HRT-002 study order, examples, validator command, Git diff command, and review questions to the GitHub documentation index and review record.
- Verified: documentation links to the frozen `golden-v2` data contract and HRT-002 evidence.
- Next: study q001, q029, and q025 before beginning HRT-003.
