"""Memory orchestration for MARS."""

from .models import Memory
from .store import SQLiteMemoryStore


class MemoryManager:
    """High-level interface for storing and retrieving persistent memories."""

    def __init__(self, store: SQLiteMemoryStore) -> None:
        self.store = store

    def remember(self, content: str, category: str = "general") -> Memory:
        return self.store.add(content, category)

    def recall(self, query: str, limit: int = 5) -> list[Memory]:
        return self.store.search(query, limit=limit)

    def recent(self, limit: int = 20) -> list[Memory]:
        return self.store.list_recent(limit=limit)
