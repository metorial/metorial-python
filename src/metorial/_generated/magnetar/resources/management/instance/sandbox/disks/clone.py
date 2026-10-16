from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxDisksCloneOutputMachine:
    id: str
    mount_path: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class ManagementInstanceSandboxDisksCloneOutputActiveResize:
    id: str
    status: str
    target_size_bytes: float
@dataclass
class ManagementInstanceSandboxDisksCloneOutput:
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
    machine: Optional[ManagementInstanceSandboxDisksCloneOutputMachine] = None
    active_resize: Optional[ManagementInstanceSandboxDisksCloneOutputActiveResize] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceSandboxDisksCloneOutputMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksCloneOutputMachine:
        return ManagementInstanceSandboxDisksCloneOutputMachine(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksCloneOutputMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksCloneOutputActiveResize:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksCloneOutputActiveResize:
        return ManagementInstanceSandboxDisksCloneOutputActiveResize(
        id=data.get('id'),
        status=data.get('status'),
        target_size_bytes=data.get('target_size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksCloneOutputActiveResize, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksCloneOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksCloneOutput:
        return ManagementInstanceSandboxDisksCloneOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        status=data.get('status'),
        region=data.get('region'),
        size_bytes=data.get('size_bytes'),
        machine=mapManagementInstanceSandboxDisksCloneOutputMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        active_resize=mapManagementInstanceSandboxDisksCloneOutputActiveResize.from_dict(data.get('active_resize')) if data.get('active_resize') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksCloneOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxDisksCloneBody:
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None


class mapManagementInstanceSandboxDisksCloneBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksCloneBody:
        return ManagementInstanceSandboxDisksCloneBody(
        metadata=data.get('metadata'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksCloneBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

