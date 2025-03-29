from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("my_tool_name")

@mcp.tool()
async def my_first_tool(param1: str, param2: int):
    """
    Your tool description here.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Your tool's result
    """
    # Your tool's logic
    result = f"You entered: {param1} and {param2}"
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")