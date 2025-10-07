from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServersImplementationsListOutputItemsServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceServersImplementationsListOutputItemsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersImplementationsListOutputItems:
    object: str
    id: str
    status: str
    is_default: bool
    is_ephemeral: bool
    name: str
    metadata: Dict[str, Any]
    server_variant: ManagementInstanceServersImplementationsListOutputItemsServerVariant
    server: ManagementInstanceServersImplementationsListOutputItemsServer
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    get_launch_params: Optional[str] = None
@dataclass
class ManagementInstanceServersImplementationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceServersImplementationsListOutput:
    items: List[ManagementInstanceServersImplementationsListOutputItems]
    pagination: ManagementInstanceServersImplementationsListOutputPagination


class mapManagementInstanceServersImplementationsListOutputItemsServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersImplementationsListOutputItemsServerVariant:
        return ManagementInstanceServersImplementationsListOutputItemsServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersImplementationsListOutputItemsServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersImplementationsListOutputItemsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersImplementationsListOutputItemsServer:
        return ManagementInstanceServersImplementationsListOutputItemsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersImplementationsListOutputItemsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersImplementationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersImplementationsListOutputItems:
        return ManagementInstanceServersImplementationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        is_ephemeral=data.get('is_ephemeral'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        get_launch_params=data.get('get_launch_params'),
        server_variant=mapManagementInstanceServersImplementationsListOutputItemsServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server=mapManagementInstanceServersImplementationsListOutputItemsServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersImplementationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersImplementationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersImplementationsListOutputPagination:
        return ManagementInstanceServersImplementationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersImplementationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersImplementationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersImplementationsListOutput:
        return ManagementInstanceServersImplementationsListOutput(
        items=[mapManagementInstanceServersImplementationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceServersImplementationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersImplementationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceServersImplementationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    server_id: Optional[Union[str, List[str]]] = None
    server_variant_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceServersImplementationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersImplementationsListQuery:
        return ManagementInstanceServersImplementationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        server_id=data.get('server_id'),
        server_variant_id=data.get('server_variant_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersImplementationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

