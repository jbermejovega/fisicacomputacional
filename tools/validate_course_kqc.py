from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TEXT = {
    "README.md": [
        "PACADOC.md",
        "SIGIL API / KQC Course Compliance",
        "docs/SIGIL_API_KQC_TEACHING_COMPLIANCE.md",
        "python tools/validate_course_kqc.py",
    ],
    "PACADOC.md": [
        "SIGIL API / KQC teaching compliance",
        "no replay",
        "method",
        "parameters",
        "units",
    ],
    "docs/SIGIL_API_KQC_TEACHING_COMPLIANCE.md": [
        "SIGIL_API_KQC_TEACHING_COMPLIANCE_V1",
        "Copyright (c) JJBV / Jara Juana Bermejo Vega. All rights reserved.",
        "no replay -> no certified result",
        "python tools/validate_course_kqc.py",
    ],
    "registry/sigil_api_kqc_teaching_compliance_v1.yaml": [
        "SIGIL_API_KQC_TEACHING_COMPLIANCE_V1",
        "jbermejovega/fisicacomputacional",
        "kqc:",
        "sigil_api_adaptation:",
        "validator:",
    ],
    "environment.yml": [
        "name: fisica-computacional",
        "python=3.12",
        "jupyterlab",
        "numpy",
        "scipy",
    ],
    ".github/workflows/course-kqc-compliance.yml": [
        "Course KQC Compliance",
        "python tools/validate_course_kqc.py",
    ],
}


def main() -> int:
    missing: list[str] = []
    for relative_path, tokens in REQUIRED_TEXT.items():
        path = ROOT / relative_path
        if not path.exists():
            missing.append(relative_path)
            continue
        content = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in content:
                missing.append(f"{relative_path}: {token}")

    if missing:
        print("KQC course compliance check failed:")
        for item in missing:
            print(f"- missing {item}")
        return 1

    print("KQC course compliance check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
