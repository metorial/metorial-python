from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsProvidersListOutputItems:
    object: str
    id: str
    session_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class SessionsProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsProvidersListOutput:
    items: List[SessionsProvidersListOutputItems]
    pagination: SessionsProvidersListOutputPagination


class mapSessionsProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersListOutputItems:
        return SessionsProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersListOutputPagination:
        return SessionsProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersListOutput:
        return SessionsProvidersListOutput(
        items=[mapSessionsProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_id: Optional[Union[str, List[str]]] = None
    status: Optional[str] = None


class mapSessionsProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersListQuery:
        return SessionsProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_id=data.get('provider_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
