from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationServiceAccountsDeleteOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ManagementOrganizationServiceAccountsDeleteOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationServiceAccountsDeleteOutputClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationServiceAccountsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    scopes: List[ManagementOrganizationServiceAccountsDeleteOutputScopes]
    client_id: str
    policies: List[ManagementOrganizationServiceAccountsDeleteOutputPolicies]
    client_secrets: List[ManagementOrganizationServiceAccountsDeleteOutputClientSecrets]
    organization_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationServiceAccountsDeleteOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsDeleteOutputScopes:
        return ManagementOrganizationServiceAccountsDeleteOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsDeleteOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsDeleteOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsDeleteOutputPolicies:
        return ManagementOrganizationServiceAccountsDeleteOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsDeleteOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsDeleteOutputClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsDeleteOutputClientSecrets:
        return ManagementOrganizationServiceAccountsDeleteOutputClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsDeleteOutputClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsDeleteOutput:
        return ManagementOrganizationServiceAccountsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapManagementOrganizationServiceAccountsDeleteOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        client_id=data.get('client_id'),
        policies=[mapManagementOrganizationServiceAccountsDeleteOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        client_secrets=[mapManagementOrganizationServiceAccountsDeleteOutputClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

