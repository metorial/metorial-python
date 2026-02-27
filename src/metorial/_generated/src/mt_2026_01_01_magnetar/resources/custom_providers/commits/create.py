from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersCommitsCreateOutputError:
    code: str
    message: str
@dataclass
class CustomProvidersCommitsCreateOutputToEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor
    commit: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit
    repository: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputTargetCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment
    environments: List[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: CustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor
    commit: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit
    repository: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputPreviousCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment
    environments: List[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsCreateOutputScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsCreateOutputScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsCreateOutputScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutputScmPush:
    object: str
    id: str
    actor: CustomProvidersCommitsCreateOutputScmPushActor
    commit: CustomProvidersCommitsCreateOutputScmPushCommit
    repository: CustomProvidersCommitsCreateOutputScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersCommitsCreateOutput:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    to_environment: CustomProvidersCommitsCreateOutputToEnvironment
    target_custom_provider_version: CustomProvidersCommitsCreateOutputTargetCustomProviderVersion
    actor: CustomProvidersCommitsCreateOutputActor
    created_at: datetime
    error: Optional[CustomProvidersCommitsCreateOutputError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    from_environment: Optional[CustomProvidersCommitsCreateOutputFromEnvironment] = None
    previous_custom_provider_version: Optional[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersion] = None
    scm_push: Optional[CustomProvidersCommitsCreateOutputScmPush] = None
    applied_at: Optional[datetime] = None


class mapCustomProvidersCommitsCreateOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputError:
        return CustomProvidersCommitsCreateOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputToEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputToEnvironment:
        return CustomProvidersCommitsCreateOutputToEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputToEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputFromEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputFromEnvironment:
        return CustomProvidersCommitsCreateOutputFromEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputTargetCustomProviderVersion:
        return CustomProvidersCommitsCreateOutputTargetCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputPreviousCustomProviderVersion:
        return CustomProvidersCommitsCreateOutputPreviousCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputPreviousCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputActor:
        return CustomProvidersCommitsCreateOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputScmPushActor:
        return CustomProvidersCommitsCreateOutputScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputScmPushCommit:
        return CustomProvidersCommitsCreateOutputScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputScmPushRepositoryProvider:
        return CustomProvidersCommitsCreateOutputScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputScmPushRepository:
        return CustomProvidersCommitsCreateOutputScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsCreateOutputScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutputScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutputScmPush:
        return CustomProvidersCommitsCreateOutputScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersCommitsCreateOutputScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersCommitsCreateOutputScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersCommitsCreateOutputScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutputScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateOutput:
        return CustomProvidersCommitsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        error=mapCustomProvidersCommitsCreateOutputError.from_dict(data.get('error')) if data.get('error') else None,
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        to_environment=mapCustomProvidersCommitsCreateOutputToEnvironment.from_dict(data.get('to_environment')) if data.get('to_environment') else None,
        from_environment=mapCustomProvidersCommitsCreateOutputFromEnvironment.from_dict(data.get('from_environment')) if data.get('from_environment') else None,
        target_custom_provider_version=mapCustomProvidersCommitsCreateOutputTargetCustomProviderVersion.from_dict(data.get('target_custom_provider_version')) if data.get('target_custom_provider_version') else None,
        previous_custom_provider_version=mapCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion.from_dict(data.get('previous_custom_provider_version')) if data.get('previous_custom_provider_version') else None,
        actor=mapCustomProvidersCommitsCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersCommitsCreateOutputScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at')) if data.get('applied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersCommitsCreateBody:
    message: str
    action: Dict[str, Any]


class mapCustomProvidersCommitsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsCreateBody:
        return CustomProvidersCommitsCreateBody(
        message=data.get('message'),
        action=data.get('action')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
