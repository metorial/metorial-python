from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutputFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesUpdateOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: DashboardInstanceSandboxMachinesUpdateOutputImage
    mounts: List[DashboardInstanceSandboxMachinesUpdateOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: DashboardInstanceSandboxMachinesUpdateOutputLifecyclePolicy
    lifecycle_hooks: List[DashboardInstanceSandboxMachinesUpdateOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[DashboardInstanceSandboxMachinesUpdateOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[DashboardInstanceSandboxMachinesUpdateOutputSpec] = None
    max_boost: Optional[DashboardInstanceSandboxMachinesUpdateOutputMaxBoost] = None
    root_disk: Optional[DashboardInstanceSandboxMachinesUpdateOutputRootDisk] = None
    runtime: Optional[DashboardInstanceSandboxMachinesUpdateOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[DashboardInstanceSandboxMachinesUpdateOutputOperation] = None
    current_instance: Optional[DashboardInstanceSandboxMachinesUpdateOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[DashboardInstanceSandboxMachinesUpdateOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapDashboardInstanceSandboxMachinesUpdateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputImage:
        return DashboardInstanceSandboxMachinesUpdateOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputSpec:
        return DashboardInstanceSandboxMachinesUpdateOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputMaxBoost:
        return DashboardInstanceSandboxMachinesUpdateOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputRootDisk:
        return DashboardInstanceSandboxMachinesUpdateOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputMounts:
        return DashboardInstanceSandboxMachinesUpdateOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputLifecyclePolicy:
        return DashboardInstanceSandboxMachinesUpdateOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputRuntime:
        return DashboardInstanceSandboxMachinesUpdateOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputLifecycleHooks:
        return DashboardInstanceSandboxMachinesUpdateOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputOperation:
        return DashboardInstanceSandboxMachinesUpdateOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputCurrentInstance:
        return DashboardInstanceSandboxMachinesUpdateOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputUpcomingEvents:
        return DashboardInstanceSandboxMachinesUpdateOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutputFailure:
        return DashboardInstanceSandboxMachinesUpdateOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateOutput:
        return DashboardInstanceSandboxMachinesUpdateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapDashboardInstanceSandboxMachinesUpdateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapDashboardInstanceSandboxMachinesUpdateOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapDashboardInstanceSandboxMachinesUpdateOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapDashboardInstanceSandboxMachinesUpdateOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapDashboardInstanceSandboxMachinesUpdateOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapDashboardInstanceSandboxMachinesUpdateOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapDashboardInstanceSandboxMachinesUpdateOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapDashboardInstanceSandboxMachinesUpdateOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapDashboardInstanceSandboxMachinesUpdateOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapDashboardInstanceSandboxMachinesUpdateOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapDashboardInstanceSandboxMachinesUpdateOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapDashboardInstanceSandboxMachinesUpdateOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesUpdateBodyLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateBodyRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesUpdateBodyMounts:
    disk_id: str
    mount_path: str
@dataclass
class DashboardInstanceSandboxMachinesUpdateBody:
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    spec_id: Optional[str] = None
    spec_identifier: Optional[str] = None
    memory_gib: Optional[float] = None
    cpus: Optional[float] = None
    lifecycle_policy: Optional[DashboardInstanceSandboxMachinesUpdateBodyLifecyclePolicy] = None
    runtime: Optional[DashboardInstanceSandboxMachinesUpdateBodyRuntime] = None
    lifecycle_hooks: Optional[List[Dict[str, Any]]] = None
    ignore_image_hooks: Optional[bool] = None
    entrypoint_wait_seconds: Optional[float] = None
    mounts: Optional[List[DashboardInstanceSandboxMachinesUpdateBodyMounts]] = None
    firewall_ids: Optional[List[str]] = None
    public_ports: Optional[List[float]] = None


class mapDashboardInstanceSandboxMachinesUpdateBodyLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateBodyLifecyclePolicy:
        return DashboardInstanceSandboxMachinesUpdateBodyLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateBodyLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateBodyRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateBodyRuntime:
        return DashboardInstanceSandboxMachinesUpdateBodyRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateBodyRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateBodyMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateBodyMounts:
        return DashboardInstanceSandboxMachinesUpdateBodyMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateBodyMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesUpdateBody:
        return DashboardInstanceSandboxMachinesUpdateBody(
        metadata=data.get('metadata'),
        name=data.get('name'),
        spec_id=data.get('spec_id'),
        spec_identifier=data.get('spec_identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus'),
        lifecycle_policy=mapDashboardInstanceSandboxMachinesUpdateBodyLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapDashboardInstanceSandboxMachinesUpdateBodyRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=data.get('lifecycle_hooks', []),
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        mounts=[mapDashboardInstanceSandboxMachinesUpdateBodyMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

