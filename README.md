# Hybrid Retrieval

A research prototype for query rewriting, hybrid keyword + semantic retrieval, reranking, and evidence-gated answers.

The first user is the project owner, using the system to learn retrieval engineering and measure quality before trusting generated answers.

## Quick start

- Runtime verified: Python 3.12.3
- Verify the corpus and golden set: `python3 scripts/validate_data.py`
- Retrieval runner: `UNKNOWN` (not implemented yet)

## Documentation

- [`docs/INDEX.md`](docs/INDEX.md) — project documentation index
- [`docs/plans/active/002-study-oriented-ticket-backlog.md`](docs/plans/active/002-study-oriented-ticket-backlog.md) — why/when/what/how/who delivery tickets

The retrieval implementation is intentionally not started yet. The current repository contains the project contract, synthetic evaluation data, and its validator so the system can be built and studied incrementally.
