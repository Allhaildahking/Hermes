"""Development model providers."""

from .core import Message


class EchoProvider:
    """Deterministic provider used before a real model is connected."""

    def generate(self, messages: list[Message]) -> str:
        if not messages:
            return "MARS is ready."
        return f"MARS received: {messages[-1].content}"
