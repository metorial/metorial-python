from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesAccessShellOutputUrls:
    type: str
    shell: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class ManagementInstanceSandboxMachinesAccessShellOutput:
    object: str
    token: str
    scope: str
    urls: ManagementInstanceSandboxMachinesAccessShellOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapManagementInstanceSandboxMachinesAccessShellOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessShellOutputUrls:
        return ManagementInstanceSandboxMachinesAccessShellOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessShellOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesAccessShellOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessShellOutput:
        return ManagementInstanceSandboxMachinesAccessShellOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapManagementInstanceSandboxMachinesAccessShellOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessShellOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesAccessShellBody:
    ttl_seconds: Optional[float] = None


class mapManagementInstanceSandboxMachinesAccessShellBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessShellBody:
        return ManagementInstanceSandboxMachinesAccessShellBody(
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessShellBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

