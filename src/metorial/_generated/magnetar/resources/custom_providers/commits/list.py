from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersCommitsListOutputItemsError:
    code: str
    message: str
@dataclass
class CustomProvidersCommitsListOutputItemsToEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit] = None
    actor: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    environment: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
    object: str
    id: str
    environments: List[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit] = None
    actor: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
    instance_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    environment: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment
    is_current_version_for_environment: Optional[bool] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
    object: str
    id: str
    environments: List[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    index: Optional[float] = None
    identifier: Optional[str] = None
    deployment: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment] = None
    provider_id: Optional[str] = None
    actor: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor] = None
@dataclass
class CustomProvidersCommitsListOutputItemsActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItems:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    error: Optional[CustomProvidersCommitsListOutputItemsError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    to_environment: Optional[CustomProvidersCommitsListOutputItemsToEnvironment] = None
    from_environment: Optional[CustomProvidersCommitsListOutputItemsFromEnvironment] = None
    target_custom_provider_version: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion] = None
    previous_custom_provider_version: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion] = None
    actor: Optional[CustomProvidersCommitsListOutputItemsActor] = None
    applied_at: Optional[datetime] = None
@dataclass
class CustomProvidersCommitsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CustomProvidersCommitsListOutput:
    items: List[CustomProvidersCommitsListOutputItems]
    pagination: CustomProvidersCommitsListOutputPagination


class mapCustomProvidersCommitsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsError:
        return CustomProvidersCommitsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsToEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsToEnvironment:
        return CustomProvidersCommitsListOutputItemsToEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsToEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsFromEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsFromEnvironment:
        return CustomProvidersCommitsListOutputItemsFromEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsActor:
        return CustomProvidersCommitsListOutputItemsActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItems:
        return CustomProvidersCommitsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        error=mapCustomProvidersCommitsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        to_environment=mapCustomProvidersCommitsListOutputItemsToEnvironment.from_dict(data.get('to_environment')) if data.get('to_environment') else None,
        from_environment=mapCustomProvidersCommitsListOutputItemsFromEnvironment.from_dict(data.get('from_environment')) if data.get('from_environment') else None,
        target_custom_provider_version=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion.from_dict(data.get('target_custom_provider_version')) if data.get('target_custom_provider_version') else None,
        previous_custom_provider_version=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion.from_dict(data.get('previous_custom_provider_version')) if data.get('previous_custom_provider_version') else None,
        actor=mapCustomProvidersCommitsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at')) if data.get('applied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputPagination:
        return CustomProvidersCommitsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutput:
        return CustomProvidersCommitsListOutput(
        items=[mapCustomProvidersCommitsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCustomProvidersCommitsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersCommitsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    ids: Optional[Union[str, List[str]]] = None
    custom_provider_version_ids: Optional[Union[str, List[str]]] = None
    custom_provider_environment_ids: Optional[Union[str, List[str]]] = None


class mapCustomProvidersCommitsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListQuery:
        return CustomProvidersCommitsListQuery(
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
    def to_dict(value: Union[CustomProvidersCommitsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
