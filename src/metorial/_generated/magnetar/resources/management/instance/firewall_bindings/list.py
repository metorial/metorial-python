from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFirewallBindingsListOutputItemsFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsListOutputItemsTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceFirewallBindingsListOutputItems:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceFirewallBindingsListOutputItemsFirewall
    created_at: datetime
    target: Optional[ManagementInstanceFirewallBindingsListOutputItemsTarget] = None
@dataclass
class ManagementInstanceFirewallBindingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceFirewallBindingsListOutput:
    items: List[ManagementInstanceFirewallBindingsListOutputItems]
    pagination: ManagementInstanceFirewallBindingsListOutputPagination


class mapManagementInstanceFirewallBindingsListOutputItemsFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsListOutputItemsFirewall:
        return ManagementInstanceFirewallBindingsListOutputItemsFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsListOutputItemsFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsListOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsListOutputItemsTarget:
        return ManagementInstanceFirewallBindingsListOutputItemsTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsListOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsListOutputItems:
        return ManagementInstanceFirewallBindingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceFirewallBindingsListOutputItemsFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceFirewallBindingsListOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsListOutputPagination:
        return ManagementInstanceFirewallBindingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFirewallBindingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsListOutput:
        return ManagementInstanceFirewallBindingsListOutput(
        items=[mapManagementInstanceFirewallBindingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceFirewallBindingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFirewallBindingsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceFirewallBindingsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    enclave_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    network_id: Optional[Union[str, List[str]]] = None
    target_type: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceFirewallBindingsListQueryCreatedAt] = None


class mapManagementInstanceFirewallBindingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFirewallBindingsListQuery:
        return ManagementInstanceFirewallBindingsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        firewall_id=data.get('firewall_id'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        network_id=data.get('network_id'),
        target_type=data.get('target_type'),
        created_at=mapManagementInstanceFirewallBindingsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFirewallBindingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

