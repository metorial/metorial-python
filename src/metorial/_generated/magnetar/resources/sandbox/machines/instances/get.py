from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesInstancesGetOutputImage:
    id: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class SandboxMachinesInstancesGetOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class SandboxMachinesInstancesGetOutputOperation:
    id: str
    kind: str
    requested_at: datetime
@dataclass
class SandboxMachinesInstancesGetOutputMounts:
    disk_id: str
    mount_path: str
    status: str
@dataclass
class SandboxMachinesInstancesGetOutputRuntimeSetup:
    id: str
    exit_code: float
    duration_ms: float
@dataclass
class SandboxMachinesInstancesGetOutputRuntimeEntrypoint:
    started_after_ms: Optional[float] = None
    exit_code: Optional[float] = None
    signal: Optional[str] = None
@dataclass
class SandboxMachinesInstancesGetOutputRuntimeError:
    code: str
    message: str
@dataclass
class SandboxMachinesInstancesGetOutputRuntime:
    state: str
    setup: List[SandboxMachinesInstancesGetOutputRuntimeSetup]
    entrypoint: Optional[SandboxMachinesInstancesGetOutputRuntimeEntrypoint] = None
    error: Optional[SandboxMachinesInstancesGetOutputRuntimeError] = None
@dataclass
class SandboxMachinesInstancesGetOutputFailure:
    code: str
    message: str
@dataclass
class SandboxMachinesInstancesGetOutput:
    object: str
    id: str
    machine_id: str
    generation: float
    status: str
    phase: str
    image: SandboxMachinesInstancesGetOutputImage
    spec: SandboxMachinesInstancesGetOutputSpec
    mounts: List[SandboxMachinesInstancesGetOutputMounts]
    disks_ready: bool
    has_logs: bool
    created_at: datetime
    creation_reason: Optional[str] = None
    operation: Optional[SandboxMachinesInstancesGetOutputOperation] = None
    runtime: Optional[SandboxMachinesInstancesGetOutputRuntime] = None
    failure: Optional[SandboxMachinesInstancesGetOutputFailure] = None
    started_at: Optional[datetime] = None
    ready_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    last_seen_at: Optional[datetime] = None


class mapSandboxMachinesInstancesGetOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputImage:
        return SandboxMachinesInstancesGetOutputImage(
        id=data.get('id'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputSpec:
        return SandboxMachinesInstancesGetOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputOperation:
        return SandboxMachinesInstancesGetOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputMounts:
        return SandboxMachinesInstancesGetOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputRuntimeSetup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputRuntimeSetup:
        return SandboxMachinesInstancesGetOutputRuntimeSetup(
        id=data.get('id'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputRuntimeSetup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputRuntimeEntrypoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputRuntimeEntrypoint:
        return SandboxMachinesInstancesGetOutputRuntimeEntrypoint(
        started_after_ms=data.get('started_after_ms'),
        exit_code=data.get('exit_code'),
        signal=data.get('signal')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputRuntimeEntrypoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputRuntimeError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputRuntimeError:
        return SandboxMachinesInstancesGetOutputRuntimeError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputRuntimeError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputRuntime:
        return SandboxMachinesInstancesGetOutputRuntime(
        state=data.get('state'),
        setup=[mapSandboxMachinesInstancesGetOutputRuntimeSetup.from_dict(item) for item in data.get('setup', []) if item],
        entrypoint=mapSandboxMachinesInstancesGetOutputRuntimeEntrypoint.from_dict(data.get('entrypoint')) if data.get('entrypoint') else None,
        error=mapSandboxMachinesInstancesGetOutputRuntimeError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutputFailure:
        return SandboxMachinesInstancesGetOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesGetOutput:
        return SandboxMachinesInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase'),
        creation_reason=data.get('creation_reason'),
        image=mapSandboxMachinesInstancesGetOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapSandboxMachinesInstancesGetOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        operation=mapSandboxMachinesInstancesGetOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        mounts=[mapSandboxMachinesInstancesGetOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        disks_ready=data.get('disks_ready'),
        runtime=mapSandboxMachinesInstancesGetOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        failure=mapSandboxMachinesInstancesGetOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        has_logs=data.get('has_logs'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        ready_at=datetime.fromisoformat(data.get('ready_at').replace('Z', '+00:00')) if data.get('ready_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

