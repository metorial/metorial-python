from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsError:
    code: str
    message: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsToEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig:
    object: str
    schema: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor
    commit: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit
    repository: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment
    environments: List[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig:
    object: str
    schema: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor
    commit: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit
    repository: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment
    environments: List[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItemsScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushActor
    commit: DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushCommit
    repository: DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputItems:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    to_environment: DashboardInstanceCustomProvidersCommitsListOutputItemsToEnvironment
    target_custom_provider_version: DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion
    actor: DashboardInstanceCustomProvidersCommitsListOutputItemsActor
    created_at: datetime
    error: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    from_environment: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsFromEnvironment] = None
    previous_custom_provider_version: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion] = None
    scm_push: Optional[DashboardInstanceCustomProvidersCommitsListOutputItemsScmPush] = None
    applied_at: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCustomProvidersCommitsListOutput:
    items: List[DashboardInstanceCustomProvidersCommitsListOutputItems]
    pagination: DashboardInstanceCustomProvidersCommitsListOutputPagination


class mapDashboardInstanceCustomProvidersCommitsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsError:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsToEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsToEnvironment:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsToEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsToEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsFromEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsFromEnvironment:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsFromEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushActor:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushCommit:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepository:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItemsScmPush:
        return DashboardInstanceCustomProvidersCommitsListOutputItemsScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItemsScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputItems:
        return DashboardInstanceCustomProvidersCommitsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        error=mapDashboardInstanceCustomProvidersCommitsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        to_environment=mapDashboardInstanceCustomProvidersCommitsListOutputItemsToEnvironment.from_dict(data.get('to_environment')) if data.get('to_environment') else None,
        from_environment=mapDashboardInstanceCustomProvidersCommitsListOutputItemsFromEnvironment.from_dict(data.get('from_environment')) if data.get('from_environment') else None,
        target_custom_provider_version=mapDashboardInstanceCustomProvidersCommitsListOutputItemsTargetCustomProviderVersion.from_dict(data.get('target_custom_provider_version')) if data.get('target_custom_provider_version') else None,
        previous_custom_provider_version=mapDashboardInstanceCustomProvidersCommitsListOutputItemsPreviousCustomProviderVersion.from_dict(data.get('previous_custom_provider_version')) if data.get('previous_custom_provider_version') else None,
        actor=mapDashboardInstanceCustomProvidersCommitsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersCommitsListOutputItemsScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutputPagination:
        return DashboardInstanceCustomProvidersCommitsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListOutput:
        return DashboardInstanceCustomProvidersCommitsListOutput(
        items=[mapDashboardInstanceCustomProvidersCommitsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCustomProvidersCommitsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersCommitsListQuery:
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


class mapDashboardInstanceCustomProvidersCommitsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsListQuery:
        return DashboardInstanceCustomProvidersCommitsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        custom_provider_environment_id=data.get('custom_provider_environment_id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

