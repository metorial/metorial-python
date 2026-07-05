from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsParticipantsListOutputItemsData:
    identifier: str
    name: str
@dataclass
class SessionsParticipantsListOutputItems:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: SessionsParticipantsListOutputItemsData
    created_at: datetime
    provider_id: Optional[str] = None
    connection_type: Optional[str] = None
    agent_id: Optional[str] = None
    agent_instance_id: Optional[str] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    agent_actor_id: Optional[str] = None
    agent_client_id: Optional[str] = None
    consumer_id: Optional[str] = None
@dataclass
class SessionsParticipantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsParticipantsListOutput:
    items: List[SessionsParticipantsListOutputItems]
    pagination: SessionsParticipantsListOutputPagination


class mapSessionsParticipantsListOutputItemsData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsParticipantsListOutputItemsData:
        return SessionsParticipantsListOutputItemsData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SessionsParticipantsListOutputItemsData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsParticipantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsParticipantsListOutputItems:
        return SessionsParticipantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapSessionsParticipantsListOutputItemsData.from_dict(data.get('data')) if data.get('data') else None,
        provider_id=data.get('provider_id'),
        connection_type=data.get('connection_type'),
        agent_id=data.get('agent_id'),
        agent_instance_id=data.get('agent_instance_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        agent_actor_id=data.get('agent_actor_id'),
        agent_client_id=data.get('agent_client_id'),
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsParticipantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsParticipantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsParticipantsListOutputPagination:
        return SessionsParticipantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsParticipantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsParticipantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsParticipantsListOutput:
        return SessionsParticipantsListOutput(
        items=[mapSessionsParticipantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsParticipantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsParticipantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsParticipantsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionsParticipantsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SessionsParticipantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    agent_id: Optional[Union[str, List[str]]] = None
    actor_id: Optional[Union[str, List[str]]] = None
    consumer_id: Optional[Union[str, List[str]]] = None
    identity_id: Optional[Union[str, List[str]]] = None
    agent_instance_id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_connection_id: Optional[Union[str, List[str]]] = None
    session_message_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SessionsParticipantsListQueryCreatedAt] = None
    updated_at: Optional[SessionsParticipantsListQueryUpdatedAt] = None


class mapSessionsParticipantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsParticipantsListQuery:
        return SessionsParticipantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        id=data.get('id'),
        agent_id=data.get('agent_id'),
        actor_id=data.get('actor_id'),
        consumer_id=data.get('consumer_id'),
        identity_id=data.get('identity_id'),
        agent_instance_id=data.get('agent_instance_id'),
        session_id=data.get('session_id'),
        session_connection_id=data.get('session_connection_id'),
        session_message_id=data.get('session_message_id'),
        created_at=mapSessionsParticipantsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapSessionsParticipantsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsParticipantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

