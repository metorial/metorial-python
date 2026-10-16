from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsListOutputItems:
    object: str
    id: str
    target_type: str
    firewall: DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall
    created_at: datetime
    target: Optional[DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsTarget] = None
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsListOutput:
    items: List[DashboardInstanceIntegrationFirewallAssignmentsListOutputItems]
    pagination: DashboardInstanceIntegrationFirewallAssignmentsListOutputPagination


class mapDashboardInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall:
        return DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsListOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsTarget:
        return DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsListOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsListOutputItems:
        return DashboardInstanceIntegrationFirewallAssignmentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapDashboardInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapDashboardInstanceIntegrationFirewallAssignmentsListOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsListOutputPagination:
        return DashboardInstanceIntegrationFirewallAssignmentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationFirewallAssignmentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsListOutput:
        return DashboardInstanceIntegrationFirewallAssignmentsListOutput(
        items=[mapDashboardInstanceIntegrationFirewallAssignmentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceIntegrationFirewallAssignmentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationFirewallAssignmentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    enclave_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    internet_gateway_id: Optional[Union[str, List[str]]] = None
    target_type: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceIntegrationFirewallAssignmentsListQueryCreatedAt] = None


class mapDashboardInstanceIntegrationFirewallAssignmentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationFirewallAssignmentsListQuery:
        return DashboardInstanceIntegrationFirewallAssignmentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        firewall_id=data.get('firewall_id'),
        enclave_id=data.get('enclave_id'),
        provider_id=data.get('provider_id'),
        internet_gateway_id=data.get('internet_gateway_id'),
        target_type=data.get('target_type'),
        created_at=mapDashboardInstanceIntegrationFirewallAssignmentsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationFirewallAssignmentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

