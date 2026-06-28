from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class NetworkPoliciesListOutputItemsRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class NetworkPoliciesListOutputItemsRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[NetworkPoliciesListOutputItemsRulesPorts]] = None
@dataclass
class NetworkPoliciesListOutputItems:
    object: str
    id: str
    name: str
    status: str
    version: float
    rules: List[NetworkPoliciesListOutputItemsRules]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    firewall_ids: Optional[List[str]] = None
    archived_at: Optional[datetime] = None
@dataclass
class NetworkPoliciesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class NetworkPoliciesListOutput:
    items: List[NetworkPoliciesListOutputItems]
    pagination: NetworkPoliciesListOutputPagination


class mapNetworkPoliciesListOutputItemsRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesListOutputItemsRulesPorts:
        return NetworkPoliciesListOutputItemsRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesListOutputItemsRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesListOutputItemsRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesListOutputItemsRules:
        return NetworkPoliciesListOutputItemsRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapNetworkPoliciesListOutputItemsRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesListOutputItemsRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesListOutputItems:
        return NetworkPoliciesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        version=data.get('version'),
        rules=[mapNetworkPoliciesListOutputItemsRules.from_dict(item) for item in data.get('rules', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesListOutputPagination:
        return NetworkPoliciesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapNetworkPoliciesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesListOutput:
        return NetworkPoliciesListOutput(
        items=[mapNetworkPoliciesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapNetworkPoliciesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class NetworkPoliciesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class NetworkPoliciesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class NetworkPoliciesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    created_at: Optional[NetworkPoliciesListQueryCreatedAt] = None
    updated_at: Optional[NetworkPoliciesListQueryUpdatedAt] = None


class mapNetworkPoliciesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> NetworkPoliciesListQuery:
        return NetworkPoliciesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status'),
        firewall_id=data.get('firewall_id'),
        search=data.get('search'),
        created_at=mapNetworkPoliciesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapNetworkPoliciesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[NetworkPoliciesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

