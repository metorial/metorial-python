from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesOperationsGetOutputFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesOperationsGetOutputInstanceOperations:
    id: str
    kind: str
    machine_instance_id: str
@dataclass
class DashboardInstanceSandboxMachinesOperationsGetOutput:
    object: str
    id: str
    machine_id: str
    kind: str
    trigger: str
    outcome: str
    instance_operations: List[DashboardInstanceSandboxMachinesOperationsGetOutputInstanceOperations]
    requested_at: datetime
    failure: Optional[DashboardInstanceSandboxMachinesOperationsGetOutputFailure] = None
    from_machine_instance_id: Optional[str] = None
    superseded_by_id: Optional[str] = None
    completed_at: Optional[datetime] = None


class mapDashboardInstanceSandboxMachinesOperationsGetOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsGetOutputFailure:
        return DashboardInstanceSandboxMachinesOperationsGetOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsGetOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesOperationsGetOutputInstanceOperations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsGetOutputInstanceOperations:
        return DashboardInstanceSandboxMachinesOperationsGetOutputInstanceOperations(
        id=data.get('id'),
        kind=data.get('kind'),
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsGetOutputInstanceOperations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesOperationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesOperationsGetOutput:
        return DashboardInstanceSandboxMachinesOperationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        outcome=data.get('outcome'),
        failure=mapDashboardInstanceSandboxMachinesOperationsGetOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        from_machine_instance_id=data.get('from_machine_instance_id'),
        superseded_by_id=data.get('superseded_by_id'),
        instance_operations=[mapDashboardInstanceSandboxMachinesOperationsGetOutputInstanceOperations.from_dict(item) for item in data.get('instance_operations', []) if item],
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesOperationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

