from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpEndpointsAddServersOutput:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapMagicMcpEndpointsAddServersOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsAddServersOutput:
        return MagicMcpEndpointsAddServersOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsAddServersOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpEndpointsAddServersBodyMagicMcpServers:
    magic_mcp_server_id: str
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
@dataclass
class MagicMcpEndpointsAddServersBody:
    magic_mcp_servers: Optional[List[MagicMcpEndpointsAddServersBodyMagicMcpServers]] = None


class mapMagicMcpEndpointsAddServersBodyMagicMcpServers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsAddServersBodyMagicMcpServers:
        return MagicMcpEndpointsAddServersBodyMagicMcpServers(
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsAddServersBodyMagicMcpServers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsAddServersBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsAddServersBody:
        return MagicMcpEndpointsAddServersBody(
        magic_mcp_servers=[mapMagicMcpEndpointsAddServersBodyMagicMcpServers.from_dict(item) for item in data.get('magic_mcp_servers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsAddServersBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

