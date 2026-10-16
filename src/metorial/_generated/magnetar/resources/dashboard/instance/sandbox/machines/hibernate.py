from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputImage:
    id: Optional[str] = None
    name: Optional[str] = None
    identifier: Optional[str] = None
    version_id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputSpec:
    identifier: str
    memory_gib: float
    cpus: float
    id: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputMaxBoost:
    memory_gib: float
    cpus: float
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputRootDisk:
    id: str
    size_bytes: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputMounts:
    disk_id: str
    mount_path: str
    state: str
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputLifecyclePolicy:
    pause_after_idle_seconds: Optional[float] = None
    hibernate_after_paused_seconds: Optional[float] = None
    connection_idle_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputRuntime:
    setup: Optional[List[str]] = None
    entrypoint: Optional[List[str]] = None
    cmd: Optional[List[str]] = None
    env: Optional[Dict[str, str]] = None
    workdir: Optional[str] = None
    user: Optional[str] = None
    stop_signal: Optional[str] = None
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputLifecycleHooks:
    type: str
    on: str
    path: str
    port: Optional[float] = None
    arguments: Optional[List[str]] = None
    wait: Optional[bool] = None
    timeout_seconds: Optional[float] = None
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputOperation:
    id: str
    kind: str
    trigger: str
    requested_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputCurrentInstance:
    id: str
    generation: float
    status: str
    phase: str
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputUpcomingEvents:
    type: str
    occurs_at: datetime
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutputFailure:
    code: str
    message: str
@dataclass
class DashboardInstanceSandboxMachinesHibernateOutput:
    object: str
    metadata: Dict[str, Any]
    id: str
    status: str
    region: str
    image: DashboardInstanceSandboxMachinesHibernateOutputImage
    mounts: List[DashboardInstanceSandboxMachinesHibernateOutputMounts]
    firewall_ids: List[str]
    public_ports: List[float]
    lifecycle_policy: DashboardInstanceSandboxMachinesHibernateOutputLifecyclePolicy
    lifecycle_hooks: List[DashboardInstanceSandboxMachinesHibernateOutputLifecycleHooks]
    ignore_image_hooks: bool
    restart_required: bool
    upcoming_events: List[DashboardInstanceSandboxMachinesHibernateOutputUpcomingEvents]
    created_at: datetime
    name: Optional[str] = None
    slug: Optional[str] = None
    spec: Optional[DashboardInstanceSandboxMachinesHibernateOutputSpec] = None
    max_boost: Optional[DashboardInstanceSandboxMachinesHibernateOutputMaxBoost] = None
    root_disk: Optional[DashboardInstanceSandboxMachinesHibernateOutputRootDisk] = None
    runtime: Optional[DashboardInstanceSandboxMachinesHibernateOutputRuntime] = None
    entrypoint_wait_seconds: Optional[float] = None
    operation: Optional[DashboardInstanceSandboxMachinesHibernateOutputOperation] = None
    current_instance: Optional[DashboardInstanceSandboxMachinesHibernateOutputCurrentInstance] = None
    last_activity_at: Optional[datetime] = None
    pause_at: Optional[datetime] = None
    hibernates_at: Optional[datetime] = None
    failure: Optional[DashboardInstanceSandboxMachinesHibernateOutputFailure] = None
    running_at: Optional[datetime] = None
    paused_at: Optional[datetime] = None
    hibernated_at: Optional[datetime] = None
    terminated_at: Optional[datetime] = None


