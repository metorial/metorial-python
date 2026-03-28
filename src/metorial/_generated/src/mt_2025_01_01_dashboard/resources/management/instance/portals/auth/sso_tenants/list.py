from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsAuthSsoTenantsListOutputItemsCounts:
    connections: float
@dataclass
class ManagementInstancePortalsAuthSsoTenantsListOutputItems:
    object: str
    id: str
    name: str
    status: str
    client_id: str
    counts: ManagementInstancePortalsAuthSsoTenantsListOutputItemsCounts
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstancePortalsAuthSsoTenantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstancePortalsAuthSsoTenantsListOutput:
    items: List[ManagementInstancePortalsAuthSsoTenantsListOutputItems]
    pagination: ManagementInstancePortalsAuthSsoTenantsListOutputPagination


class mapManagementInstancePortalsAuthSsoTenantsListOutputItemsCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsListOutputItemsCounts:
        return ManagementInstancePortalsAuthSsoTenantsListOutputItemsCounts(
        connections=data.get('connections')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsListOutputItemsCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAuthSsoTenantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsListOutputItems:
        return ManagementInstancePortalsAuthSsoTenantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        status=data.get('status'),
        client_id=data.get('client_id'),
        counts=mapManagementInstancePortalsAuthSsoTenantsListOutputItemsCounts.from_dict(data.get('counts')) if data.get('counts') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAuthSsoTenantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsListOutputPagination:
        return ManagementInstancePortalsAuthSsoTenantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAuthSsoTenantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsListOutput:
        return ManagementInstancePortalsAuthSsoTenantsListOutput(
        items=[mapManagementInstancePortalsAuthSsoTenantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstancePortalsAuthSsoTenantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsAuthSsoTenantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstancePortalsAuthSsoTenantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsListQuery:
        return ManagementInstancePortalsAuthSsoTenantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

