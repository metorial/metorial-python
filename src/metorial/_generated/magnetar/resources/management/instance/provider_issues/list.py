from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderIssuesListOutputItemsDailyOccurrences:
    starts_at: datetime
    ends_at: datetime
    count: float
@dataclass
class ManagementInstanceProviderIssuesListOutputItems:
    object: str
    id: str
    type: str
    subtype: str
    severity: str
    code: str
    message: str
    occurrence_count: float
    daily_occurrences: List[ManagementInstanceProviderIssuesListOutputItemsDailyOccurrences]
    first_seen_at: datetime
    last_seen_at: datetime
    created_at: datetime
    provider_id: Optional[str] = None
    protoguard_filter_id: Optional[str] = None
@dataclass
class ManagementInstanceProviderIssuesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderIssuesListOutput:
    items: List[ManagementInstanceProviderIssuesListOutputItems]
    pagination: ManagementInstanceProviderIssuesListOutputPagination


class mapManagementInstanceProviderIssuesListOutputItemsDailyOccurrences:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderIssuesListOutputItemsDailyOccurrences:
        return ManagementInstanceProviderIssuesListOutputItemsDailyOccurrences(
        starts_at=datetime.fromisoformat(data.get('starts_at').replace('Z', '+00:00')) if data.get('starts_at') else None,
        ends_at=datetime.fromisoformat(data.get('ends_at').replace('Z', '+00:00')) if data.get('ends_at') else None,
        count=data.get('count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderIssuesListOutputItemsDailyOccurrences, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderIssuesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderIssuesListOutputItems:
        return ManagementInstanceProviderIssuesListOutputItems(
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
        daily_occurrences=[mapManagementInstanceProviderIssuesListOutputItemsDailyOccurrences.from_dict(item) for item in data.get('daily_occurrences', []) if item],
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at').replace('Z', '+00:00')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderIssuesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderIssuesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderIssuesListOutputPagination:
        return ManagementInstanceProviderIssuesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderIssuesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderIssuesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderIssuesListOutput:
        return ManagementInstanceProviderIssuesListOutput(
        items=[mapManagementInstanceProviderIssuesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderIssuesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderIssuesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderIssuesListQueryLastSeenAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceProviderIssuesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceProviderIssuesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    severity: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    last_seen_at: Optional[ManagementInstanceProviderIssuesListQueryLastSeenAt] = None
    created_at: Optional[ManagementInstanceProviderIssuesListQueryCreatedAt] = None
    search: Optional[str] = None


class mapManagementInstanceProviderIssuesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderIssuesListQuery:
        return ManagementInstanceProviderIssuesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        severity=data.get('severity'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        last_seen_at=mapManagementInstanceProviderIssuesListQueryLastSeenAt.from_dict(data.get('last_seen_at')) if data.get('last_seen_at') else None,
        created_at=mapManagementInstanceProviderIssuesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderIssuesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

