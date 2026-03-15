from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsConnectionsListOutputItemsUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class DashboardInstanceSessionsConnectionsListOutputItemsMcp:
    capabilities: Dict[str, Any]
    protocol_version: str
    transport: str
@dataclass
class DashboardInstanceSessionsConnectionsListOutputItemsParticipant:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: Dict[str, Any]
    created_at: datetime
    provider_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsListOutputItems:
    object: str
    id: str
    connection_state: str
    transport: str
    usage: DashboardInstanceSessionsConnectionsListOutputItemsUsage
    session_id: str
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    last_message_at: datetime
    last_active_at: datetime
    mcp: Optional[DashboardInstanceSessionsConnectionsListOutputItemsMcp] = None
    participant: Optional[DashboardInstanceSessionsConnectionsListOutputItemsParticipant] = None
@dataclass
class DashboardInstanceSessionsConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsConnectionsListOutput:
    items: List[DashboardInstanceSessionsConnectionsListOutputItems]
    pagination: DashboardInstanceSessionsConnectionsListOutputPagination


class mapDashboardInstanceSessionsConnectionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItemsUsage:
        return DashboardInstanceSessionsConnectionsListOutputItemsUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputItemsMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItemsMcp:
        return DashboardInstanceSessionsConnectionsListOutputItemsMcp(
        capabilities=data.get('capabilities'),
        protocol_version=data.get('protocol_version'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItemsMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputItemsParticipant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItemsParticipant:
        return DashboardInstanceSessionsConnectionsListOutputItemsParticipant(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=data.get('data'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItemsParticipant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItems:
        return DashboardInstanceSessionsConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        connection_state=data.get('connection_state'),
        transport=data.get('transport'),
        usage=mapDashboardInstanceSessionsConnectionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        mcp=mapDashboardInstanceSessionsConnectionsListOutputItemsMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        session_id=data.get('session_id'),
        participant=mapDashboardInstanceSessionsConnectionsListOutputItemsParticipant.from_dict(data.get('participant')) if data.get('participant') else None,
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_message_at=datetime.fromisoformat(data.get('last_message_at').replace('Z', '+00:00')) if data.get('last_message_at') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputPagination:
        return DashboardInstanceSessionsConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutput:
        return DashboardInstanceSessionsConnectionsListOutput(
        items=[mapDashboardInstanceSessionsConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsConnectionsListQuery:
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


class mapDashboardInstanceSessionsConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListQuery:
        return DashboardInstanceSessionsConnectionsListQuery(
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
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

