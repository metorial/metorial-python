from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesPauseOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class SandboxMachinesPauseOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class SandboxMachinesPauseOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class SandboxMachinesPauseOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class SandboxMachinesPauseOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class SandboxMachinesPauseOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class SandboxMachinesPauseOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class SandboxMachinesPauseOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class SandboxMachinesPauseOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class SandboxMachinesPauseOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class SandboxMachinesPauseOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class SandboxMachinesPauseOutputFailure:
    code: str
    message: str
@dataclass
class SandboxMachinesPauseOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: SandboxMachinesPauseOutputImage
    mounts: List[SandboxMachinesPauseOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: SandboxMachinesPauseOutputLifecyclePolicy
    lifecycle_hooks: List[SandboxMachinesPauseOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[SandboxMachinesPauseOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[SandboxMachinesPauseOutputSpec] = None
    max_boost: Optional[SandboxMachinesPauseOutputMaxBoost] = None
    root_disk: Optional[SandboxMachinesPauseOutputRootDisk] = None
    runtime: Optional[SandboxMachinesPauseOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[SandboxMachinesPauseOutputOperation] = None
    current_instance: Optional[SandboxMachinesPauseOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[SandboxMachinesPauseOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapSandboxMachinesPauseOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputImage:
        return SandboxMachinesPauseOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputSpec:
        return SandboxMachinesPauseOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputMaxBoost:
        return SandboxMachinesPauseOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputRootDisk:
        return SandboxMachinesPauseOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputMounts:
        return SandboxMachinesPauseOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputLifecyclePolicy:
        return SandboxMachinesPauseOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputRuntime:
        return SandboxMachinesPauseOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputLifecycleHooks:
        return SandboxMachinesPauseOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputOperation:
        return SandboxMachinesPauseOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputCurrentInstance:
        return SandboxMachinesPauseOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputUpcomingEvents:
        return SandboxMachinesPauseOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutputFailure:
        return SandboxMachinesPauseOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesPauseOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesPauseOutput:
        return SandboxMachinesPauseOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapSandboxMachinesPauseOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapSandboxMachinesPauseOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapSandboxMachinesPauseOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapSandboxMachinesPauseOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapSandboxMachinesPauseOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapSandboxMachinesPauseOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapSandboxMachinesPauseOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapSandboxMachinesPauseOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapSandboxMachinesPauseOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapSandboxMachinesPauseOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapSandboxMachinesPauseOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapSandboxMachinesPauseOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesPauseOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

