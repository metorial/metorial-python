from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor
    commit: ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit
    repository: ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersVersionsGetOutputDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentCommit] = None
    immutable_bucket: Optional[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket] = None
    scm_push: Optional[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPush] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: ManagementInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersVersionsGetOutput:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: ManagementInstanceCustomProvidersVersionsGetOutputDeployment
    environments: List[ManagementInstanceCustomProvidersVersionsGetOutputEnvironments]
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersVersionsGetOutputActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None


class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentCommit:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentActor:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPush:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputDeployment:
        return ManagementInstanceCustomProvidersVersionsGetOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersVersionsGetOutputDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputEnvironments:
        return ManagementInstanceCustomProvidersVersionsGetOutputEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersVersionsGetOutputEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutputActor:
        return ManagementInstanceCustomProvidersVersionsGetOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersVersionsGetOutput:
        return ManagementInstanceCustomProvidersVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersVersionsGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersVersionsGetOutputEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersVersionsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
