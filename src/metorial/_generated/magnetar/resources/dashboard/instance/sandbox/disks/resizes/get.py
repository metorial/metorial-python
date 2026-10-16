from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxDisksResizesGetOutputFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxDisksResizesGetOutput:
    object: str
    id: str
    disk_id: str
    status: str
    original_size_bytes: float
    target_size_bytes: float
    machine_ids: List[str]
    created_at: datetime
    updated_at: datetime
    failure: Optional[DashboardInstanceSandboxDisksResizesGetOutputFailure] = None
    completed_at: Optional[datetime] = None


class mapDashboardInstanceSandboxDisksResizesGetOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksResizesGetOutputFailure:
        return DashboardInstanceSandboxDisksResizesGetOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksResizesGetOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxDisksResizesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxDisksResizesGetOutput:
        return DashboardInstanceSandboxDisksResizesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        disk_id=data.get('disk_id'),
        status=data.get('status'),
        original_size_bytes=data.get('original_size_bytes'),
        target_size_bytes=data.get('target_size_bytes'),
        machine_ids=data.get('machine_ids', []),
        failure=mapDashboardInstanceSandboxDisksResizesGetOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxDisksResizesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

