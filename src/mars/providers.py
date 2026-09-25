"""Model providers for MARS."""

from google import genai
from google.genai import types

from .config import settings
from .core import Message


class EchoProvider:
    """Deterministic provider used for local development and tests."""

    def generate(self, messages: list[Message]) -> str:
        if not messages:
            return "MARS is ready."
        return f"MARS received: {messages[-1].content}"


class GeminiProvider:
    """Gemini-backed model provider."""

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        client: genai.Client | None = None,
    ) -> None:
        self.model = model or settings.gemini_model
        self.client = client or genai.Client(api_key=api_key or settings.gemini_api_key)

    def generate(self, messages: list[Message]) -> str:
        contents = [
            types.Content(
                role="model" if message.role == "assistant" else "user",
                parts=[types.Part(text=message.content)],
            )
            for message in messages
        ]
        response = self.client.models.generate_content(
            model=self.model,
            contents=contents,
        )
        if not response.text:
            raise RuntimeError("Gemini returned an empty response.")
        return response.text
