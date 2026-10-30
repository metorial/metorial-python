from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpEndpointsAddServersOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class MagicMcpEndpointsAddServersOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class MagicMcpEndpointsAddServersOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[MagicMcpEndpointsAddServersOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[MagicMcpEndpointsAddServersOutputAccessOwnerConsumer] = None
@dataclass
class MagicMcpEndpointsAddServersOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[MagicMcpEndpointsAddServersOutputAccessOwner] = None
@dataclass
class MagicMcpEndpointsAddServersOutput:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    enable_skill_editing: bool
    access: MagicMcpEndpointsAddServersOutputAccess
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapMagicMcpEndpointsAddServersOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsAddServersOutputAccessOwnerOrganizationMember:
        return MagicMcpEndpointsAddServersOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsAddServersOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsAddServersOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsAddServersOutputAccessOwnerConsumer:
        return MagicMcpEndpointsAddServersOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsAddServersOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsAddServersOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsAddServersOutputAccessOwner:
        return MagicMcpEndpointsAddServersOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapMagicMcpEndpointsAddServersOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapMagicMcpEndpointsAddServersOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsAddServersOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsAddServersOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsAddServersOutputAccess:
        return MagicMcpEndpointsAddServersOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapMagicMcpEndpointsAddServersOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsAddServersOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

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
        enable_skill_editing=data.get('enable_skill_editing'),
        access=mapMagicMcpEndpointsAddServersOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
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

