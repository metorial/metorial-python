from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServersVersionsListOutputItemsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersVersionsListOutputItems:
    object: str
    id: str
    identifier: str
    server_id: str
    server_variant_id: str
    get_launch_params: str
    source: Dict[str, Any]
    schema: Dict[str, Any]
    server: ManagementInstanceServersVersionsListOutputItemsServer
    created_at: datetime
@dataclass
class ManagementInstanceServersVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceServersVersionsListOutput:
    items: List[ManagementInstanceServersVersionsListOutputItems]
    pagination: ManagementInstanceServersVersionsListOutputPagination


class mapManagementInstanceServersVersionsListOutputItemsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersVersionsListOutputItemsServer:
        return ManagementInstanceServersVersionsListOutputItemsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersVersionsListOutputItemsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersVersionsListOutputItems:
        return ManagementInstanceServersVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        server_variant_id=data.get('server_variant_id'),
        get_launch_params=data.get('get_launch_params'),
        source=data.get('source'),
        schema=data.get('schema'),
        server=mapManagementInstanceServersVersionsListOutputItemsServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersVersionsListOutputPagination:
        return ManagementInstanceServersVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersVersionsListOutput:
        return ManagementInstanceServersVersionsListOutput(
        items=[mapManagementInstanceServersVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceServersVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceServersVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    variant_id: Optional[str] = None


class mapManagementInstanceServersVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersVersionsListQuery:
        return ManagementInstanceServersVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        variant_id=data.get('variant_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

