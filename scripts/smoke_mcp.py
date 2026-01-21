import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters


async def main():
    params = StdioServerParameters(
        command="python",
        args=["-m", "app.mcp.server"],
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\n--- campaign_performance ---")
            res = await session.call_tool("campaign_performance", {"client_id": "abc"})
            print(res.content[0].text)

            print("\n--- donor_retention ---")
            res = await session.call_tool("donor_retention", {"client_id": "abc"})
            print(res.content[0].text)

            print("\n--- ask_docs ---")
            res = await session.call_tool(
                "ask_docs", {"question": "What is donor retention?"}
            )
            print(res.content[0].text)


asyncio.run(main())
