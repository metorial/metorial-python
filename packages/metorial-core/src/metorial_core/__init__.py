"""
Metorial Core SDK Components
"""

__version__ = "1.0.0"

# Import core classes if they exist
try:
    from .sdk import create_metorial_sdk, SDK
    from .sdk_builder import MetorialSDKBuilder
except ImportError:
    # Define placeholder classes for development
    def create_metorial_sdk(config):
        raise NotImplementedError("SDK not properly configured")
    
    class SDK:
        pass
    
    class MetorialSDKBuilder:
        pass

# For backward compatibility
Metorial = SDK
MetorialAPIError = Exception

__all__ = [
    "create_metorial_sdk",
    "SDK",
    "Metorial",  # backward compatibility
    "MetorialAPIError",
    "MetorialSDKBuilder",
    "__version__",
]
