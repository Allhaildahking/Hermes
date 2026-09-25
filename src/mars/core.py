"""Stable reasoning boundary for MARS."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Message:
    role: str
    content: str


class ModelProvider(Protocol):
    def generate(self, messages: list[Message]) -> str:
        """Generate a response from a conversation."""


class Mars:
    """Top-level application boundary."""

    def __init__(self, provider: ModelProvider) -> None:
        self.provider = provider

    def respond(self, message: str, history: list[Message] | None = None) -> str:
        messages = list(history or [])
        messages.append(Message(role="user", content=message))
        return self.provider.generate(messages)
