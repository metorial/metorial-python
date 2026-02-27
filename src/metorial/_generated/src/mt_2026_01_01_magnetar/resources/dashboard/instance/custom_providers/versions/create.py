from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushActor
    commit: DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushCommit
    repository: DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit] = None
    immutable_bucket: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucket] = None
    scm_push: Optional[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPush] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateOutput:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: DashboardInstanceCustomProvidersVersionsCreateOutputDeployment
    environments: List[DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments]
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersVersionsCreateOutputActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None


class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepository:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLink:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucket:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushActor:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushCommit:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepository:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPush:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputDeployment:
        return DashboardInstanceCustomProvidersVersionsCreateOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments:
        return DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutputActor:
        return DashboardInstanceCustomProvidersVersionsCreateOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateOutput:
        return DashboardInstanceCustomProvidersVersionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersVersionsCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersVersionsCreateOutputEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersVersionsCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersVersionsCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersVersionsCreateBody:
    custom_provider_id: str
    from_: Dict[str, Any]
    config: Optional[DashboardInstanceCustomProvidersVersionsCreateBodyConfig] = None


class mapDashboardInstanceCustomProvidersVersionsCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateBodyConfig:
        return DashboardInstanceCustomProvidersVersionsCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersVersionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsCreateBody:
        return DashboardInstanceCustomProvidersVersionsCreateBody(
        custom_provider_id=data.get('custom_provider_id'),
        from_=data.get('from'),
        config=mapDashboardInstanceCustomProvidersVersionsCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
