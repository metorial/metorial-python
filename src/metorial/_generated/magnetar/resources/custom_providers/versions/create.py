from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersVersionsCreateOutputDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class CustomProvidersVersionsCreateOutputDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsCreateOutputDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersVersionsCreateOutputDeploymentCommit] = None
    actor: Optional[CustomProvidersVersionsCreateOutputDeploymentActor] = None
@dataclass
class CustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsCreateOutputEnvironments:
    object: str
    id: str
    environment: CustomProvidersVersionsCreateOutputEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class CustomProvidersVersionsCreateOutputActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsCreateOutput:
    object: str
    id: str
    environments: List[CustomProvidersVersionsCreateOutputEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[CustomProvidersVersionsCreateOutputDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[CustomProvidersVersionsCreateOutputActor] = None


class mapCustomProvidersVersionsCreateOutputDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateOutputDeploymentCommit:
        return CustomProvidersVersionsCreateOutputDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateOutputDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsCreateOutputDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateOutputDeploymentActor:
        return CustomProvidersVersionsCreateOutputDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateOutputDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateOutputDeployment:
        return CustomProvidersVersionsCreateOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersVersionsCreateOutputDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapCustomProvidersVersionsCreateOutputDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
        return CustomProvidersVersionsCreateOutputEnvironmentsEnvironment(
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
    def to_dict(value: Union[CustomProvidersVersionsCreateOutputEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsCreateOutputEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateOutputEnvironments:
        return CustomProvidersVersionsCreateOutputEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapCustomProvidersVersionsCreateOutputEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateOutputEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateOutputActor:
        return CustomProvidersVersionsCreateOutputActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateOutput:
        return CustomProvidersVersionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersVersionsCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersVersionsCreateOutputEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersVersionsCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersVersionsCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class CustomProvidersVersionsCreateBody:
    from_: Dict[str, Any]
    config: Optional[CustomProvidersVersionsCreateBodyConfig] = None


class mapCustomProvidersVersionsCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateBodyConfig:
        return CustomProvidersVersionsCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsCreateBody:
        return CustomProvidersVersionsCreateBody(
        from_=data.get('from'),
        config=mapCustomProvidersVersionsCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
