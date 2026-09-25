from mars.core import Mars
from mars.memory import MemoryManager, SQLiteMemoryStore
from mars.providers import EchoProvider


def test_mars_responds_through_provider() -> None:
    mars = Mars(EchoProvider())
    assert mars.respond("hello") == "MARS received: hello"


def test_mars_preserves_input() -> None:
    mars = Mars(EchoProvider())
    assert "second" in mars.respond("second", history=[])


def test_mars_retrieves_relevant_memory() -> None:
    memory = MemoryManager(SQLiteMemoryStore(":memory:"))
    memory.remember("User wants MARS to be a general personal AI.", category="project")

    mars = Mars(EchoProvider(), memory=memory)
    response = mars.respond("What is MARS supposed to be?")

    assert "What is MARS supposed to be?" in response
