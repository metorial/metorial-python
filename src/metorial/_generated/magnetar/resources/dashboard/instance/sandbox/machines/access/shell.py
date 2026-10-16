from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesAccessShellOutputUrls:
    type: str
    shell: Optional[str] = None
    exec_: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class DashboardInstanceSandboxMachinesAccessShellOutput:
    object: str
    token: str
    scope: str
    urls: DashboardInstanceSandboxMachinesAccessShellOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapDashboardInstanceSandboxMachinesAccessShellOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesAccessShellOutputUrls:
        return DashboardInstanceSandboxMachinesAccessShellOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        exec_=data.get('exec'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesAccessShellOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesAccessShellOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesAccessShellOutput:
        return DashboardInstanceSandboxMachinesAccessShellOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapDashboardInstanceSandboxMachinesAccessShellOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesAccessShellOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesAccessShellBody:
    ttl_seconds: Optional[float] = None


class mapDashboardInstanceSandboxMachinesAccessShellBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesAccessShellBody:
        return DashboardInstanceSandboxMachinesAccessShellBody(
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesAccessShellBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

