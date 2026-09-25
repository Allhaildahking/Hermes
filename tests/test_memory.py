from mars.memory import MemoryManager, SQLiteMemoryStore


def test_memory_persists_and_can_be_recalled() -> None:
    store = SQLiteMemoryStore(":memory:")
    memory = MemoryManager(store)

    saved = memory.remember(
        "User wants MARS to be a general personal AI.",
        category="project",
    )

    results = memory.recall("general personal AI")

    assert saved.id is not None
    assert len(results) == 1
    assert results[0].content == saved.content
    assert results[0].category == "project"


def test_empty_memory_is_rejected() -> None:
    store = SQLiteMemoryStore(":memory:")

    try:
        store.add("   ")
    except ValueError as error:
        assert str(error) == "Memory content cannot be empty."
    else:
        raise AssertionError("Expected empty memory to be rejected.")


def test_recent_memories_are_newest_first() -> None:
    store = SQLiteMemoryStore(":memory:")
    memory = MemoryManager(store)

    memory.remember("first")
    memory.remember("second")

    assert [item.content for item in memory.recent()] == ["second", "first"]
