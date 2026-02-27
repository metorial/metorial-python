from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputItemsDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit] = None
    actor: Optional[ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentActor] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironments:
    object: str
    id: str
    environment: ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputItemsActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputItems:
    object: str
    id: str
    environments: List[ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[ManagementInstanceCustomProvidersVersionsListOutputItemsDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[ManagementInstanceCustomProvidersVersionsListOutputItemsActor] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCustomProvidersVersionsListOutput:
    items: List[ManagementInstanceCustomProvidersVersionsListOutputItems]
    pagination: ManagementInstanceCustomProvidersVersionsListOutputPagination


class mapManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit:
        return ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentActor:
        return ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputItemsDeployment:
        return ManagementInstanceCustomProvidersVersionsListOutputItemsDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapManagementInstanceCustomProvidersVersionsListOutputItemsDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutputItemsEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironments:
        return ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputItemsEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputItemsActor:
        return ManagementInstanceCustomProvidersVersionsListOutputItemsActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputItems:
        return ManagementInstanceCustomProvidersVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersVersionsListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersVersionsListOutputItemsEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersVersionsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutputPagination:
        return ManagementInstanceCustomProvidersVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListOutput:
        return ManagementInstanceCustomProvidersVersionsListOutput(
        items=[mapManagementInstanceCustomProvidersVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCustomProvidersVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomProvidersVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    ids: Optional[Union[str, List[str]]] = None


class mapManagementInstanceCustomProvidersVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsListQuery:
        return ManagementInstanceCustomProvidersVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        ids=data.get('ids')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
