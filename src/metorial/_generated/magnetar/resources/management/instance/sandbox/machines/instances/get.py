from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputImage:
    id: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputOperation:
    id: str
    kind: str
    requested_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputMounts:
    disk_id: str
    mount_path: str
    status: str
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeSetup:
    id: str
    exit_code: float
    duration_ms: float
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint:
    started_after_ms: Optional[float] = None
    exit_code: Optional[float] = None
    signal: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeError:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputRuntime:
    state: str
    setup: List[ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeSetup]
    entrypoint: Optional[ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint] = None
    error: Optional[ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeError] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutputFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesInstancesGetOutput:
    object: str
    id: str
    machine_id: str
    generation: float
    status: str
    phase: str
    image: ManagementInstanceSandboxMachinesInstancesGetOutputImage
    spec: ManagementInstanceSandboxMachinesInstancesGetOutputSpec
    mounts: List[ManagementInstanceSandboxMachinesInstancesGetOutputMounts]
    disks_ready: bool
    has_logs: bool
    created_at: datetime
    creation_reason: Optional[str] = None
    operation: Optional[ManagementInstanceSandboxMachinesInstancesGetOutputOperation] = None
    runtime: Optional[ManagementInstanceSandboxMachinesInstancesGetOutputRuntime] = None
    failure: Optional[ManagementInstanceSandboxMachinesInstancesGetOutputFailure] = None
    started_at: Optional[datetime] = None
    ready_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    last_seen_at: Optional[datetime] = None


class mapManagementInstanceSandboxMachinesInstancesGetOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputImage:
        return ManagementInstanceSandboxMachinesInstancesGetOutputImage(
        id=data.get('id'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputSpec:
        return ManagementInstanceSandboxMachinesInstancesGetOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputOperation:
        return ManagementInstanceSandboxMachinesInstancesGetOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputMounts:
        return ManagementInstanceSandboxMachinesInstancesGetOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputRuntimeSetup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeSetup:
        return ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeSetup(
        id=data.get('id'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeSetup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint:
        return ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint(
        started_after_ms=data.get('started_after_ms'),
        exit_code=data.get('exit_code'),
        signal=data.get('signal')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputRuntimeError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeError:
        return ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputRuntimeError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputRuntime:
        return ManagementInstanceSandboxMachinesInstancesGetOutputRuntime(
        state=data.get('state'),
        setup=[mapManagementInstanceSandboxMachinesInstancesGetOutputRuntimeSetup.from_dict(item) for item in data.get('setup', []) if item],
        entrypoint=mapManagementInstanceSandboxMachinesInstancesGetOutputRuntimeEntrypoint.from_dict(data.get('entrypoint')) if data.get('entrypoint') else None,
        error=mapManagementInstanceSandboxMachinesInstancesGetOutputRuntimeError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutputFailure:
        return ManagementInstanceSandboxMachinesInstancesGetOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesGetOutput:
        return ManagementInstanceSandboxMachinesInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase'),
        creation_reason=data.get('creation_reason'),
        image=mapManagementInstanceSandboxMachinesInstancesGetOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapManagementInstanceSandboxMachinesInstancesGetOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        operation=mapManagementInstanceSandboxMachinesInstancesGetOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        mounts=[mapManagementInstanceSandboxMachinesInstancesGetOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        disks_ready=data.get('disks_ready'),
        runtime=mapManagementInstanceSandboxMachinesInstancesGetOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        failure=mapManagementInstanceSandboxMachinesInstancesGetOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        has_logs=data.get('has_logs'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        ready_at=datetime.fromisoformat(data.get('ready_at').replace('Z', '+00:00')) if data.get('ready_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

