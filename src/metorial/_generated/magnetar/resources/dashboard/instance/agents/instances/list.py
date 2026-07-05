from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAgentsInstancesListOutputItemsAgentClient:
    object: str
    id: str
    type: str
    name: str
    created_at: datetime
    updated_at: datetime
    last_connected_at: Optional[datetime] = None
@dataclass
class DashboardInstanceAgentsInstancesListOutputItems:
    object: str
    id: str
    type: str
    name: str
    agent_id: str
    created_at: datetime
    updated_at: datetime
    version: Optional[str] = None
    description: Optional[str] = None
    agent_client: Optional[DashboardInstanceAgentsInstancesListOutputItemsAgentClient] = None
    last_connected_at: Optional[datetime] = None
@dataclass
class DashboardInstanceAgentsInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceAgentsInstancesListOutput:
    items: List[DashboardInstanceAgentsInstancesListOutputItems]
    pagination: DashboardInstanceAgentsInstancesListOutputPagination


class mapDashboardInstanceAgentsInstancesListOutputItemsAgentClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAgentsInstancesListOutputItemsAgentClient:
        return DashboardInstanceAgentsInstancesListOutputItemsAgentClient(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_connected_at=datetime.fromisoformat(data.get('last_connected_at').replace('Z', '+00:00')) if data.get('last_connected_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAgentsInstancesListOutputItemsAgentClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAgentsInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAgentsInstancesListOutputItems:
        return DashboardInstanceAgentsInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        version=data.get('version'),
        description=data.get('description'),
        agent_id=data.get('agent_id'),
        agent_client=mapDashboardInstanceAgentsInstancesListOutputItemsAgentClient.from_dict(data.get('agent_client')) if data.get('agent_client') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_connected_at=datetime.fromisoformat(data.get('last_connected_at').replace('Z', '+00:00')) if data.get('last_connected_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAgentsInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAgentsInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAgentsInstancesListOutputPagination:
        return DashboardInstanceAgentsInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAgentsInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAgentsInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAgentsInstancesListOutput:
        return DashboardInstanceAgentsInstancesListOutput(
        items=[mapDashboardInstanceAgentsInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAgentsInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAgentsInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAgentsInstancesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceAgentsInstancesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceAgentsInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    agent_client_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceAgentsInstancesListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceAgentsInstancesListQueryUpdatedAt] = None


class mapDashboardInstanceAgentsInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAgentsInstancesListQuery:
        return DashboardInstanceAgentsInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        id=data.get('id'),
        agent_client_id=data.get('agent_client_id'),
        created_at=mapDashboardInstanceAgentsInstancesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceAgentsInstancesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAgentsInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

