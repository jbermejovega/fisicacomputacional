from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import pytest
p=Path(__file__).resolve().parents[1]/"examples/color_relational.py"
s=spec_from_file_location("color_relational",p);m=module_from_spec(s);s.loader.exec_module(m)

def test_black_white():
    assert m.luminance((0,0,0))==0
    assert m.luminance((255,255,255))==pytest.approx(1)
    assert m.contrast((0,0,0),(255,255,255))==pytest.approx(21)

def test_symmetry():
    assert m.contrast((10,20,30),(220,230,240))==pytest.approx(
        m.contrast((220,230,240),(10,20,30)))

def test_source_preserved_across_style():
    a=m.prepare("S","sRGB",(10,20,30))
    b=m.prepare("S","sRGB",(40,50,60))
    assert a["source_id"]==b["source_id"] and a["digest"]!=b["digest"]
    assert not a["perceptual_equivalence_claimed"]

def test_invalid_channel():
    with pytest.raises(ValueError):m.luminance((256,0,0))
