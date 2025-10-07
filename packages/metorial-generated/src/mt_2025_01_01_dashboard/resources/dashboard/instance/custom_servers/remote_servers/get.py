from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomServersRemoteServersGetOutputProviderOauth:
    config: Dict[str, Any]
    scopes: List[str]
@dataclass
class DashboardInstanceCustomServersRemoteServersGetOutput:
    object: str
    id: str
    remote_url: str
    created_at: datetime
    updated_at: datetime
    provider_oauth: Optional[DashboardInstanceCustomServersRemoteServersGetOutputProviderOauth] = None


class mapDashboardInstanceCustomServersRemoteServersGetOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersRemoteServersGetOutputProviderOauth:
        return DashboardInstanceCustomServersRemoteServersGetOutputProviderOauth(
        config=data.get('config'),
        scopes=data.get('scopes', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersRemoteServersGetOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersRemoteServersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersRemoteServersGetOutput:
        return DashboardInstanceCustomServersRemoteServersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        remote_url=data.get('remote_url'),
        provider_oauth=mapDashboardInstanceCustomServersRemoteServersGetOutputProviderOauth.from_dict(data.get('provider_oauth')) if data.get('provider_oauth') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersRemoteServersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

