from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesAccessPortsOutputUrls:
    type: str
    shell: Optional[str] = None
    exec_: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class SandboxMachinesAccessPortsOutput:
    object: str
    token: str
    scope: str
    urls: SandboxMachinesAccessPortsOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapSandboxMachinesAccessPortsOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessPortsOutputUrls:
        return SandboxMachinesAccessPortsOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        exec_=data.get('exec'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessPortsOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesAccessPortsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessPortsOutput:
        return SandboxMachinesAccessPortsOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapSandboxMachinesAccessPortsOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessPortsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesAccessPortsBody:
    ports: Union[List[float], str]
    ttl_seconds: Optional[float] = None


class mapSandboxMachinesAccessPortsBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessPortsBody:
        return SandboxMachinesAccessPortsBody(
        ports=data.get('ports'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessPortsBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

