from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesAccessShellOutputUrls:
    type: str
    shell: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class SandboxMachinesAccessShellOutput:
    object: str
    token: str
    scope: str
    urls: SandboxMachinesAccessShellOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapSandboxMachinesAccessShellOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessShellOutputUrls:
        return SandboxMachinesAccessShellOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessShellOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesAccessShellOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessShellOutput:
        return SandboxMachinesAccessShellOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapSandboxMachinesAccessShellOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessShellOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesAccessShellBody:
    ttl_seconds: Optional[float] = None


class mapSandboxMachinesAccessShellBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessShellBody:
        return SandboxMachinesAccessShellBody(
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessShellBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