class mapDashboardInstanceSandboxMachinesHibernateOutputImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputImage:
        return DashboardInstanceSandboxMachinesHibernateOutputImage(
        id=data.get('id'),
        name=data.get('name'),
        identifier=data.get('identifier'),
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputSpec:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputSpec:
        return DashboardInstanceSandboxMachinesHibernateOutputSpec(
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputSpec, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputMaxBoost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputMaxBoost:
        return DashboardInstanceSandboxMachinesHibernateOutputMaxBoost(
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputMaxBoost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputRootDisk:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputRootDisk:
        return DashboardInstanceSandboxMachinesHibernateOutputRootDisk(
        id=data.get('id'),
        size_bytes=data.get('size_bytes')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputRootDisk, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputMounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputMounts:
        return DashboardInstanceSandboxMachinesHibernateOutputMounts(
        disk_id=data.get('disk_id'),
        mount_path=data.get('mount_path'),
        state=data.get('state')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputMounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputLifecyclePolicy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputLifecyclePolicy:
        return DashboardInstanceSandboxMachinesHibernateOutputLifecyclePolicy(
        pause_after_idle_seconds=data.get('pause_after_idle_seconds'),
        hibernate_after_paused_seconds=data.get('hibernate_after_paused_seconds'),
        connection_idle_seconds=data.get('connection_idle_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputLifecyclePolicy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputRuntime:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputRuntime:
        return DashboardInstanceSandboxMachinesHibernateOutputRuntime(
        setup=data.get('setup', []),
        entrypoint=data.get('entrypoint', []),
        cmd=data.get('cmd', []),
        env=data.get('env'),
        workdir=data.get('workdir'),
        user=data.get('user'),
        stop_signal=data.get('stop_signal')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputRuntime, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputLifecycleHooks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputLifecycleHooks:
        return DashboardInstanceSandboxMachinesHibernateOutputLifecycleHooks(
        type=data.get('type'),
        on=data.get('on'),
        port=data.get('port'),
        path=data.get('path'),
        arguments=data.get('arguments', []),
        wait=data.get('wait'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputLifecycleHooks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputOperation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputOperation:
        return DashboardInstanceSandboxMachinesHibernateOutputOperation(
        id=data.get('id'),
        kind=data.get('kind'),
        trigger=data.get('trigger'),
        requested_at=datetime.fromisoformat(data.get('requested_at').replace('Z', '+00:00')) if data.get('requested_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputOperation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputCurrentInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputCurrentInstance:
        return DashboardInstanceSandboxMachinesHibernateOutputCurrentInstance(
        id=data.get('id'),
        generation=data.get('generation'),
        status=data.get('status'),
        phase=data.get('phase')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputCurrentInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputUpcomingEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputUpcomingEvents:
        return DashboardInstanceSandboxMachinesHibernateOutputUpcomingEvents(
        type=data.get('type'),
        occurs_at=datetime.fromisoformat(data.get('occurs_at').replace('Z', '+00:00')) if data.get('occurs_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputUpcomingEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutputFailure:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutputFailure:
        return DashboardInstanceSandboxMachinesHibernateOutputFailure(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutputFailure, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxMachinesHibernateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesHibernateOutput:
        return DashboardInstanceSandboxMachinesHibernateOutput(
        object=data.get('object'),
        metadata=data.get('metadata'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        slug=data.get('slug'),
        region=data.get('region'),
        image=mapDashboardInstanceSandboxMachinesHibernateOutputImage.from_dict(data.get('image')) if data.get('image') else None,
        spec=mapDashboardInstanceSandboxMachinesHibernateOutputSpec.from_dict(data.get('spec')) if data.get('spec') else None,
        max_boost=mapDashboardInstanceSandboxMachinesHibernateOutputMaxBoost.from_dict(data.get('max_boost')) if data.get('max_boost') else None,
        root_disk=mapDashboardInstanceSandboxMachinesHibernateOutputRootDisk.from_dict(data.get('root_disk')) if data.get('root_disk') else None,
        mounts=[mapDashboardInstanceSandboxMachinesHibernateOutputMounts.from_dict(item) for item in data.get('mounts', []) if item],
        firewall_ids=data.get('firewall_ids', []),
        public_ports=data.get('public_ports', []),
        lifecycle_policy=mapDashboardInstanceSandboxMachinesHibernateOutputLifecyclePolicy.from_dict(data.get('lifecycle_policy')) if data.get('lifecycle_policy') else None,
        runtime=mapDashboardInstanceSandboxMachinesHibernateOutputRuntime.from_dict(data.get('runtime')) if data.get('runtime') else None,
        lifecycle_hooks=[mapDashboardInstanceSandboxMachinesHibernateOutputLifecycleHooks.from_dict(item) for item in data.get('lifecycle_hooks', []) if item],
        ignore_image_hooks=data.get('ignore_image_hooks'),
        entrypoint_wait_seconds=data.get('entrypoint_wait_seconds'),
        operation=mapDashboardInstanceSandboxMachinesHibernateOutputOperation.from_dict(data.get('operation')) if data.get('operation') else None,
        current_instance=mapDashboardInstanceSandboxMachinesHibernateOutputCurrentInstance.from_dict(data.get('current_instance')) if data.get('current_instance') else None,
        restart_required=data.get('restart_required'),
        last_activity_at=datetime.fromisoformat(data.get('last_activity_at').replace('Z', '+00:00')) if data.get('last_activity_at') else None,
        pause_at=datetime.fromisoformat(data.get('pause_at').replace('Z', '+00:00')) if data.get('pause_at') else None,
        hibernates_at=datetime.fromisoformat(data.get('hibernates_at').replace('Z', '+00:00')) if data.get('hibernates_at') else None,
        upcoming_events=[mapDashboardInstanceSandboxMachinesHibernateOutputUpcomingEvents.from_dict(item) for item in data.get('upcoming_events', []) if item],
        failure=mapDashboardInstanceSandboxMachinesHibernateOutputFailure.from_dict(data.get('failure')) if data.get('failure') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        running_at=datetime.fromisoformat(data.get('running_at').replace('Z', '+00:00')) if data.get('running_at') else None,
        paused_at=datetime.fromisoformat(data.get('paused_at').replace('Z', '+00:00')) if data.get('paused_at') else None,
        hibernated_at=datetime.fromisoformat(data.get('hibernated_at').replace('Z', '+00:00')) if data.get('hibernated_at') else None,
        terminated_at=datetime.fromisoformat(data.get('terminated_at').replace('Z', '+00:00')) if data.get('terminated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesHibernateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

