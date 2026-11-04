from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationsInstanceGroupsDeleteOutputImplementation:
    type: str
    magic_mcp_endpoint_id: str
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsDeleteOutputProviders:
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
class ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerConsumer] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwner] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    providers: List[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputProviders]
    access: ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccess
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    implementation: Optional[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputImplementation] = None
    archived_at: Optional[datetime] = None


class mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsDeleteOutputImplementation:
        return ManagementInstanceIntegrationsInstanceGroupsDeleteOutputImplementation(
        type=data.get('type'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsDeleteOutputProviders:
        return ManagementInstanceIntegrationsInstanceGroupsDeleteOutputProviders(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerOrganizationMember:
        return ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerConsumer:
        return ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwner:
        return ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccess:
        return ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsDeleteOutput:
        return ManagementInstanceIntegrationsInstanceGroupsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        implementation=mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        access=mapManagementInstanceIntegrationsInstanceGroupsDeleteOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

