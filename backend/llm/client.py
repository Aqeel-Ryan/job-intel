"""Thin async wrapper around the Anthropic SDK.

All model parameters (``LLM_MODEL``, ``LLM_MAX_TOKENS``, ``LLM_TEMPERATURE``)
and the API key come from config — never hardcoded.
"""

import json
from types import ModuleType

import anthropic


class LLMClient:
    """Wraps ``anthropic.AsyncAnthropic`` with config-driven defaults."""

    def __init__(self, config: ModuleType) -> None:
        """Initialise the async Anthropic client from config.

        Args:
            config: The config module (provides ``ANTHROPIC_API_KEY``,
                ``LLM_MODEL``, ``LLM_MAX_TOKENS``, ``LLM_TEMPERATURE``).
        """
        self.config = config
        self.client = anthropic.AsyncAnthropic(api_key=config.ANTHROPIC_API_KEY)

    async def complete(self, system: str, user: str) -> str:
        """Send a single-turn chat request and return the text response.

        Uses ``LLM_MODEL``, ``LLM_MAX_TOKENS``, and ``LLM_TEMPERATURE`` from
        config via ``client.messages.create``.

        Args:
            system: System prompt.
            user: User message content.

        Returns:
            The concatenated text of the model's response.
        """
        # TODO: await self.client.messages.create(model=config.LLM_MODEL,
        #   max_tokens=config.LLM_MAX_TOKENS, temperature=config.LLM_TEMPERATURE,
        #   system=system, messages=[{"role": "user", "content": user}])
        #   then join text blocks.
        raise NotImplementedError

    async def complete_json(self, system: str, user: str, schema: dict) -> dict:
        """Send a request instructing the model to return JSON, then parse it.

        Same model parameters as :meth:`complete`; uses ``output_config.format``
        with the supplied JSON schema so the response is constrained and
        parseable with :func:`json.loads`.

        Args:
            system: System prompt.
            user: User message content.
            schema: JSON schema the response must conform to.

        Returns:
            The parsed JSON object.
        """
        # TODO: call messages.create with output_config={"format":
        #   {"type": "json_schema", "schema": schema}}, then json.loads the text.
        raise NotImplementedError
