from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationServiceAccountsCreateOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ManagementOrganizationServiceAccountsCreateOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationServiceAccountsCreateOutputClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationServiceAccountsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    scopes: List[ManagementOrganizationServiceAccountsCreateOutputScopes]
    client_id: str
    policies: List[ManagementOrganizationServiceAccountsCreateOutputPolicies]
    client_secrets: List[ManagementOrganizationServiceAccountsCreateOutputClientSecrets]
    organization_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationServiceAccountsCreateOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsCreateOutputScopes:
        return ManagementOrganizationServiceAccountsCreateOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsCreateOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsCreateOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsCreateOutputPolicies:
        return ManagementOrganizationServiceAccountsCreateOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsCreateOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsCreateOutputClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsCreateOutputClientSecrets:
        return ManagementOrganizationServiceAccountsCreateOutputClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsCreateOutputClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsCreateOutput:
        return ManagementOrganizationServiceAccountsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapManagementOrganizationServiceAccountsCreateOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        client_id=data.get('client_id'),
        policies=[mapManagementOrganizationServiceAccountsCreateOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        client_secrets=[mapManagementOrganizationServiceAccountsCreateOutputClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationServiceAccountsCreateBody:
    name: str
    scopes: List[str]
    description: Optional[str] = None


class mapManagementOrganizationServiceAccountsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsCreateBody:
        return ManagementOrganizationServiceAccountsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        scopes=data.get('scopes', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

