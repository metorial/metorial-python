from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class IntegrationsInstancesCreateSessionTemplateOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer] = None
@dataclass
class IntegrationsInstancesCreateSessionTemplateOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[IntegrationsInstancesCreateSessionTemplateOutputAccessOwner] = None
@dataclass
class IntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment:
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
class IntegrationsInstancesCreateSessionTemplateOutputProvidersConfig:
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
class IntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class IntegrationsInstancesCreateSessionTemplateOutputProviders:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: IntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment
    config: IntegrationsInstancesCreateSessionTemplateOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[IntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig] = None
@dataclass
class IntegrationsInstancesCreateSessionTemplateOutput:
    object: str
    id: str
    status: str
    name: str
    access: IntegrationsInstancesCreateSessionTemplateOutputAccess
    providers: List[IntegrationsInstancesCreateSessionTemplateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    integration_instance_id: Optional[str] = None
    integration_instance_group_id: Optional[str] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None


class mapIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember:
        return IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer:
        return IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputAccessOwner:
        return IntegrationsInstancesCreateSessionTemplateOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputAccess:
        return IntegrationsInstancesCreateSessionTemplateOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapIntegrationsInstancesCreateSessionTemplateOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment:
        return IntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment(
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
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputProvidersConfig:
        return IntegrationsInstancesCreateSessionTemplateOutputProvidersConfig(
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
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig:
        return IntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutputProviders:
        return IntegrationsInstancesCreateSessionTemplateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionTemplateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateOutput:
        return IntegrationsInstancesCreateSessionTemplateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_group_id=data.get('integration_instance_group_id'),
        identity_actor_id=data.get('identity_actor_id'),
        access=mapIntegrationsInstancesCreateSessionTemplateOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        identity_id=data.get('identity_id'),
        providers=[mapIntegrationsInstancesCreateSessionTemplateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstancesCreateSessionTemplateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapIntegrationsInstancesCreateSessionTemplateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionTemplateBody:
        return IntegrationsInstancesCreateSessionTemplateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionTemplateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

