from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutputFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesUpdateOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: ManagementInstanceSandboxMachinesUpdateOutputImage
    mounts: List[ManagementInstanceSandboxMachinesUpdateOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: ManagementInstanceSandboxMachinesUpdateOutputLifecyclePolicy
    lifecycle_hooks: List[ManagementInstanceSandboxMachinesUpdateOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[ManagementInstanceSandboxMachinesUpdateOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[ManagementInstanceSandboxMachinesUpdateOutputSpec] = None
    max_boost: Optional[ManagementInstanceSandboxMachinesUpdateOutputMaxBoost] = None
    root_disk: Optional[ManagementInstanceSandboxMachinesUpdateOutputRootDisk] = None
    runtime: Optional[ManagementInstanceSandboxMachinesUpdateOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[ManagementInstanceSandboxMachinesUpdateOutputOperation] = None
    current_instance: Optional[ManagementInstanceSandboxMachinesUpdateOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[ManagementInstanceSandboxMachinesUpdateOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapManagementInstanceSandboxMachinesUpdateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputImage:
        return ManagementInstanceSandboxMachinesUpdateOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputSpec:
        return ManagementInstanceSandboxMachinesUpdateOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputMaxBoost:
        return ManagementInstanceSandboxMachinesUpdateOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputRootDisk:
        return ManagementInstanceSandboxMachinesUpdateOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputMounts:
        return ManagementInstanceSandboxMachinesUpdateOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputLifecyclePolicy:
        return ManagementInstanceSandboxMachinesUpdateOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputRuntime:
        return ManagementInstanceSandboxMachinesUpdateOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputLifecycleHooks:
        return ManagementInstanceSandboxMachinesUpdateOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputOperation:
        return ManagementInstanceSandboxMachinesUpdateOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputCurrentInstance:
        return ManagementInstanceSandboxMachinesUpdateOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputUpcomingEvents:
        return ManagementInstanceSandboxMachinesUpdateOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutputFailure:
        return ManagementInstanceSandboxMachinesUpdateOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateOutput:
        return ManagementInstanceSandboxMachinesUpdateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapManagementInstanceSandboxMachinesUpdateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapManagementInstanceSandboxMachinesUpdateOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapManagementInstanceSandboxMachinesUpdateOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapManagementInstanceSandboxMachinesUpdateOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapManagementInstanceSandboxMachinesUpdateOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapManagementInstanceSandboxMachinesUpdateOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapManagementInstanceSandboxMachinesUpdateOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapManagementInstanceSandboxMachinesUpdateOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapManagementInstanceSandboxMachinesUpdateOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapManagementInstanceSandboxMachinesUpdateOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapManagementInstanceSandboxMachinesUpdateOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapManagementInstanceSandboxMachinesUpdateOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxMachinesUpdateBodyLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateBodyRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesUpdateBodyMounts:
    disk_id: str
    mount_path: str
@dataclass
class ManagementInstanceSandboxMachinesUpdateBody:
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    spec_id: Optional[str] = None
    spec_identifier: Optional[str] = None
    memory_gib: Optional[float] = None
    cpus: Optional[float] = None
    lifecycle_policy: Optional[ManagementInstanceSandboxMachinesUpdateBodyLifecyclePolicy] = None
    runtime: Optional[ManagementInstanceSandboxMachinesUpdateBodyRuntime] = None
    lifecycle_hooks: Optional[List[Dict[str, Any]]] = None
    ignore_image_hooks: Optional[bool] = None
    entrypoint_wait_seconds: Optional[float] = None
    mounts: Optional[List[ManagementInstanceSandboxMachinesUpdateBodyMounts]] = None
    firewall_ids: Optional[List[str]] = None
    public_ports: Optional[List[float]] = None


class mapManagementInstanceSandboxMachinesUpdateBodyLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateBodyLifecyclePolicy:
        return ManagementInstanceSandboxMachinesUpdateBodyLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateBodyLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateBodyRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateBodyRuntime:
        return ManagementInstanceSandboxMachinesUpdateBodyRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateBodyRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateBodyMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateBodyMounts:
        return ManagementInstanceSandboxMachinesUpdateBodyMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateBodyMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesUpdateBody:
        return ManagementInstanceSandboxMachinesUpdateBody(
        metadata=data.get('metadata'),
        name=data.get('name'),
        spec_id=data.get('spec_id'),
        spec_identifier=data.get('spec_identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus'),
        lifecycle_policy=mapManagementInstanceSandboxMachinesUpdateBodyLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapManagementInstanceSandboxMachinesUpdateBodyRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=data.get('lifecycle_hooks', []),
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        mounts=[mapManagementInstanceSandboxMachinesUpdateBodyMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

