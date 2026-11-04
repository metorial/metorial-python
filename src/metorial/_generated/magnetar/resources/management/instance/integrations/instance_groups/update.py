from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateOutputImplementation:
    type: str
    magic_mcp_endpoint_id: str
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateOutputProviders:
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
class ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerConsumer] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwner] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    providers: List[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputProviders]
    access: ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccess
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    implementation: Optional[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputImplementation] = None
    archived_at: Optional[datetime] = None


class mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateOutputImplementation:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateOutputImplementation(
        type=data.get('type'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateOutputProviders:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateOutputProviders(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerOrganizationMember:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerConsumer:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwner:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccess:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateOutput:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        implementation=mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        access=mapManagementInstanceIntegrationsInstanceGroupsUpdateOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateBodyProviders:
    integration_instance_provider_id: str
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    providers: Optional[List[ManagementInstanceIntegrationsInstanceGroupsUpdateBodyProviders]] = None


class mapManagementInstanceIntegrationsInstanceGroupsUpdateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateBodyProviders:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateBodyProviders(
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsUpdateBody:
        return ManagementInstanceIntegrationsInstanceGroupsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapManagementInstanceIntegrationsInstanceGroupsUpdateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

