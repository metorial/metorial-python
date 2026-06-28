from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class EnclavesListOutputItemsEnclaveEnvironment:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
@dataclass
class EnclavesListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    network_id: str
    provider_deployment_id: str
    enclave_environment: EnclavesListOutputItemsEnclaveEnvironment
    created_at: datetime
    description: Optional[str] = None
    last_used_at: Optional[datetime] = None
@dataclass
class EnclavesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class EnclavesListOutput:
    items: List[EnclavesListOutputItems]
    pagination: EnclavesListOutputPagination


class mapEnclavesListOutputItemsEnclaveEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> EnclavesListOutputItemsEnclaveEnvironment:
        return EnclavesListOutputItemsEnclaveEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[EnclavesListOutputItemsEnclaveEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapEnclavesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> EnclavesListOutputItems:
        return EnclavesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        network_id=data.get('network_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        enclave_environment=mapEnclavesListOutputItemsEnclaveEnvironment.from_dict(data.get('enclave_environment')) if data.get('enclave_environment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None
        )

    @staticmethod
    def to_dict(value: Union[EnclavesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapEnclavesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> EnclavesListOutputPagination:
        return EnclavesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[EnclavesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapEnclavesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> EnclavesListOutput:
        return EnclavesListOutput(
        items=[mapEnclavesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapEnclavesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[EnclavesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class EnclavesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class EnclavesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    slug: Optional[Union[str, List[str]]] = None
    network_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    firewall_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[EnclavesListQueryCreatedAt] = None


class mapEnclavesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> EnclavesListQuery:
        return EnclavesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        slug=data.get('slug'),
        network_id=data.get('network_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_id=data.get('provider_id'),
        firewall_id=data.get('firewall_id'),
        created_at=mapEnclavesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[EnclavesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

