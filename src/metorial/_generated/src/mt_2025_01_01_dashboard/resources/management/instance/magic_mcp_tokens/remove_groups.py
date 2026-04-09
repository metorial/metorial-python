from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpTokensRemoveGroupsOutputServer:
    object: str
    id: str
    status: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpTokensRemoveGroupsOutputEndpoint:
    object: str
    id: str
    status: str
    slug: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpTokensRemoveGroupsOutputGroups:
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
class ManagementInstanceMagicMcpTokensRemoveGroupsOutput:
    object: str
    id: str
    status: str
    secret: str
    groups: List[ManagementInstanceMagicMcpTokensRemoveGroupsOutputGroups]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    server: Optional[ManagementInstanceMagicMcpTokensRemoveGroupsOutputServer] = None
    endpoint: Optional[ManagementInstanceMagicMcpTokensRemoveGroupsOutputEndpoint] = None


class mapManagementInstanceMagicMcpTokensRemoveGroupsOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensRemoveGroupsOutputServer:
        return ManagementInstanceMagicMcpTokensRemoveGroupsOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensRemoveGroupsOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpTokensRemoveGroupsOutputEndpoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensRemoveGroupsOutputEndpoint:
        return ManagementInstanceMagicMcpTokensRemoveGroupsOutputEndpoint(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensRemoveGroupsOutputEndpoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpTokensRemoveGroupsOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensRemoveGroupsOutputGroups:
        return ManagementInstanceMagicMcpTokensRemoveGroupsOutputGroups(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensRemoveGroupsOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpTokensRemoveGroupsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensRemoveGroupsOutput:
        return ManagementInstanceMagicMcpTokensRemoveGroupsOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret=data.get('secret'),
        name=data.get('name'),
        description=data.get('description'),
        server=mapManagementInstanceMagicMcpTokensRemoveGroupsOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        endpoint=mapManagementInstanceMagicMcpTokensRemoveGroupsOutputEndpoint.from_dict(data.get('endpoint')) if data.get('endpoint') else None,
        groups=[mapManagementInstanceMagicMcpTokensRemoveGroupsOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensRemoveGroupsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMagicMcpTokensRemoveGroupsBody:
    magic_mcp_group_ids: List[str]


class mapManagementInstanceMagicMcpTokensRemoveGroupsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpTokensRemoveGroupsBody:
        return ManagementInstanceMagicMcpTokensRemoveGroupsBody(
        magic_mcp_group_ids=data.get('magic_mcp_group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpTokensRemoveGroupsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

