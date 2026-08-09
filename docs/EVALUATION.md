# Evaluation Protocol

## Dataset

The first golden-set draft is `data/golden/golden_queries.jsonl`. It contains assistant-drafted qrels and claim labels, not human-approved or LLM-judge labels. The project owner must review it before the benchmark is frozen. The development split may be used to choose fixed implementation details; the test split remains held out.

Each query has:

- `original_query` — the user wording and immutable baseline;
- `rewrite_candidates` — human-authored experimental inputs, each with an intent-preservation label;
- graded `relevant_chunks` (`0`–`3`) and `required_chunks` for answer completeness;
- `reference_answer` and atomic `claims` for answer/citation review when answerable;
- `expected_abstention` and a reason when unanswerable.

## Retrieval variants

Run the same query IDs through these named paths:

1. `lexical_original`
2. `dense_original`
3. `hybrid_original`
4. `hybrid_reranked_original`
5. `lexical_rewrite`
6. `dense_rewrite`
7. `hybrid_rewrite`
8. `hybrid_reranked_rewrite`

A result record must include the original query, rewrite ID/text (or null), model/index versions, retrieved chunk IDs and scores, and timing. Rewritten paths are compared against the corresponding original-query path, not against a moving target.

## Retrieval metrics

Report each metric at `k ∈ {1, 3, 5, 10}` on development and held-out test splits:

- **Recall@k:** fraction of graded-relevant chunks (`grade >= 2`) retrieved in the top k; also report required-chunk coverage for multi-hop queries.
- **MRR:** reciprocal rank of the first graded-relevant chunk; zero when none is retrieved.
- **nDCG@k:** graded relevance using the stored `0`–`3` labels.
- **Latency:** warm-query p50/p95, with index-build and model-load time reported separately.

Do not claim a variant wins from aggregate averages alone; retain per-query deltas and failure categories.

## Answer and evidence metrics

Answer generation is eligible only when the evidence gate finds every `required_chunk` for an answerable query and no blocking conflict. All unanswerable queries abstain. The provisional gate is intentionally strict and may be relaxed only from development evidence.

For human review, label each generated answer:

- **Citation correctness:** every cited chunk actually supports the nearby claim and identifies the correct source.
- **Unsupported claim:** an atomic claim has no supporting retrieved chunk or exceeds what its cited chunk says.
- **Abstention:** correct abstention, false abstention, or unsafe answer.

Report citation correctness and unsupported-claim rate per claim and per answer. Report abstention confusion counts separately for answerable and unanswerable queries.

An LLM judge may be added only after the project owner approves a human-labeled sample and its agreement/disagreement cases are recorded. It is not a quality gate in the initial benchmark.

## Reproducibility

Freeze the corpus, query-set version, model IDs, fusion constant, chunking rule, and runtime versions in each result file. A benchmark is not complete until its command and verification evidence are recorded in `docs/STATUS.md` and `docs/BUILD_LOG.md`.
