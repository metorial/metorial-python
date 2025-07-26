from metorial_openai_compatible import MetorialOpenAICompatibleSession


class MetorialDeepSeekSession(MetorialOpenAICompatibleSession):
    """DeepSeek provider session using OpenAI-compatible interface without strict mode."""
    
    def __init__(self, tool_mgr):
        # DeepSeek doesn't support strict mode
        super().__init__(tool_mgr, with_strict=False)


# Convenience functions
def build_deepseek_tools(tool_mgr):
    """Build DeepSeek-compatible tool definitions from Metorial tools."""
    session = MetorialDeepSeekSession(tool_mgr)
    return session.tools


async def call_deepseek_tools(tool_mgr, tool_calls):
    """Call Metorial tools from DeepSeek tool calls."""
    session = MetorialDeepSeekSession(tool_mgr)
    return await session.call_tools(tool_calls)
