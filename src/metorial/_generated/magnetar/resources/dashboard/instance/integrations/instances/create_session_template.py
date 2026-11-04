from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer] = None
@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwner] = None
@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment:
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
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig:
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
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProviders:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment
    config: DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig] = None
@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput:
    object: str
    id: str
    status: str
    name: str
    access: DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccess
    providers: List[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    integration_instance_id: Optional[str] = None
    integration_instance_group_id: Optional[str] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None


class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwner:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccess:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProviders:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_group_id=data.get('integration_instance_group_id'),
        identity_actor_id=data.get('identity_actor_id'),
        access=mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        identity_id=data.get('identity_id'),
        providers=[mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIntegrationsInstancesCreateSessionTemplateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceIntegrationsInstancesCreateSessionTemplateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesCreateSessionTemplateBody:
        return DashboardInstanceIntegrationsInstancesCreateSessionTemplateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesCreateSessionTemplateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

