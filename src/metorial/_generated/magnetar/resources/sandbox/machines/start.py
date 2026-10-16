from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesStartOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class SandboxMachinesStartOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class SandboxMachinesStartOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class SandboxMachinesStartOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class SandboxMachinesStartOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class SandboxMachinesStartOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class SandboxMachinesStartOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class SandboxMachinesStartOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class SandboxMachinesStartOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class SandboxMachinesStartOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class SandboxMachinesStartOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class SandboxMachinesStartOutputFailure:
    code: str
    message: str
@dataclass
class SandboxMachinesStartOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: SandboxMachinesStartOutputImage
    mounts: List[SandboxMachinesStartOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: SandboxMachinesStartOutputLifecyclePolicy
    lifecycle_hooks: List[SandboxMachinesStartOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[SandboxMachinesStartOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[SandboxMachinesStartOutputSpec] = None
    max_boost: Optional[SandboxMachinesStartOutputMaxBoost] = None
    root_disk: Optional[SandboxMachinesStartOutputRootDisk] = None
    runtime: Optional[SandboxMachinesStartOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[SandboxMachinesStartOutputOperation] = None
    current_instance: Optional[SandboxMachinesStartOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[SandboxMachinesStartOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapSandboxMachinesStartOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputImage:
        return SandboxMachinesStartOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputSpec:
        return SandboxMachinesStartOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputMaxBoost:
        return SandboxMachinesStartOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputRootDisk:
        return SandboxMachinesStartOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputMounts:
        return SandboxMachinesStartOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputLifecyclePolicy:
        return SandboxMachinesStartOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputRuntime:
        return SandboxMachinesStartOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputLifecycleHooks:
        return SandboxMachinesStartOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputOperation:
        return SandboxMachinesStartOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputCurrentInstance:
        return SandboxMachinesStartOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputUpcomingEvents:
        return SandboxMachinesStartOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutputFailure:
        return SandboxMachinesStartOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesStartOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesStartOutput:
        return SandboxMachinesStartOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapSandboxMachinesStartOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapSandboxMachinesStartOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapSandboxMachinesStartOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapSandboxMachinesStartOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapSandboxMachinesStartOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapSandboxMachinesStartOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapSandboxMachinesStartOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapSandboxMachinesStartOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapSandboxMachinesStartOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapSandboxMachinesStartOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapSandboxMachinesStartOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapSandboxMachinesStartOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesStartOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

