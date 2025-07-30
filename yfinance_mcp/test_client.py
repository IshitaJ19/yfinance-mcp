from fastmcp import Client
import asyncio


async def main() -> None:

    async with Client("http://127.0.0.1:8000/mcp") as client:
       
        tools = await client.list_tools()

        print(f"Available tools: {tools}")

        result = await client.call_tool("get_gross_margins", {"ticker": "AAPL"})
        print(f'\nGross margins for {"AAPL"}: {result.structured_content.get("result")}\n')

        # result = await client.call_tool("screen_stocks", {
        #     "sector": "Technology",
        #     "market_cap": "large",
        #     "revenue_growth_lower_bound": 10.0,
        #     "margin_trend": "improving"
        # })
        # print(f'\nScreened stocks: {result.structured_content.get("results")}\n')

        result = await client.call_tool("get_market_cap", {"ticker": "GOOGL"})
        print(f'\nMarket cap for {"GOOGL"}: {result.structured_content}')


if __name__ == "__main__":
    asyncio.run(main())
