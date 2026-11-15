from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProtoGuardSuppressionsListOutputItemsFilter:
    object: str
    id: str
    key: str
    name: str
@dataclass
class DashboardInstanceProtoGuardSuppressionsListOutputItems:
    object: str
    id: str
    status: str
    filter: DashboardInstanceProtoGuardSuppressionsListOutputItemsFilter
    created_at: datetime
    updated_at: datetime
    reason: Optional[str] = None
    provider_id: Optional[str] = None
    tool_key: Optional[str] = None
    content_hash: Optional[str] = None
    expires_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceProtoGuardSuppressionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProtoGuardSuppressionsListOutput:
    items: List[DashboardInstanceProtoGuardSuppressionsListOutputItems]
    pagination: DashboardInstanceProtoGuardSuppressionsListOutputPagination


class mapDashboardInstanceProtoGuardSuppressionsListOutputItemsFilter:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardSuppressionsListOutputItemsFilter:
        return DashboardInstanceProtoGuardSuppressionsListOutputItemsFilter(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardSuppressionsListOutputItemsFilter, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardSuppressionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardSuppressionsListOutputItems:
        return DashboardInstanceProtoGuardSuppressionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        reason=data.get('reason'),
        filter=mapDashboardInstanceProtoGuardSuppressionsListOutputItemsFilter.from_dict(data.get('filter')) if data.get('filter') else None,
        provider_id=data.get('provider_id'),
        tool_key=data.get('tool_key'),
        content_hash=data.get('content_hash'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardSuppressionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardSuppressionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardSuppressionsListOutputPagination:
        return DashboardInstanceProtoGuardSuppressionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardSuppressionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardSuppressionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardSuppressionsListOutput:
        return DashboardInstanceProtoGuardSuppressionsListOutput(
        items=[mapDashboardInstanceProtoGuardSuppressionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProtoGuardSuppressionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardSuppressionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProtoGuardSuppressionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    filter_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceProtoGuardSuppressionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardSuppressionsListQuery:
        return DashboardInstanceProtoGuardSuppressionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        filter_id=data.get('filter_id'),
        provider_id=data.get('provider_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardSuppressionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

