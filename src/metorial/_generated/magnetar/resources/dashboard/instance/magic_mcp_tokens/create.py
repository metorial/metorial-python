from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpTokensCreateOutputServer:
    object: str
    id: str
    status: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpTokensCreateOutputEndpoint:
    object: str
    id: str
    status: str
    slug: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpTokensCreateOutputGroups:
    object: str
    id: str
    status: str
    slug: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpTokensCreateOutput:
    object: str
    id: str
    status: str
    secret: str
    groups: List[DashboardInstanceMagicMcpTokensCreateOutputGroups]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    server: Optional[DashboardInstanceMagicMcpTokensCreateOutputServer] = None
    endpoint: Optional[DashboardInstanceMagicMcpTokensCreateOutputEndpoint] = None


class mapDashboardInstanceMagicMcpTokensCreateOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensCreateOutputServer:
        return DashboardInstanceMagicMcpTokensCreateOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensCreateOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensCreateOutputEndpoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensCreateOutputEndpoint:
        return DashboardInstanceMagicMcpTokensCreateOutputEndpoint(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensCreateOutputEndpoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensCreateOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensCreateOutputGroups:
        return DashboardInstanceMagicMcpTokensCreateOutputGroups(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensCreateOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensCreateOutput:
        return DashboardInstanceMagicMcpTokensCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret=data.get('secret'),
        name=data.get('name'),
        description=data.get('description'),
        server=mapDashboardInstanceMagicMcpTokensCreateOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        endpoint=mapDashboardInstanceMagicMcpTokensCreateOutputEndpoint.from_dict(data.get('endpoint')) if data.get('endpoint') else None,
        groups=[mapDashboardInstanceMagicMcpTokensCreateOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpTokensCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    magic_mcp_group_ids: Optional[List[str]] = None
    magic_mcp_server_id: Optional[str] = None
    magic_mcp_endpoint_id: Optional[str] = None


class mapDashboardInstanceMagicMcpTokensCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensCreateBody:
        return DashboardInstanceMagicMcpTokensCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        magic_mcp_group_ids=data.get('magic_mcp_group_ids', []),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

