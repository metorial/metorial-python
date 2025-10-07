from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomServersVersionsCreateOutputServerVersionServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceCustomServersVersionsCreateOutputServerVersion:
    object: str
    id: str
    identifier: str
    server_id: str
    server_variant_id: str
    get_launch_params: str
    source: Dict[str, Any]
    schema: Dict[str, Any]
    server: DashboardInstanceCustomServersVersionsCreateOutputServerVersionServer
    created_at: datetime
@dataclass
class DashboardInstanceCustomServersVersionsCreateOutputServerInstanceRemoteServerProviderOauth:
    config: Dict[str, Any]
    scopes: List[str]
@dataclass
class DashboardInstanceCustomServersVersionsCreateOutputServerInstanceRemoteServer:
    object: str
    id: str
    remote_url: str
    created_at: datetime
    updated_at: datetime
    provider_oauth: Optional[DashboardInstanceCustomServersVersionsCreateOutputServerInstanceRemoteServerProviderOauth] = None
@dataclass
class DashboardInstanceCustomServersVersionsCreateOutputServerInstanceManagedServerProviderOauth:
    config: Dict[str, Any]
    scopes: List[str]
@dataclass
class DashboardInstanceCustomServersVersionsCreateOutputServerInstanceManagedServer:
    object: str
    id: str
    created_at: datetime
    updated_at: datetime
    provider_oauth: Optional[DashboardInstanceCustomServersVersionsCreateOutputServerInstanceManagedServerProviderOauth] = None
@dataclass
class DashboardInstanceCustomServersVersionsCreateOutputServerInstance:
    type: str
    remote_server: Optional[DashboardInstanceCustomServersVersionsCreateOutputServerInstanceRemoteServer] = None
    managed_server: Optional[DashboardInstanceCustomServersVersionsCreateOutputServerInstanceManagedServer] = None
@dataclass
class DashboardInstanceCustomServersVersionsCreateOutput:
    object: str
    id: str
    status: str
    type: str
    is_current: bool
    version_index: float
    server_instance: DashboardInstanceCustomServersVersionsCreateOutputServerInstance
    custom_server_id: str
    created_at: datetime
    updated_at: datetime
    version_hash: str
    server_version: Optional[DashboardInstanceCustomServersVersionsCreateOutputServerVersion] = None
    deployment_id: Optional[str] = None


class mapDashboardInstanceCustomServersVersionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersVersionsCreateOutput:
        return DashboardInstanceCustomServersVersionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        is_current=data.get('is_current'),
        version_index=data.get('version_index'),
        server_version=mapDashboardInstanceCustomServersVersionsCreateOutputServerVersion.from_dict(data.get('server_version')) if data.get('server_version') else None,
        server_instance=mapDashboardInstanceCustomServersVersionsCreateOutputServerInstance.from_dict(data.get('server_instance')) if data.get('server_instance') else None,
        custom_server_id=data.get('custom_server_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        version_hash=data.get('version_hash'),
        deployment_id=data.get('deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersVersionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomServersVersionsCreateBody:
    implementation: Dict[str, Any]


class mapDashboardInstanceCustomServersVersionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersVersionsCreateBody:
        return DashboardInstanceCustomServersVersionsCreateBody(
        implementation=data.get('implementation')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersVersionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

