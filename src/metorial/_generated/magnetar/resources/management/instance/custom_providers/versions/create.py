from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsCreateOutputDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentCommit] = None
    actor: Optional[ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentActor] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsCreateOutputEnvironments:
    object: str
    id: str
    environment: ManagementInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsCreateOutputActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsCreateOutput:
    object: str
    id: str
    environments: List[ManagementInstanceCustomProvidersVersionsCreateOutputEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[ManagementInstanceCustomProvidersVersionsCreateOutputDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[ManagementInstanceCustomProvidersVersionsCreateOutputActor] = None


class mapManagementInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
        return ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
        return ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateOutputDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateOutputDeployment:
        return ManagementInstanceCustomProvidersVersionsCreateOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersVersionsCreateOutputDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapManagementInstanceCustomProvidersVersionsCreateOutputDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        current_provider_version_id=data.get('current_provider_version_id'),
        instance_id=data.get('instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsCreateOutputEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateOutputEnvironments:
        return ManagementInstanceCustomProvidersVersionsCreateOutputEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateOutputEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateOutputActor:
        return ManagementInstanceCustomProvidersVersionsCreateOutputActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateOutput:
        return ManagementInstanceCustomProvidersVersionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersVersionsCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersVersionsCreateOutputEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersVersionsCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomProvidersVersionsCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersVersionsCreateBody:
    from_: Dict[str, Any]
    config: Optional[ManagementInstanceCustomProvidersVersionsCreateBodyConfig] = None


class mapManagementInstanceCustomProvidersVersionsCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateBodyConfig:
        return ManagementInstanceCustomProvidersVersionsCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsCreateBody:
        return ManagementInstanceCustomProvidersVersionsCreateBody(
        from_=data.get('from'),
        config=mapManagementInstanceCustomProvidersVersionsCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
