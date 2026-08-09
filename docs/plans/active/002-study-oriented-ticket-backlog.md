# Feature F-001: Evidence-Gated Hybrid Retrieval MVP

## Purpose

Make the project usable as a local retrieval system, teach the complete system design, and keep the work publishable as a GitHub project that an interviewer can clone and run.

## User story

As the project owner and student, I can run a query through lexical, dense, hybrid, reranked, and rewritten-query retrieval; inspect evidence and evaluation results; and study each design decision before trusting generated answers.

## Roles

- **Owner/student:** project owner; reviews labels, chooses trade-offs, runs the system, and studies the results.
- **Builder:** implements the bounded ticket.
- **Reviewer:** owner plus automated tests and GitHub checks.
- **External providers:** none in the initial benchmark.

## Ticket format

Every ticket answers: **why**, **when**, **what**, **how**, **who**, dependencies, and completion evidence. A ticket is not complete from code alone; its design explanation and runnable verification must be recorded.

## Ordered tickets

### HRT-001 — Repository and GitHub foundation

- **Status:** complete; the project contract, README, ADRs, plans, `.gitignore`, and initial public commit exist.
- **Why:** A fresh reader needs to understand the purpose, boundaries, decisions, and verification path.
- **When:** First.
- **What:** Preserve the current project contract and make the repository’s first clean, reviewable commit.
- **How:** Keep root instructions short; route design detail into `docs/`; exclude secrets, caches, databases, and generated output.
- **Who:** Builder prepares; owner approves the public repository contents.
- **Done when:** A fresh clone explains the project and points to one runnable verification command.
- **Study:** project boundaries, Git history, ADRs, and reproducibility.

### HRT-002 — Review and freeze the golden set

- **Status:** complete; the owner-approved `golden-v2` set and stronger validator are committed.
- **Why:** Assistant-drafted labels cannot be treated as ground truth for a benchmark.
- **When:** Before retrieval quality is reported.
- **What:** Review qrels, claims, rewrites, answerability, and abstention labels while preserving the dev/test split.
- **How:** Use the data contract and validator; version the frozen set and record the reviewer and date.
- **Who:** Owner is the human labeler; builder supplies validation tools.
- **Done when:** No rows are marked `pending-human-review`, and the test split remains held out.
- **Study:** relevance judgments, qrels, leakage, answerability, and evaluation bias.

### HRT-003 — Reproducible Python environment

- **Status:** partial; Python 3.12.3 and SQLite 3.45.1 FTS5 are verified, but no dependency manifest exists.
- **Why:** Interviewers and future sessions must be able to reproduce the same run.
- **When:** Before model-dependent implementation.
- **What:** Add one standard dependency/setup path, model IDs, runtime checks, and model-cache guidance.
- **How:** Use Python 3.12, built-in SQLite, pinned direct dependencies, and local model inference; do not add an external provider.
- **Who:** Builder implements; owner verifies from a clean environment.
- **Done when:** Setup and verification work from a fresh clone without undocumented machine state.
- **Study:** runtime reproducibility, dependency trade-offs, model versioning, and local inference.

### HRT-004 — Corpus ingestion and chunking

- **Status:** planned.
- **Why:** Retrieval needs stable units with source provenance.
- **When:** After the data contract is understood; before either retriever.
- **What:** Parse Markdown frontmatter, split on `##` headings, and produce stable document/chunk records.
- **How:** Use one small ingestion interface; reject malformed documents clearly; preserve document ID, heading, text, and source path.
- **Who:** Builder implements; owner reviews representative chunks.
- **Done when:** The corpus reproducibly yields 18 documents and 54 stable chunks.
- **Study:** ingestion versus retrieval, chunk-size trade-offs, identifiers, and provenance.

### HRT-005 — SQLite FTS5 index

