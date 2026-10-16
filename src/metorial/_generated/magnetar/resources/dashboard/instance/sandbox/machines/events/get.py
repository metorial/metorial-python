from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesEventsGetOutputMachine:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesEventsGetOutputInstance:
    to_status: str
    from_status: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesEventsGetOutputError:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesEventsGetOutput:
    object: str
    id: str
    machine_id: str
    type: str
    source: str
    occurred_at: datetime
    machine_instance_id: Optional[str] = None
    generation: Optional[float] = None
    machine: Optional[DashboardInstanceSandboxMachinesEventsGetOutputMachine] = None
    instance: Optional[DashboardInstanceSandboxMachinesEventsGetOutputInstance] = None
    operation_id: Optional[str] = None
    guest_error_id: Optional[str] = None
    error: Optional[DashboardInstanceSandboxMachinesEventsGetOutputError] = None


class mapDashboardInstanceSandboxMachinesEventsGetOutputMachine:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsGetOutputMachine:
        return DashboardInstanceSandboxMachinesEventsGetOutputMachine(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsGetOutputMachine, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsGetOutputInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsGetOutputInstance:
        return DashboardInstanceSandboxMachinesEventsGetOutputInstance(
        from_status=data.get('from_status'),
        to_status=data.get('to_status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsGetOutputInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsGetOutputError:
        return DashboardInstanceSandboxMachinesEventsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesEventsGetOutput:
        return DashboardInstanceSandboxMachinesEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        machine_instance_id=data.get('machine_instance_id'),
        generation=data.get('generation'),
        type=data.get('type'),
        source=data.get('source'),
        machine=mapDashboardInstanceSandboxMachinesEventsGetOutputMachine.from_dict(data.get('machine')) if data.get('machine') else None,
        instance=mapDashboardInstanceSandboxMachinesEventsGetOutputInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        operation_id=data.get('operation_id'),
        guest_error_id=data.get('guest_error_id'),
        error=mapDashboardInstanceSandboxMachinesEventsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

