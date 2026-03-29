from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsServiceAccountsDeleteOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsServiceAccountsDeleteOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsServiceAccountsDeleteOutputClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsServiceAccountsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    scopes: List[DashboardOrganizationsServiceAccountsDeleteOutputScopes]
    client_id: str
    policies: List[DashboardOrganizationsServiceAccountsDeleteOutputPolicies]
    client_secrets: List[DashboardOrganizationsServiceAccountsDeleteOutputClientSecrets]
    organization_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsServiceAccountsDeleteOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsDeleteOutputScopes:
        return DashboardOrganizationsServiceAccountsDeleteOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsDeleteOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsDeleteOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsDeleteOutputPolicies:
        return DashboardOrganizationsServiceAccountsDeleteOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsDeleteOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsDeleteOutputClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsDeleteOutputClientSecrets:
        return DashboardOrganizationsServiceAccountsDeleteOutputClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsDeleteOutputClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsDeleteOutput:
        return DashboardOrganizationsServiceAccountsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOrganizationsServiceAccountsDeleteOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        client_id=data.get('client_id'),
        policies=[mapDashboardOrganizationsServiceAccountsDeleteOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        client_secrets=[mapDashboardOrganizationsServiceAccountsDeleteOutputClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

