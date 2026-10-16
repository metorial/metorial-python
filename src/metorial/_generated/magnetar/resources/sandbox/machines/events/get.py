from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesEventsGetOutputMachine:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class SandboxMachinesEventsGetOutputInstance:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class SandboxMachinesEventsGetOutputError:
    code: str
    message: str
@dataclass
class SandboxMachinesEventsGetOutput:
    object: str
    id: str
    machine_id: str
    type: str
    source: str
    occurred_at: datetime
    machine_instance_id: Optional[str] = None
    generation: Optional[float] = None
    machine: Optional[SandboxMachinesEventsGetOutputMachine] = None
    instance: Optional[SandboxMachinesEventsGetOutputInstance] = None
    operation_id: Optional[str] = None
    guest_error_id: Optional[str] = None
    error: Optional[SandboxMachinesEventsGetOutputError] = None


class mapSandboxMachinesEventsGetOutputMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsGetOutputMachine:
        return SandboxMachinesEventsGetOutputMachine(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsGetOutputMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsGetOutputInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsGetOutputInstance:
        return SandboxMachinesEventsGetOutputInstance(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsGetOutputInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsGetOutputError:
        return SandboxMachinesEventsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesEventsGetOutput:
        return SandboxMachinesEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        generation=data.get('generation'),
        type=data.get('type'),
        source=data.get('source'),
        machine=mapSandboxMachinesEventsGetOutputMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        instance=mapSandboxMachinesEventsGetOutputInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        operation_id=data.get('operation_id'),
        guest_error_id=data.get('guest_error_id'),
        error=mapSandboxMachinesEventsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

