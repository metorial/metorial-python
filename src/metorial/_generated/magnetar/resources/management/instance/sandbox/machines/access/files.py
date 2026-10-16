from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesAccessFilesOutputUrls:
    type: str
    shell: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class ManagementInstanceSandboxMachinesAccessFilesOutput:
    object: str
    token: str
    scope: str
    urls: ManagementInstanceSandboxMachinesAccessFilesOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapManagementInstanceSandboxMachinesAccessFilesOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessFilesOutputUrls:
        return ManagementInstanceSandboxMachinesAccessFilesOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessFilesOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesAccessFilesOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessFilesOutput:
        return ManagementInstanceSandboxMachinesAccessFilesOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapManagementInstanceSandboxMachinesAccessFilesOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessFilesOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesAccessFilesBody:
    ttl_seconds: Optional[float] = None


class mapManagementInstanceSandboxMachinesAccessFilesBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesAccessFilesBody:
        return ManagementInstanceSandboxMachinesAccessFilesBody(
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesAccessFilesBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

