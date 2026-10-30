from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class MagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class MagicMcpEndpointsRemoveServersOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[MagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[MagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer] = None
@dataclass
class MagicMcpEndpointsRemoveServersOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[MagicMcpEndpointsRemoveServersOutputAccessOwner] = None
@dataclass
class MagicMcpEndpointsRemoveServersOutput:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    enable_skill_editing: bool
    access: MagicMcpEndpointsRemoveServersOutputAccess
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember:
        return MagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer:
        return MagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsRemoveServersOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsRemoveServersOutputAccessOwner:
        return MagicMcpEndpointsRemoveServersOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsRemoveServersOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsRemoveServersOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsRemoveServersOutputAccess:
        return MagicMcpEndpointsRemoveServersOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapMagicMcpEndpointsRemoveServersOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsRemoveServersOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsRemoveServersOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsRemoveServersOutput:
        return MagicMcpEndpointsRemoveServersOutput(
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
        access=mapMagicMcpEndpointsRemoveServersOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsRemoveServersOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpEndpointsRemoveServersBody:
    magic_mcp_server_ids: List[str]


class mapMagicMcpEndpointsRemoveServersBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsRemoveServersBody:
        return MagicMcpEndpointsRemoveServersBody(
        magic_mcp_server_ids=data.get('magic_mcp_server_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsRemoveServersBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

