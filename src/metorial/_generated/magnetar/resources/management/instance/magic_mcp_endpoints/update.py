from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerConsumer] = None
@dataclass
class ManagementInstanceMagicMcpEndpointsUpdateOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwner] = None
@dataclass
class ManagementInstanceMagicMcpEndpointsUpdateOutput:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    enable_skill_editing: bool
    access: ManagementInstanceMagicMcpEndpointsUpdateOutputAccess
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerOrganizationMember:
        return ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerConsumer:
        return ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwner:
        return ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpEndpointsUpdateOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsUpdateOutputAccess:
        return ManagementInstanceMagicMcpEndpointsUpdateOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapManagementInstanceMagicMcpEndpointsUpdateOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsUpdateOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpEndpointsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsUpdateOutput:
        return ManagementInstanceMagicMcpEndpointsUpdateOutput(
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
        access=mapManagementInstanceMagicMcpEndpointsUpdateOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMagicMcpEndpointsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    enable_skill_editing: Optional[bool] = None


class mapManagementInstanceMagicMcpEndpointsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpEndpointsUpdateBody:
        return ManagementInstanceMagicMcpEndpointsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        enable_skill_editing=data.get('enable_skill_editing')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpEndpointsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

