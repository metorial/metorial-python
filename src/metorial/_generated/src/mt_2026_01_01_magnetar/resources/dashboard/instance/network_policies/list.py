from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceNetworkPoliciesListOutputItemsRulesPorts:
    object: str
    from_: float
    to: float
@dataclass
class DashboardInstanceNetworkPoliciesListOutputItemsRules:
    object: str
    id: str
    effect: str
    direction: str
    cidrs: List[str]
    enabled: bool
    priority: float
    description: Optional[str] = None
    ports: Optional[List[DashboardInstanceNetworkPoliciesListOutputItemsRulesPorts]] = None
@dataclass
class DashboardInstanceNetworkPoliciesListOutputItems:
    object: str
    id: str
    name: str
    status: str
    version: float
    rules: List[DashboardInstanceNetworkPoliciesListOutputItemsRules]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    firewall_ids: Optional[List[str]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceNetworkPoliciesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceNetworkPoliciesListOutput:
    items: List[DashboardInstanceNetworkPoliciesListOutputItems]
    pagination: DashboardInstanceNetworkPoliciesListOutputPagination


class mapDashboardInstanceNetworkPoliciesListOutputItemsRulesPorts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesListOutputItemsRulesPorts:
        return DashboardInstanceNetworkPoliciesListOutputItemsRulesPorts(
        object=data.get('object'),
        from_=data.get('from'),
        to=data.get('to')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesListOutputItemsRulesPorts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesListOutputItemsRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesListOutputItemsRules:
        return DashboardInstanceNetworkPoliciesListOutputItemsRules(
        object=data.get('object'),
        id=data.get('id'),
        effect=data.get('effect'),
        direction=data.get('direction'),
        cidrs=data.get('cidrs', []),
        description=data.get('description'),
        enabled=data.get('enabled'),
        priority=data.get('priority'),
        ports=[mapDashboardInstanceNetworkPoliciesListOutputItemsRulesPorts.from_dict(item) for item in data.get('ports', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesListOutputItemsRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesListOutputItems:
        return DashboardInstanceNetworkPoliciesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        version=data.get('version'),
        rules=[mapDashboardInstanceNetworkPoliciesListOutputItemsRules.from_dict(item) for item in data.get('rules', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesListOutputPagination:
        return DashboardInstanceNetworkPoliciesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceNetworkPoliciesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesListOutput:
        return DashboardInstanceNetworkPoliciesListOutput(
        items=[mapDashboardInstanceNetworkPoliciesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceNetworkPoliciesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceNetworkPoliciesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceNetworkPoliciesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceNetworkPoliciesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    created_at: Optional[DashboardInstanceNetworkPoliciesListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceNetworkPoliciesListQueryUpdatedAt] = None


class mapDashboardInstanceNetworkPoliciesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceNetworkPoliciesListQuery:
        return DashboardInstanceNetworkPoliciesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status'),
        firewall_id=data.get('firewall_id'),
        search=data.get('search'),
        created_at=mapDashboardInstanceNetworkPoliciesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceNetworkPoliciesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceNetworkPoliciesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

