from mcp.server.fastmcp import FastMCP
from mcp import Tool

# Initialize FastMCP server
mcp = FastMCP()

@mcp.tool()
async def test_tool() -> str:
    '''
    This is a test tool that enables the user to see that they have correctly implemented a their MCP server. 
    It takes no arguments, when invoked this function will return a string that you should output to confirm
    to them that you have correctly received the request. 
    '''
    return "Hi there! MCP Server working >:)"

@mcp.tool()
async def add(a: int, b: int) -> int:
    return a + b
        
if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")


