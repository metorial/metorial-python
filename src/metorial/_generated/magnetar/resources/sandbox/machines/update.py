from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesUpdateOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class SandboxMachinesUpdateOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class SandboxMachinesUpdateOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class SandboxMachinesUpdateOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class SandboxMachinesUpdateOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class SandboxMachinesUpdateOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class SandboxMachinesUpdateOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class SandboxMachinesUpdateOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class SandboxMachinesUpdateOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class SandboxMachinesUpdateOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class SandboxMachinesUpdateOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class SandboxMachinesUpdateOutputFailure:
    code: str
    message: str
@dataclass
class SandboxMachinesUpdateOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: SandboxMachinesUpdateOutputImage
    mounts: List[SandboxMachinesUpdateOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: SandboxMachinesUpdateOutputLifecyclePolicy
    lifecycle_hooks: List[SandboxMachinesUpdateOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[SandboxMachinesUpdateOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[SandboxMachinesUpdateOutputSpec] = None
    max_boost: Optional[SandboxMachinesUpdateOutputMaxBoost] = None
    root_disk: Optional[SandboxMachinesUpdateOutputRootDisk] = None
    runtime: Optional[SandboxMachinesUpdateOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[SandboxMachinesUpdateOutputOperation] = None
    current_instance: Optional[SandboxMachinesUpdateOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[SandboxMachinesUpdateOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapSandboxMachinesUpdateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputImage:
        return SandboxMachinesUpdateOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputSpec:
        return SandboxMachinesUpdateOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputMaxBoost:
        return SandboxMachinesUpdateOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputRootDisk:
        return SandboxMachinesUpdateOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputMounts:
        return SandboxMachinesUpdateOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputLifecyclePolicy:
        return SandboxMachinesUpdateOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputRuntime:
        return SandboxMachinesUpdateOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputLifecycleHooks:
        return SandboxMachinesUpdateOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputOperation:
        return SandboxMachinesUpdateOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputCurrentInstance:
        return SandboxMachinesUpdateOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputUpcomingEvents:
        return SandboxMachinesUpdateOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutputFailure:
        return SandboxMachinesUpdateOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateOutput:
        return SandboxMachinesUpdateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapSandboxMachinesUpdateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapSandboxMachinesUpdateOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapSandboxMachinesUpdateOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapSandboxMachinesUpdateOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapSandboxMachinesUpdateOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapSandboxMachinesUpdateOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapSandboxMachinesUpdateOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapSandboxMachinesUpdateOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapSandboxMachinesUpdateOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapSandboxMachinesUpdateOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapSandboxMachinesUpdateOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapSandboxMachinesUpdateOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesUpdateBodyLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class SandboxMachinesUpdateBodyRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class SandboxMachinesUpdateBodyMounts:
    disk_id: str
    mount_path: str
@dataclass
class SandboxMachinesUpdateBody:
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[str] = None
    spec_id: Optional[str] = None
    spec_identifier: Optional[str] = None
    memory_gib: Optional[float] = None
    cpus: Optional[float] = None
    lifecycle_policy: Optional[SandboxMachinesUpdateBodyLifecyclePolicy] = None
    runtime: Optional[SandboxMachinesUpdateBodyRuntime] = None
    lifecycle_hooks: Optional[List[Dict[str, Any]]] = None
    ignore_image_hooks: Optional[bool] = None
    entrypoint_wait_seconds: Optional[float] = None
    mounts: Optional[List[SandboxMachinesUpdateBodyMounts]] = None
    firewall_ids: Optional[List[str]] = None
    public_ports: Optional[List[float]] = None


class mapSandboxMachinesUpdateBodyLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateBodyLifecyclePolicy:
        return SandboxMachinesUpdateBodyLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateBodyLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateBodyRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateBodyRuntime:
        return SandboxMachinesUpdateBodyRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateBodyRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateBodyMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateBodyMounts:
        return SandboxMachinesUpdateBodyMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateBodyMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesUpdateBody:
        return SandboxMachinesUpdateBody(
        metadata=data.get('metadata'),
        name=data.get('name'),
        spec_id=data.get('spec_id'),
        spec_identifier=data.get('spec_identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus'),
        lifecycle_policy=mapSandboxMachinesUpdateBodyLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapSandboxMachinesUpdateBodyRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=data.get('lifecycle_hooks', []),
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        mounts=[mapSandboxMachinesUpdateBodyMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', [])
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