- **Status:** planned.
- **Why:** A transparent lexical baseline gives the project a measurable starting point.
- **When:** After HRT-004.
- **What:** Store chunk metadata and searchable text in a rebuildable SQLite FTS5 index.
- **How:** Use SQLite 3.45.1, the approved `unicode61` tokenizer, parameterized queries, and transactional rebuilds.
- **Who:** Builder implements; owner inspects the schema and rebuild path.
- **Done when:** The index can be deleted and recreated entirely from `data/corpus/`.
- **Study:** schema design, tokenization, indexing, transactions, and rebuildability.

### HRT-006 — Lexical retriever

- **Status:** planned.
- **Why:** Establish the first usable retrieval path and baseline metrics.
- **When:** After HRT-005.
- **What:** Return the top `k` chunks, scores, and provenance for a query.
- **How:** Keep a small retrieval interface; hide FTS5 syntax and score handling behind it; test through that interface.
- **Who:** Builder implements; owner tests known queries.
- **Done when:** Known lexical and rare-identifier queries return relevant chunks with automated checks.
- **Study:** retrieval interfaces, ranking scores, deep modules, seams, and testability.

### HRT-007 — Dense retriever

- **Status:** planned.
- **Why:** Test semantic matches that keyword search may miss.
- **When:** After HRT-004; can proceed beside HRT-005/006.
- **What:** Embed chunks and queries with `all-MiniLM-L6-v2`, normalize vectors, and use exact NumPy cosine comparison.
- **How:** Persist model/index metadata; keep the exact scan because the initial corpus is small; measure its limits instead of guessing.
- **Who:** Builder implements; owner compares semantic examples and runtime.
- **Done when:** Paraphrase queries retrieve relevant chunks and model/version metadata is recorded.
- **Study:** embeddings, vector normalization, cosine similarity, exact scan versus ANN, and model cost.

### HRT-008 — Hybrid rank fusion

- **Status:** planned.
- **Why:** Lexical and semantic retrieval provide complementary signals.
- **When:** After HRT-006 and HRT-007.
- **What:** Combine ranked lexical and dense results with fixed Reciprocal Rank Fusion, `k=60`.
- **How:** Union candidate IDs, calculate the fixed formula, and retain source ranks/scores for inspection.
- **Who:** Builder implements; owner checks a hand-worked example.
- **Done when:** Fusion is deterministic, transparent, and uses no held-out tuning.
- **Study:** rank fusion, score calibration, candidate union, and reproducible parameters.

### HRT-009 — Cross-encoder reranking

- **Status:** planned.
- **Why:** Improve precision on the fused shortlist while exposing quality/latency trade-offs.
- **When:** After HRT-008.
- **What:** Rerank only the fused top 20 with `ms-marco-MiniLM-L-6-v2`.
- **How:** Batch query/chunk pairs locally, preserve the pre-rerank order and scores, and record model-load and query time separately.
- **Who:** Builder implements; owner decides whether the measured lift justifies the cost.
- **Done when:** Reranked results are comparable with non-reranked results and latency is reported.
- **Study:** two-stage retrieval, cross-encoders, batching, and performance budgets.

### HRT-010 — Query-rewrite experiment

- **Status:** planned; human-authored rewrite candidates already exist.
- **Why:** Rewriting can improve recall but can also change intent or introduce unsupported terms.
- **When:** After original-query baselines exist.
- **What:** Compare original queries with valid human-authored rewrites; never discard the original.
- **How:** Run paired experiments, exclude intent-changing rewrites, and report per-query gains and regressions.
- **Who:** Owner reviews intent preservation; builder runs the experiment.
- **Done when:** Rewrite results are compared against the matching original-query path.
- **Study:** query planning, intent preservation, experimental controls, and failure analysis.

### HRT-011 — Unified retrieval pipeline

- **Status:** planned.
- **Why:** Separate scripts for every variant would drift and make comparisons unfair.
- **When:** After HRT-006 through HRT-010.
- **What:** One orchestration interface for the named variants in `docs/EVALUATION.md`.
- **How:** Use lexical and dense adapters behind a small retrieval seam; keep configuration explicit and result records uniform.
- **Who:** Builder implements; owner reviews the data flow.
- **Done when:** Every variant preserves the original query, rewrite metadata, chunk IDs, scores, model versions, and timings.
- **Study:** orchestration, adapters, seams, provenance, and controlled comparisons.

