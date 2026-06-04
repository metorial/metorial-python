from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class FirewallBindingsListOutputItemsFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class FirewallBindingsListOutputItemsTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class FirewallBindingsListOutputItems:
    object: str
    id: str
    target_type: str
    firewall: FirewallBindingsListOutputItemsFirewall
    created_at: datetime
    target: Optional[FirewallBindingsListOutputItemsTarget] = None
@dataclass
class FirewallBindingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class FirewallBindingsListOutput:
    items: List[FirewallBindingsListOutputItems]
    pagination: FirewallBindingsListOutputPagination


class mapFirewallBindingsListOutputItemsFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsListOutputItemsFirewall:
        return FirewallBindingsListOutputItemsFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsListOutputItemsFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsListOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsListOutputItemsTarget:
        return FirewallBindingsListOutputItemsTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsListOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsListOutputItems:
        return FirewallBindingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapFirewallBindingsListOutputItemsFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapFirewallBindingsListOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsListOutputPagination:
        return FirewallBindingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallBindingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsListOutput:
        return FirewallBindingsListOutput(
        items=[mapFirewallBindingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapFirewallBindingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class FirewallBindingsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class FirewallBindingsListQuery:
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
    created_at: Optional[FirewallBindingsListQueryCreatedAt] = None


class mapFirewallBindingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallBindingsListQuery:
        return FirewallBindingsListQuery(
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
        created_at=mapFirewallBindingsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallBindingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

