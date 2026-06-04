from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class NetworksListOutputItemsPublicIps:
    object: str
    id: str
    ip: str
    region: str
    created_at: datetime
    updated_at: datetime
@dataclass
class NetworksListOutputItems:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    public_ips: List[NetworksListOutputItemsPublicIps]
    description: Optional[str] = None
@dataclass
class NetworksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class NetworksListOutput:
    items: List[NetworksListOutputItems]
    pagination: NetworksListOutputPagination


class mapNetworksListOutputItemsPublicIps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworksListOutputItemsPublicIps:
        return NetworksListOutputItemsPublicIps(
        object=data.get('object'),
        id=data.get('id'),
        ip=data.get('ip'),
        region=data.get('region'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworksListOutputItemsPublicIps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworksListOutputItems:
        return NetworksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        public_ips=[mapNetworksListOutputItemsPublicIps.from_dict(item) for item in data.get('public_ips', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworksListOutputPagination:
        return NetworksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[NetworksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworksListOutput:
        return NetworksListOutput(
        items=[mapNetworksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapNetworksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class NetworksListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class NetworksListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class NetworksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    enclave_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[NetworksListQueryCreatedAt] = None
    updated_at: Optional[NetworksListQueryUpdatedAt] = None


class mapNetworksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworksListQuery:
        return NetworksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        firewall_id=data.get('firewall_id'),
        enclave_id=data.get('enclave_id'),
        created_at=mapNetworksListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapNetworksListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

