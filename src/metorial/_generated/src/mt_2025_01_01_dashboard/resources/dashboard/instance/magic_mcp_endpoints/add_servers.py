from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpEndpointsAddServersOutput:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    consumer_profile_id: Optional[str] = None
    session_template_id: Optional[str] = None
    session_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class mapDashboardInstanceMagicMcpEndpointsAddServersOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsAddServersOutput:
        return DashboardInstanceMagicMcpEndpointsAddServersOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        consumer_profile_id=data.get('consumer_profile_id'),
        session_template_id=data.get('session_template_id'),
        session_id=data.get('session_id'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsAddServersOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpEndpointsAddServersBodyServers:
    magic_mcp_server_id: str
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
@dataclass
class DashboardInstanceMagicMcpEndpointsAddServersBody:
    magic_mcp_server_ids: Optional[List[str]] = None
    servers: Optional[List[DashboardInstanceMagicMcpEndpointsAddServersBodyServers]] = None


class mapDashboardInstanceMagicMcpEndpointsAddServersBodyServers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsAddServersBodyServers:
        return DashboardInstanceMagicMcpEndpointsAddServersBodyServers(
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsAddServersBodyServers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpEndpointsAddServersBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsAddServersBody:
        return DashboardInstanceMagicMcpEndpointsAddServersBody(
        magic_mcp_server_ids=data.get('magic_mcp_server_ids', []),
        servers=[mapDashboardInstanceMagicMcpEndpointsAddServersBodyServers.from_dict(item) for item in data.get('servers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsAddServersBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

