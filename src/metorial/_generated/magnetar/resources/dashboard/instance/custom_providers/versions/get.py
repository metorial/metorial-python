from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit] = None
    actor: Optional[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputEnvironments:
    object: str
    id: str
    environment: DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutput:
    object: str
    id: str
    environments: List[DashboardInstanceCustomProvidersVersionsGetOutputEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[DashboardInstanceCustomProvidersVersionsGetOutputDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[DashboardInstanceCustomProvidersVersionsGetOutputActor] = None


class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeployment:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputEnvironments:
        return DashboardInstanceCustomProvidersVersionsGetOutputEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputActor:
        return DashboardInstanceCustomProvidersVersionsGetOutputActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutput:
        return DashboardInstanceCustomProvidersVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersVersionsGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersVersionsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
