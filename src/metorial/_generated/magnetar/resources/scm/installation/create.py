from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ScmInstallationCreateOutput:
    object: str
    id: str
    authorization_url: str


class mapScmInstallationCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmInstallationCreateOutput:
        return ScmInstallationCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        authorization_url=data.get('authorization_url')
        )

    @staticmethod
    def to_dict(value: Union[ScmInstallationCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ScmInstallationCreateBody:
    provider: Optional[str] = None
    redirect_url: Optional[str] = None


class mapScmInstallationCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ScmInstallationCreateBody:
        return ScmInstallationCreateBody(
        provider=data.get('provider'),
        redirect_url=data.get('redirect_url')
        )

    @staticmethod
    def to_dict(value: Union[ScmInstallationCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
