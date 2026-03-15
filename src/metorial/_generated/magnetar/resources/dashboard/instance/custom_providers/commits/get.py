from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputError:
    code: str
    message: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputToEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig:
    object: str
    schema: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor
    commit: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit
    repository: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment
    environments: List[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig:
    object: str
    schema: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor
    commit: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit
    repository: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment
    environments: List[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutputScmPush:
    object: str
    id: str
    actor: DashboardInstanceCustomProvidersCommitsGetOutputScmPushActor
    commit: DashboardInstanceCustomProvidersCommitsGetOutputScmPushCommit
    repository: DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepository
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCommitsGetOutput:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    to_environment: DashboardInstanceCustomProvidersCommitsGetOutputToEnvironment
    target_custom_provider_version: DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion
    actor: DashboardInstanceCustomProvidersCommitsGetOutputActor
    created_at: datetime
    error: Optional[DashboardInstanceCustomProvidersCommitsGetOutputError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    from_environment: Optional[DashboardInstanceCustomProvidersCommitsGetOutputFromEnvironment] = None
    previous_custom_provider_version: Optional[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion] = None
    scm_push: Optional[DashboardInstanceCustomProvidersCommitsGetOutputScmPush] = None
    applied_at: Optional[datetime] = None


class mapDashboardInstanceCustomProvidersCommitsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputError:
        return DashboardInstanceCustomProvidersCommitsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputToEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputToEnvironment:
        return DashboardInstanceCustomProvidersCommitsGetOutputToEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputToEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputFromEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputFromEnvironment:
        return DashboardInstanceCustomProvidersCommitsGetOutputFromEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion:
        return DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion:
        return DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputScmPushActor:
        return DashboardInstanceCustomProvidersCommitsGetOutputScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputScmPushCommit:
        return DashboardInstanceCustomProvidersCommitsGetOutputScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider:
        return DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepository:
        return DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutputScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutputScmPush:
        return DashboardInstanceCustomProvidersCommitsGetOutputScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapDashboardInstanceCustomProvidersCommitsGetOutputScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutputScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCommitsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCommitsGetOutput:
        return DashboardInstanceCustomProvidersCommitsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        error=mapDashboardInstanceCustomProvidersCommitsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        to_environment=mapDashboardInstanceCustomProvidersCommitsGetOutputToEnvironment.from_dict(data.get('to_environment')) if data.get('to_environment') else None,
        from_environment=mapDashboardInstanceCustomProvidersCommitsGetOutputFromEnvironment.from_dict(data.get('from_environment')) if data.get('from_environment') else None,
        target_custom_provider_version=mapDashboardInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion.from_dict(data.get('target_custom_provider_version')) if data.get('target_custom_provider_version') else None,
        previous_custom_provider_version=mapDashboardInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion.from_dict(data.get('previous_custom_provider_version')) if data.get('previous_custom_provider_version') else None,
        actor=mapDashboardInstanceCustomProvidersCommitsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapDashboardInstanceCustomProvidersCommitsGetOutputScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCommitsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

