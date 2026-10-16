from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
@dataclass
class ManagementInstanceIntegrationEnclavesListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    internet_gateway_id: str
    provider_deployment_id: str
    enclave_environment: ManagementInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment
    created_at: datetime
    description: Optional[str] = None
    last_used_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationEnclavesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceIntegrationEnclavesListOutput:
    items: List[ManagementInstanceIntegrationEnclavesListOutputItems]
    pagination: ManagementInstanceIntegrationEnclavesListOutputPagination


class mapManagementInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment:
        return ManagementInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationEnclavesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationEnclavesListOutputItems:
        return ManagementInstanceIntegrationEnclavesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        internet_gateway_id=data.get('internet_gateway_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        enclave_environment=mapManagementInstanceIntegrationEnclavesListOutputItemsEnclaveEnvironment.from_dict(data.get('enclave_environment')) if data.get('enclave_environment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationEnclavesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationEnclavesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationEnclavesListOutputPagination:
        return ManagementInstanceIntegrationEnclavesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationEnclavesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationEnclavesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationEnclavesListOutput:
        return ManagementInstanceIntegrationEnclavesListOutput(
        items=[mapManagementInstanceIntegrationEnclavesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceIntegrationEnclavesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationEnclavesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationEnclavesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationEnclavesListQuery:
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
    created_at: Optional[ManagementInstanceIntegrationEnclavesListQueryCreatedAt] = None


class mapManagementInstanceIntegrationEnclavesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationEnclavesListQuery:
        return ManagementInstanceIntegrationEnclavesListQuery(
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
        created_at=mapManagementInstanceIntegrationEnclavesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationEnclavesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

