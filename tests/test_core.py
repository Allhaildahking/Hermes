from mars.core import Mars
from mars.providers import EchoProvider


def test_mars_responds_through_provider() -> None:
    mars = Mars(EchoProvider())
    assert mars.respond("hello") == "MARS received: hello"


def test_mars_preserves_input() -> None:
    mars = Mars(EchoProvider())
    assert "second" in mars.respond("second", history=[])
