from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit] = None
    actor: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments:
    object: str
    id: str
    environment: DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutput:
    object: str
    id: str
    environments: List[DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputActor] = None


class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeployment:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments:
        return DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputActor:
        return DashboardInstanceCustomProvidersVersionsCreateOutputActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutput:
        return DashboardInstanceCustomProvidersVersionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersVersionsCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersVersionsCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateBody:
    from_: Dict[str, Any]
    config: Optional[DashboardInstanceCustomProvidersVersionsCreateBodyConfig] = None


class mapDashboardInstanceCustomProvidersVersionsCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateBodyConfig:
        return DashboardInstanceCustomProvidersVersionsCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateBody:
        return DashboardInstanceCustomProvidersVersionsCreateBody(
        from_=data.get('from'),
        config=mapDashboardInstanceCustomProvidersVersionsCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
