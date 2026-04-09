from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServer:
    object: str
    id: str
    status: str
    source: str
    endpoints: List[ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpSessionsGetOutputMagicMcpEndpoint:
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
@dataclass
class ManagementInstanceMagicMcpSessionsGetOutput:
    object: str
    id: str
    session_id: str
    created_at: datetime
    updated_at: datetime
    magic_mcp_server: Optional[ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServer] = None
    magic_mcp_endpoint: Optional[ManagementInstanceMagicMcpSessionsGetOutputMagicMcpEndpoint] = None


class mapManagementInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints:
        return ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsGetOutputMagicMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServer:
        return ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapManagementInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsGetOutputMagicMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsGetOutputMagicMcpEndpoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsGetOutputMagicMcpEndpoint:
        return ManagementInstanceMagicMcpSessionsGetOutputMagicMcpEndpoint(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsGetOutputMagicMcpEndpoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsGetOutput:
        return ManagementInstanceMagicMcpSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        magic_mcp_server=mapManagementInstanceMagicMcpSessionsGetOutputMagicMcpServer.from_dict(data.get('magic_mcp_server')) if data.get('magic_mcp_server') else None,
        magic_mcp_endpoint=mapManagementInstanceMagicMcpSessionsGetOutputMagicMcpEndpoint.from_dict(data.get('magic_mcp_endpoint')) if data.get('magic_mcp_endpoint') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

