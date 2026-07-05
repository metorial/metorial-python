from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsErrorsListOutputItems:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    status: str
    session_id: str
    similar_error_count: float
    created_at: datetime
    provider_run_id: Optional[str] = None
    connection_id: Optional[str] = None
    group_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsErrorsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsErrorsListOutput:
    items: List[ManagementInstanceSessionsErrorsListOutputItems]
    pagination: ManagementInstanceSessionsErrorsListOutputPagination


class mapManagementInstanceSessionsErrorsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsErrorsListOutputItems:
        return ManagementInstanceSessionsErrorsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        status=data.get('status'),
        session_id=data.get('session_id'),
        provider_run_id=data.get('provider_run_id'),
        connection_id=data.get('connection_id'),
        group_id=data.get('group_id'),
        similar_error_count=data.get('similar_error_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsErrorsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsErrorsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsErrorsListOutputPagination:
        return ManagementInstanceSessionsErrorsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsErrorsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsErrorsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsErrorsListOutput:
        return ManagementInstanceSessionsErrorsListOutput(
        items=[mapManagementInstanceSessionsErrorsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsErrorsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsErrorsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsErrorsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsErrorsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsErrorsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    session_connection_id: Optional[Union[str, List[str]]] = None
    session_error_group_id: Optional[Union[str, List[str]]] = None
    provider_run_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    session_message_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceSessionsErrorsListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceSessionsErrorsListQueryUpdatedAt] = None


class mapManagementInstanceSessionsErrorsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsErrorsListQuery:
        return ManagementInstanceSessionsErrorsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        id=data.get('id'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        session_connection_id=data.get('session_connection_id'),
        session_error_group_id=data.get('session_error_group_id'),
        provider_run_id=data.get('provider_run_id'),
        provider_id=data.get('provider_id'),
        session_message_id=data.get('session_message_id'),
        created_at=mapManagementInstanceSessionsErrorsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceSessionsErrorsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsErrorsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

