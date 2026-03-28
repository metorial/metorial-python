from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationServiceAccountsPoliciesDeleteOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ManagementOrganizationServiceAccountsPoliciesDeleteOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationServiceAccountsPoliciesDeleteOutputClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationServiceAccountsPoliciesDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    scopes: List[ManagementOrganizationServiceAccountsPoliciesDeleteOutputScopes]
    client_id: str
    policies: List[ManagementOrganizationServiceAccountsPoliciesDeleteOutputPolicies]
    client_secrets: List[ManagementOrganizationServiceAccountsPoliciesDeleteOutputClientSecrets]
    organization_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationServiceAccountsPoliciesDeleteOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsPoliciesDeleteOutputScopes:
        return ManagementOrganizationServiceAccountsPoliciesDeleteOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsPoliciesDeleteOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsPoliciesDeleteOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsPoliciesDeleteOutputPolicies:
        return ManagementOrganizationServiceAccountsPoliciesDeleteOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsPoliciesDeleteOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsPoliciesDeleteOutputClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsPoliciesDeleteOutputClientSecrets:
        return ManagementOrganizationServiceAccountsPoliciesDeleteOutputClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsPoliciesDeleteOutputClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationServiceAccountsPoliciesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationServiceAccountsPoliciesDeleteOutput:
        return ManagementOrganizationServiceAccountsPoliciesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapManagementOrganizationServiceAccountsPoliciesDeleteOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        client_id=data.get('client_id'),
        policies=[mapManagementOrganizationServiceAccountsPoliciesDeleteOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        client_secrets=[mapManagementOrganizationServiceAccountsPoliciesDeleteOutputClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationServiceAccountsPoliciesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

