from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutputFailure:
    code: str
    message: str
@dataclass
class ManagementInstanceSandboxMachinesDeleteOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: ManagementInstanceSandboxMachinesDeleteOutputImage
    mounts: List[ManagementInstanceSandboxMachinesDeleteOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: ManagementInstanceSandboxMachinesDeleteOutputLifecyclePolicy
    lifecycle_hooks: List[ManagementInstanceSandboxMachinesDeleteOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[ManagementInstanceSandboxMachinesDeleteOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[ManagementInstanceSandboxMachinesDeleteOutputSpec] = None
    max_boost: Optional[ManagementInstanceSandboxMachinesDeleteOutputMaxBoost] = None
    root_disk: Optional[ManagementInstanceSandboxMachinesDeleteOutputRootDisk] = None
    runtime: Optional[ManagementInstanceSandboxMachinesDeleteOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[ManagementInstanceSandboxMachinesDeleteOutputOperation] = None
    current_instance: Optional[ManagementInstanceSandboxMachinesDeleteOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[ManagementInstanceSandboxMachinesDeleteOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapManagementInstanceSandboxMachinesDeleteOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputImage:
        return ManagementInstanceSandboxMachinesDeleteOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputSpec:
        return ManagementInstanceSandboxMachinesDeleteOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputMaxBoost:
        return ManagementInstanceSandboxMachinesDeleteOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputRootDisk:
        return ManagementInstanceSandboxMachinesDeleteOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputMounts:
        return ManagementInstanceSandboxMachinesDeleteOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputLifecyclePolicy:
        return ManagementInstanceSandboxMachinesDeleteOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputRuntime:
        return ManagementInstanceSandboxMachinesDeleteOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputLifecycleHooks:
        return ManagementInstanceSandboxMachinesDeleteOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputOperation:
        return ManagementInstanceSandboxMachinesDeleteOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputCurrentInstance:
        return ManagementInstanceSandboxMachinesDeleteOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputUpcomingEvents:
        return ManagementInstanceSandboxMachinesDeleteOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutputFailure:
        return ManagementInstanceSandboxMachinesDeleteOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxMachinesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxMachinesDeleteOutput:
        return ManagementInstanceSandboxMachinesDeleteOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapManagementInstanceSandboxMachinesDeleteOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapManagementInstanceSandboxMachinesDeleteOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapManagementInstanceSandboxMachinesDeleteOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapManagementInstanceSandboxMachinesDeleteOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapManagementInstanceSandboxMachinesDeleteOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapManagementInstanceSandboxMachinesDeleteOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapManagementInstanceSandboxMachinesDeleteOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapManagementInstanceSandboxMachinesDeleteOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapManagementInstanceSandboxMachinesDeleteOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapManagementInstanceSandboxMachinesDeleteOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapManagementInstanceSandboxMachinesDeleteOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapManagementInstanceSandboxMachinesDeleteOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxMachinesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

