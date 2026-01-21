import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server = StdioServerParameters(command="python", args=["mcp/server.py"])

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\n--- Available tools ---")
            tools = await session.list_tools()
            for name, schema in tools:
                print("-", name)

            print("\n--- Calling campaign_performance ---")
            res = await session.call_tool("campaign_performance", {"client_id": "abc"})
            print(res.content[0].text)

            print("\n--- Calling ask_docs ---")
            res = await session.call_tool(
                "ask_docs", {"question": "How is donor retention defined?"}
            )
            print(res.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
