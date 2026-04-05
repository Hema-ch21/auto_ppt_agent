# mcp/client.py
# -----------------------------------
# MCP Client: Routes tool calls from agent → server
# -----------------------------------

class MCPClient:
    def __init__(self, server):
        self.server = server

    async def call(self, tool_name, **kwargs):

        if tool_name == "create_presentation":
            return self.server.create_presentation()

        elif tool_name == "add_slide":
            return self.server.add_slide(kwargs["title"], kwargs["content"])

        elif tool_name == "save":
            return self.server.save()

        return "Unknown tool"