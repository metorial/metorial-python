from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MonitorsListOutputItems:
    object: str
    id: str
    name: str
    target: str
    status: str
    owner: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    proto_guard_filter_id: Optional[str] = None
    provider_id: Optional[str] = None
    first_alert_at: Optional[datetime] = None
    last_alert_at: Optional[datetime] = None
@dataclass
class MonitorsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MonitorsListOutput:
    items: List[MonitorsListOutputItems]
    pagination: MonitorsListOutputPagination


class mapMonitorsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorsListOutputItems:
        return MonitorsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        target=data.get('target'),
        status=data.get('status'),
        owner=data.get('owner'),
        proto_guard_filter_id=data.get('proto_guard_filter_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        first_alert_at=datetime.fromisoformat(data.get('first_alert_at').replace('Z', '+00:00')) if data.get('first_alert_at') else None,
        last_alert_at=datetime.fromisoformat(data.get('last_alert_at').replace('Z', '+00:00')) if data.get('last_alert_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorsListOutputPagination:
        return MonitorsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MonitorsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorsListOutput:
        return MonitorsListOutput(
        items=[mapMonitorsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMonitorsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MonitorsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class MonitorsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class MonitorsListQueryFirstAlertAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class MonitorsListQueryLastAlertAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class MonitorsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    target: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    proto_guard_filter_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    created_at: Optional[MonitorsListQueryCreatedAt] = None
    updated_at: Optional[MonitorsListQueryUpdatedAt] = None
    first_alert_at: Optional[MonitorsListQueryFirstAlertAt] = None
    last_alert_at: Optional[MonitorsListQueryLastAlertAt] = None


class mapMonitorsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorsListQuery:
        return MonitorsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        target=data.get('target'),
        status=data.get('status'),
        provider_id=data.get('provider_id'),
        proto_guard_filter_id=data.get('proto_guard_filter_id'),
        search=data.get('search'),
        created_at=mapMonitorsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapMonitorsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None,
        first_alert_at=mapMonitorsListQueryFirstAlertAt.from_dict(data.get('first_alert_at')) if data.get('first_alert_at') else None,
        last_alert_at=mapMonitorsListQueryLastAlertAt.from_dict(data.get('last_alert_at')) if data.get('last_alert_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

