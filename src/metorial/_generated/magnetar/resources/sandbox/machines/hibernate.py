from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesHibernateOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class SandboxMachinesHibernateOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class SandboxMachinesHibernateOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class SandboxMachinesHibernateOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class SandboxMachinesHibernateOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class SandboxMachinesHibernateOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class SandboxMachinesHibernateOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class SandboxMachinesHibernateOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class SandboxMachinesHibernateOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class SandboxMachinesHibernateOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class SandboxMachinesHibernateOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class SandboxMachinesHibernateOutputFailure:
    code: str
    message: str
@dataclass
class SandboxMachinesHibernateOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: SandboxMachinesHibernateOutputImage
    mounts: List[SandboxMachinesHibernateOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: SandboxMachinesHibernateOutputLifecyclePolicy
    lifecycle_hooks: List[SandboxMachinesHibernateOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[SandboxMachinesHibernateOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[SandboxMachinesHibernateOutputSpec] = None
    max_boost: Optional[SandboxMachinesHibernateOutputMaxBoost] = None
    root_disk: Optional[SandboxMachinesHibernateOutputRootDisk] = None
    runtime: Optional[SandboxMachinesHibernateOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[SandboxMachinesHibernateOutputOperation] = None
    current_instance: Optional[SandboxMachinesHibernateOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[SandboxMachinesHibernateOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapSandboxMachinesHibernateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputImage:
        return SandboxMachinesHibernateOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputSpec:
        return SandboxMachinesHibernateOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputMaxBoost:
        return SandboxMachinesHibernateOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputRootDisk:
        return SandboxMachinesHibernateOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputMounts:
        return SandboxMachinesHibernateOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputLifecyclePolicy:
        return SandboxMachinesHibernateOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputRuntime:
        return SandboxMachinesHibernateOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputLifecycleHooks:
        return SandboxMachinesHibernateOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputOperation:
        return SandboxMachinesHibernateOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputCurrentInstance:
        return SandboxMachinesHibernateOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputUpcomingEvents:
        return SandboxMachinesHibernateOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutputFailure:
        return SandboxMachinesHibernateOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesHibernateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesHibernateOutput:
        return SandboxMachinesHibernateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapSandboxMachinesHibernateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapSandboxMachinesHibernateOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapSandboxMachinesHibernateOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapSandboxMachinesHibernateOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapSandboxMachinesHibernateOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapSandboxMachinesHibernateOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapSandboxMachinesHibernateOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapSandboxMachinesHibernateOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapSandboxMachinesHibernateOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapSandboxMachinesHibernateOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapSandboxMachinesHibernateOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapSandboxMachinesHibernateOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesHibernateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

