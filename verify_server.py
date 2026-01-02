import asyncio
import os
import sys

# Add the virtual environment site-packages to python path
sys.path.append(os.path.abspath("."))

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession
from mcp.types import ClientRequest, CallToolRequest, Tool

server_script = "/Users/grendel/repos/mcp_test/server.py"
python_executable = "/Users/grendel/repos/mcp_test/.venv/bin/python"

async def run():
    print(f"Connecting to server at {server_script}...")
    
    server_params = StdioServerParameters(
        command=python_executable,
        args=[server_script],
        env=os.environ.copy()
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            print("Connected! Initializing...")
            await session.initialize()
            
            print("Listing tools...")
            tools = await session.list_tools()
            print(f"Found {len(tools.tools)} tools")
            for t in tools.tools:
                print(f"- {t.name}: {t.description}")
            
            tool_name = "test_tool"
            print(f"\nCalling tool '{tool_name}'...")
            try:
                result = await session.call_tool(tool_name, arguments={})
                print("Tool Result:")
                # Initialize content as an empty string to handle the result
                content = ""
                if hasattr(result, 'content'):
                    for item in result.content:
                        if hasattr(item, 'text'):
                            content += item.text
                print(content if content else result)
            except Exception as e:
                print(f"Error calling tool: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except Exception as e:
        print(f"Failed to run client: {e}")
