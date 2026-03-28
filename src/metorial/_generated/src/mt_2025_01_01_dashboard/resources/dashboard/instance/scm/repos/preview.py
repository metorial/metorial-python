from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmReposPreviewOutputRepos:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
@dataclass
class DashboardInstanceScmReposPreviewOutput:
    object: str
    repos: List[DashboardInstanceScmReposPreviewOutputRepos]


class mapDashboardInstanceScmReposPreviewOutputRepos:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewOutputRepos:
        return DashboardInstanceScmReposPreviewOutputRepos(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewOutputRepos, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmReposPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewOutput:
        return DashboardInstanceScmReposPreviewOutput(
        object=data.get('object'),
        repos=[mapDashboardInstanceScmReposPreviewOutputRepos.from_dict(item) for item in data.get('repos', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceScmReposPreviewBody:
    installation_id: str
    external_account_id: Optional[str] = None


class mapDashboardInstanceScmReposPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposPreviewBody:
        return DashboardInstanceScmReposPreviewBody(
        installation_id=data.get('installation_id'),
        external_account_id=data.get('external_account_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

