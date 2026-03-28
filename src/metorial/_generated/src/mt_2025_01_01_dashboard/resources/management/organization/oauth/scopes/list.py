from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationOauthScopesListOutputPermissions:
    identifier: str
    name: str
    description: str
    dependencies: List[str]
@dataclass
class ManagementOrganizationOauthScopesListOutput:
    object: str
    permissions: List[ManagementOrganizationOauthScopesListOutputPermissions]


class mapManagementOrganizationOauthScopesListOutputPermissions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthScopesListOutputPermissions:
        return ManagementOrganizationOauthScopesListOutputPermissions(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        dependencies=data.get('dependencies', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthScopesListOutputPermissions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOauthScopesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthScopesListOutput:
        return ManagementOrganizationOauthScopesListOutput(
        object=data.get('object'),
        permissions=[mapManagementOrganizationOauthScopesListOutputPermissions.from_dict(item) for item in data.get('permissions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthScopesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

