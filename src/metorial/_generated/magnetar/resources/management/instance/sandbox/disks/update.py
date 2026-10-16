from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxDisksUpdateOutputMachine:
    id: str
    mount_path: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class ManagementInstanceSandboxDisksUpdateOutputActiveResize:
    id: str
    status: str
    target_size_bytes: float
@dataclass
class ManagementInstanceSandboxDisksUpdateOutput:
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
    machine: Optional[ManagementInstanceSandboxDisksUpdateOutputMachine] = None
    active_resize: Optional[ManagementInstanceSandboxDisksUpdateOutputActiveResize] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceSandboxDisksUpdateOutputMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksUpdateOutputMachine:
        return ManagementInstanceSandboxDisksUpdateOutputMachine(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksUpdateOutputMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksUpdateOutputActiveResize:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksUpdateOutputActiveResize:
        return ManagementInstanceSandboxDisksUpdateOutputActiveResize(
        id=data.get('id'),
        status=data.get('status'),
        target_size_bytes=data.get('target_size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksUpdateOutputActiveResize, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksUpdateOutput:
        return ManagementInstanceSandboxDisksUpdateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        status=data.get('status'),
        region=data.get('region'),
        size_bytes=data.get('size_bytes'),
        machine=mapManagementInstanceSandboxDisksUpdateOutputMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        active_resize=mapManagementInstanceSandboxDisksUpdateOutputActiveResize.from_dict(data.get('active_resize')) if data.get('active_resize') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxDisksUpdateBody:
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None


class mapManagementInstanceSandboxDisksUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksUpdateBody:
        return ManagementInstanceSandboxDisksUpdateBody(
        metadata=data.get('metadata'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

