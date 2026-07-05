from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceNetworksListOutputItemsPublicIps:
    object: str
    id: str
    ip: str
    region: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceNetworksListOutputItems:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    public_ips: List[ManagementInstanceNetworksListOutputItemsPublicIps]
    description: Optional[str] = None
@dataclass
class ManagementInstanceNetworksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceNetworksListOutput:
    items: List[ManagementInstanceNetworksListOutputItems]
    pagination: ManagementInstanceNetworksListOutputPagination


class mapManagementInstanceNetworksListOutputItemsPublicIps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworksListOutputItemsPublicIps:
        return ManagementInstanceNetworksListOutputItemsPublicIps(
        object=data.get('object'),
        id=data.get('id'),
        ip=data.get('ip'),
        region=data.get('region'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworksListOutputItemsPublicIps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworksListOutputItems:
        return ManagementInstanceNetworksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        public_ips=[mapManagementInstanceNetworksListOutputItemsPublicIps.from_dict(item) for item in data.get('public_ips', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworksListOutputPagination:
        return ManagementInstanceNetworksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworksListOutput:
        return ManagementInstanceNetworksListOutput(
        items=[mapManagementInstanceNetworksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceNetworksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceNetworksListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceNetworksListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceNetworksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    enclave_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceNetworksListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceNetworksListQueryUpdatedAt] = None


class mapManagementInstanceNetworksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworksListQuery:
        return ManagementInstanceNetworksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        firewall_id=data.get('firewall_id'),
        enclave_id=data.get('enclave_id'),
        created_at=mapManagementInstanceNetworksListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceNetworksListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

