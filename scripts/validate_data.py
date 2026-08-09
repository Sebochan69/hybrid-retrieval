"""Validate the synthetic corpus and golden-query draft schema."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "data" / "corpus"
QUERIES = ROOT / "data" / "golden" / "golden_queries.jsonl"
SLUG_RE = re.compile(r"[^a-z0-9]+")


def slug(text: str) -> str:
    return SLUG_RE.sub("-", text.lower()).strip("-")


def load_corpus() -> set[str]:
    chunk_ids: set[str] = set()
    docs = sorted(CORPUS.glob("*.md"))
    assert len(docs) == 18, f"expected 18 corpus docs, found {len(docs)}"
    for path in docs:
        text = path.read_text(encoding="utf-8")
        frontmatter, body = text.split("---\n", 2)[1:]
        metadata = dict(
            line.split(":", 1)
            for line in frontmatter.splitlines()
            if ":" in line
        )
        doc_id = metadata["doc_id"].strip()
        headings = [
            line.removeprefix("## ").strip()
            for line in body.splitlines()
            if line.startswith("## ")
        ]
        assert len(headings) == 3, f"{path.name}: expected 3 sections"
        for heading in headings:
            chunk_ids.add(f"{doc_id}:{slug(heading)}")
    assert len(chunk_ids) == 54, f"expected 54 chunks, found {len(chunk_ids)}"
    return chunk_ids


def load_queries(chunk_ids: set[str]) -> list[dict]:
    rows = [json.loads(line) for line in QUERIES.read_text(encoding="utf-8").splitlines()]
    assert len(rows) == 44, f"expected 44 queries, found {len(rows)}"
    assert len({row["query_id"] for row in rows}) == len(rows), "duplicate query ID"
    assert {row["query_id"] for row in rows} == {f"q{i:03d}" for i in range(1, 45)}
    assert {row["split"] for row in rows} == {"dev", "test"}
    assert sum(row["split"] == "dev" for row in rows) == 28
    assert sum(row["split"] == "test" for row in rows) == 16
    assert sum(row["answerability"] == "answerable" for row in rows) == 32
    assert sum(row["answerability"] == "unanswerable" for row in rows) == 12

    for row in rows:
        assert row["original_query"].strip()
        assert row["rewrite_candidates"]
        for rewrite in row["rewrite_candidates"]:
            assert rewrite["text"].strip()
            assert rewrite["intent_preserved"] is True
        for item in row.get("relevant_chunks", []) + row.get("distractor_chunks", []):
            assert item["chunk_id"] in chunk_ids, item["chunk_id"]
            assert item["grade"] in {0, 1, 2, 3}
        for chunk_id in row["required_chunks"]:
            assert chunk_id in chunk_ids, chunk_id
        if row["answerability"] == "answerable":
            assert row["expected_abstention"] is False
            assert row["required_chunks"]
            assert row["reference_answer"]
            assert row["claims"]
            for claim in row["claims"]:
                assert claim["evidence"]
                assert set(claim["evidence"]).issubset(chunk_ids)
        else:
            assert row["expected_abstention"] is True
            assert row["required_chunks"] == []
            assert row["reference_answer"] is None
            assert row["claims"] == []
            assert row["abstention_reason"]
        assert row["label"]["labeler"] == "assistant-draft"
        assert row["label"]["status"] == "pending-human-review"
    return rows


def main() -> None:
    chunk_ids = load_corpus()
    rows = load_queries(chunk_ids)
    print(
        f"data schema valid: {len({chunk.split(':', 1)[0] for chunk in chunk_ids})} docs, "
        f"{len(chunk_ids)} chunks, {len(rows)} queries "
        f"({sum(row['answerability'] == 'answerable' for row in rows)} answerable / "
        f"{sum(row['answerability'] == 'unanswerable' for row in rows)} abstention)"
    )


if __name__ == "__main__":
    main()
