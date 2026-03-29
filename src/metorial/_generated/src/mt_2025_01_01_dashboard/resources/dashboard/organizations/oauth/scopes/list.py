from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOauthScopesListOutputPermissions:
    identifier: str
    name: str
    description: str
    dependencies: List[str]
@dataclass
class DashboardOrganizationsOauthScopesListOutput:
    object: str
    permissions: List[DashboardOrganizationsOauthScopesListOutputPermissions]


class mapDashboardOrganizationsOauthScopesListOutputPermissions:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthScopesListOutputPermissions:
        return DashboardOrganizationsOauthScopesListOutputPermissions(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        dependencies=data.get('dependencies', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthScopesListOutputPermissions, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthScopesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthScopesListOutput:
        return DashboardOrganizationsOauthScopesListOutput(
        object=data.get('object'),
        permissions=[mapDashboardOrganizationsOauthScopesListOutputPermissions.from_dict(item) for item in data.get('permissions', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthScopesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

