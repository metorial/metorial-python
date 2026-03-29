from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsServiceAccountsPoliciesCreateOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsServiceAccountsPoliciesCreateOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsServiceAccountsPoliciesCreateOutputClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsServiceAccountsPoliciesCreateOutput:
    object: str
    id: str
    status: str
    name: str
    scopes: List[DashboardOrganizationsServiceAccountsPoliciesCreateOutputScopes]
    client_id: str
    policies: List[DashboardOrganizationsServiceAccountsPoliciesCreateOutputPolicies]
    client_secrets: List[DashboardOrganizationsServiceAccountsPoliciesCreateOutputClientSecrets]
    organization_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsServiceAccountsPoliciesCreateOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsPoliciesCreateOutputScopes:
        return DashboardOrganizationsServiceAccountsPoliciesCreateOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsPoliciesCreateOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsPoliciesCreateOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsPoliciesCreateOutputPolicies:
        return DashboardOrganizationsServiceAccountsPoliciesCreateOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsPoliciesCreateOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsPoliciesCreateOutputClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsPoliciesCreateOutputClientSecrets:
        return DashboardOrganizationsServiceAccountsPoliciesCreateOutputClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsPoliciesCreateOutputClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsServiceAccountsPoliciesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsPoliciesCreateOutput:
        return DashboardOrganizationsServiceAccountsPoliciesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOrganizationsServiceAccountsPoliciesCreateOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        client_id=data.get('client_id'),
        policies=[mapDashboardOrganizationsServiceAccountsPoliciesCreateOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        client_secrets=[mapDashboardOrganizationsServiceAccountsPoliciesCreateOutputClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsPoliciesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsServiceAccountsPoliciesCreateBody:
    access_policy_id: str


class mapDashboardOrganizationsServiceAccountsPoliciesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsServiceAccountsPoliciesCreateBody:
        return DashboardOrganizationsServiceAccountsPoliciesCreateBody(
        access_policy_id=data.get('access_policy_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsServiceAccountsPoliciesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

