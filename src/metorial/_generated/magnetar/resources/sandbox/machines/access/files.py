from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesAccessFilesOutputUrls:
    type: str
    shell: Optional[str] = None
    exec_: Optional[str] = None
    files: Optional[str] = None
    ports: Optional[Dict[str, str]] = None
@dataclass
class SandboxMachinesAccessFilesOutput:
    object: str
    token: str
    scope: str
    urls: SandboxMachinesAccessFilesOutputUrls
    expires_at: datetime
    ports: Optional[Union[List[float], str]] = None


class mapSandboxMachinesAccessFilesOutputUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessFilesOutputUrls:
        return SandboxMachinesAccessFilesOutputUrls(
        type=data.get('type'),
        shell=data.get('shell'),
        exec_=data.get('exec'),
        files=data.get('files'),
        ports=data.get('ports')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessFilesOutputUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesAccessFilesOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessFilesOutput:
        return SandboxMachinesAccessFilesOutput(
        object=data.get('object'),
        token=data.get('token'),
        scope=data.get('scope'),
        ports=data.get('ports'),
        urls=mapSandboxMachinesAccessFilesOutputUrls.from_dict(data.get('urls')) if data.get('urls') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessFilesOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesAccessFilesBody:
    ttl_seconds: Optional[float] = None


class mapSandboxMachinesAccessFilesBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesAccessFilesBody:
        return SandboxMachinesAccessFilesBody(
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesAccessFilesBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

