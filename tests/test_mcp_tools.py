import os
import pytest
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters


@pytest.mark.asyncio
async def test_mcp_campaign_tool():
    params = StdioServerParameters(
        command="python",
        args=["-m", "app.mcp.server"],
        env={**os.environ, "APP_ENV": "test"},
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "campaign_performance", {"client_id": "abc"}
            )

            # MCP returns JSON text inside content[0].text
            assert "client_id" in result.content[0].text


@pytest.mark.asyncio
async def test_mcp_rag_tool():
    params = StdioServerParameters(
        command="python",
        args=["-m", "app.mcp.server"],
        env={**os.environ, "APP_ENV": "test"},  # 🔥 THIS IS THE FIX
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "ask_docs", {"question": "What is donor retention?"}
            )

            assert "answer" in result.content[0].text
