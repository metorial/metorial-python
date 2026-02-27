from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmInstallationCreateOutput:
    object: str
    id: str
    authorization_url: str


class mapDashboardInstanceScmInstallationCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmInstallationCreateOutput:
        return DashboardInstanceScmInstallationCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        authorization_url=data.get('authorization_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmInstallationCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceScmInstallationCreateBody:
    provider: Optional[str] = None
    redirect_url: Optional[str] = None


class mapDashboardInstanceScmInstallationCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmInstallationCreateBody:
        return DashboardInstanceScmInstallationCreateBody(
        provider=data.get('provider'),
        redirect_url=data.get('redirect_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmInstallationCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
