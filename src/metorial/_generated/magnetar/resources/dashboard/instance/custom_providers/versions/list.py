from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputItemsDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit] = None
    actor: Optional[DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentActor] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironments:
    object: str
    id: str
    environment: DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputItemsActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputItems:
    object: str
    id: str
    environments: List[DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[DashboardInstanceCustomProvidersVersionsListOutputItemsDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[DashboardInstanceCustomProvidersVersionsListOutputItemsActor] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCustomProvidersVersionsListOutput:
    items: List[DashboardInstanceCustomProvidersVersionsListOutputItems]
    pagination: DashboardInstanceCustomProvidersVersionsListOutputPagination


class mapDashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit:
        return DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentActor:
        return DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputItemsDeployment:
        return DashboardInstanceCustomProvidersVersionsListOutputItemsDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapDashboardInstanceCustomProvidersVersionsListOutputItemsDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutputItemsEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironments:
        return DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputItemsEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputItemsActor:
        return DashboardInstanceCustomProvidersVersionsListOutputItemsActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputItems:
        return DashboardInstanceCustomProvidersVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersVersionsListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersVersionsListOutputItemsEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersVersionsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutputPagination:
        return DashboardInstanceCustomProvidersVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListOutput:
        return DashboardInstanceCustomProvidersVersionsListOutput(
        items=[mapDashboardInstanceCustomProvidersVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCustomProvidersVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    ids: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCustomProvidersVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsListQuery:
        return DashboardInstanceCustomProvidersVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        ids=data.get('ids')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
