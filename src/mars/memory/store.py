"""SQLite-backed persistent memory store."""

import sqlite3
from pathlib import Path

from .models import Memory


class SQLiteMemoryStore:
    """Stores durable MARS memories in SQLite."""

    def __init__(self, database_path: str = "data/mars.db") -> None:
        self.database_path = database_path
        if database_path != ":memory:":
            Path(database_path).parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    category TEXT NOT NULL DEFAULT 'general',
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def add(self, content: str, category: str = "general") -> Memory:
        content = content.strip()
        if not content:
            raise ValueError("Memory content cannot be empty.")

        with self._connect() as connection:
            cursor = connection.execute(
                "INSERT INTO memories (content, category) VALUES (?, ?)",
                (content, category),
            )
            memory_id = cursor.lastrowid

        return Memory(id=memory_id, content=content, category=category)

    def search(self, query: str, limit: int = 5) -> list[Memory]:
        query = query.strip()
        if not query:
            return []

        terms = [term for term in query.lower().split() if term]
        if not terms:
            return []

        clauses = " OR ".join("LOWER(content) LIKE ?" for _ in terms)
        parameters = [f"%{term}%" for term in terms]

        with self._connect() as connection:
            rows = connection.execute(
                f"""
                SELECT id, content, category
                FROM memories
                WHERE {clauses}
                ORDER BY id DESC
                LIMIT ?
                """,
                [*parameters, limit],
            ).fetchall()

        return [
            Memory(id=row["id"], content=row["content"], category=row["category"])
            for row in rows
        ]

    def list_recent(self, limit: int = 20) -> list[Memory]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT id, content, category
                FROM memories
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        return [
            Memory(id=row["id"], content=row["content"], category=row["category"])
            for row in rows
        ]
