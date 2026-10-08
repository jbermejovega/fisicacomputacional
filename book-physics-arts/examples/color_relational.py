"""Finite sRGB relative luminance and contrast, source-preserving example.

Assumes standard sRGB transfer function and relative luminance coefficients.
No claim of complete color perception or device calibration.
"""
from __future__ import annotations
from hashlib import sha256
import json

def _linear(v: int) -> float:
    if type(v) is not int or not 0 <= v <= 255:
        raise ValueError("RGB channel must be integer 0..255")
    c = v / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def luminance(rgb: tuple[int, int, int]) -> float:
    if not isinstance(rgb, tuple) or len(rgb) != 3:
        raise ValueError("RGB triplet required")
    r, g, b = (_linear(v) for v in rgb)
    return 0.2126*r + 0.7152*g + 0.0722*b

def contrast(a: tuple[int,int,int], b: tuple[int,int,int]) -> float:
    x, y = sorted((luminance(a), luminance(b)))
    return (y + 0.05) / (x + 0.05)

def prepare(source_id: str, context_id: str, rgb: tuple[int,int,int]) -> dict:
    if not source_id or not context_id:
        raise ValueError("source and context required")
    lum = luminance(rgb)
    data = {"source_id":source_id,"context_id":context_id,
            "rgb":list(rgb),"luminance":lum}
    return {**data,"digest":sha256(json.dumps(data,sort_keys=True).encode()).hexdigest(),
            "source_preserved":True,"perceptual_equivalence_claimed":False,
            "display_calibrated":False,"renderer_executed":False}

if __name__ == "__main__":
    print(json.dumps(prepare("INDRA_PENTAGON","SRGB_STANDARD",(138,43,226)),indent=2))
