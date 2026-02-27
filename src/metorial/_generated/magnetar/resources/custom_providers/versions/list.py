from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersVersionsListOutputItemsDeploymentCommit] = None
    actor: Optional[CustomProvidersVersionsListOutputItemsDeploymentActor] = None
@dataclass
class CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsEnvironments:
    object: str
    id: str
    environment: CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class CustomProvidersVersionsListOutputItemsActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItems:
    object: str
    id: str
    environments: List[CustomProvidersVersionsListOutputItemsEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[CustomProvidersVersionsListOutputItemsDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[CustomProvidersVersionsListOutputItemsActor] = None
@dataclass
class CustomProvidersVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CustomProvidersVersionsListOutput:
    items: List[CustomProvidersVersionsListOutputItems]
    pagination: CustomProvidersVersionsListOutputPagination


class mapCustomProvidersVersionsListOutputItemsDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentCommit:
        return CustomProvidersVersionsListOutputItemsDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentActor:
        return CustomProvidersVersionsListOutputItemsDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeployment:
        return CustomProvidersVersionsListOutputItemsDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersVersionsListOutputItemsDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapCustomProvidersVersionsListOutputItemsDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
        return CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment(
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
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsEnvironments:
        return CustomProvidersVersionsListOutputItemsEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsActor:
        return CustomProvidersVersionsListOutputItemsActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItems:
        return CustomProvidersVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersVersionsListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersVersionsListOutputItemsEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersVersionsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputPagination:
        return CustomProvidersVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutput:
        return CustomProvidersVersionsListOutput(
        items=[mapCustomProvidersVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCustomProvidersVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    ids: Optional[Union[str, List[str]]] = None


class mapCustomProvidersVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListQuery:
        return CustomProvidersVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        ids=data.get('ids')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
