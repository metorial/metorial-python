from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerAgentsListOutputItemsAgent:
    object: str
    id: str
    type: str
    status: str
    name: str
    slug: str
    actor_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class ConsumerAgentsListOutputItemsMagicMcpEndpoints:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ConsumerAgentsListOutputItems:
    object: str
    agent: ConsumerAgentsListOutputItemsAgent
    magic_mcp_endpoints: List[ConsumerAgentsListOutputItemsMagicMcpEndpoints]
@dataclass
class ConsumerAgentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerAgentsListOutput:
    items: List[ConsumerAgentsListOutputItems]
    pagination: ConsumerAgentsListOutputPagination


class mapConsumerAgentsListOutputItemsAgent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsListOutputItemsAgent:
        return ConsumerAgentsListOutputItemsAgent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsListOutputItemsAgent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsListOutputItemsMagicMcpEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsListOutputItemsMagicMcpEndpoints:
        return ConsumerAgentsListOutputItemsMagicMcpEndpoints(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsListOutputItemsMagicMcpEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsListOutputItems:
        return ConsumerAgentsListOutputItems(
        object=data.get('object'),
        agent=mapConsumerAgentsListOutputItemsAgent.from_dict(data.get('agent')) if data.get('agent') else None,
        magic_mcp_endpoints=[mapConsumerAgentsListOutputItemsMagicMcpEndpoints.from_dict(item) for item in data.get('magic_mcp_endpoints', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsListOutputPagination:
        return ConsumerAgentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerAgentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsListOutput:
        return ConsumerAgentsListOutput(
        items=[mapConsumerAgentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumerAgentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerAgentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None


class mapConsumerAgentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerAgentsListQuery:
        return ConsumerAgentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerAgentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

