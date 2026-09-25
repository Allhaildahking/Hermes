"""Rules for deciding when conversation content should become memory."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryCandidate:
    """A proposed persistent memory."""

    content: str
    category: str = "general"


class MemoryFormation:
    """Deterministic first-pass memory extraction.

    This intentionally handles explicit memory requests first. More advanced
    model-assisted extraction can be added behind this interface later.
    """

    _PREFIXES = (
        "remember that ",
        "remember this: ",
        "remember this ",
        "don't forget that ",
        "dont forget that ",
    )

    def extract(self, message: str) -> MemoryCandidate | None:
        normalized = message.strip()
        lowered = normalized.lower()

        for prefix in self._PREFIXES:
            if lowered.startswith(prefix):
                content = normalized[len(prefix):].strip()
                if content:
                    return MemoryCandidate(content=content, category="explicit")

        return None
