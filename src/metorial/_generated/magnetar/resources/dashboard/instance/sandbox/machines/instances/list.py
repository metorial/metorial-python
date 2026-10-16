from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsImage:
    id: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsOperation:
    id: str
    kind: str
    requested_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsMounts:
    disk_id: str
    mount_path: str
    status: str
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup:
    id: str
    exit_code: float
    duration_ms: float
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
    started_after_ms: Optional[float] = None
    exit_code: Optional[float] = None
    signal: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeError:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntime:
    state: str
    setup: List[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup]
    entrypoint: Optional[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint] = None
    error: Optional[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeError] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItemsFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputItems:
    object: str
    id: str
    machine_id: str
    generation: float
    status: str
    phase: str
    image: DashboardInstanceSandboxMachinesInstancesListOutputItemsImage
    spec: DashboardInstanceSandboxMachinesInstancesListOutputItemsSpec
    mounts: List[DashboardInstanceSandboxMachinesInstancesListOutputItemsMounts]
    disks_ready: bool
    has_logs: bool
    created_at: datetime
    creation_reason: Optional[str] = None
    operation: Optional[DashboardInstanceSandboxMachinesInstancesListOutputItemsOperation] = None
    runtime: Optional[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntime] = None
    failure: Optional[DashboardInstanceSandboxMachinesInstancesListOutputItemsFailure] = None
    started_at: Optional[datetime] = None
    ready_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None
    last_seen_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSandboxMachinesInstancesListOutput:
    items: List[DashboardInstanceSandboxMachinesInstancesListOutputItems]
    pagination: DashboardInstanceSandboxMachinesInstancesListOutputPagination


class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsImage:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsImage(
        id=data.get('id'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsSpec:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsOperation:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsMounts:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup(
        id=data.get('id'),
        exit_code=data.get('exit_code'),
        duration_ms=data.get('duration_ms')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint(
        started_after_ms=data.get('started_after_ms'),
        exit_code=data.get('exit_code'),
        signal=data.get('signal')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeError:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntime:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntime(
        state=data.get('state'),
        setup=[mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeSetup.from_dict(item) for item in data.get('setup', []) if item],
        entrypoint=mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeEntrypoint.from_dict(data.get('entrypoint')) if data.get('entrypoint') else None,
        error=mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntimeError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItemsFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItemsFailure:
        return DashboardInstanceSandboxMachinesInstancesListOutputItemsFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItemsFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputItems:
        return DashboardInstanceSandboxMachinesInstancesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        machine_id=data.get('machine_id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase'),
        creation_reason=data.get('creation_reason'),
        image=mapDashboardInstanceSandboxMachinesInstancesListOutputItemsImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapDashboardInstanceSandboxMachinesInstancesListOutputItemsSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        operation=mapDashboardInstanceSandboxMachinesInstancesListOutputItemsOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        mounts=[mapDashboardInstanceSandboxMachinesInstancesListOutputItemsMounts.from_dict(item) for item in data.get('mounts', []) if item],
        disks_ready=data.get('disks_ready'),
        runtime=mapDashboardInstanceSandboxMachinesInstancesListOutputItemsRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        failure=mapDashboardInstanceSandboxMachinesInstancesListOutputItemsFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        has_logs=data.get('has_logs'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        ready_at=datetime.fromisoformat(data.get('ready_at').replace('Z', '+00:00')) if data.get('ready_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutputPagination:
        return DashboardInstanceSandboxMachinesInstancesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListOutput:
        return DashboardInstanceSandboxMachinesInstancesListOutput(
        items=[mapDashboardInstanceSandboxMachinesInstancesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSandboxMachinesInstancesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesInstancesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSandboxMachinesInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesInstancesListQuery:
        return DashboardInstanceSandboxMachinesInstancesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

