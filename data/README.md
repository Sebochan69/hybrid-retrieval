# Research Data Contract

## Corpus

`corpus/` contains 18 project-authored synthetic English Markdown documents. They describe the fictional Atlas platform and deliberately include overlapping terms, paraphrases, rare identifiers, multi-hop facts, and plausible distractors. No private enterprise data, credentials, or external provider output is included.

Each document has frontmatter with a stable `doc_id`. The initial chunking rule is one chunk per `##` section. A chunk ID is `<doc_id>:<heading-slug>`, for example `doc-cache-policy:ttl-and-invalidation`. The evaluator must record the actual chunking version so later chunking changes do not silently invalidate judgments.

PDF extraction is intentionally not represented in this first corpus. It is a separate ingestion experiment after the text baseline.

## Golden queries

`golden/golden_queries.jsonl` is JSON Lines: one assistant-drafted object per query. The schema is intentionally explicit. The project owner must review the qrels, claims, and abstention labels before this becomes the frozen human-labeled set:

- `query_id`: stable ID;
- `split`: `dev` or `test`;
- `original_query`: immutable baseline wording;
- `challenge`: `lexical`, `semantic`, `entity`, `multi-hop`, `evidence`, `security`, `abstention`, or `unanswerable`;
- `answerability` and `expected_abstention`;
- `rewrite_candidates`: human-authored, intent-preserving hypotheses; these are experiments, not gold answers;
- `relevant_chunks`: graded qrels (`3` essential, `2` directly supporting, `1` related, `0` not relevant);
- `required_chunks`: chunks needed for the reference answer/evidence gate;
- `reference_answer` and atomic `claims` for answerable queries;
- `abstention_reason` for unanswerable queries;
- `label`: provenance and status of the human labels.

The draft set has 44 queries: 28 development and 16 held-out test queries. It contains 32 answerable and 12 intentionally unanswerable queries. A draft reference answer is not a claim that a future generated answer is correct; it becomes the evaluation reference only after human review.

## Labeling rules

1. Label chunk relevance against the original query intent, not against a rewrite.
2. A rewrite may be marked `intent_preserved: false` if it adds an entity, changes polarity, narrows scope, or loses a required condition. Such a rewrite must not be treated as a valid improvement.
3. Mark every atomic reference claim with the chunk(s) that support it.
4. For unanswerable queries, do not assign a nearby chunk as relevant merely because it shares vocabulary; use an empty `required_chunks` list and require abstention.
5. The current rows are assistant drafts, not human labels. The project owner must review and approve them before any LLM judge is trusted.
