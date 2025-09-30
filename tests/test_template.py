import asyncio
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
module_src = (repo_root / "src").resolve()
core_src = (repo_root.parent / "amplifier-core" / "src").resolve()
assert module_src.exists()
assert core_src.exists()
sys.path.extend([str(module_src), str(core_src)])

from amplifier_core import Kernel
from amplifier_core.interfaces import ModelRequest, ToolRequest

from amplifier_mod_example_template import register


def test_template_module_registers_resources() -> None:
    kernel = Kernel()

    async def scenario() -> None:
        await kernel.start()
        await register(
            kernel,
            {
                "message": "Howdy",
                "tool_topic": "tool:test-template",
                "model_topic": "llm:test-template",
            },
        )
        tool_results = await kernel.bus.publish(
            "tool:test-template",
            ToolRequest(payload={"name": "Amplifier"}),
        )
        assert tool_results[0].data == {"message": "Howdy, Amplifier!"}

        model_results = await kernel.bus.publish(
            "llm:test-template",
            ModelRequest(prompt="demo"),
        )
        assert model_results[0].text == "Howdy -> demo"
        await kernel.shutdown()

    asyncio.run(scenario())
