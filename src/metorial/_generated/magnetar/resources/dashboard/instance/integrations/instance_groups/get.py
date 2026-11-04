from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationsInstanceGroupsGetOutputImplementation:
    type: str
    magic_mcp_endpoint_id: str
@dataclass
class DashboardInstanceIntegrationsInstanceGroupsGetOutputProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_group_id: str
    integration_instance_id: str
    integration_instance_provider_id: str
    is_override_tool_filter: bool
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    integration_provider_id: Optional[str] = None
    tool_filter: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerConsumer] = None
@dataclass
class DashboardInstanceIntegrationsInstanceGroupsGetOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwner] = None
@dataclass
class DashboardInstanceIntegrationsInstanceGroupsGetOutput:
    object: str
    id: str
    status: str
    name: str
    providers: List[DashboardInstanceIntegrationsInstanceGroupsGetOutputProviders]
    access: DashboardInstanceIntegrationsInstanceGroupsGetOutputAccess
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    implementation: Optional[DashboardInstanceIntegrationsInstanceGroupsGetOutputImplementation] = None
    archived_at: Optional[datetime] = None


class mapDashboardInstanceIntegrationsInstanceGroupsGetOutputImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstanceGroupsGetOutputImplementation:
        return DashboardInstanceIntegrationsInstanceGroupsGetOutputImplementation(
        type=data.get('type'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstanceGroupsGetOutputImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstanceGroupsGetOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstanceGroupsGetOutputProviders:
        return DashboardInstanceIntegrationsInstanceGroupsGetOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        integration_instance_group_id=data.get('integration_instance_group_id'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_provider_id=data.get('integration_provider_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        tool_filter=data.get('tool_filter'),
        is_override_tool_filter=data.get('is_override_tool_filter'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstanceGroupsGetOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerOrganizationMember:
        return DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerConsumer:
        return DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwner:
        return DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstanceGroupsGetOutputAccess:
        return DashboardInstanceIntegrationsInstanceGroupsGetOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstanceGroupsGetOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstanceGroupsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstanceGroupsGetOutput:
        return DashboardInstanceIntegrationsInstanceGroupsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        implementation=mapDashboardInstanceIntegrationsInstanceGroupsGetOutputImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapDashboardInstanceIntegrationsInstanceGroupsGetOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        access=mapDashboardInstanceIntegrationsInstanceGroupsGetOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstanceGroupsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

