from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
@dataclass
class DashboardInstanceIntegrationEnclavesListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    internet_gateway_id: str
    provider_deployment_id: str
    enclave_environment: DashboardInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment
    created_at: datetime
    description: Optional[str] = None
    last_used_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationEnclavesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceIntegrationEnclavesListOutput:
    items: List[DashboardInstanceIntegrationEnclavesListOutputItems]
    pagination: DashboardInstanceIntegrationEnclavesListOutputPagination


class mapDashboardInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment:
        return DashboardInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationEnclavesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationEnclavesListOutputItems:
        return DashboardInstanceIntegrationEnclavesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        internet_gateway_id=data.get('internet_gateway_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        enclave_environment=mapDashboardInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment.from_dict(data.get('enclave_environment')) if data.get('enclave_environment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationEnclavesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationEnclavesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationEnclavesListOutputPagination:
        return DashboardInstanceIntegrationEnclavesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationEnclavesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationEnclavesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationEnclavesListOutput:
        return DashboardInstanceIntegrationEnclavesListOutput(
        items=[mapDashboardInstanceIntegrationEnclavesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceIntegrationEnclavesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationEnclavesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIntegrationEnclavesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationEnclavesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    slug: Optional[Union[str, List[str]]] = None
    internet_gateway_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceIntegrationEnclavesListQueryCreatedAt] = None


class mapDashboardInstanceIntegrationEnclavesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationEnclavesListQuery:
        return DashboardInstanceIntegrationEnclavesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        slug=data.get('slug'),
        internet_gateway_id=data.get('internet_gateway_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_id=data.get('provider_id'),
        firewall_id=data.get('firewall_id'),
        created_at=mapDashboardInstanceIntegrationEnclavesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationEnclavesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

