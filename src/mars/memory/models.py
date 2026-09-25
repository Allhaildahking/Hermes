"""Memory data models."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Memory:
    id: int | None
    content: str
    category: str = "general"
