from metorial_openai_compatible import MetorialOpenAICompatibleSession


class MetorialTogetherAISession(MetorialOpenAICompatibleSession):
    """TogetherAI provider session using OpenAI-compatible interface without strict mode."""
    
    def __init__(self, tool_mgr):
        # TogetherAI doesn't support strict mode
        super().__init__(tool_mgr, with_strict=False)


# Convenience functions
def build_togetherai_tools(tool_mgr):
    """Build TogetherAI-compatible tool definitions from Metorial tools."""
    session = MetorialTogetherAISession(tool_mgr)
    return session.tools


async def call_togetherai_tools(tool_mgr, tool_calls):
    """Call Metorial tools from TogetherAI tool calls."""
    session = MetorialTogetherAISession(tool_mgr)
    return await session.call_tools(tool_calls)
