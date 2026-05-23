from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpEndpointsCreateOutput:
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


class mapManagementInstanceMagicMcpEndpointsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsCreateOutput:
        return ManagementInstanceMagicMcpEndpointsCreateOutput(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMagicMcpEndpointsCreateBodyMagicMcpServers:
    magic_mcp_server_id: str
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
@dataclass
class ManagementInstanceMagicMcpEndpointsCreateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    consumer_profile_id: Optional[str] = None
    skill_plugin_id: Optional[str] = None
    magic_mcp_servers: Optional[List[ManagementInstanceMagicMcpEndpointsCreateBodyMagicMcpServers]] = None


class mapManagementInstanceMagicMcpEndpointsCreateBodyMagicMcpServers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsCreateBodyMagicMcpServers:
        return ManagementInstanceMagicMcpEndpointsCreateBodyMagicMcpServers(
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsCreateBodyMagicMcpServers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpEndpointsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsCreateBody:
        return ManagementInstanceMagicMcpEndpointsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        consumer_profile_id=data.get('consumer_profile_id'),
        skill_plugin_id=data.get('skill_plugin_id'),
        magic_mcp_servers=[mapManagementInstanceMagicMcpEndpointsCreateBodyMagicMcpServers.from_dict(item) for item in data.get('magic_mcp_servers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

