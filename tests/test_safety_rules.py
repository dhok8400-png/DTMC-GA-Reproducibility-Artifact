from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src' / 'call_use_displacement'))
from safety_rules import decide_call_use_displacement


def test_safe_decision_allows_when_all_checks_pass():
    d = decide_call_use_displacement(True, True, True, True, True, True, True, True, True, True)
    assert d.allowed
    assert d.reasons == []


def test_unsafe_aliasing_blocks_transformation():
    d = decide_call_use_displacement(True, True, True, True, False, True, True, True, True, True)
    assert not d.allowed
    assert any('aliasing' in r for r in d.reasons)
