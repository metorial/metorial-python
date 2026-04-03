from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class DashboardInstanceMagicMcpServersListOutputItems:
    object: str
    id: str
    status: str
    source: str
    session_template_id: str
    endpoints: List[DashboardInstanceMagicMcpServersListOutputItemsEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceMagicMcpServersListOutput:
    items: List[DashboardInstanceMagicMcpServersListOutputItems]
    pagination: DashboardInstanceMagicMcpServersListOutputPagination


class mapDashboardInstanceMagicMcpServersListOutputItemsEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsEndpoints:
        return DashboardInstanceMagicMcpServersListOutputItemsEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItems:
        return DashboardInstanceMagicMcpServersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        session_template_id=data.get('session_template_id'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapDashboardInstanceMagicMcpServersListOutputItemsEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputPagination:
        return DashboardInstanceMagicMcpServersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutput:
        return DashboardInstanceMagicMcpServersListOutput(
        items=[mapDashboardInstanceMagicMcpServersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceMagicMcpServersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpServersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    magic_mcp_group_id: Optional[Union[str, List[str]]] = None
    consumer_id: Optional[Union[str, List[str]]] = None
    consumer_profile_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    preconfigured_only: Optional[bool] = None


class mapDashboardInstanceMagicMcpServersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListQuery:
        return DashboardInstanceMagicMcpServersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        magic_mcp_group_id=data.get('magic_mcp_group_id'),
        consumer_id=data.get('consumer_id'),
        consumer_profile_id=data.get('consumer_profile_id'),
        search=data.get('search'),
        preconfigured_only=data.get('preconfigured_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

