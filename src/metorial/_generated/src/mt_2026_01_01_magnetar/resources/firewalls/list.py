from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class FirewallsListOutputItemsNetworkPoliciesRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class FirewallsListOutputItemsNetworkPoliciesRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[FirewallsListOutputItemsNetworkPoliciesRulesPorts]] = None
@dataclass
class FirewallsListOutputItemsNetworkPolicies:
    object: str
    id: str
    name: str
    version: float
    rules: List[FirewallsListOutputItemsNetworkPoliciesRules]
@dataclass
class FirewallsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    status: str
    network_id: str
    network_policies: List[FirewallsListOutputItemsNetworkPolicies]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    archived_at: Optional[datetime] = None
@dataclass
class FirewallsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class FirewallsListOutput:
    items: List[FirewallsListOutputItems]
    pagination: FirewallsListOutputPagination


class mapFirewallsListOutputItemsNetworkPoliciesRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsListOutputItemsNetworkPoliciesRulesPorts:
        return FirewallsListOutputItemsNetworkPoliciesRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[FirewallsListOutputItemsNetworkPoliciesRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsListOutputItemsNetworkPoliciesRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsListOutputItemsNetworkPoliciesRules:
        return FirewallsListOutputItemsNetworkPoliciesRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapFirewallsListOutputItemsNetworkPoliciesRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[FirewallsListOutputItemsNetworkPoliciesRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsListOutputItemsNetworkPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsListOutputItemsNetworkPolicies:
        return FirewallsListOutputItemsNetworkPolicies(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        version=data.get('version'),
        rules=[mapFirewallsListOutputItemsNetworkPoliciesRules.from_dict(item) for item in data.get('rules', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[FirewallsListOutputItemsNetworkPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsListOutputItems:
        return FirewallsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        network_policies=[mapFirewallsListOutputItemsNetworkPolicies.from_dict(item) for item in data.get('network_policies', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsListOutputPagination:
        return FirewallsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[FirewallsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapFirewallsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsListOutput:
        return FirewallsListOutput(
        items=[mapFirewallsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapFirewallsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class FirewallsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class FirewallsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class FirewallsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    slug: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    network_id: Optional[Union[str, List[str]]] = None
    enclave_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    network_policy_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[FirewallsListQueryCreatedAt] = None
    updated_at: Optional[FirewallsListQueryUpdatedAt] = None


class mapFirewallsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FirewallsListQuery:
        return FirewallsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        slug=data.get('slug'),
        status=data.get('status'),
        network_id=data.get('network_id'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        network_policy_id=data.get('network_policy_id'),
        created_at=mapFirewallsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapFirewallsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[FirewallsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

