from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesInstancesListOutputItemsImage:
    id: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class SandboxMachinesInstancesListOutputItemsSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class SandboxMachinesInstancesListOutputItemsOperation:
    id: str
    kind: str
    requested_at: datetime
@dataclass
class SandboxMachinesInstancesListOutputItemsMounts:
    disk_id: str
    mount_path: str
    status: str
@dataclass
class SandboxMachinesInstancesListOutputItemsRuntimeSetup:
    id: str
    exit_code: float
    duration_ms: float
@dataclass
class SandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
    started_after_ms: Optional[float] = None
    exit_code: Optional[float] = None
    signal: Optional[str] = None
@dataclass
class SandboxMachinesInstancesListOutputItemsRuntimeError:
    code: str
    message: str
@dataclass
class SandboxMachinesInstancesListOutputItemsRuntime:
    state: str
    setup: List[SandboxMachinesInstancesListOutputItemsRuntimeSetup]
    entrypoint: Optional[SandboxMachinesInstancesListOutputItemsRuntimeEntrypoint] = None
    error: Optional[SandboxMachinesInstancesListOutputItemsRuntimeError] = None
@dataclass
class SandboxMachinesInstancesListOutputItemsFailure:
    code: str
    message: str
@dataclass
class SandboxMachinesInstancesListOutputItems:
    object: str
    id: str
    machine_id: str
    generation: float
    status: str
    phase: str
    image: SandboxMachinesInstancesListOutputItemsImage
    spec: SandboxMachinesInstancesListOutputItemsSpec
    mounts: List[SandboxMachinesInstancesListOutputItemsMounts]
    disks_ready: bool
    has_logs: bool
    created_at: datetime
    creation_reason: Optional[str] = None
    operation: Optional[SandboxMachinesInstancesListOutputItemsOperation] = None
    runtime: Optional[SandboxMachinesInstancesListOutputItemsRuntime] = None
    failure: Optional[SandboxMachinesInstancesListOutputItemsFailure] = None
    started_at: Optional[datetime] = None
    ready_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    last_seen_at: Optional[datetime] = None
@dataclass
class SandboxMachinesInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SandboxMachinesInstancesListOutput:
    items: List[SandboxMachinesInstancesListOutputItems]
    pagination: SandboxMachinesInstancesListOutputPagination


class mapSandboxMachinesInstancesListOutputItemsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsImage:
        return SandboxMachinesInstancesListOutputItemsImage(
        id=data.get('id'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsSpec:
        return SandboxMachinesInstancesListOutputItemsSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsOperation:
        return SandboxMachinesInstancesListOutputItemsOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsMounts:
        return SandboxMachinesInstancesListOutputItemsMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsRuntimeSetup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsRuntimeSetup:
        return SandboxMachinesInstancesListOutputItemsRuntimeSetup(
        id=data.get('id'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsRuntimeSetup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
        return SandboxMachinesInstancesListOutputItemsRuntimeEntrypoint(
        started_after_ms=data.get('started_after_ms'),
        exit_code=data.get('exit_code'),
        signal=data.get('signal')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsRuntimeEntrypoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsRuntimeError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsRuntimeError:
        return SandboxMachinesInstancesListOutputItemsRuntimeError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsRuntimeError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsRuntime:
        return SandboxMachinesInstancesListOutputItemsRuntime(
        state=data.get('state'),
        setup=[mapSandboxMachinesInstancesListOutputItemsRuntimeSetup.from_dict(item) for item in data.get('setup', []) if item],
        entrypoint=mapSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint.from_dict(data.get('entrypoint')) if data.get('entrypoint') else None,
        error=mapSandboxMachinesInstancesListOutputItemsRuntimeError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItemsFailure:
        return SandboxMachinesInstancesListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputItems:
        return SandboxMachinesInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase'),
        creation_reason=data.get('creation_reason'),
        image=mapSandboxMachinesInstancesListOutputItemsImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapSandboxMachinesInstancesListOutputItemsSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        operation=mapSandboxMachinesInstancesListOutputItemsOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        mounts=[mapSandboxMachinesInstancesListOutputItemsMounts.from_dict(item) for item in data.get('mounts', []) if item],
        disks_ready=data.get('disks_ready'),
        runtime=mapSandboxMachinesInstancesListOutputItemsRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        failure=mapSandboxMachinesInstancesListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        has_logs=data.get('has_logs'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        ready_at=datetime.fromisoformat(data.get('ready_at').replace('Z', '+00:00')) if data.get('ready_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutputPagination:
        return SandboxMachinesInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListOutput:
        return SandboxMachinesInstancesListOutput(
        items=[mapSandboxMachinesInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSandboxMachinesInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapSandboxMachinesInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesListQuery:
        return SandboxMachinesInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

