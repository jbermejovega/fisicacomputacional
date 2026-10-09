# SPDX-License-Identifier: Apache-2.0
"""Generate new procedural educational SVG drawings from SymPy geometry.

These figures are original course *templates*, not digitizations of JJBV's
pre-existing artworks. New authored drawings can be imported only with their
own per-work provenance and rights record. No GUI, provider or network needed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp
from sympy.geometry import Point, Polygon

SOURCE = "curso_abierto/codebooks/dibujos_sympy.py"
SCHEMA = "KRONE_SIGIL_SYMPY_FIGURE_PROVENANCE_V1"


def _prepare_svg() -> None:
    plt.rcParams["svg.hashsalt"] = "KRONE-HYPERJARRA-ORIGINAL-V1"


def _save(figure: plt.Figure, path: Path) -> None:
    figure.savefig(path, format="svg", metadata={"Date": None})
    plt.close(figure)


def draw_boolean_lattice(path: Path) -> None:
    """Own diagram of the four-element Boolean poset B2."""
    pos = {
        "∅": (-0.0, -1.0),
        "{a}": (-1.0, 0.0),
        "{b}": (1.0, 0.0),
        "{a,b}": (0.0, 1.0),
    }
    edges = [("∅", "{a}"), ("∅", "{b}"), ("{a}", "{a,b}"), ("{b}", "{a,b}")]
    figure, ax = plt.subplots(figsize=(5, 4))
    for source, target in edges:
        x0, y0 = pos[source]
        x1, y1 = pos[target]
        ax.plot([x0, x1], [y0, y1], linewidth=1.8)
    for label, (x, y) in pos.items():
        ax.scatter([x], [y], s=240, zorder=2)
        ax.annotate(label, (x, y), xytext=(10, 9), textcoords="offset points")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.55, 1.5)
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_title("Retículo booleano B₂ · diagrama original")
    figure.tight_layout()
    _save(figure, path)


def draw_triangle_laplacian(path: Path) -> None:
    """SymPy exact geometry -> Matplotlib SVG for graph K3."""
    vertices = [
        Point(sp.Integer(0), sp.Integer(1)),
        Point(-sp.sqrt(3)/2, -sp.Rational(1, 2)),
        Point(sp.sqrt(3)/2, -sp.Rational(1, 2)),
    ]
    triangle = Polygon(*vertices)
    assert len(triangle.sides) == 3
    figure, ax = plt.subplots(figsize=(5, 4.5))
    for side in triangle.sides:
        ax.plot(
            [float(side.p1.x), float(side.p2.x)],
            [float(side.p1.y), float(side.p2.y)],
            linewidth=2.5,
        )
    for i, point in enumerate(vertices):
        x, y = float(point.x), float(point.y)
        ax.scatter([x], [y], s=270, zorder=2)
        ax.annotate(str(i), (x, y), xytext=(9, 10), textcoords="offset points")
    ax.set_xlim(-1.35, 1.35)
    ax.set_ylim(-0.95, 1.45)
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_title("K₃ · 3 árboles generadores · dibujado con SIGIL/SymPy")
    figure.tight_layout()
    _save(figure, path)


def generate(out: Path) -> dict[str, object]:
    _prepare_svg()
    out.mkdir(parents=True, exist_ok=True)
    figures = [
        ("reticulo_booleano_b2.svg", draw_boolean_lattice, "poset_and_mobius"),
        ("grafo_triangulo_k3.svg", draw_triangle_laplacian, "matrix_tree_theorem"),
    ]
    metadata = []
    for filename, draw, lesson_id in figures:
        destination = out / filename
        draw(destination)
        metadata.append({
            "path": filename,
            "generator": SOURCE,
            "lesson_id": lesson_id,
            "format": "SVG",
            "rights_status": "ARTWORK_LICENSE_PENDING_PER_ASSET_REVIEW",
            "copy_of_existing_jjbv_art": False,
            "copy_of_mit_ocw_image": False,
        })
    receipt: dict[str, object] = {
        "schema_id": SCHEMA,
        "source": SOURCE,
        "generated_images": metadata,
        "provider_io": False,
        "human_artwork_copyright_verified": False,
        "scientific_certification": False,
    }
    (out / "provenance.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("figuras_locales"))
    args = parser.parse_args()
    print(json.dumps(generate(args.out), ensure_ascii=False, indent=2))
