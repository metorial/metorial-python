# metorial-util-endpoint

Endpoint utilities for Metorial. Provides HTTP client functionality and endpoint management.

## Installation

```bash
pip install metorial-util-endpoint
# or
uv add metorial-util-endpoint
# or
poetry add metorial-util-endpoint
```

## Features

- 🌐 **HTTP Client**: HTTP client utilities for API communication
- 🔧 **Endpoint Management**: Manage API endpoints and requests
- ⚡ **Async Support**: Full async/await support
- 🛠️ **Utility Functions**: Common HTTP utilities

## Usage

This package is typically used internally by other Metorial packages and not directly by end users.

### Internal Usage

```python
from metorial_util_endpoint import EndpointClient

# Used internally by Metorial packages
client = EndpointClient()
```

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
