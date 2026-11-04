from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerConsumer] = None
@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwner] = None
@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersDeployment:
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
class IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersConfig:
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
class IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateOutputProviders:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersDeployment
    config: IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersAuthConfig] = None
@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateOutput:
    object: str
    id: str
    status: str
    name: str
    access: IntegrationsInstanceGroupsCreateSessionTemplateOutputAccess
    providers: List[IntegrationsInstanceGroupsCreateSessionTemplateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    integration_instance_id: Optional[str] = None
    integration_instance_group_id: Optional[str] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None


class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerOrganizationMember:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerConsumer:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwner:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputAccess:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersDeployment:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersDeployment(
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
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersConfig:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersConfig(
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
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersAuthConfig:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutputProviders:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionTemplateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateOutput:
        return IntegrationsInstanceGroupsCreateSessionTemplateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_group_id=data.get('integration_instance_group_id'),
        identity_actor_id=data.get('identity_actor_id'),
        access=mapIntegrationsInstanceGroupsCreateSessionTemplateOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        identity_id=data.get('identity_id'),
        providers=[mapIntegrationsInstanceGroupsCreateSessionTemplateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstanceGroupsCreateSessionTemplateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapIntegrationsInstanceGroupsCreateSessionTemplateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionTemplateBody:
        return IntegrationsInstanceGroupsCreateSessionTemplateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionTemplateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

