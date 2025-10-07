from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomServersDeploymentsListOutputItemsCreatorActor:
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
class ManagementInstanceCustomServersDeploymentsListOutputItemsStepsLogs:
    timestamp: datetime
    line: str
    type: str
@dataclass
class ManagementInstanceCustomServersDeploymentsListOutputItemsSteps:
    object: str
    id: str
    index: float
    status: str
    type: str
    logs: List[ManagementInstanceCustomServersDeploymentsListOutputItemsStepsLogs]
    created_at: datetime
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class ManagementInstanceCustomServersDeploymentsListOutputItems:
    object: str
    id: str
    status: str
    trigger: str
    creator_actor: ManagementInstanceCustomServersDeploymentsListOutputItemsCreatorActor
    custom_server_id: str
    created_at: datetime
    updated_at: datetime
    steps: List[ManagementInstanceCustomServersDeploymentsListOutputItemsSteps]
    custom_server_version_id: Optional[str] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class ManagementInstanceCustomServersDeploymentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCustomServersDeploymentsListOutput:
    items: List[ManagementInstanceCustomServersDeploymentsListOutputItems]
    pagination: ManagementInstanceCustomServersDeploymentsListOutputPagination


class mapManagementInstanceCustomServersDeploymentsListOutputItemsCreatorActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersDeploymentsListOutputItemsCreatorActor:
        return ManagementInstanceCustomServersDeploymentsListOutputItemsCreatorActor(
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
    def to_dict(value: Union[ManagementInstanceCustomServersDeploymentsListOutputItemsCreatorActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersDeploymentsListOutputItemsStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersDeploymentsListOutputItemsStepsLogs:
        return ManagementInstanceCustomServersDeploymentsListOutputItemsStepsLogs(
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None,
        line=data.get('line'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersDeploymentsListOutputItemsStepsLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersDeploymentsListOutputItemsSteps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersDeploymentsListOutputItemsSteps:
        return ManagementInstanceCustomServersDeploymentsListOutputItemsSteps(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index'),
        status=data.get('status'),
        type=data.get('type'),
        logs=[mapManagementInstanceCustomServersDeploymentsListOutputItemsStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersDeploymentsListOutputItemsSteps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersDeploymentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersDeploymentsListOutputItems:
        return ManagementInstanceCustomServersDeploymentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        creator_actor=mapManagementInstanceCustomServersDeploymentsListOutputItemsCreatorActor.from_dict(data.get('creator_actor')) if data.get('creator_actor') else None,
        custom_server_id=data.get('custom_server_id'),
        custom_server_version_id=data.get('custom_server_version_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        steps=[mapManagementInstanceCustomServersDeploymentsListOutputItemsSteps.from_dict(item) for item in data.get('steps', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersDeploymentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersDeploymentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersDeploymentsListOutputPagination:
        return ManagementInstanceCustomServersDeploymentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersDeploymentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomServersDeploymentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersDeploymentsListOutput:
        return ManagementInstanceCustomServersDeploymentsListOutput(
        items=[mapManagementInstanceCustomServersDeploymentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCustomServersDeploymentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersDeploymentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomServersDeploymentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    version_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceCustomServersDeploymentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersDeploymentsListQuery:
        return ManagementInstanceCustomServersDeploymentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersDeploymentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

