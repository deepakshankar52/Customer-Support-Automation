# from mcp.server.mcpserver import MCPServer

# mcp = MCPServer("Customer Support MCP Server")


# @mcp.tool()
# def get_ticket(ticket_id: str) -> str:
#     """Get information about a customer support ticket."""

#     return f"Ticket {ticket_id} retrieved successfully."


# if __name__ == "__main__":
#     mcp.run(transport="stdio")


import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from mcp.server.mcpserver import MCPServer
from ticketing.client import TicketingClient


mcp = MCPServer("Customer Support MCP Server")

ticketing_client = TicketingClient()


@mcp.tool()
def create_ticket(
    customer_ticket: str,
    category: str,
    priority: str,
    sentiment: str,
    reason: str,
) -> dict:
    """Create a customer support ticket."""

    return ticketing_client.create_ticket(
        customer_ticket=customer_ticket,
        category=category,
        priority=priority,
        sentiment=sentiment,
        reason=reason,
    )


@mcp.tool()
def get_ticket(ticket_id: str) -> dict:
    """Retrieve an existing customer support ticket by ticket ID."""

    return ticketing_client.get_ticket(ticket_id)


if __name__ == "__main__":
    mcp.run(transport="stdio")