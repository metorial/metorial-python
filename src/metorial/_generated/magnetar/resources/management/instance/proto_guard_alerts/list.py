from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProtoGuardAlertsListOutputItemsFilters:
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
class ManagementInstanceProtoGuardAlertsListOutputItems:
    object: str
    id: str
    run_id: str
    filters: List[ManagementInstanceProtoGuardAlertsListOutputItemsFilters]
    created_at: datetime
    session_id: Optional[str] = None
    session_message_id: Optional[str] = None
    session_connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
@dataclass
class ManagementInstanceProtoGuardAlertsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProtoGuardAlertsListOutput:
    items: List[ManagementInstanceProtoGuardAlertsListOutputItems]
    pagination: ManagementInstanceProtoGuardAlertsListOutputPagination


class mapManagementInstanceProtoGuardAlertsListOutputItemsFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardAlertsListOutputItemsFilters:
        return ManagementInstanceProtoGuardAlertsListOutputItemsFilters(
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
    def to_dict(value: Union[ManagementInstanceProtoGuardAlertsListOutputItemsFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardAlertsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardAlertsListOutputItems:
        return ManagementInstanceProtoGuardAlertsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        run_id=data.get('run_id'),
        session_id=data.get('session_id'),
        session_message_id=data.get('session_message_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        filters=[mapManagementInstanceProtoGuardAlertsListOutputItemsFilters.from_dict(item) for item in data.get('filters', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardAlertsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardAlertsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardAlertsListOutputPagination:
        return ManagementInstanceProtoGuardAlertsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardAlertsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardAlertsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardAlertsListOutput:
        return ManagementInstanceProtoGuardAlertsListOutput(
        items=[mapManagementInstanceProtoGuardAlertsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProtoGuardAlertsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardAlertsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProtoGuardAlertsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceProtoGuardAlertsListQuery:
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
    created_at: Optional[ManagementInstanceProtoGuardAlertsListQueryCreatedAt] = None


class mapManagementInstanceProtoGuardAlertsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardAlertsListQuery:
        return ManagementInstanceProtoGuardAlertsListQuery(
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
        created_at=mapManagementInstanceProtoGuardAlertsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardAlertsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

