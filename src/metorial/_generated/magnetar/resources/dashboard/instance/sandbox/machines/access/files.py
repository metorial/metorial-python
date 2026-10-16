from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesAccessFilesOutputUrls:
    type: str
    shell: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class DashboardInstanceSandboxMachinesAccessFilesOutput:
    object: str
    token: str
    scope: str
    urls: DashboardInstanceSandboxMachinesAccessFilesOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapDashboardInstanceSandboxMachinesAccessFilesOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesAccessFilesOutputUrls:
        return DashboardInstanceSandboxMachinesAccessFilesOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesAccessFilesOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesAccessFilesOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesAccessFilesOutput:
        return DashboardInstanceSandboxMachinesAccessFilesOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapDashboardInstanceSandboxMachinesAccessFilesOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesAccessFilesOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesAccessFilesBody:
    ttl_seconds: Optional[float] = None


class mapDashboardInstanceSandboxMachinesAccessFilesBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesAccessFilesBody:
        return DashboardInstanceSandboxMachinesAccessFilesBody(
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesAccessFilesBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

