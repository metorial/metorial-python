from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpSessionsGetOutputMagicMcpServerEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class MagicMcpSessionsGetOutputMagicMcpServer:
    object: str
    id: str
    status: str
    source: str
    endpoints: List[MagicMcpSessionsGetOutputMagicMcpServerEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpSessionsGetOutput:
    object: str
    id: str
    subspace_session_id: str
    subspace_session_template_id: str
    magic_mcp_server: MagicMcpSessionsGetOutputMagicMcpServer
    created_at: datetime
    updated_at: datetime


class mapMagicMcpSessionsGetOutputMagicMcpServerEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsGetOutputMagicMcpServerEndpoints:
        return MagicMcpSessionsGetOutputMagicMcpServerEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsGetOutputMagicMcpServerEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsGetOutputMagicMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsGetOutputMagicMcpServer:
        return MagicMcpSessionsGetOutputMagicMcpServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapMagicMcpSessionsGetOutputMagicMcpServerEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsGetOutputMagicMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsGetOutput:
        return MagicMcpSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        subspace_session_id=data.get('subspace_session_id'),
        subspace_session_template_id=data.get('subspace_session_template_id'),
        magic_mcp_server=mapMagicMcpSessionsGetOutputMagicMcpServer.from_dict(data.get('magic_mcp_server')) if data.get('magic_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

