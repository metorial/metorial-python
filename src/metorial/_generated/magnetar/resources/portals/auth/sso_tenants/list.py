from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsAuthSsoTenantsListOutputItemsCounts:
    connections: float
@dataclass
class PortalsAuthSsoTenantsListOutputItems:
    object: str
    id: str
    name: str
    status: str
    client_id: str
    counts: PortalsAuthSsoTenantsListOutputItemsCounts
    created_at: datetime
    updated_at: datetime
@dataclass
class PortalsAuthSsoTenantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class PortalsAuthSsoTenantsListOutput:
    items: List[PortalsAuthSsoTenantsListOutputItems]
    pagination: PortalsAuthSsoTenantsListOutputPagination


class mapPortalsAuthSsoTenantsListOutputItemsCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAuthSsoTenantsListOutputItemsCounts:
        return PortalsAuthSsoTenantsListOutputItemsCounts(
        connections=data.get('connections')
        )

    @staticmethod
    def to_dict(value: Union[PortalsAuthSsoTenantsListOutputItemsCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsAuthSsoTenantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAuthSsoTenantsListOutputItems:
        return PortalsAuthSsoTenantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        status=data.get('status'),
        client_id=data.get('client_id'),
        counts=mapPortalsAuthSsoTenantsListOutputItemsCounts.from_dict(data.get('counts')) if data.get('counts') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsAuthSsoTenantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsAuthSsoTenantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAuthSsoTenantsListOutputPagination:
        return PortalsAuthSsoTenantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[PortalsAuthSsoTenantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsAuthSsoTenantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAuthSsoTenantsListOutput:
        return PortalsAuthSsoTenantsListOutput(
        items=[mapPortalsAuthSsoTenantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapPortalsAuthSsoTenantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsAuthSsoTenantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsAuthSsoTenantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapPortalsAuthSsoTenantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAuthSsoTenantsListQuery:
        return PortalsAuthSsoTenantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[PortalsAuthSsoTenantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

