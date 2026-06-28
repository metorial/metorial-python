from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceFirewallBindingsListOutputItemsFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsListOutputItemsTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceFirewallBindingsListOutputItems:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceFirewallBindingsListOutputItemsFirewall
    created_at: datetime
    target: Optional[DashboardInstanceFirewallBindingsListOutputItemsTarget] = None
@dataclass
class DashboardInstanceFirewallBindingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceFirewallBindingsListOutput:
    items: List[DashboardInstanceFirewallBindingsListOutputItems]
    pagination: DashboardInstanceFirewallBindingsListOutputPagination


class mapDashboardInstanceFirewallBindingsListOutputItemsFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsListOutputItemsFirewall:
        return DashboardInstanceFirewallBindingsListOutputItemsFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsListOutputItemsFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsListOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsListOutputItemsTarget:
        return DashboardInstanceFirewallBindingsListOutputItemsTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsListOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsListOutputItems:
        return DashboardInstanceFirewallBindingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceFirewallBindingsListOutputItemsFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceFirewallBindingsListOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsListOutputPagination:
        return DashboardInstanceFirewallBindingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceFirewallBindingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsListOutput:
        return DashboardInstanceFirewallBindingsListOutput(
        items=[mapDashboardInstanceFirewallBindingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceFirewallBindingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceFirewallBindingsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceFirewallBindingsListQuery:
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
    created_at: Optional[DashboardInstanceFirewallBindingsListQueryCreatedAt] = None


class mapDashboardInstanceFirewallBindingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceFirewallBindingsListQuery:
        return DashboardInstanceFirewallBindingsListQuery(
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
        created_at=mapDashboardInstanceFirewallBindingsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceFirewallBindingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

