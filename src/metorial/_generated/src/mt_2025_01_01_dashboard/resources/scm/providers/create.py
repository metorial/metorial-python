from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmProvidersCreateOutputProvider:
    object: str
    id: str
    type: str
    name: str
    is_default: bool
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    api_url: Optional[str] = None
    web_url: Optional[str] = None
@dataclass
class ScmProvidersCreateOutput:
    object: str
    id: str
    type: str
    url: str
    status: str
    created_at: datetime
    expires_at: datetime
    provider: Optional[ScmProvidersCreateOutputProvider] = None


class mapScmProvidersCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmProvidersCreateOutputProvider:
        return ScmProvidersCreateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        api_url=data.get('api_url'),
        web_url=data.get('web_url'),
        is_default=data.get('is_default'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmProvidersCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapScmProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmProvidersCreateOutput:
        return ScmProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        url=data.get('url'),
        status=data.get('status'),
        provider=mapScmProvidersCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ScmProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmProvidersCreateBody:
    type: str


class mapScmProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmProvidersCreateBody:
        return ScmProvidersCreateBody(
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[ScmProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

