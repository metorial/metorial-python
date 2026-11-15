from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderIssuesListOutputItemsDailyOccurrences:
    starts_at: datetime
    ends_at: datetime
    count: float
@dataclass
class DashboardInstanceProviderIssuesListOutputItems:
    object: str
    id: str
    type: str
    subtype: str
    severity: str
    code: str
    message: str
    occurrence_count: float
    daily_occurrences: List[DashboardInstanceProviderIssuesListOutputItemsDailyOccurrences]
    first_seen_at: datetime
    last_seen_at: datetime
    created_at: datetime
    provider_id: Optional[str] = None
    protoguard_filter_id: Optional[str] = None
@dataclass
class DashboardInstanceProviderIssuesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderIssuesListOutput:
    items: List[DashboardInstanceProviderIssuesListOutputItems]
    pagination: DashboardInstanceProviderIssuesListOutputPagination


class mapDashboardInstanceProviderIssuesListOutputItemsDailyOccurrences:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderIssuesListOutputItemsDailyOccurrences:
        return DashboardInstanceProviderIssuesListOutputItemsDailyOccurrences(
        starts_at=datetime.fromisoformat(data.get('starts_at').replace('Z', '+00:00')) if data.get('starts_at') else None,
        ends_at=datetime.fromisoformat(data.get('ends_at').replace('Z', '+00:00')) if data.get('ends_at') else None,
        count=data.get('count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderIssuesListOutputItemsDailyOccurrences, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderIssuesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderIssuesListOutputItems:
        return DashboardInstanceProviderIssuesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        subtype=data.get('subtype'),
        severity=data.get('severity'),
        code=data.get('code'),
        message=data.get('message'),
        provider_id=data.get('provider_id'),
        protoguard_filter_id=data.get('protoguard_filter_id'),
        occurrence_count=data.get('occurrence_count'),
        daily_occurrences=[mapDashboardInstanceProviderIssuesListOutputItemsDailyOccurrences.from_dict(item) for item in data.get('daily_occurrences', []) if item],
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at').replace('Z', '+00:00')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderIssuesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderIssuesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderIssuesListOutputPagination:
        return DashboardInstanceProviderIssuesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderIssuesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderIssuesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderIssuesListOutput:
        return DashboardInstanceProviderIssuesListOutput(
        items=[mapDashboardInstanceProviderIssuesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderIssuesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderIssuesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderIssuesListQueryLastSeenAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceProviderIssuesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceProviderIssuesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    severity: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    last_seen_at: Optional[DashboardInstanceProviderIssuesListQueryLastSeenAt] = None
    created_at: Optional[DashboardInstanceProviderIssuesListQueryCreatedAt] = None
    search: Optional[str] = None


class mapDashboardInstanceProviderIssuesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderIssuesListQuery:
        return DashboardInstanceProviderIssuesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        severity=data.get('severity'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        last_seen_at=mapDashboardInstanceProviderIssuesListQueryLastSeenAt.from_dict(data.get('last_seen_at')) if data.get('last_seen_at') else None,
        created_at=mapDashboardInstanceProviderIssuesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderIssuesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

