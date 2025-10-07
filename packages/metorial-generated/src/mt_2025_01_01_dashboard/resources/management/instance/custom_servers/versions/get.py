from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomServersVersionsGetOutputServerVersionServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCustomServersVersionsGetOutputServerVersion:
    object: str
    id: str
    identifier: str
    server_id: str
    server_variant_id: str
    get_launch_params: str
    source: Dict[str, Any]
    schema: Dict[str, Any]
    server: ManagementInstanceCustomServersVersionsGetOutputServerVersionServer
    created_at: datetime
@dataclass
class ManagementInstanceCustomServersVersionsGetOutputServerInstanceRemoteServerProviderOauth:
    config: Dict[str, Any]
    scopes: List[str]
@dataclass
class ManagementInstanceCustomServersVersionsGetOutputServerInstanceRemoteServer:
    object: str
    id: str
    remote_url: str
    created_at: datetime
    updated_at: datetime
    provider_oauth: Optional[ManagementInstanceCustomServersVersionsGetOutputServerInstanceRemoteServerProviderOauth] = None
@dataclass
class ManagementInstanceCustomServersVersionsGetOutputServerInstanceManagedServerProviderOauth:
    config: Dict[str, Any]
    scopes: List[str]
@dataclass
class ManagementInstanceCustomServersVersionsGetOutputServerInstanceManagedServer:
    object: str
    id: str
    created_at: datetime
    updated_at: datetime
    provider_oauth: Optional[ManagementInstanceCustomServersVersionsGetOutputServerInstanceManagedServerProviderOauth] = None
@dataclass
class ManagementInstanceCustomServersVersionsGetOutputServerInstance:
    type: str
    remote_server: Optional[ManagementInstanceCustomServersVersionsGetOutputServerInstanceRemoteServer] = None
    managed_server: Optional[ManagementInstanceCustomServersVersionsGetOutputServerInstanceManagedServer] = None
@dataclass
class ManagementInstanceCustomServersVersionsGetOutput:
    object: str
    id: str
    status: str
    type: str
    is_current: bool
    version_index: float
    server_instance: ManagementInstanceCustomServersVersionsGetOutputServerInstance
    custom_server_id: str
    created_at: datetime
    updated_at: datetime
    version_hash: str
    server_version: Optional[ManagementInstanceCustomServersVersionsGetOutputServerVersion] = None
    deployment_id: Optional[str] = None


class mapManagementInstanceCustomServersVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomServersVersionsGetOutput:
        return ManagementInstanceCustomServersVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        is_current=data.get('is_current'),
        version_index=data.get('version_index'),
        server_version=mapManagementInstanceCustomServersVersionsGetOutputServerVersion.from_dict(data.get('server_version')) if data.get('server_version') else None,
        server_instance=mapManagementInstanceCustomServersVersionsGetOutputServerInstance.from_dict(data.get('server_instance')) if data.get('server_instance') else None,
        custom_server_id=data.get('custom_server_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        version_hash=data.get('version_hash'),
        deployment_id=data.get('deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomServersVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

