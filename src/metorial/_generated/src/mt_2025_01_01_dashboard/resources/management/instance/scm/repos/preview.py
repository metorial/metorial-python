from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmReposPreviewOutputReposProvider:
    type: str
    name: str
    owner: str
@dataclass
class ManagementInstanceScmReposPreviewOutputRepos:
    object: str
    provider: ManagementInstanceScmReposPreviewOutputReposProvider
    external_id: str
    name: str
    identifier: str
@dataclass
class ManagementInstanceScmReposPreviewOutput:
    object: str
    repos: List[ManagementInstanceScmReposPreviewOutputRepos]


class mapManagementInstanceScmReposPreviewOutputReposProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewOutputReposProvider:
        return ManagementInstanceScmReposPreviewOutputReposProvider(
        type=data.get('type'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewOutputReposProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposPreviewOutputRepos:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewOutputRepos:
        return ManagementInstanceScmReposPreviewOutputRepos(
        object=data.get('object'),
        provider=mapManagementInstanceScmReposPreviewOutputReposProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewOutputRepos, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmReposPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewOutput:
        return ManagementInstanceScmReposPreviewOutput(
        object=data.get('object'),
        repos=[mapManagementInstanceScmReposPreviewOutputRepos.from_dict(item) for item in data.get('repos', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmReposPreviewBody:
    installation_id: str
    external_account_id: Optional[str] = None


class mapManagementInstanceScmReposPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmReposPreviewBody:
        return ManagementInstanceScmReposPreviewBody(
        installation_id=data.get('installation_id'),
        external_account_id=data.get('external_account_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmReposPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

