from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationFirewallAssignmentsListOutputItemsFirewall:
    object: str
    id: str
    slug: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsListOutputItemsTarget:
    object: str
    type: str
    id: str
    name: str
@dataclass
class IntegrationFirewallAssignmentsListOutputItems:
    object: str
    id: str
    target_type: str
    firewall: IntegrationFirewallAssignmentsListOutputItemsFirewall
    created_at: datetime
    target: Optional[IntegrationFirewallAssignmentsListOutputItemsTarget] = None
@dataclass
class IntegrationFirewallAssignmentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IntegrationFirewallAssignmentsListOutput:
    items: List[IntegrationFirewallAssignmentsListOutputItems]
    pagination: IntegrationFirewallAssignmentsListOutputPagination


class mapIntegrationFirewallAssignmentsListOutputItemsFirewall:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsListOutputItemsFirewall:
        return IntegrationFirewallAssignmentsListOutputItemsFirewall(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsListOutputItemsFirewall, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsListOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsListOutputItemsTarget:
        return IntegrationFirewallAssignmentsListOutputItemsTarget(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsListOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsListOutputItems:
        return IntegrationFirewallAssignmentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target_type=data.get('target_type'),
        firewall=mapIntegrationFirewallAssignmentsListOutputItemsFirewall.from_dict(data.get('firewall')) if data.get('firewall') else None,
        target=mapIntegrationFirewallAssignmentsListOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsListOutputPagination:
        return IntegrationFirewallAssignmentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationFirewallAssignmentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsListOutput:
        return IntegrationFirewallAssignmentsListOutput(
        items=[mapIntegrationFirewallAssignmentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIntegrationFirewallAssignmentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationFirewallAssignmentsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IntegrationFirewallAssignmentsListQuery:
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
    created_at: Optional[IntegrationFirewallAssignmentsListQueryCreatedAt] = None


class mapIntegrationFirewallAssignmentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationFirewallAssignmentsListQuery:
        return IntegrationFirewallAssignmentsListQuery(
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
        created_at=mapIntegrationFirewallAssignmentsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationFirewallAssignmentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

