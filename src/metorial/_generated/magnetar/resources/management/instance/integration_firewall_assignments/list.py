from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsListOutputItems:
    object: str
    id: str
    target_type: str
    firewall: ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall
    created_at: datetime
    target: Optional[ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsTarget] = None
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsListOutput:
    items: List[ManagementInstanceIntegrationFirewallAssignmentsListOutputItems]
    pagination: ManagementInstanceIntegrationFirewallAssignmentsListOutputPagination


class mapManagementInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall:
        return ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsListOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsTarget:
        return ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsListOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsListOutputItems:
        return ManagementInstanceIntegrationFirewallAssignmentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapManagementInstanceIntegrationFirewallAssignmentsListOutputItemsFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapManagementInstanceIntegrationFirewallAssignmentsListOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsListOutputPagination:
        return ManagementInstanceIntegrationFirewallAssignmentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationFirewallAssignmentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsListOutput:
        return ManagementInstanceIntegrationFirewallAssignmentsListOutput(
        items=[mapManagementInstanceIntegrationFirewallAssignmentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceIntegrationFirewallAssignmentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationFirewallAssignmentsListQuery:
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
    created_at: Optional[ManagementInstanceIntegrationFirewallAssignmentsListQueryCreatedAt] = None


class mapManagementInstanceIntegrationFirewallAssignmentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationFirewallAssignmentsListQuery:
        return ManagementInstanceIntegrationFirewallAssignmentsListQuery(
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
        created_at=mapManagementInstanceIntegrationFirewallAssignmentsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationFirewallAssignmentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

