from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer:
    object: str
    id: str
    status: str
    source: str
    endpoints: List[DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpSessionsGetOutput:
    object: str
    id: str
    subspace_session_id: str
    subspace_session_template_id: str
    magic_mcp_server: DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer
    created_at: datetime
    updated_at: datetime


class mapDashboardInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints:
        return DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer:
        return DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapDashboardInstanceMagicMcpSessionsGetOutputMagicMcpServerEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsGetOutput:
        return DashboardInstanceMagicMcpSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        subspace_session_id=data.get('subspace_session_id'),
        subspace_session_template_id=data.get('subspace_session_template_id'),
        magic_mcp_server=mapDashboardInstanceMagicMcpSessionsGetOutputMagicMcpServer.from_dict(data.get('magic_mcp_server')) if data.get('magic_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

