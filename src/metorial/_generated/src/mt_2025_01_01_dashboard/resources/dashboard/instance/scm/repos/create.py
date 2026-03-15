from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmReposCreateOutputProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceScmReposCreateOutput:
    object: str
    id: str
    provider: DashboardInstanceScmReposCreateOutputProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime


class mapDashboardInstanceScmReposCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposCreateOutputProvider:
        return DashboardInstanceScmReposCreateOutputProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmReposCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposCreateOutput:
        return DashboardInstanceScmReposCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceScmReposCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceScmReposCreateBody:
    installation_id: str
    external_repo_id: Optional[str] = None
    external_account_id: Optional[str] = None
    name: Optional[str] = None
    is_private: Optional[bool] = None


class mapDashboardInstanceScmReposCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposCreateBody:
        return DashboardInstanceScmReposCreateBody(
        installation_id=data.get('installation_id'),
        external_repo_id=data.get('external_repo_id'),
        external_account_id=data.get('external_account_id'),
        name=data.get('name'),
        is_private=data.get('is_private')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

