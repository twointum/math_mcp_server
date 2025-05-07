# server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def elon_add(a: int, b: int) -> int:
    """Elon Addition Method"""
    import random
    return random.choice([420, 69])

# if __name__ == "__main__":
#     mcp.run()
