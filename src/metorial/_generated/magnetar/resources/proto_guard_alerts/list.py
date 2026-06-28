from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProtoGuardAlertsListOutputItemsFilters:
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
class ProtoGuardAlertsListOutputItems:
    object: str
    id: str
    run_id: str
    filters: List[ProtoGuardAlertsListOutputItemsFilters]
    created_at: datetime
    session_id: Optional[str] = None
    session_message_id: Optional[str] = None
    session_connection_id: Optional[str] = None
    provider_run_id: Optional[str] = None
@dataclass
class ProtoGuardAlertsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProtoGuardAlertsListOutput:
    items: List[ProtoGuardAlertsListOutputItems]
    pagination: ProtoGuardAlertsListOutputPagination


class mapProtoGuardAlertsListOutputItemsFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProtoGuardAlertsListOutputItemsFilters:
        return ProtoGuardAlertsListOutputItemsFilters(
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
    def to_dict(value: Union[ProtoGuardAlertsListOutputItemsFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProtoGuardAlertsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProtoGuardAlertsListOutputItems:
        return ProtoGuardAlertsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        run_id=data.get('run_id'),
        session_id=data.get('session_id'),
        session_message_id=data.get('session_message_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        filters=[mapProtoGuardAlertsListOutputItemsFilters.from_dict(item) for item in data.get('filters', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProtoGuardAlertsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProtoGuardAlertsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProtoGuardAlertsListOutputPagination:
        return ProtoGuardAlertsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProtoGuardAlertsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProtoGuardAlertsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProtoGuardAlertsListOutput:
        return ProtoGuardAlertsListOutput(
        items=[mapProtoGuardAlertsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProtoGuardAlertsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProtoGuardAlertsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProtoGuardAlertsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProtoGuardAlertsListQuery:
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
    created_at: Optional[ProtoGuardAlertsListQueryCreatedAt] = None


class mapProtoGuardAlertsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProtoGuardAlertsListQuery:
        return ProtoGuardAlertsListQuery(
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
        created_at=mapProtoGuardAlertsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProtoGuardAlertsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

