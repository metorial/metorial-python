from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpTokensAddGroupsOutputServer:
    object: str
    id: str
    status: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpTokensAddGroupsOutputGroups:
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
class MagicMcpTokensAddGroupsOutput:
    object: str
    id: str
    status: str
    secret: str
    groups: List[MagicMcpTokensAddGroupsOutputGroups]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    server: Optional[MagicMcpTokensAddGroupsOutputServer] = None


class mapMagicMcpTokensAddGroupsOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensAddGroupsOutputServer:
        return MagicMcpTokensAddGroupsOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensAddGroupsOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensAddGroupsOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensAddGroupsOutputGroups:
        return MagicMcpTokensAddGroupsOutputGroups(
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
    def to_dict(value: Union[MagicMcpTokensAddGroupsOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensAddGroupsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensAddGroupsOutput:
        return MagicMcpTokensAddGroupsOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret=data.get('secret'),
        name=data.get('name'),
        description=data.get('description'),
        server=mapMagicMcpTokensAddGroupsOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        groups=[mapMagicMcpTokensAddGroupsOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensAddGroupsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpTokensAddGroupsBody:
    magic_mcp_group_ids: List[str]


class mapMagicMcpTokensAddGroupsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensAddGroupsBody:
        return MagicMcpTokensAddGroupsBody(
        magic_mcp_group_ids=data.get('magic_mcp_group_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensAddGroupsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

