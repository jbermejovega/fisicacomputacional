# SPDX-License-Identifier: Apache-2.0
"""Deterministic local HyperJarra course lookup; no LLM or network required.

LLAMAINDEX / OLLAMA / LLAMA_CPP are OPTIONAL adapter plans, not a running
backend. The true index is the source-bound HyperJarra/KRONE JSON.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

INDEX = Path(__file__).resolve().parents[1] / "INDICE_HYPERJARRA_KRONE_V1.json"
SCHEMA = "FISICACOMPUTACIONAL_HYPERJARRA_KRONE_OPEN_COURSE_INDEX_V1"
PROVIDERS = {"LEXICAL", "LLAMAINDEX", "OLLAMA", "LLAMA_CPP", "META_LLAMA"}


def tokens(value: str) -> set[str]:
    folded = unicodedata.normalize("NFKD", value.casefold())
    ascii_like = "".join(c for c in folded if not unicodedata.combining(c))
    return set(re.findall(r"[a-z0-9_]+", ascii_like))


def load_index(path: Path = INDEX) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_id") != SCHEMA:
        raise ValueError("HYPERJARRA_INDEX_SCHEMA_MISMATCH")
    parent = data.get("derived_from_previous_index", {})
    if parent.get("schema_id") != "HYPERJARRA_SIGILBOOK_AST_INDEX_V1":
        raise ValueError("HYPERJARRA_PREDECESSOR_DRIFT")
    if parent.get("schema_categorical") != "TOTAL_HYPERJARRA_CATEGORICAL_INDEX_JARA_TOP_V1":
        raise ValueError("JARA_TOP_INDEX_DRIFT")
    if data.get("index_properties", {}).get("authority_transport") is not False:
        raise ValueError("FORBIDDEN_AUTHORITY_TRANSPORT")
    records = data.get("records", [])
    ids = [r["id"] for r in records]
    if not records or len(ids) != len(set(ids)):
        raise ValueError("DUPLICATE_INDEX_OCCURRENCE")
    for item in records:
        if item.get("visibility") != "PUBLIC":
            raise ValueError("PRIVATE_RECORD_IN_PUBLIC_COURSE")
        if not (item.get("source") and item.get("path") and item.get("license_scope")):
            raise ValueError("UNBOUND_INDEX_SOURCE")
        if item["path"].startswith("/") or ".." in item["path"].split("/"):
            raise ValueError("NON_CANONICAL_INDEX_PATH")
    retrieval = data.get("retrieval", {})
    if retrieval.get("restricted_sources_exportable") is not False:
        raise ValueError("RESTRICTED_SOURCES_EXPORT")
    return data


def lookup(query: str, *, index: dict, limit: int = 8) -> list[dict]:
    if not query.strip() or not 1 <= limit <= 30:
        return []
    keys = tokens(query)
    hits = []
    for item in index["records"]:
        title_keys = tokens(item["title"])
        topic_keys = tokens(item["topic"])
        path_keys = tokens(item["path"])
        score = 3 * len(keys & title_keys) + 2 * len(keys & topic_keys) + len(keys & path_keys)
        if score:
            hits.append({"id": item["id"], "title": item["title"],
                         "path": item["path"], "score": score,
                         "source": item["source"], "visibility": item["visibility"],
                         "kind": item["kind"]})
    return sorted(hits, key=lambda r: (-r["score"], r["id"]))[:limit]


def adapter_plan(provider: str, *, index: dict) -> dict:
    provider = provider.upper()
    if provider not in PROVIDERS:
        raise ValueError("UNKNOWN_INDEX_PROVIDER")
    return {
        "canonical_index": index["retrieval"]["canonical_index"],
        "requested_adapter": provider,
        "operation": "PLAN_ONLY",
        "index_node_count": len(index["records"]),
        "provider_imported": False,
        "provider_io": False,
        "model_loaded": False,
        "embedding_computed": False,
        "framework_is_canonical": False,
        "restricted_content_included": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?", default="fisica computacional")
    parser.add_argument("--index", type=Path, default=INDEX)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--adapter-plan", choices=sorted(PROVIDERS))
    args = parser.parse_args()
    data = load_index(args.index)
    result = (adapter_plan(args.adapter_plan, index=data)
              if args.adapter_plan else {"hits": lookup(args.query, index=data, limit=args.limit),
                                        "mode": "LOCAL_LEXICAL_NO_MODEL"})
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
