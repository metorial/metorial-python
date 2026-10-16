from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesCreateOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesCreateOutputFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesCreateOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: ManagementInstanceSandboxMachinesCreateOutputImage
    mounts: List[ManagementInstanceSandboxMachinesCreateOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: ManagementInstanceSandboxMachinesCreateOutputLifecyclePolicy
    lifecycle_hooks: List[ManagementInstanceSandboxMachinesCreateOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[ManagementInstanceSandboxMachinesCreateOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[ManagementInstanceSandboxMachinesCreateOutputSpec] = None
    max_boost: Optional[ManagementInstanceSandboxMachinesCreateOutputMaxBoost] = None
    root_disk: Optional[ManagementInstanceSandboxMachinesCreateOutputRootDisk] = None
    runtime: Optional[ManagementInstanceSandboxMachinesCreateOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[ManagementInstanceSandboxMachinesCreateOutputOperation] = None
    current_instance: Optional[ManagementInstanceSandboxMachinesCreateOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[ManagementInstanceSandboxMachinesCreateOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapManagementInstanceSandboxMachinesCreateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputImage:
        return ManagementInstanceSandboxMachinesCreateOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputSpec:
        return ManagementInstanceSandboxMachinesCreateOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputMaxBoost:
        return ManagementInstanceSandboxMachinesCreateOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputRootDisk:
        return ManagementInstanceSandboxMachinesCreateOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputMounts:
        return ManagementInstanceSandboxMachinesCreateOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputLifecyclePolicy:
        return ManagementInstanceSandboxMachinesCreateOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputRuntime:
        return ManagementInstanceSandboxMachinesCreateOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputLifecycleHooks:
        return ManagementInstanceSandboxMachinesCreateOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputOperation:
        return ManagementInstanceSandboxMachinesCreateOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputCurrentInstance:
        return ManagementInstanceSandboxMachinesCreateOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputUpcomingEvents:
        return ManagementInstanceSandboxMachinesCreateOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutputFailure:
        return ManagementInstanceSandboxMachinesCreateOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateOutput:
        return ManagementInstanceSandboxMachinesCreateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapManagementInstanceSandboxMachinesCreateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapManagementInstanceSandboxMachinesCreateOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapManagementInstanceSandboxMachinesCreateOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapManagementInstanceSandboxMachinesCreateOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapManagementInstanceSandboxMachinesCreateOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapManagementInstanceSandboxMachinesCreateOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapManagementInstanceSandboxMachinesCreateOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapManagementInstanceSandboxMachinesCreateOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapManagementInstanceSandboxMachinesCreateOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapManagementInstanceSandboxMachinesCreateOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapManagementInstanceSandboxMachinesCreateOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapManagementInstanceSandboxMachinesCreateOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesCreateBodyLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateBodyRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesCreateBodyMounts:
    disk_id: str
    mount_path: str
@dataclass
class ManagementInstanceSandboxMachinesCreateBody:
    region: str
    image_id: str
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    spec_id: Optional[str] = None
    spec_identifier: Optional[str] = None
    memory_gib: Optional[float] = None
    cpus: Optional[float] = None
    lifecycle_policy: Optional[ManagementInstanceSandboxMachinesCreateBodyLifecyclePolicy] = None
    runtime: Optional[ManagementInstanceSandboxMachinesCreateBodyRuntime] = None
    lifecycle_hooks: Optional[List[Dict[str, Any]]] = None
    ignore_image_hooks: Optional[bool] = None
    entrypoint_wait_seconds: Optional[float] = None
    mounts: Optional[List[ManagementInstanceSandboxMachinesCreateBodyMounts]] = None
    firewall_ids: Optional[List[str]] = None
    public_ports: Optional[List[float]] = None
    start: Optional[bool] = None


class mapManagementInstanceSandboxMachinesCreateBodyLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateBodyLifecyclePolicy:
        return ManagementInstanceSandboxMachinesCreateBodyLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateBodyLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateBodyRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateBodyRuntime:
        return ManagementInstanceSandboxMachinesCreateBodyRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateBodyRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateBodyMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateBodyMounts:
        return ManagementInstanceSandboxMachinesCreateBodyMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateBodyMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesCreateBody:
        return ManagementInstanceSandboxMachinesCreateBody(
        region=data.get('region'),
        metadata=data.get('metadata'),
        name=data.get('name'),
        image_id=data.get('image_id'),
        spec_id=data.get('spec_id'),
        spec_identifier=data.get('spec_identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus'),
        lifecycle_policy=mapManagementInstanceSandboxMachinesCreateBodyLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapManagementInstanceSandboxMachinesCreateBodyRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=data.get('lifecycle_hooks', []),
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        mounts=[mapManagementInstanceSandboxMachinesCreateBodyMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        start=data.get('start')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

