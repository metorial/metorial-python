from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer] = None
@dataclass
class DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwner] = None
@dataclass
class DashboardInstanceMagicMcpEndpointsRemoveServersOutput:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    enable_skill_editing: bool
    access: DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccess
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None


class mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember:
        return DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer:
        return DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwner:
        return DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccess:
        return DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsRemoveServersOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpEndpointsRemoveServersOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsRemoveServersOutput:
        return DashboardInstanceMagicMcpEndpointsRemoveServersOutput(
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
        access=mapDashboardInstanceMagicMcpEndpointsRemoveServersOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsRemoveServersOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpEndpointsRemoveServersBody:
    magic_mcp_server_ids: List[str]


class mapDashboardInstanceMagicMcpEndpointsRemoveServersBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpEndpointsRemoveServersBody:
        return DashboardInstanceMagicMcpEndpointsRemoveServersBody(
        magic_mcp_server_ids=data.get('magic_mcp_server_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpEndpointsRemoveServersBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

