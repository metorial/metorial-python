from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmReposCreateOutputProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ScmReposCreateOutput:
    object: str
    id: str
    provider: ScmReposCreateOutputProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime


class mapScmReposCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposCreateOutputProvider:
        return ScmReposCreateOutputProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmReposCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposCreateOutput:
        return ScmReposCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapScmReposCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmReposCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmReposCreateBody:
    installation_id: str
    external_repo_id: Optional[str] = None
    external_account_id: Optional[str] = None
    name: Optional[str] = None
    is_private: Optional[bool] = None


class mapScmReposCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmReposCreateBody:
        return ScmReposCreateBody(
        installation_id=data.get('installation_id'),
        external_repo_id=data.get('external_repo_id'),
        external_account_id=data.get('external_account_id'),
        name=data.get('name'),
        is_private=data.get('is_private')
        )

    @staticmethod
    def to_dict(value: Union[ScmReposCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
