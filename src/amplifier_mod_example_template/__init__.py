"""Example Amplifier module template."""

from __future__ import annotations

from typing import Any

from amplifier_core import Kernel
from amplifier_core.interfaces import ModelRequest, ModelResponse, ToolRequest, ToolResult


async def register(kernel: Kernel, config: dict[str, Any] | None = None) -> None:
    """Registers template capabilities with the kernel."""

    config = config or {}
    greeting = str(config.get("message", "Hello from template"))
    tool_topic = str(config.get("tool_topic", "tool:template"))
    model_topic = str(config.get("model_topic", "llm:template"))

    async def tool_handler(_topic: str, payload: object) -> ToolResult:
        if isinstance(payload, ToolRequest):
            name = payload.payload.get("name", "world")
        elif isinstance(payload, dict):
            name = payload.get("name", "world")
        else:
            name = str(payload)
        return ToolResult(success=True, data={"message": f"{greeting}, {name}!"})

    async def model_handler(_topic: str, payload: object) -> ModelResponse:
        if isinstance(payload, ModelRequest):
            prompt = payload.prompt
        else:
            prompt = str(payload)
        text = f"{greeting} -> {prompt}"
        return ModelResponse(text=text)

    await kernel.bus.subscribe(tool_topic, tool_handler)
    await kernel.bus.subscribe(model_topic, model_handler)


__all__ = ["register"]
