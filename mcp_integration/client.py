import asyncio
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


SERVER_PATH = Path(__file__).resolve().parent / "server.py"


async def call_mcp_tool(tool_name: str, arguments: dict):
    server_params = StdioServerParameters(
        command="python",
        args=[str(SERVER_PATH)],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            result = await session.call_tool(
                tool_name,
                arguments
            )

            return result


def create_ticket_via_mcp(
    customer_ticket,
    category,
    priority,
    sentiment,
    reason
):
    result = asyncio.run(
        call_mcp_tool(
            "create_ticket",
            {
                "customer_ticket": customer_ticket,
                "category": category,
                "priority": priority,
                "sentiment": sentiment,
                "reason": reason,
            }
        )
    )

    return result


def get_ticket_via_mcp(ticket_id):
    result = asyncio.run(
        call_mcp_tool(
            "get_ticket",
            {
                "ticket_id": ticket_id
            }
        )
    )

    return result