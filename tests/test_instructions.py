from mars.instructions import MARS_SYSTEM_INSTRUCTIONS


def test_mars_has_stable_system_identity() -> None:
    assert "You are MARS" in MARS_SYSTEM_INSTRUCTIONS
    assert "Multifunctional Autonomous Reasoning System" in MARS_SYSTEM_INSTRUCTIONS


def test_mars_instructions_include_safety_boundaries() -> None:
    assert "tool permissions" in MARS_SYSTEM_INSTRUCTIONS
    assert "risk controls" in MARS_SYSTEM_INSTRUCTIONS
