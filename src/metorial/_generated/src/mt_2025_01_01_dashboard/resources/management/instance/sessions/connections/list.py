from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsConnectionsListOutputItemsUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsConnectionsListOutputItemsMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class ManagementInstanceSessionsConnectionsListOutputItemsParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsConnectionsListOutputItems:
    object: str
    id: str
    status: str
    connection_state: str
    transport: str
    usage: ManagementInstanceSessionsConnectionsListOutputItemsUsage
    session_id: str
    created_at: datetime
    last_message_at: datetime
    last_active_at: datetime
    mcp: Optional[ManagementInstanceSessionsConnectionsListOutputItemsMcp] = None
    participant: Optional[ManagementInstanceSessionsConnectionsListOutputItemsParticipant] = None
@dataclass
class ManagementInstanceSessionsConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsConnectionsListOutput:
    items: List[ManagementInstanceSessionsConnectionsListOutputItems]
    pagination: ManagementInstanceSessionsConnectionsListOutputPagination


class mapManagementInstanceSessionsConnectionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsListOutputItemsUsage:
        return ManagementInstanceSessionsConnectionsListOutputItemsUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsListOutputItemsMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsListOutputItemsMcp:
        return ManagementInstanceSessionsConnectionsListOutputItemsMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsListOutputItemsMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsListOutputItemsParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsListOutputItemsParticipant:
        return ManagementInstanceSessionsConnectionsListOutputItemsParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=data.get('data'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsListOutputItemsParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsListOutputItems:
        return ManagementInstanceSessionsConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapManagementInstanceSessionsConnectionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapManagementInstanceSessionsConnectionsListOutputItemsMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapManagementInstanceSessionsConnectionsListOutputItemsParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsListOutputPagination:
        return ManagementInstanceSessionsConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsListOutput:
        return ManagementInstanceSessionsConnectionsListOutput(
        items=[mapManagementInstanceSessionsConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    connection_state: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    participant_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSessionsConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsListQuery:
        return ManagementInstanceSessionsConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        id=data.get('id'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        participant_id=data.get('participant_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
