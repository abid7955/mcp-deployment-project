from typing import Any
import requests
from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Binance MCP", port=8001, host="0.0.0.0")



@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather location."""
    return "It's always raining in California"

if __name__ == "__main__":
    # Run the MCP server with HTTP transport
    mcp.run(transport="streamable-http")
