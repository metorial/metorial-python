from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxDisksResizeOutputFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxDisksResizeOutput:
    object: str
    id: str
    disk_id: str
    status: str
    original_size_bytes: float
    target_size_bytes: float
    machine_ids: List[str]
    created_at: datetime
    updated_at: datetime
    failure: Optional[ManagementInstanceSandboxDisksResizeOutputFailure] = None
    completed_at: Optional[datetime] = None


class mapManagementInstanceSandboxDisksResizeOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksResizeOutputFailure:
        return ManagementInstanceSandboxDisksResizeOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksResizeOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxDisksResizeOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksResizeOutput:
        return ManagementInstanceSandboxDisksResizeOutput(
        object=data.get('object'),
        id=data.get('id'),
        disk_id=data.get('disk_id'),
        status=data.get('status'),
        original_size_bytes=data.get('original_size_bytes'),
        target_size_bytes=data.get('target_size_bytes'),
        machine_ids=data.get('machine_ids', []),
        failure=mapManagementInstanceSandboxDisksResizeOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksResizeOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxDisksResizeBody:
    size_bytes: float


class mapManagementInstanceSandboxDisksResizeBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxDisksResizeBody:
        return ManagementInstanceSandboxDisksResizeBody(
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxDisksResizeBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

