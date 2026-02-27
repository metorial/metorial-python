from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsEventsListOutputItems:
    object: str
    id: str
    session_id: str
    created_at: datetime
    type: Optional[str] = None
    name: Optional[str] = None
    message: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    session_provider_id: Optional[str] = None
    provider_run_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsEventsListOutput:
    items: List[DashboardInstanceSessionsEventsListOutputItems]
    pagination: DashboardInstanceSessionsEventsListOutputPagination


class mapDashboardInstanceSessionsEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItems:
        return DashboardInstanceSessionsEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        message=data.get('message'),
        data=data.get('data'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        provider_run_id=data.get('provider_run_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputPagination:
        return DashboardInstanceSessionsEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutput:
        return DashboardInstanceSessionsEventsListOutput(
        items=[mapDashboardInstanceSessionsEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    provider_run_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSessionsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListQuery:
        return DashboardInstanceSessionsEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        session_provider_id=data.get('session_provider_id'),
        provider_run_id=data.get('provider_run_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
