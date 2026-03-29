from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsServiceAccountsCreateOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsServiceAccountsCreateOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsServiceAccountsCreateOutputClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsServiceAccountsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    scopes: List[DashboardOrganizationsServiceAccountsCreateOutputScopes]
    client_id: str
    policies: List[DashboardOrganizationsServiceAccountsCreateOutputPolicies]
    client_secrets: List[DashboardOrganizationsServiceAccountsCreateOutputClientSecrets]
    organization_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsServiceAccountsCreateOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsCreateOutputScopes:
        return DashboardOrganizationsServiceAccountsCreateOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsCreateOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsCreateOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsCreateOutputPolicies:
        return DashboardOrganizationsServiceAccountsCreateOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsCreateOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsCreateOutputClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsCreateOutputClientSecrets:
        return DashboardOrganizationsServiceAccountsCreateOutputClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsCreateOutputClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsCreateOutput:
        return DashboardOrganizationsServiceAccountsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOrganizationsServiceAccountsCreateOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        client_id=data.get('client_id'),
        policies=[mapDashboardOrganizationsServiceAccountsCreateOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        client_secrets=[mapDashboardOrganizationsServiceAccountsCreateOutputClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsServiceAccountsCreateBody:
    name: str
    scopes: List[str]
    description: Optional[str] = None


class mapDashboardOrganizationsServiceAccountsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsCreateBody:
        return DashboardOrganizationsServiceAccountsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        scopes=data.get('scopes', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

