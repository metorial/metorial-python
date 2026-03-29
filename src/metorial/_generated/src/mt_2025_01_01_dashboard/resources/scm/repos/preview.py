from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmReposPreviewOutputRepos:
    object: str
    provider: str
    external_id: str
    name: str
    identifier: str
@dataclass
class ScmReposPreviewOutput:
    object: str
    repos: List[ScmReposPreviewOutputRepos]


class mapScmReposPreviewOutputRepos:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewOutputRepos:
        return ScmReposPreviewOutputRepos(
        object=data.get('object'),
        provider=data.get('provider'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        identifier=data.get('identifier')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewOutputRepos, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewOutput:
        return ScmReposPreviewOutput(
        object=data.get('object'),
        repos=[mapScmReposPreviewOutputRepos.from_dict(item) for item in data.get('repos', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmReposPreviewBody:
    installation_id: str
    external_account_id: Optional[str] = None


class mapScmReposPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposPreviewBody:
        return ScmReposPreviewBody(
        installation_id=data.get('installation_id'),
        external_account_id=data.get('external_account_id')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

