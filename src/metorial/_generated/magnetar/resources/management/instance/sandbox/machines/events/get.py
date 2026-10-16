from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesEventsGetOutputMachine:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesEventsGetOutputInstance:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesEventsGetOutputError:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesEventsGetOutput:
    object: str
    id: str
    machine_id: str
    type: str
    source: str
    occurred_at: datetime
    machine_instance_id: Optional[str] = None
    generation: Optional[float] = None
    machine: Optional[ManagementInstanceSandboxMachinesEventsGetOutputMachine] = None
    instance: Optional[ManagementInstanceSandboxMachinesEventsGetOutputInstance] = None
    operation_id: Optional[str] = None
    guest_error_id: Optional[str] = None
    error: Optional[ManagementInstanceSandboxMachinesEventsGetOutputError] = None


class mapManagementInstanceSandboxMachinesEventsGetOutputMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsGetOutputMachine:
        return ManagementInstanceSandboxMachinesEventsGetOutputMachine(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsGetOutputMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsGetOutputInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsGetOutputInstance:
        return ManagementInstanceSandboxMachinesEventsGetOutputInstance(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsGetOutputInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsGetOutputError:
        return ManagementInstanceSandboxMachinesEventsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesEventsGetOutput:
        return ManagementInstanceSandboxMachinesEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        generation=data.get('generation'),
        type=data.get('type'),
        source=data.get('source'),
        machine=mapManagementInstanceSandboxMachinesEventsGetOutputMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        instance=mapManagementInstanceSandboxMachinesEventsGetOutputInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        operation_id=data.get('operation_id'),
        guest_error_id=data.get('guest_error_id'),
        error=mapManagementInstanceSandboxMachinesEventsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

