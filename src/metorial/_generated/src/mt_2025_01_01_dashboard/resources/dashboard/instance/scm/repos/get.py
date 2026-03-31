from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmReposGetOutputProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceScmReposGetOutput:
    object: str
    id: str
    provider: DashboardInstanceScmReposGetOutputProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime


class mapDashboardInstanceScmReposGetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposGetOutputProvider:
        return DashboardInstanceScmReposGetOutputProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposGetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmReposGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmReposGetOutput:
        return DashboardInstanceScmReposGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceScmReposGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmReposGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

