from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProtoGuardAlertsListOutputItemsFilters:
    object: str
    id: str
    filter_id: str
    key: str
    name: str
    issue_type: str
    severity: str
    created_at: datetime
    description: Optional[str] = None
    confidence: Optional[float] = None
@dataclass
class DashboardInstanceProtoGuardAlertsListOutputItems:
    object: str
    id: str
    run_id: str
    filters: List[DashboardInstanceProtoGuardAlertsListOutputItemsFilters]
    created_at: datetime
    session_id: Optional[str] = None
    session_message_id: Optional[str] = None
    session_connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
@dataclass
class DashboardInstanceProtoGuardAlertsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProtoGuardAlertsListOutput:
    items: List[DashboardInstanceProtoGuardAlertsListOutputItems]
    pagination: DashboardInstanceProtoGuardAlertsListOutputPagination


class mapDashboardInstanceProtoGuardAlertsListOutputItemsFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardAlertsListOutputItemsFilters:
        return DashboardInstanceProtoGuardAlertsListOutputItemsFilters(
        object=data.get('object'),
        id=data.get('id'),
        filter_id=data.get('filter_id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        issue_type=data.get('issue_type'),
        severity=data.get('severity'),
        confidence=data.get('confidence'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardAlertsListOutputItemsFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardAlertsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardAlertsListOutputItems:
        return DashboardInstanceProtoGuardAlertsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        run_id=data.get('run_id'),
        session_id=data.get('session_id'),
        session_message_id=data.get('session_message_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        filters=[mapDashboardInstanceProtoGuardAlertsListOutputItemsFilters.from_dict(item) for item in data.get('filters', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardAlertsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardAlertsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardAlertsListOutputPagination:
        return DashboardInstanceProtoGuardAlertsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardAlertsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardAlertsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardAlertsListOutput:
        return DashboardInstanceProtoGuardAlertsListOutput(
        items=[mapDashboardInstanceProtoGuardAlertsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProtoGuardAlertsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardAlertsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProtoGuardAlertsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceProtoGuardAlertsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    run_id: Optional[Union[str, List[str]]] = None
    filter_id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_message_id: Optional[Union[str, List[str]]] = None
    session_connection_id: Optional[Union[str, List[str]]] = None
    provider_run_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceProtoGuardAlertsListQueryCreatedAt] = None


class mapDashboardInstanceProtoGuardAlertsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardAlertsListQuery:
        return DashboardInstanceProtoGuardAlertsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        run_id=data.get('run_id'),
        filter_id=data.get('filter_id'),
        session_id=data.get('session_id'),
        session_message_id=data.get('session_message_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        created_at=mapDashboardInstanceProtoGuardAlertsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardAlertsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

