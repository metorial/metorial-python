from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomServersDeploymentsListOutputItemsCreatorActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomServersDeploymentsListOutputItemsStepsLogs:
    timestamp: datetime
    line: str
    type: str
@dataclass
class DashboardInstanceCustomServersDeploymentsListOutputItemsSteps:
    object: str
    id: str
    index: float
    status: str
    type: str
    logs: List[DashboardInstanceCustomServersDeploymentsListOutputItemsStepsLogs]
    created_at: datetime
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomServersDeploymentsListOutputItems:
    object: str
    id: str
    status: str
    trigger: str
    creator_actor: DashboardInstanceCustomServersDeploymentsListOutputItemsCreatorActor
    custom_server_id: str
    created_at: datetime
    updated_at: datetime
    steps: List[DashboardInstanceCustomServersDeploymentsListOutputItemsSteps]
    custom_server_version_id: Optional[str] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomServersDeploymentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCustomServersDeploymentsListOutput:
    items: List[DashboardInstanceCustomServersDeploymentsListOutputItems]
    pagination: DashboardInstanceCustomServersDeploymentsListOutputPagination


class mapDashboardInstanceCustomServersDeploymentsListOutputItemsCreatorActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsListOutputItemsCreatorActor:
        return DashboardInstanceCustomServersDeploymentsListOutputItemsCreatorActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsListOutputItemsCreatorActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsListOutputItemsStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsListOutputItemsStepsLogs:
        return DashboardInstanceCustomServersDeploymentsListOutputItemsStepsLogs(
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None,
        line=data.get('line'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsListOutputItemsStepsLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsListOutputItemsSteps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsListOutputItemsSteps:
        return DashboardInstanceCustomServersDeploymentsListOutputItemsSteps(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index'),
        status=data.get('status'),
        type=data.get('type'),
        logs=[mapDashboardInstanceCustomServersDeploymentsListOutputItemsStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsListOutputItemsSteps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsListOutputItems:
        return DashboardInstanceCustomServersDeploymentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        creator_actor=mapDashboardInstanceCustomServersDeploymentsListOutputItemsCreatorActor.from_dict(data.get('creator_actor')) if data.get('creator_actor') else None,
        custom_server_id=data.get('custom_server_id'),
        custom_server_version_id=data.get('custom_server_version_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        steps=[mapDashboardInstanceCustomServersDeploymentsListOutputItemsSteps.from_dict(item) for item in data.get('steps', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsListOutputPagination:
        return DashboardInstanceCustomServersDeploymentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsListOutput:
        return DashboardInstanceCustomServersDeploymentsListOutput(
        items=[mapDashboardInstanceCustomServersDeploymentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCustomServersDeploymentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomServersDeploymentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    version_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCustomServersDeploymentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsListQuery:
        return DashboardInstanceCustomServersDeploymentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

