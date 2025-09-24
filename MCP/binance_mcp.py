from typing import Any
import requests
from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Binance MCP", port=8000, host="0.0.0.0")


def get_symbol_from_name(name: str) -> str:
    """
    Convert a friendly crypto name to the Binance trading pair symbol.
    """
    if name.lower() in ["bitcoin", "btc"]:
        return "BTCUSDT"
    elif name.lower() in ["ethereum", "eth"]:
        return "ETHUSDT"
    else:
        return name.upper()


@mcp.tool()
def get_price(symbol: str) -> Any:
    """
    Get the current price of a crypto asset from Binance.

    Args:
        symbol (str): The symbol of the crypto asset (e.g., BTC, ETH).

    Returns:
        Any: The current price of the crypto asset.
    """
    symbol = get_symbol_from_name(symbol)
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()




if __name__ == "__main__":
    # Run the MCP server with HTTP transport
    mcp.run(transport="streamable-http")
