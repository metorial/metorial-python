from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesAccessPortsOutputUrls:
    type: str
    shell: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class ManagementInstanceSandboxMachinesAccessPortsOutput:
    object: str
    token: str
    scope: str
    urls: ManagementInstanceSandboxMachinesAccessPortsOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapManagementInstanceSandboxMachinesAccessPortsOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessPortsOutputUrls:
        return ManagementInstanceSandboxMachinesAccessPortsOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessPortsOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesAccessPortsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessPortsOutput:
        return ManagementInstanceSandboxMachinesAccessPortsOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapManagementInstanceSandboxMachinesAccessPortsOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessPortsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesAccessPortsBody:
    ports: Union[List[float], str]
    ttl_seconds: Optional[float] = None


class mapManagementInstanceSandboxMachinesAccessPortsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessPortsBody:
        return ManagementInstanceSandboxMachinesAccessPortsBody(
        ports=data.get('ports'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessPortsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

