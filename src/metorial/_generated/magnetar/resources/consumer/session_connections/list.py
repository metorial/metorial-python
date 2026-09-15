from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerSessionConnectionsListOutputItemsConnectionUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class ConsumerSessionConnectionsListOutputItemsConnectionMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class ConsumerSessionConnectionsListOutputItemsConnectionParticipantData:
    identifier: str
    name: str
@dataclass
class ConsumerSessionConnectionsListOutputItemsConnectionParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: ConsumerSessionConnectionsListOutputItemsConnectionParticipantData
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
class ConsumerSessionConnectionsListOutputItemsConnection:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: ConsumerSessionConnectionsListOutputItemsConnectionUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    mcp: Optional[ConsumerSessionConnectionsListOutputItemsConnectionMcp] = None
    participant: Optional[ConsumerSessionConnectionsListOutputItemsConnectionParticipant] = None
    last_active_at: Optional[datetime] = None
@dataclass
class ConsumerSessionConnectionsListOutputItems:
    object: str
    connection: ConsumerSessionConnectionsListOutputItemsConnection
    magic_mcp_session_id: Optional[str] = None
    magic_mcp_endpoint_id: Optional[str] = None
    magic_mcp_server_id: Optional[str] = None
@dataclass
class ConsumerSessionConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerSessionConnectionsListOutput:
    items: List[ConsumerSessionConnectionsListOutputItems]
    pagination: ConsumerSessionConnectionsListOutputPagination


class mapConsumerSessionConnectionsListOutputItemsConnectionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutputItemsConnectionUsage:
        return ConsumerSessionConnectionsListOutputItemsConnectionUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListOutputItemsConnectionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSessionConnectionsListOutputItemsConnectionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutputItemsConnectionMcp:
        return ConsumerSessionConnectionsListOutputItemsConnectionMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListOutputItemsConnectionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSessionConnectionsListOutputItemsConnectionParticipantData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutputItemsConnectionParticipantData:
        return ConsumerSessionConnectionsListOutputItemsConnectionParticipantData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListOutputItemsConnectionParticipantData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSessionConnectionsListOutputItemsConnectionParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutputItemsConnectionParticipant:
        return ConsumerSessionConnectionsListOutputItemsConnectionParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapConsumerSessionConnectionsListOutputItemsConnectionParticipantData.from_dict(data.get('data')) if data.get('data') else None,
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
    def to_dict(value: Union[ConsumerSessionConnectionsListOutputItemsConnectionParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSessionConnectionsListOutputItemsConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutputItemsConnection:
        return ConsumerSessionConnectionsListOutputItemsConnection(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapConsumerSessionConnectionsListOutputItemsConnectionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapConsumerSessionConnectionsListOutputItemsConnectionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapConsumerSessionConnectionsListOutputItemsConnectionParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListOutputItemsConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSessionConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutputItems:
        return ConsumerSessionConnectionsListOutputItems(
        object=data.get('object'),
        connection=mapConsumerSessionConnectionsListOutputItemsConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        magic_mcp_session_id=data.get('magic_mcp_session_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSessionConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutputPagination:
        return ConsumerSessionConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerSessionConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListOutput:
        return ConsumerSessionConnectionsListOutput(
        items=[mapConsumerSessionConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumerSessionConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerSessionConnectionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ConsumerSessionConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    connection_state: Optional[Union[str, List[str]]] = None
    agent_id: Optional[str] = None
    session_id: Optional[str] = None
    created_at: Optional[ConsumerSessionConnectionsListQueryCreatedAt] = None


class mapConsumerSessionConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerSessionConnectionsListQuery:
        return ConsumerSessionConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        connection_state=data.get('connection_state'),
        agent_id=data.get('agent_id'),
        session_id=data.get('session_id'),
        created_at=mapConsumerSessionConnectionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerSessionConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

