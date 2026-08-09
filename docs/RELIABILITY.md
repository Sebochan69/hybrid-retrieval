# Reliability

## Standard paths

- Bootstrap: Python 3.12.3 is present; dependency setup is not recorded yet.
- Verification: `python3 scripts/validate_data.py` — corpus/golden-set gate; retrieval benchmark is not implemented.
- Start: `UNKNOWN` — a CLI/library is proposed before an HTTP service.
- Debug: `UNKNOWN`

## Golden journeys

- Ingest a known document and retrieve its relevant chunk.
- Run the same labeled query through lexical-only, dense-only, hybrid, reranked, and rewritten-query variants.
- Ask an answerable question and receive an answer with correct source citations.
- Ask an unanswerable question and receive abstention instead of an invented answer.

## Required signals

- Recall@k, MRR, and nDCG@k on a held-out query set.
- Reranker and query-rewrite lift versus the original-query baseline.
- Query latency, including reranking cost.
- Citation correctness and unsupported-claim rate.
- Abstention behavior on unanswerable queries.

## Recovery

- RTO: `UNKNOWN` — research prototype.
- RPO: `UNKNOWN` — define after persistence is selected.
- Recovery test: rebuild the index from `data/corpus/` and reproduce the evaluation run (not yet run).
