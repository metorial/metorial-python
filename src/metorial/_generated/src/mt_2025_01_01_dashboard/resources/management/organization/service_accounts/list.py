from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationServiceAccountsListOutputItemsScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ManagementOrganizationServiceAccountsListOutputItemsPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationServiceAccountsListOutputItemsClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationServiceAccountsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    scopes: List[ManagementOrganizationServiceAccountsListOutputItemsScopes]
    client_id: str
    policies: List[ManagementOrganizationServiceAccountsListOutputItemsPolicies]
    client_secrets: List[ManagementOrganizationServiceAccountsListOutputItemsClientSecrets]
    organization_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementOrganizationServiceAccountsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationServiceAccountsListOutput:
    items: List[ManagementOrganizationServiceAccountsListOutputItems]
    pagination: ManagementOrganizationServiceAccountsListOutputPagination


class mapManagementOrganizationServiceAccountsListOutputItemsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsListOutputItemsScopes:
        return ManagementOrganizationServiceAccountsListOutputItemsScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsListOutputItemsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsListOutputItemsPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsListOutputItemsPolicies:
        return ManagementOrganizationServiceAccountsListOutputItemsPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsListOutputItemsPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsListOutputItemsClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsListOutputItemsClientSecrets:
        return ManagementOrganizationServiceAccountsListOutputItemsClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsListOutputItemsClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsListOutputItems:
        return ManagementOrganizationServiceAccountsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapManagementOrganizationServiceAccountsListOutputItemsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        client_id=data.get('client_id'),
        policies=[mapManagementOrganizationServiceAccountsListOutputItemsPolicies.from_dict(item) for item in data.get('policies', []) if item],
        client_secrets=[mapManagementOrganizationServiceAccountsListOutputItemsClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsListOutputPagination:
        return ManagementOrganizationServiceAccountsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsListOutput:
        return ManagementOrganizationServiceAccountsListOutput(
        items=[mapManagementOrganizationServiceAccountsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationServiceAccountsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationServiceAccountsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementOrganizationServiceAccountsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsListQuery:
        return ManagementOrganizationServiceAccountsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

