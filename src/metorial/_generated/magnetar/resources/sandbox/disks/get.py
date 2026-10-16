from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxDisksGetOutputMachine:
    id: str
    mount_path: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class SandboxDisksGetOutputActiveResize:
    id: str
    status: str
    target_size_bytes: float
@dataclass
class SandboxDisksGetOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    type: str
    status: str
    region: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    size_bytes: Optional[float] = None
    machine: Optional[SandboxDisksGetOutputMachine] = None
    active_resize: Optional[SandboxDisksGetOutputActiveResize] = None
    deleted_at: Optional[datetime] = None


class mapSandboxDisksGetOutputMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksGetOutputMachine:
        return SandboxDisksGetOutputMachine(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksGetOutputMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxDisksGetOutputActiveResize:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksGetOutputActiveResize:
        return SandboxDisksGetOutputActiveResize(
        id=data.get('id'),
        status=data.get('status'),
        target_size_bytes=data.get('target_size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksGetOutputActiveResize, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxDisksGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxDisksGetOutput:
        return SandboxDisksGetOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        status=data.get('status'),
        region=data.get('region'),
        size_bytes=data.get('size_bytes'),
        machine=mapSandboxDisksGetOutputMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        active_resize=mapSandboxDisksGetOutputActiveResize.from_dict(data.get('active_resize')) if data.get('active_resize') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxDisksGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

