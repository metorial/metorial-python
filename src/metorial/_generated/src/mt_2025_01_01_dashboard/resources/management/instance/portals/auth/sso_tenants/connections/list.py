from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputItems:
    object: str
    id: str
    name: str
    provider_type: str
    created_at: datetime
    provider_name: Optional[str] = None
@dataclass
class ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstancePortalsAuthSsoTenantsConnectionsListOutput:
    items: List[ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputItems]
    pagination: ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputPagination


class mapManagementInstancePortalsAuthSsoTenantsConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputItems:
        return ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        provider_type=data.get('provider_type'),
        provider_name=data.get('provider_name'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAuthSsoTenantsConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputPagination:
        return ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAuthSsoTenantsConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsConnectionsListOutput:
        return ManagementInstancePortalsAuthSsoTenantsConnectionsListOutput(
        items=[mapManagementInstancePortalsAuthSsoTenantsConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstancePortalsAuthSsoTenantsConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsAuthSsoTenantsConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstancePortalsAuthSsoTenantsConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsConnectionsListQuery:
        return ManagementInstancePortalsAuthSsoTenantsConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

