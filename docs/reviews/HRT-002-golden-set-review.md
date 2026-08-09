# HRT-002: Golden-Set Review

## Status

**Assistant pre-review complete; human approval required.** The draft labels remain unchanged and are still marked `assistant-draft` / `pending-human-review`.

## Scope and method

Reviewed all 44 rows in `data/golden/golden_queries.jsonl` against the 18 synthetic corpus documents and `data/README.md`.

Checks performed:

- query IDs, splits, answerability counts, and rewrite metadata;
- chunk IDs and source headings;
- required chunks versus graded relevance;
- claim evidence versus relevant chunks;
- answerable and unanswerable row shape;
- reference answers and claims against the corpus text;
- rewrite intent preservation;
- structural validator and an additional cross-reference audit.

## Verification

- `python3 scripts/validate_data.py` passed: 18 documents, 54 chunks, 44 queries.
- Additional structural audit passed: no missing chunk IDs, invalid required chunks, or answerability-shape errors.
- All corpus references used by the draft exist.

## Decisions required from the owner

These are not silently changed because the owner is the human labeler.

| Query | Finding | Suggested decision |
|---|---|---|
| q005 | The rewrite broadens the original notification question to include billing side effects. | Keep the rewrite notification-specific, or mark it `intent_preserved: false`. |
| q010 | Claim `q010-c2` cites `doc-platform-overview:request-lifecycle`, but that chunk is not in `required_chunks`. | Add it to `required_chunks`, or remove the claim/reference detail that needs it. |
| q018 | The query says a lag threshold triggers scaling. The corpus states that `>30 seconds` triggers an alert; scaling occurs within the partition limit, without the same trigger being stated. | Reword the query/reference to distinguish alerting from scaling. |
| q026 | The rewrite drops the original `Kafka` constraint and broadens the question to any queue vendor. | Retain `Kafka`, or mark the rewrite `intent_preserved: false`. |
| q029 | Claim `q029-c3` uses queue delivery semantics, but that chunk is not in `required_chunks`. | Add `doc-message-queue:delivery-semantics`, or remove the at-least-once claim from the reference answer. |
| q030 | The query mentions slow dependencies exhausting request threads, and the rewrite adds timeouts. The cited corpus directly supports circuit-breaker behavior but not a complete timeout/thread-exhaustion mechanism. | Narrow the query/rewrite to circuit-breaker blast-radius behavior, or add corpus evidence before keeping the current wording. |
| q031 | Claim `q031-c2` uses over-limit behavior, but that chunk is not in `required_chunks`. | Add `doc-rate-limiting:over-limit-behavior`, or remove the queueing detail from the reference answer. |
| q036 | Claim `q036-c2` uses migration acceptance criteria, but that chunk is not in `required_chunks`. | Add `doc-capacity-plan:growth-boundaries`, or remove the migration-reproduction claim. |

## Non-blocking review notes

- q003's reference answer includes the request ID even though no claim labels it; either make it an explicit claim or treat it as optional context.
- q017's original wording says “signal” while the rewrite says “routing policy”; the intended answer is the routing policy. Consider making the original wording equally precise.
- q022's rewrite asks for the prevention mechanism while the original asks for the reason. It is likely useful, but the owner should confirm that this change is intentional.

## Approval procedure

1. Owner reviews the eight blocking rows and the three non-blocking notes.
2. Apply only the approved query, rewrite, qrel, claim, or required-chunk changes.
3. Update the validator to accept the final human-label status and enforce required/evidence consistency.
4. Change labels from `assistant-draft` / `pending-human-review` only after owner approval.
5. Record the frozen dataset version and rerun the validator.

Until step 1 is complete, HRT-002 is not marked done.
