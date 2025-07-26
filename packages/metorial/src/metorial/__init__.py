"""
Metorial Python SDK

The official Python SDK for Metorial - AI-powered tool calling and session management.
"""

__version__ = "1.0.0-rc.1"
__author__ = "Metorial Team"
__email__ = "support@metorial.com"

# Import main classes
try:
    from metorial_core import Metorial, MetorialAPIError
    from metorial_mcp_session import MetorialMcpSession
except ImportError:
    # Fallback for development
    pass

# Re-export main interfaces
__all__ = [
    "Metorial",
    "MetorialAPIError", 
    "MetorialMcpSession",
    "__version__",
]
