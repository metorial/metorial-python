from metorial_openai_compatible import MetorialOpenAICompatibleSession


class MetorialXAISession(MetorialOpenAICompatibleSession):
    """XAI (Grok) provider session using OpenAI-compatible interface with strict mode."""
    
    def __init__(self, tool_mgr):
        # XAI supports strict mode
        super().__init__(tool_mgr, with_strict=True)


# Convenience functions
def build_xai_tools(tool_mgr):
    """Build XAI-compatible tool definitions from Metorial tools."""
    session = MetorialXAISession(tool_mgr)
    return session.tools


async def call_xai_tools(tool_mgr, tool_calls):
    """Call Metorial tools from XAI tool calls."""
    session = MetorialXAISession(tool_mgr)
    return await session.call_tools(tool_calls)
