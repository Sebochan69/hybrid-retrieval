# Current Status

## Verified now

- Project harness and documentation contract are present.
- Git repository initialized on branch `main`; no commit has been created.
- MVP stack approved in ADR-002: Python 3.12, SQLite FTS5, MiniLM dense baseline, MiniLM cross-encoder, exact NumPy scan, fixed RRF `k=60`, and human-authored rewrites.
- Synthetic corpus created: 18 Markdown documents and 54 stable heading chunks.
- Golden set frozen as `golden-v2`: 44 JSONL queries, 28 development and 16 held-out test queries, with 32 answerable and 12 abstention cases; project-owner review is recorded.
- `python3 scripts/validate_data.py` passed: `18 docs, 54 chunks, 44 queries`.

## In progress

- Implement the ingestion and lexical/dense retrieval baselines against the frozen data contract.

## Blocked or unverified

- Runtime dependencies and model weights are not installed or loaded yet.
- Retrieval quality, latency, citation correctness, unsupported-claim rate, and abstention results do not exist yet; the retrieval benchmark is not implemented.
- Graphify remains deferred until source implementation creates a useful repository map.
- PDF ingestion and external/local LLM rewriting are intentionally deferred.

## Next best action

Implement the smallest ingestion/chunking and SQLite FTS5 lexical baseline, then add one runnable retrieval check before dense retrieval.

## Handoff for next session

- Completed: stack approval, Git initialization, synthetic corpus, golden-query draft, data validator, evaluation protocol, and ADR-002.
- Verification: `python3 scripts/validate_data.py` passed after freezing `golden-v2`; no retrieval benchmark has run.
- Do not start answer generation or an LLM judge; build and measure retrieval baselines first. The next implementation ticket is HRT-003, followed by HRT-004/HRT-005.

## Last updated

2026-08-08
