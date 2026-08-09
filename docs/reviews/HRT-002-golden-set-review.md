# HRT-002: Golden-Set Review

## Status

**Complete.** The owner approved the suggested corrections. The dataset is frozen as `golden-v2`; all rows are labeled `project-owner` / `human-approved`.

## Scope and method

Reviewed all 44 rows in `data/golden/golden_queries.jsonl` against the 18 synthetic corpus documents and `data/README.md`.

Checks covered:

- query IDs, splits, answerability counts, and rewrite metadata;
- chunk IDs and source headings;
- required chunks versus graded relevance;
- claim evidence versus relevant chunks;
- answerable and unanswerable row shape;
- reference answers and claims against the corpus text;
- rewrite intent preservation;
- structural validation and cross-reference consistency.

## Applied corrections

| Query | Correction | Reason |
|---|---|---|
| q003 | Removed the unlabelled request-ID detail from the reference answer. | Keep the reference focused on the requested status and header. |
| q005 | Narrowed the rewrite from notification or billing to notification only. | Preserve the original scope. |
| q010 | Added `doc-platform-overview:request-lifecycle` to `required_chunks`. | It supports the propagation claim. |
| q017 | Changed “signal” to “routing policy” in the original query. | Match the corpus evidence and expected answer. |
| q018 | Reworded the query and rewrite to distinguish the 30-second alert threshold from scaling behavior. | The corpus does not say that the same threshold triggers scaling. |
| q022 | Reworded the rewrite to preserve the original causal question while retaining the idempotency mechanism. | Keep rewrite intent aligned. |
| q026 | Retained the `Kafka` constraint in the rewrite. | Do not broaden the requested entity. |
| q029 | Added `doc-message-queue:delivery-semantics` to `required_chunks`. | It supports the at-least-once claim. |
| q030 | Narrowed the query and rewrite to repeated downstream failures and circuit-breaker behavior. | Avoid unsupported timeout/thread-exhaustion claims. |
| q031 | Added `doc-rate-limiting:over-limit-behavior` to `required_chunks`. | It supports the rejection-versus-queueing claim. |
| q036 | Added `doc-capacity-plan:growth-boundaries` to `required_chunks`. | It supports the migration-reproduction claim. |

## Verification

- `python3 scripts/validate_data.py` passes: 18 documents, 54 chunks, 44 queries.
- The validator now enforces uniform label state, required-chunk relevance, claim-evidence membership, and grade-1 distractors.
- All rows use `project-owner`, `human-approved`, and `golden-v2`.
- The 28/16 development/test split and 32/12 answerable/abstention split are unchanged.
- No retrieval benchmark, answer generation, or LLM judge has been added.

## Result

HRT-002 is closed. The next ticket is HRT-003: create the reproducible Python dependency and model setup.
