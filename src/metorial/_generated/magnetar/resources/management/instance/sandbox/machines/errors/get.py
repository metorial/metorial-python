from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesErrorsGetOutput:
    object: str
    id: str
    machine_id: str
    machine_instance_id: str
    operation_id: str
    kind: str
    stage: str
    reason: str
    code: str
    message: str
    occurred_at: datetime
    event_id: Optional[str] = None
    exit_code: Optional[float] = None
    duration_ms: Optional[float] = None
    stdout: Optional[str] = None


class mapManagementInstanceSandboxMachinesErrorsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesErrorsGetOutput:
        return ManagementInstanceSandboxMachinesErrorsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        operation_id=data.get('operation_id'),
        event_id=data.get('event_id'),
        kind=data.get('kind'),
        stage=data.get('stage'),
        reason=data.get('reason'),
        code=data.get('code'),
        message=data.get('message'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms'),
        stdout=data.get('stdout'),
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesErrorsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

