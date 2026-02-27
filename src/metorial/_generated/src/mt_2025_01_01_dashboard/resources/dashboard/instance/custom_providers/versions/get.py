from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor
    commit: DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit
    repository: DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit] = None
    immutable_bucket: Optional[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket] = None
    scm_push: Optional[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPush] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsGetOutput:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: DashboardInstanceCustomProvidersVersionsGetOutputDeployment
    environments: List[DashboardInstanceCustomProvidersVersionsGetOutputEnvironments]
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersVersionsGetOutputActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None


class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPush:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputDeployment:
        return DashboardInstanceCustomProvidersVersionsGetOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersVersionsGetOutputDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputEnvironments:
        return DashboardInstanceCustomProvidersVersionsGetOutputEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutputActor:
        return DashboardInstanceCustomProvidersVersionsGetOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetOutput:
        return DashboardInstanceCustomProvidersVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersVersionsGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersVersionsGetOutputEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersVersionsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
