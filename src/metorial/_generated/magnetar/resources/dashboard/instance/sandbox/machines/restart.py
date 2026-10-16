from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesRestartOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesRestartOutputFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesRestartOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: DashboardInstanceSandboxMachinesRestartOutputImage
    mounts: List[DashboardInstanceSandboxMachinesRestartOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: DashboardInstanceSandboxMachinesRestartOutputLifecyclePolicy
    lifecycle_hooks: List[DashboardInstanceSandboxMachinesRestartOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[DashboardInstanceSandboxMachinesRestartOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[DashboardInstanceSandboxMachinesRestartOutputSpec] = None
    max_boost: Optional[DashboardInstanceSandboxMachinesRestartOutputMaxBoost] = None
    root_disk: Optional[DashboardInstanceSandboxMachinesRestartOutputRootDisk] = None
    runtime: Optional[DashboardInstanceSandboxMachinesRestartOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[DashboardInstanceSandboxMachinesRestartOutputOperation] = None
    current_instance: Optional[DashboardInstanceSandboxMachinesRestartOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[DashboardInstanceSandboxMachinesRestartOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapDashboardInstanceSandboxMachinesRestartOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputImage:
        return DashboardInstanceSandboxMachinesRestartOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputSpec:
        return DashboardInstanceSandboxMachinesRestartOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputMaxBoost:
        return DashboardInstanceSandboxMachinesRestartOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputRootDisk:
        return DashboardInstanceSandboxMachinesRestartOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputMounts:
        return DashboardInstanceSandboxMachinesRestartOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputLifecyclePolicy:
        return DashboardInstanceSandboxMachinesRestartOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputRuntime:
        return DashboardInstanceSandboxMachinesRestartOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputLifecycleHooks:
        return DashboardInstanceSandboxMachinesRestartOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputOperation:
        return DashboardInstanceSandboxMachinesRestartOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputCurrentInstance:
        return DashboardInstanceSandboxMachinesRestartOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputUpcomingEvents:
        return DashboardInstanceSandboxMachinesRestartOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutputFailure:
        return DashboardInstanceSandboxMachinesRestartOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesRestartOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesRestartOutput:
        return DashboardInstanceSandboxMachinesRestartOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapDashboardInstanceSandboxMachinesRestartOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapDashboardInstanceSandboxMachinesRestartOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapDashboardInstanceSandboxMachinesRestartOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapDashboardInstanceSandboxMachinesRestartOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapDashboardInstanceSandboxMachinesRestartOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapDashboardInstanceSandboxMachinesRestartOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapDashboardInstanceSandboxMachinesRestartOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapDashboardInstanceSandboxMachinesRestartOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapDashboardInstanceSandboxMachinesRestartOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapDashboardInstanceSandboxMachinesRestartOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapDashboardInstanceSandboxMachinesRestartOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapDashboardInstanceSandboxMachinesRestartOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesRestartOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

