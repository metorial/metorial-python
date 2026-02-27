from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmInstallationCreateOutput:
    object: str
    id: str
    authorization_url: str


class mapManagementInstanceScmInstallationCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationCreateOutput:
        return ManagementInstanceScmInstallationCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        authorization_url=data.get('authorization_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmInstallationCreateBody:
    provider: Optional[str] = None
    redirect_url: Optional[str] = None


class mapManagementInstanceScmInstallationCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationCreateBody:
        return ManagementInstanceScmInstallationCreateBody(
        provider=data.get('provider'),
        redirect_url=data.get('redirect_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
