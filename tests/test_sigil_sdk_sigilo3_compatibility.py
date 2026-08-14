from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = (
    ROOT
    / "sigil_compat"
    / "SIGIL_SDK_SIGILO3_REVERSIBLE_PORTAL_PATTERN_V1.compat.json"
)
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def load_manifest() -> dict[str, object]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def test_source_is_exactly_pinned_to_sigilbook_checkpoint():
    source = load_manifest()["canonical_source"]
    assert source["repository"] == "jbermejovega/sigilbook"
    assert source["pull_request"] == 867
    assert SHA40.fullmatch(source["head_sha"])
    assert SHA40.fullmatch(source["module_blob_sha"])
    assert SHA40.fullmatch(source["manifest_blob_sha"])
    assert source["authority"] == "SOURCE_BOUND_REFERENCE_ONLY"


def test_invocation_and_kokompi_move_precede_compilation():
    pipeline = load_manifest()["required_pipeline"]
    assert pipeline[:2] == ["INVOCATION", "KOKOMPI_MOVE"]
    assert pipeline.index("KOKOMPI_MOVE") < pipeline.index("PYDANTIKA")
    assert pipeline[-3:] == ["PACAPDG", "UAP", "SAFE_REPLAY"]


def test_plural_fusion_contract_is_reversible_and_noncollapsing():
    invariants = load_manifest()["compatibility_invariants"]
    assert invariants["fan_in_bounded"] is True
    assert invariants["fan_in_maximum"] == 8
    assert invariants["pi_fixed"] is True
    assert invariants["fusion_reversible"] is True
    assert invariants["voices_recoverable"] is True
    assert invariants["identity_transport"] is False
    assert invariants["plural_collapse"] is False


def test_compatibility_manifest_grants_no_execution_authority():
    manifest = load_manifest()
    invariants = manifest["compatibility_invariants"]
    assert manifest["implementation_copied"] is False
    assert manifest["compatibility_mode"] == "MANIFEST_AND_TESTS_ONLY"
    assert invariants["runtime_authority"] is False
    assert invariants["workflow_dispatch_authority"] is False
    assert invariants["git_mutation_authority"] is False
    assert invariants["general_hott_equivalence_claimed"] is False
    assert invariants["safe_replay"] is True

