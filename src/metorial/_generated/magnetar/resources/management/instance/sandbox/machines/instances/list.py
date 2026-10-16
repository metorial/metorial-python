from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsImage:
    id: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsOperation:
    id: str
    kind: str
    requested_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsMounts:
    disk_id: str
    mount_path: str
    status: str
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup:
    id: str
    exit_code: float
    duration_ms: float
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
    started_after_ms: Optional[float] = None
    exit_code: Optional[float] = None
    signal: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeError:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntime:
    state: str
    setup: List[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup]
    entrypoint: Optional[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint] = None
    error: Optional[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeError] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItemsFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputItems:
    object: str
    id: str
    machine_id: str
    generation: float
    status: str
    phase: str
    image: ManagementInstanceSandboxMachinesInstancesListOutputItemsImage
    spec: ManagementInstanceSandboxMachinesInstancesListOutputItemsSpec
    mounts: List[ManagementInstanceSandboxMachinesInstancesListOutputItemsMounts]
    disks_ready: bool
    has_logs: bool
    created_at: datetime
    creation_reason: Optional[str] = None
    operation: Optional[ManagementInstanceSandboxMachinesInstancesListOutputItemsOperation] = None
    runtime: Optional[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntime] = None
    failure: Optional[ManagementInstanceSandboxMachinesInstancesListOutputItemsFailure] = None
    started_at: Optional[datetime] = None
    ready_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    last_seen_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSandboxMachinesInstancesListOutput:
    items: List[ManagementInstanceSandboxMachinesInstancesListOutputItems]
    pagination: ManagementInstanceSandboxMachinesInstancesListOutputPagination


class mapManagementInstanceSandboxMachinesInstancesListOutputItemsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsImage:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsImage(
        id=data.get('id'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsSpec:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsOperation:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsMounts:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup(
        id=data.get('id'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint(
        started_after_ms=data.get('started_after_ms'),
        exit_code=data.get('exit_code'),
        signal=data.get('signal')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeError:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntime:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntime(
        state=data.get('state'),
        setup=[mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup.from_dict(item) for item in data.get('setup', []) if item],
        entrypoint=mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint.from_dict(data.get('entrypoint')) if data.get('entrypoint') else None,
        error=mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntimeError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItemsFailure:
        return ManagementInstanceSandboxMachinesInstancesListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputItems:
        return ManagementInstanceSandboxMachinesInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase'),
        creation_reason=data.get('creation_reason'),
        image=mapManagementInstanceSandboxMachinesInstancesListOutputItemsImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapManagementInstanceSandboxMachinesInstancesListOutputItemsSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        operation=mapManagementInstanceSandboxMachinesInstancesListOutputItemsOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        mounts=[mapManagementInstanceSandboxMachinesInstancesListOutputItemsMounts.from_dict(item) for item in data.get('mounts', []) if item],
        disks_ready=data.get('disks_ready'),
        runtime=mapManagementInstanceSandboxMachinesInstancesListOutputItemsRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        failure=mapManagementInstanceSandboxMachinesInstancesListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        has_logs=data.get('has_logs'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        ready_at=datetime.fromisoformat(data.get('ready_at').replace('Z', '+00:00')) if data.get('ready_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutputPagination:
        return ManagementInstanceSandboxMachinesInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListOutput:
        return ManagementInstanceSandboxMachinesInstancesListOutput(
        items=[mapManagementInstanceSandboxMachinesInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSandboxMachinesInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSandboxMachinesInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesInstancesListQuery:
        return ManagementInstanceSandboxMachinesInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

