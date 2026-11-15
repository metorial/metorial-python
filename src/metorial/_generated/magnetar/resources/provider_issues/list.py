from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderIssuesListOutputItemsDailyOccurrences:
    starts_at: datetime
    ends_at: datetime
    count: float
@dataclass
class ProviderIssuesListOutputItems:
    object: str
    id: str
    type: str
    subtype: str
    severity: str
    code: str
    message: str
    occurrence_count: float
    daily_occurrences: List[ProviderIssuesListOutputItemsDailyOccurrences]
    first_seen_at: datetime
    last_seen_at: datetime
    created_at: datetime
    provider_id: Optional[str] = None
    protoguard_filter_id: Optional[str] = None
@dataclass
class ProviderIssuesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderIssuesListOutput:
    items: List[ProviderIssuesListOutputItems]
    pagination: ProviderIssuesListOutputPagination


class mapProviderIssuesListOutputItemsDailyOccurrences:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderIssuesListOutputItemsDailyOccurrences:
        return ProviderIssuesListOutputItemsDailyOccurrences(
        starts_at=datetime.fromisoformat(data.get('starts_at').replace('Z', '+00:00')) if data.get('starts_at') else None,
        ends_at=datetime.fromisoformat(data.get('ends_at').replace('Z', '+00:00')) if data.get('ends_at') else None,
        count=data.get('count')
        )

    @staticmethod
    def to_dict(value: Union[ProviderIssuesListOutputItemsDailyOccurrences, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderIssuesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderIssuesListOutputItems:
        return ProviderIssuesListOutputItems(
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
        daily_occurrences=[mapProviderIssuesListOutputItemsDailyOccurrences.from_dict(item) for item in data.get('daily_occurrences', []) if item],
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at').replace('Z', '+00:00')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderIssuesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderIssuesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderIssuesListOutputPagination:
        return ProviderIssuesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderIssuesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderIssuesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderIssuesListOutput:
        return ProviderIssuesListOutput(
        items=[mapProviderIssuesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderIssuesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderIssuesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderIssuesListQueryLastSeenAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProviderIssuesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProviderIssuesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    severity: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    last_seen_at: Optional[ProviderIssuesListQueryLastSeenAt] = None
    created_at: Optional[ProviderIssuesListQueryCreatedAt] = None
    search: Optional[str] = None


class mapProviderIssuesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderIssuesListQuery:
        return ProviderIssuesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        severity=data.get('severity'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        last_seen_at=mapProviderIssuesListQueryLastSeenAt.from_dict(data.get('last_seen_at')) if data.get('last_seen_at') else None,
        created_at=mapProviderIssuesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ProviderIssuesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

