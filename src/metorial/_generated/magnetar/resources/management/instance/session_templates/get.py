from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionTemplatesGetOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class ManagementInstanceSessionTemplatesGetOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionTemplatesGetOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[ManagementInstanceSessionTemplatesGetOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[ManagementInstanceSessionTemplatesGetOutputAccessOwnerConsumer] = None
@dataclass
class ManagementInstanceSessionTemplatesGetOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[ManagementInstanceSessionTemplatesGetOutputAccessOwner] = None
@dataclass
class ManagementInstanceSessionTemplatesGetOutputProvidersDeployment:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSessionTemplatesGetOutputProvidersConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSessionTemplatesGetOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionTemplatesGetOutputProviders:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: ManagementInstanceSessionTemplatesGetOutputProvidersDeployment
    config: ManagementInstanceSessionTemplatesGetOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[ManagementInstanceSessionTemplatesGetOutputProvidersAuthConfig] = None
@dataclass
class ManagementInstanceSessionTemplatesGetOutput:
    object: str
    id: str
    status: str
    name: str
    access: ManagementInstanceSessionTemplatesGetOutputAccess
    providers: List[ManagementInstanceSessionTemplatesGetOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    integration_instance_id: Optional[str] = None
    integration_instance_group_id: Optional[str] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None


class mapManagementInstanceSessionTemplatesGetOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputAccessOwnerOrganizationMember:
        return ManagementInstanceSessionTemplatesGetOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputAccessOwnerConsumer:
        return ManagementInstanceSessionTemplatesGetOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputAccessOwner:
        return ManagementInstanceSessionTemplatesGetOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapManagementInstanceSessionTemplatesGetOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapManagementInstanceSessionTemplatesGetOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputAccess:
        return ManagementInstanceSessionTemplatesGetOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapManagementInstanceSessionTemplatesGetOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputProvidersDeployment:
        return ManagementInstanceSessionTemplatesGetOutputProvidersDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputProvidersConfig:
        return ManagementInstanceSessionTemplatesGetOutputProvidersConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputProvidersAuthConfig:
        return ManagementInstanceSessionTemplatesGetOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutputProviders:
        return ManagementInstanceSessionTemplatesGetOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapManagementInstanceSessionTemplatesGetOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapManagementInstanceSessionTemplatesGetOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceSessionTemplatesGetOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesGetOutput:
        return ManagementInstanceSessionTemplatesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_group_id=data.get('integration_instance_group_id'),
        identity_actor_id=data.get('identity_actor_id'),
        access=mapManagementInstanceSessionTemplatesGetOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        identity_id=data.get('identity_id'),
        providers=[mapManagementInstanceSessionTemplatesGetOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

