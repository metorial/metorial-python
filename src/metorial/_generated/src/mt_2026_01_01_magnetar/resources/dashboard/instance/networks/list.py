from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceNetworksListOutputItemsPublicIps:
    object: str
    id: str
    ip: str
    region: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceNetworksListOutputItems:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    public_ips: List[DashboardInstanceNetworksListOutputItemsPublicIps]
    description: Optional[str] = None
@dataclass
class DashboardInstanceNetworksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceNetworksListOutput:
    items: List[DashboardInstanceNetworksListOutputItems]
    pagination: DashboardInstanceNetworksListOutputPagination


class mapDashboardInstanceNetworksListOutputItemsPublicIps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworksListOutputItemsPublicIps:
        return DashboardInstanceNetworksListOutputItemsPublicIps(
        object=data.get('object'),
        id=data.get('id'),
        ip=data.get('ip'),
        region=data.get('region'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworksListOutputItemsPublicIps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworksListOutputItems:
        return DashboardInstanceNetworksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        public_ips=[mapDashboardInstanceNetworksListOutputItemsPublicIps.from_dict(item) for item in data.get('public_ips', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworksListOutputPagination:
        return DashboardInstanceNetworksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworksListOutput:
        return DashboardInstanceNetworksListOutput(
        items=[mapDashboardInstanceNetworksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceNetworksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceNetworksListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceNetworksListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceNetworksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    enclave_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceNetworksListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceNetworksListQueryUpdatedAt] = None


class mapDashboardInstanceNetworksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworksListQuery:
        return DashboardInstanceNetworksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        firewall_id=data.get('firewall_id'),
        enclave_id=data.get('enclave_id'),
        created_at=mapDashboardInstanceNetworksListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceNetworksListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

