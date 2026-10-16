from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesOperationsGetOutputFailure:
    code: str
    message: str
@dataclass
class SandboxMachinesOperationsGetOutputInstanceOperations:
    id: str
    kind: str
    machine_instance_id: str
@dataclass
class SandboxMachinesOperationsGetOutput:
    object: str
    id: str
    machine_id: str
    kind: str
    trigger: str
    outcome: str
    instance_operations: List[SandboxMachinesOperationsGetOutputInstanceOperations]
    requested_at: datetime
    failure: Optional[SandboxMachinesOperationsGetOutputFailure] = None
    from_machine_instance_id: Optional[str] = None
    superseded_by_id: Optional[str] = None
    completed_at: Optional[datetime] = None


class mapSandboxMachinesOperationsGetOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesOperationsGetOutputFailure:
        return SandboxMachinesOperationsGetOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesOperationsGetOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesOperationsGetOutputInstanceOperations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesOperationsGetOutputInstanceOperations:
        return SandboxMachinesOperationsGetOutputInstanceOperations(
        id=data.get('id'),
        kind=data.get('kind'),
        machine_instance_id=data.get('machine_instance_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesOperationsGetOutputInstanceOperations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesOperationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesOperationsGetOutput:
        return SandboxMachinesOperationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        outcome=data.get('outcome'),
        failure=mapSandboxMachinesOperationsGetOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        from_machine_instance_id=data.get('from_machine_instance_id'),
        superseded_by_id=data.get('superseded_by_id'),
        instance_operations=[mapSandboxMachinesOperationsGetOutputInstanceOperations.from_dict(item) for item in data.get('instance_operations', []) if item],
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesOperationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

