from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsProviderRunsListOutputItems:
    object: str
    id: str
    session_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    session_provider_id: Optional[str] = None
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    provider_version_id: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SessionsProviderRunsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsProviderRunsListOutput:
    items: List[SessionsProviderRunsListOutputItems]
    pagination: SessionsProviderRunsListOutputPagination


class mapSessionsProviderRunsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProviderRunsListOutputItems:
        return SessionsProviderRunsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_version_id=data.get('provider_version_id'),
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProviderRunsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProviderRunsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProviderRunsListOutputPagination:
        return SessionsProviderRunsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProviderRunsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProviderRunsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProviderRunsListOutput:
        return SessionsProviderRunsListOutput(
        items=[mapSessionsProviderRunsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsProviderRunsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProviderRunsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsProviderRunsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[str] = None
    provider_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None


class mapSessionsProviderRunsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProviderRunsListQuery:
        return SessionsProviderRunsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        provider_id=data.get('provider_id'),
        session_provider_id=data.get('session_provider_id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProviderRunsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
