from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesTouchOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesTouchOutputFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesTouchOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: DashboardInstanceSandboxMachinesTouchOutputImage
    mounts: List[DashboardInstanceSandboxMachinesTouchOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: DashboardInstanceSandboxMachinesTouchOutputLifecyclePolicy
    lifecycle_hooks: List[DashboardInstanceSandboxMachinesTouchOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[DashboardInstanceSandboxMachinesTouchOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[DashboardInstanceSandboxMachinesTouchOutputSpec] = None
    max_boost: Optional[DashboardInstanceSandboxMachinesTouchOutputMaxBoost] = None
    root_disk: Optional[DashboardInstanceSandboxMachinesTouchOutputRootDisk] = None
    runtime: Optional[DashboardInstanceSandboxMachinesTouchOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[DashboardInstanceSandboxMachinesTouchOutputOperation] = None
    current_instance: Optional[DashboardInstanceSandboxMachinesTouchOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[DashboardInstanceSandboxMachinesTouchOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapDashboardInstanceSandboxMachinesTouchOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputImage:
        return DashboardInstanceSandboxMachinesTouchOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputSpec:
        return DashboardInstanceSandboxMachinesTouchOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputMaxBoost:
        return DashboardInstanceSandboxMachinesTouchOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputRootDisk:
        return DashboardInstanceSandboxMachinesTouchOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputMounts:
        return DashboardInstanceSandboxMachinesTouchOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputLifecyclePolicy:
        return DashboardInstanceSandboxMachinesTouchOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputRuntime:
        return DashboardInstanceSandboxMachinesTouchOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputLifecycleHooks:
        return DashboardInstanceSandboxMachinesTouchOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputOperation:
        return DashboardInstanceSandboxMachinesTouchOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputCurrentInstance:
        return DashboardInstanceSandboxMachinesTouchOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputUpcomingEvents:
        return DashboardInstanceSandboxMachinesTouchOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutputFailure:
        return DashboardInstanceSandboxMachinesTouchOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesTouchOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesTouchOutput:
        return DashboardInstanceSandboxMachinesTouchOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapDashboardInstanceSandboxMachinesTouchOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapDashboardInstanceSandboxMachinesTouchOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapDashboardInstanceSandboxMachinesTouchOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapDashboardInstanceSandboxMachinesTouchOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapDashboardInstanceSandboxMachinesTouchOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapDashboardInstanceSandboxMachinesTouchOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapDashboardInstanceSandboxMachinesTouchOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapDashboardInstanceSandboxMachinesTouchOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapDashboardInstanceSandboxMachinesTouchOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapDashboardInstanceSandboxMachinesTouchOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapDashboardInstanceSandboxMachinesTouchOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapDashboardInstanceSandboxMachinesTouchOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesTouchOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

