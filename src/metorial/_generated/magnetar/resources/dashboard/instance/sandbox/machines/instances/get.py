from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputImage:
    id: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputOperation:
    id: str
    kind: str
    requested_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputMounts:
    disk_id: str
    mount_path: str
    status: str
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeSetup:
    id: str
    exit_code: float
    duration_ms: float
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint:
    started_after_ms: Optional[float] = None
    exit_code: Optional[float] = None
    signal: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeError:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputRuntime:
    state: str
    setup: List[DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeSetup]
    entrypoint: Optional[DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint] = None
    error: Optional[DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeError] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutputFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesInstancesGetOutput:
    object: str
    id: str
    machine_id: str
    generation: float
    status: str
    phase: str
    image: DashboardInstanceSandboxMachinesInstancesGetOutputImage
    spec: DashboardInstanceSandboxMachinesInstancesGetOutputSpec
    mounts: List[DashboardInstanceSandboxMachinesInstancesGetOutputMounts]
    disks_ready: bool
    has_logs: bool
    created_at: datetime
    creation_reason: Optional[str] = None
    operation: Optional[DashboardInstanceSandboxMachinesInstancesGetOutputOperation] = None
    runtime: Optional[DashboardInstanceSandboxMachinesInstancesGetOutputRuntime] = None
    failure: Optional[DashboardInstanceSandboxMachinesInstancesGetOutputFailure] = None
    started_at: Optional[datetime] = None
    ready_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    last_seen_at: Optional[datetime] = None


class mapDashboardInstanceSandboxMachinesInstancesGetOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputImage:
        return DashboardInstanceSandboxMachinesInstancesGetOutputImage(
        id=data.get('id'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputSpec:
        return DashboardInstanceSandboxMachinesInstancesGetOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputOperation:
        return DashboardInstanceSandboxMachinesInstancesGetOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputMounts:
        return DashboardInstanceSandboxMachinesInstancesGetOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntimeSetup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeSetup:
        return DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeSetup(
        id=data.get('id'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeSetup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint:
        return DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint(
        started_after_ms=data.get('started_after_ms'),
        exit_code=data.get('exit_code'),
        signal=data.get('signal')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntimeError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeError:
        return DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputRuntimeError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputRuntime:
        return DashboardInstanceSandboxMachinesInstancesGetOutputRuntime(
        state=data.get('state'),
        setup=[mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntimeSetup.from_dict(item) for item in data.get('setup', []) if item],
        entrypoint=mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint.from_dict(data.get('entrypoint')) if data.get('entrypoint') else None,
        error=mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntimeError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutputFailure:
        return DashboardInstanceSandboxMachinesInstancesGetOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesGetOutput:
        return DashboardInstanceSandboxMachinesInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase'),
        creation_reason=data.get('creation_reason'),
        image=mapDashboardInstanceSandboxMachinesInstancesGetOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapDashboardInstanceSandboxMachinesInstancesGetOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        operation=mapDashboardInstanceSandboxMachinesInstancesGetOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        mounts=[mapDashboardInstanceSandboxMachinesInstancesGetOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        disks_ready=data.get('disks_ready'),
        runtime=mapDashboardInstanceSandboxMachinesInstancesGetOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        failure=mapDashboardInstanceSandboxMachinesInstancesGetOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        has_logs=data.get('has_logs'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        ready_at=datetime.fromisoformat(data.get('ready_at').replace('Z', '+00:00')) if data.get('ready_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