### HRT-012 — Evaluation runner and experiment artifacts

- **Status:** planned.
- **Why:** Retrieval quality must be measured rather than inferred from a few examples.
- **When:** After HRT-011 and HRT-002.
- **What:** Run all variants on dev and held-out test queries; calculate Recall@k, MRR, nDCG@k, required-chunk coverage, and p50/p95 latency.
- **How:** Emit JSONL results, summaries, per-query deltas, and model/index/runtime versions; never report aggregate averages alone.
- **Who:** Builder implements; owner interprets and approves conclusions.
- **Done when:** A single documented command reproduces the benchmark and its evidence is recorded in `STATUS.md` and `BUILD_LOG.md`.
- **Study:** IR metrics, held-out evaluation, latency measurement, experiment design, and reproducibility.

### HRT-013 — Evidence gate and abstention

- **Status:** planned.
- **Why:** A fluent answer is unsafe when required evidence is missing or conflicting.
- **When:** After the evaluation data and retrieval result schema exist; before answer generation.
- **What:** Require all `required_chunks` for answerable questions and abstain otherwise.
- **How:** Keep retrieved evidence separate from generated text; make the provisional gate strict and observable.
- **Who:** Builder implements; owner reviews false and correct abstentions.
- **Done when:** Unanswerable queries abstain and answerable queries cannot bypass missing required evidence.
- **Study:** groundedness, abstention, safety gates, conflicts, and trust boundaries.

### HRT-014 — Minimal user CLI

- **Status:** planned.
- **Why:** The project must be usable by the owner and testable by an interviewer.
- **When:** Add incrementally once ingestion and retrieval exist.
- **What:** Provide simple commands for validation, indexing, searching, and evaluation.
- **How:** Use the standard library CLI; avoid an HTTP service until local measurements justify it.
- **Who:** Builder implements; owner follows the README from a clean clone.
- **Done when:** A user can build the index, run a query, inspect evidence, and reproduce the benchmark.
- **Study:** user-facing interfaces, command design, failure messages, and operational simplicity.

### HRT-015 — Answer generation and citations

- **Status:** deferred.
- **Why:** Answers are useful only after retrieval and evidence gating are trustworthy.
- **When:** Only after HRT-012 and HRT-013 produce acceptable development evidence.
- **What:** Generate answers from approved evidence and attach claim-level citations.
- **How:** Record a separate model decision; measure citation correctness, unsupported claims, and abstention confusion; do not introduce an LLM judge first.
- **Who:** Owner approves the model and human review protocol; builder implements.
- **Done when:** Answer quality is evaluated independently from retrieval quality.
- **Study:** generation boundaries, citation design, human calibration, and hallucination failure modes.

### HRT-016 — Tests, CI, and study documentation

- **Status:** planned; project documentation already provides the initial contract.
- **Why:** The public repository must remain safe to change and easy to study.
- **When:** Incrementally, beginning with the first implementation.
- **What:** Add tests at module interfaces, GitHub Actions for non-model checks, architecture diagrams, ADRs, and walkthroughs.
- **How:** Keep tests small and runnable; separate model-dependent checks from fast checks; document every measured trade-off.
- **Who:** Builder prepares; owner reviews pull requests and study notes.
- **Done when:** A pull request runs checks and a reader can trace each system-design decision to code and evidence.
- **Study:** quality gates, CI, architecture communication, and maintainability.

## Recommended execution order

Start with:

```text
HRT-003 → HRT-004 → HRT-005 → HRT-006
```

Stop after the lexical baseline and study it before adding dense retrieval. Then continue through fusion, reranking, evaluation, evidence gating, and finally answer generation.

## Non-goals for this feature

- Production deployment or multi-tenancy
- HTTP service before the local pipeline is measured
- PDF ingestion before the Markdown baseline
- Multi-agent orchestration
- External runtime LLM providers
- Automatic LLM judging before human calibration
