"""Stable reasoning boundary for MARS."""

from dataclasses import dataclass
from typing import Protocol

from .memory import MemoryManager


@dataclass(frozen=True)
class Message:
    role: str
    content: str


class ModelProvider(Protocol):
    def generate(self, messages: list[Message]) -> str:
        """Generate a response from a conversation."""


class Mars:
    """Top-level application boundary."""

    def __init__(
        self,
        provider: ModelProvider,
        memory: MemoryManager | None = None,
    ) -> None:
        self.provider = provider
        self.memory = memory

    def respond(self, message: str, history: list[Message] | None = None) -> str:
        messages = list(history or [])

        if self.memory is not None:
            memories = self.memory.recall(message)
            if memories:
                memory_context = "\n".join(
                    f"- [{memory.category}] {memory.content}" for memory in memories
                )
                messages.append(
                    Message(
                        role="system",
                        content=(
                            "Relevant persistent memory about the user/project:\n"
                            f"{memory_context}"
                        ),
                    )
                )

        messages.append(Message(role="user", content=message))
        return self.provider.generate(messages)
