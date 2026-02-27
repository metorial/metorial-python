from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersDeploymentsListOutputItemsCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsListOutputItemsActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsListOutputItems:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersDeploymentsListOutputItemsCommit] = None
    actor: Optional[DashboardInstanceCustomProvidersDeploymentsListOutputItemsActor] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCustomProvidersDeploymentsListOutput:
    items: List[DashboardInstanceCustomProvidersDeploymentsListOutputItems]
    pagination: DashboardInstanceCustomProvidersDeploymentsListOutputPagination


class mapDashboardInstanceCustomProvidersDeploymentsListOutputItemsCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsListOutputItemsCommit:
        return DashboardInstanceCustomProvidersDeploymentsListOutputItemsCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsListOutputItemsCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsListOutputItemsActor:
        return DashboardInstanceCustomProvidersDeploymentsListOutputItemsActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsListOutputItems:
        return DashboardInstanceCustomProvidersDeploymentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersDeploymentsListOutputItemsCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapDashboardInstanceCustomProvidersDeploymentsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsListOutputPagination:
        return DashboardInstanceCustomProvidersDeploymentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsListOutput:
        return DashboardInstanceCustomProvidersDeploymentsListOutput(
        items=[mapDashboardInstanceCustomProvidersDeploymentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCustomProvidersDeploymentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersDeploymentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    ids: Optional[Union[str, List[str]]] = None
    custom_provider_version_ids: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCustomProvidersDeploymentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsListQuery:
        return DashboardInstanceCustomProvidersDeploymentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        ids=data.get('ids'),
        custom_provider_version_ids=data.get('custom_provider_version_ids')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
