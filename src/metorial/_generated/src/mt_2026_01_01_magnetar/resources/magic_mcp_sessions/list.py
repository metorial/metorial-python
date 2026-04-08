from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServer:
    object: str
    id: str
    status: str
    source: str
    endpoints: List[MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpSessionsListOutputItems:
    object: str
    id: str
    session_id: str
    magic_mcp_server: MagicMcpSessionsListOutputItemsMagicMcpServer
    created_at: datetime
    updated_at: datetime
@dataclass
class MagicMcpSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MagicMcpSessionsListOutput:
    items: List[MagicMcpSessionsListOutputItems]
    pagination: MagicMcpSessionsListOutputPagination


class mapMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
        return MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServer:
        return MagicMcpSessionsListOutputItemsMagicMcpServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItems:
        return MagicMcpSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        session_id=data.get('session_id'),
        magic_mcp_server=mapMagicMcpSessionsListOutputItemsMagicMcpServer.from_dict(data.get('magic_mcp_server')) if data.get('magic_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputPagination:
        return MagicMcpSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutput:
        return MagicMcpSessionsListOutput(
        items=[mapMagicMcpSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMagicMcpSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None


class mapMagicMcpSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListQuery:
        return MagicMcpSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

