from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsError:
    code: str
    message: str
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsToEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit] = None
    actor: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    environment: ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
    object: str
    id: str
    environments: List[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit] = None
    actor: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    environment: ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
    object: str
    id: str
    environments: List[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItemsActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputItems:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    error: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    to_environment: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsToEnvironment] = None
    from_environment: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsFromEnvironment] = None
    target_custom_provider_version: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion] = None
    previous_custom_provider_version: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion] = None
    actor: Optional[ManagementInstanceCustomProvidersCommitsListOutputItemsActor] = None
    applied_at: Optional[datetime] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCustomProvidersCommitsListOutput:
    items: List[ManagementInstanceCustomProvidersCommitsListOutputItems]
    pagination: ManagementInstanceCustomProvidersCommitsListOutputPagination


class mapManagementInstanceCustomProvidersCommitsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsError:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsToEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsToEnvironment:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsToEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        current_provider_version_id=data.get('current_provider_version_id'),
        instance_id=data.get('instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsToEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsFromEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsFromEnvironment:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsFromEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        current_provider_version_id=data.get('current_provider_version_id'),
        instance_id=data.get('instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        current_provider_version_id=data.get('current_provider_version_id'),
        instance_id=data.get('instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        current_provider_version_id=data.get('current_provider_version_id'),
        instance_id=data.get('instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItemsActor:
        return ManagementInstanceCustomProvidersCommitsListOutputItemsActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputItems:
        return ManagementInstanceCustomProvidersCommitsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        error=mapManagementInstanceCustomProvidersCommitsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        to_environment=mapManagementInstanceCustomProvidersCommitsListOutputItemsToEnvironment.from_dict(data.get('to_environment')) if data.get('to_environment') else None,
        from_environment=mapManagementInstanceCustomProvidersCommitsListOutputItemsFromEnvironment.from_dict(data.get('from_environment')) if data.get('from_environment') else None,
        target_custom_provider_version=mapManagementInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion.from_dict(data.get('target_custom_provider_version')) if data.get('target_custom_provider_version') else None,
        previous_custom_provider_version=mapManagementInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion.from_dict(data.get('previous_custom_provider_version')) if data.get('previous_custom_provider_version') else None,
        actor=mapManagementInstanceCustomProvidersCommitsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at')) if data.get('applied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutputPagination:
        return ManagementInstanceCustomProvidersCommitsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListOutput:
        return ManagementInstanceCustomProvidersCommitsListOutput(
        items=[mapManagementInstanceCustomProvidersCommitsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCustomProvidersCommitsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomProvidersCommitsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    ids: Optional[Union[str, List[str]]] = None
    custom_provider_version_ids: Optional[Union[str, List[str]]] = None
    custom_provider_environment_ids: Optional[Union[str, List[str]]] = None


class mapManagementInstanceCustomProvidersCommitsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsListQuery:
        return ManagementInstanceCustomProvidersCommitsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        ids=data.get('ids'),
        custom_provider_version_ids=data.get('custom_provider_version_ids'),
        custom_provider_environment_ids=data.get('custom_provider_environment_ids')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
