from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersVersionsListOutputItemsConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersVersionsListOutputItemsConfig:
    object: str
    schema: CustomProvidersVersionsListOutputItemsConfigSchema
    transformer: str
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentScmPushRepository:
    object: str
    id: str
    provider: CustomProvidersVersionsListOutputItemsDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersVersionsListOutputItemsDeploymentScmPush:
    object: str
    id: str
    actor: CustomProvidersVersionsListOutputItemsDeploymentScmPushActor
    commit: CustomProvidersVersionsListOutputItemsDeploymentScmPushCommit
    repository: CustomProvidersVersionsListOutputItemsDeploymentScmPushRepository
    created_at: datetime
@dataclass
class CustomProvidersVersionsListOutputItemsDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: CustomProvidersVersionsListOutputItemsDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[CustomProvidersVersionsListOutputItemsDeploymentCommit] = None
    immutable_bucket: Optional[CustomProvidersVersionsListOutputItemsDeploymentImmutableBucket] = None
    scm_push: Optional[CustomProvidersVersionsListOutputItemsDeploymentScmPush] = None
@dataclass
class CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment
@dataclass
class CustomProvidersVersionsListOutputItemsActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class CustomProvidersVersionsListOutputItemsContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersVersionsListOutputItemsRemoteMcpServer:
    url: str
    transport: str
@dataclass
class CustomProvidersVersionsListOutputItems:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: CustomProvidersVersionsListOutputItemsDeployment
    environments: List[CustomProvidersVersionsListOutputItemsEnvironments]
    custom_provider_id: str
    actor: CustomProvidersVersionsListOutputItemsActor
    created_at: datetime
    updated_at: datetime
    config: Optional[CustomProvidersVersionsListOutputItemsConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[CustomProvidersVersionsListOutputItemsContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersVersionsListOutputItemsRemoteMcpServer] = None
@dataclass
class CustomProvidersVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CustomProvidersVersionsListOutput:
    items: List[CustomProvidersVersionsListOutputItems]
    pagination: CustomProvidersVersionsListOutputPagination


class mapCustomProvidersVersionsListOutputItemsConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsConfigSchema:
        return CustomProvidersVersionsListOutputItemsConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsConfig:
        return CustomProvidersVersionsListOutputItemsConfig(
        object=data.get('object'),
        schema=mapCustomProvidersVersionsListOutputItemsConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentCommit:
        return CustomProvidersVersionsListOutputItemsDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepository:
        return CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLink:
        return CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentImmutableBucket:
        return CustomProvidersVersionsListOutputItemsDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentActor:
        return CustomProvidersVersionsListOutputItemsDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentScmPushActor:
        return CustomProvidersVersionsListOutputItemsDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentScmPushCommit:
        return CustomProvidersVersionsListOutputItemsDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentScmPushRepositoryProvider:
        return CustomProvidersVersionsListOutputItemsDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentScmPushRepository:
        return CustomProvidersVersionsListOutputItemsDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersVersionsListOutputItemsDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeploymentScmPush:
        return CustomProvidersVersionsListOutputItemsDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapCustomProvidersVersionsListOutputItemsDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapCustomProvidersVersionsListOutputItemsDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapCustomProvidersVersionsListOutputItemsDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsDeployment:
        return CustomProvidersVersionsListOutputItemsDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapCustomProvidersVersionsListOutputItemsDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapCustomProvidersVersionsListOutputItemsDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapCustomProvidersVersionsListOutputItemsDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapCustomProvidersVersionsListOutputItemsDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment:
        return CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment(
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
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsEnvironments:
        return CustomProvidersVersionsListOutputItemsEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapCustomProvidersVersionsListOutputItemsEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsActor:
        return CustomProvidersVersionsListOutputItemsActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsContainerImage:
        return CustomProvidersVersionsListOutputItemsContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItemsRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItemsRemoteMcpServer:
        return CustomProvidersVersionsListOutputItemsRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItemsRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputItems:
        return CustomProvidersVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapCustomProvidersVersionsListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapCustomProvidersVersionsListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapCustomProvidersVersionsListOutputItemsEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapCustomProvidersVersionsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapCustomProvidersVersionsListOutputItemsContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapCustomProvidersVersionsListOutputItemsRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutputPagination:
        return CustomProvidersVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListOutput:
        return CustomProvidersVersionsListOutput(
        items=[mapCustomProvidersVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCustomProvidersVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersVersionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersVersionsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_version_id: Optional[Union[str, List[str]]] = None
    custom_provider_id: Optional[Union[str, List[str]]] = None
    custom_provider_deployment_id: Optional[Union[str, List[str]]] = None
    custom_provider_environment_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[CustomProvidersVersionsListQueryCreatedAt] = None
    updated_at: Optional[CustomProvidersVersionsListQueryUpdatedAt] = None


class mapCustomProvidersVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersVersionsListQuery:
        return CustomProvidersVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        custom_provider_id=data.get('custom_provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        custom_provider_environment_id=data.get('custom_provider_environment_id'),
        created_at=mapCustomProvidersVersionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCustomProvidersVersionsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

