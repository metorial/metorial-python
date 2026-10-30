from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpEndpointsCreateOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class MagicMcpEndpointsCreateOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class MagicMcpEndpointsCreateOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[MagicMcpEndpointsCreateOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[MagicMcpEndpointsCreateOutputAccessOwnerConsumer] = None
@dataclass
class MagicMcpEndpointsCreateOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[MagicMcpEndpointsCreateOutputAccessOwner] = None
@dataclass
class MagicMcpEndpointsCreateOutput:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    enable_skill_editing: bool
    access: MagicMcpEndpointsCreateOutputAccess
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapMagicMcpEndpointsCreateOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsCreateOutputAccessOwnerOrganizationMember:
        return MagicMcpEndpointsCreateOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsCreateOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsCreateOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsCreateOutputAccessOwnerConsumer:
        return MagicMcpEndpointsCreateOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsCreateOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsCreateOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsCreateOutputAccessOwner:
        return MagicMcpEndpointsCreateOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapMagicMcpEndpointsCreateOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapMagicMcpEndpointsCreateOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsCreateOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsCreateOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsCreateOutputAccess:
        return MagicMcpEndpointsCreateOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapMagicMcpEndpointsCreateOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsCreateOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsCreateOutput:
        return MagicMcpEndpointsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        enable_skill_editing=data.get('enable_skill_editing'),
        access=mapMagicMcpEndpointsCreateOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpEndpointsCreateBodyMagicMcpServers:
    magic_mcp_server_id: str
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
@dataclass
class MagicMcpEndpointsCreateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    consumer_profile_id: Optional[str] = None
    skill_plugin_id: Optional[str] = None
    enable_skill_editing: Optional[bool] = None
    magic_mcp_servers: Optional[List[MagicMcpEndpointsCreateBodyMagicMcpServers]] = None


class mapMagicMcpEndpointsCreateBodyMagicMcpServers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsCreateBodyMagicMcpServers:
        return MagicMcpEndpointsCreateBodyMagicMcpServers(
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsCreateBodyMagicMcpServers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsCreateBody:
        return MagicMcpEndpointsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        consumer_profile_id=data.get('consumer_profile_id'),
        skill_plugin_id=data.get('skill_plugin_id'),
        enable_skill_editing=data.get('enable_skill_editing'),
        magic_mcp_servers=[mapMagicMcpEndpointsCreateBodyMagicMcpServers.from_dict(item) for item in data.get('magic_mcp_servers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

