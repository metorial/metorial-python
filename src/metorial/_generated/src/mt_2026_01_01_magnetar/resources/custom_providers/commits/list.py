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
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig:
    object: str
    schema: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor
    commit: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit
    repository: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment
    environments: List[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig:
    object: str
    schema: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor
    commit: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit
    repository: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment
    environments: List[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer] = None
@dataclass
class CustomProvidersCommitsListOutputItemsActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersCommitsListOutputItemsScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCommitsListOutputItemsScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersCommitsListOutputItemsScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItemsScmPush:
    object: str
    id: str
    actor: CustomProvidersCommitsListOutputItemsScmPushActor
    commit: CustomProvidersCommitsListOutputItemsScmPushCommit
    repository: CustomProvidersCommitsListOutputItemsScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersCommitsListOutputItems:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    to_environment: CustomProvidersCommitsListOutputItemsToEnvironment
    target_custom_provider_version: CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion
    actor: CustomProvidersCommitsListOutputItemsActor
    created_at: datetime
    error: Optional[CustomProvidersCommitsListOutputItemsError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    from_environment: Optional[CustomProvidersCommitsListOutputItemsFromEnvironment] = None
    previous_custom_provider_version: Optional[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion] = None
    scm_push: Optional[CustomProvidersCommitsListOutputItemsScmPush] = None
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
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        immutable_bucket=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer:
        return CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        config=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        immutable_bucket=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer:
        return CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        config=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsScmPushActor:
        return CustomProvidersCommitsListOutputItemsScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsScmPushCommit:
        return CustomProvidersCommitsListOutputItemsScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsScmPushRepositoryProvider:
        return CustomProvidersCommitsListOutputItemsScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsScmPushRepository:
        return CustomProvidersCommitsListOutputItemsScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCommitsListOutputItemsScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListOutputItemsScmPush:
        return CustomProvidersCommitsListOutputItemsScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersCommitsListOutputItemsScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersCommitsListOutputItemsScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersCommitsListOutputItemsScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListOutputItemsScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        scm_push=mapCustomProvidersCommitsListOutputItemsScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None
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
class CustomProvidersCommitsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersCommitsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersCommitsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    custom_provider_version_id: Optional[Union[str, List[str]]] = None
    custom_provider_environment_id: Optional[Union[str, List[str]]] = None
    custom_provider_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[CustomProvidersCommitsListQueryCreatedAt] = None
    updated_at: Optional[CustomProvidersCommitsListQueryUpdatedAt] = None


class mapCustomProvidersCommitsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCommitsListQuery:
        return CustomProvidersCommitsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        custom_provider_environment_id=data.get('custom_provider_environment_id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        created_at=mapCustomProvidersCommitsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCustomProvidersCommitsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCommitsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

