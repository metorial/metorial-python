from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProtoGuardSuppressionsListOutputItemsFilter:
    object: str
    id: str
    key: str
    name: str
@dataclass
class ManagementInstanceProtoGuardSuppressionsListOutputItems:
    object: str
    id: str
    status: str
    filter: ManagementInstanceProtoGuardSuppressionsListOutputItemsFilter
    created_at: datetime
    updated_at: datetime
    reason: Optional[str] = None
    provider_id: Optional[str] = None
    tool_key: Optional[str] = None
    content_hash: Optional[str] = None
    expires_at: Optional[datetime] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceProtoGuardSuppressionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceProtoGuardSuppressionsListOutput:
    object: str
    items: List[ManagementInstanceProtoGuardSuppressionsListOutputItems]
    pagination: ManagementInstanceProtoGuardSuppressionsListOutputPagination


class mapManagementInstanceProtoGuardSuppressionsListOutputItemsFilter:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardSuppressionsListOutputItemsFilter:
        return ManagementInstanceProtoGuardSuppressionsListOutputItemsFilter(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardSuppressionsListOutputItemsFilter, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardSuppressionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardSuppressionsListOutputItems:
        return ManagementInstanceProtoGuardSuppressionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        reason=data.get('reason'),
        filter=mapManagementInstanceProtoGuardSuppressionsListOutputItemsFilter.from_dict(data.get('filter')) if data.get('filter') else None,
        provider_id=data.get('provider_id'),
        tool_key=data.get('tool_key'),
        content_hash=data.get('content_hash'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardSuppressionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardSuppressionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardSuppressionsListOutputPagination:
        return ManagementInstanceProtoGuardSuppressionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardSuppressionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardSuppressionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardSuppressionsListOutput:
        return ManagementInstanceProtoGuardSuppressionsListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceProtoGuardSuppressionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProtoGuardSuppressionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardSuppressionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProtoGuardSuppressionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    filter_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceProtoGuardSuppressionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardSuppressionsListQuery:
        return ManagementInstanceProtoGuardSuppressionsListQuery(
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
    def to_dict(value: Union[ManagementInstanceProtoGuardSuppressionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

