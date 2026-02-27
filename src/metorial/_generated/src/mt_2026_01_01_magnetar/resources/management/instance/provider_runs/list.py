from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderRunsListOutputItems:
    object: str
    id: str
    status: str
    session_id: str
    session_provider_id: str
    provider_id: str
    connection_id: str
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceProviderRunsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderRunsListOutput:
    items: List[ManagementInstanceProviderRunsListOutputItems]
    pagination: ManagementInstanceProviderRunsListOutputPagination


class mapManagementInstanceProviderRunsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderRunsListOutputItems:
        return ManagementInstanceProviderRunsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        provider_id=data.get('provider_id'),
        connection_id=data.get('connection_id'),
        completed_at=datetime.fromisoformat(data.get('completed_at')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderRunsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderRunsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderRunsListOutputPagination:
        return ManagementInstanceProviderRunsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderRunsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderRunsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderRunsListOutput:
        return ManagementInstanceProviderRunsListOutput(
        items=[mapManagementInstanceProviderRunsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderRunsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderRunsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderRunsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    session_connection_id: Optional[Union[str, List[str]]] = None
    provider_version_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceProviderRunsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderRunsListQuery:
        return ManagementInstanceProviderRunsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        session_id=data.get('session_id'),
        provider_id=data.get('provider_id'),
        session_provider_id=data.get('session_provider_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderRunsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
