from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputError:
    code: str
    message: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputToEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfig:
    object: str
    schema: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor
    commit: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit
    repository: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment
    environments: List[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionRemoteMcpServer] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfig:
    object: str
    schema: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor
    commit: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit
    repository: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment
    environments: List[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionRemoteMcpServer] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutputScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputScmPushActor
    commit: ManagementInstanceCustomProvidersCommitsCreateOutputScmPushCommit
    repository: ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsCreateOutput:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    to_environment: ManagementInstanceCustomProvidersCommitsCreateOutputToEnvironment
    target_custom_provider_version: ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersion
    actor: ManagementInstanceCustomProvidersCommitsCreateOutputActor
    created_at: datetime
    error: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    from_environment: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputFromEnvironment] = None
    previous_custom_provider_version: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion] = None
    scm_push: Optional[ManagementInstanceCustomProvidersCommitsCreateOutputScmPush] = None
    applied_at: Optional[datetime] = None


class mapManagementInstanceCustomProvidersCommitsCreateOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputError:
        return ManagementInstanceCustomProvidersCommitsCreateOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputToEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputToEnvironment:
        return ManagementInstanceCustomProvidersCommitsCreateOutputToEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputToEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputFromEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputFromEnvironment:
        return ManagementInstanceCustomProvidersCommitsCreateOutputFromEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfigSchema:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfig:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionContainerImage:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionRemoteMcpServer:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersion:
        return ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfigSchema:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfig:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionContainerImage:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionRemoteMcpServer:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion:
        return ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputScmPushActor:
        return ManagementInstanceCustomProvidersCommitsCreateOutputScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputScmPushCommit:
        return ManagementInstanceCustomProvidersCommitsCreateOutputScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepository:
        return ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutputScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutputScmPush:
        return ManagementInstanceCustomProvidersCommitsCreateOutputScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapManagementInstanceCustomProvidersCommitsCreateOutputScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutputScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateOutput:
        return ManagementInstanceCustomProvidersCommitsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        error=mapManagementInstanceCustomProvidersCommitsCreateOutputError.from_dict(data.get('error')) if data.get('error') else None,
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        to_environment=mapManagementInstanceCustomProvidersCommitsCreateOutputToEnvironment.from_dict(data.get('to_environment')) if data.get('to_environment') else None,
        from_environment=mapManagementInstanceCustomProvidersCommitsCreateOutputFromEnvironment.from_dict(data.get('from_environment')) if data.get('from_environment') else None,
        target_custom_provider_version=mapManagementInstanceCustomProvidersCommitsCreateOutputTargetCustomProviderVersion.from_dict(data.get('target_custom_provider_version')) if data.get('target_custom_provider_version') else None,
        previous_custom_provider_version=mapManagementInstanceCustomProvidersCommitsCreateOutputPreviousCustomProviderVersion.from_dict(data.get('previous_custom_provider_version')) if data.get('previous_custom_provider_version') else None,
        actor=mapManagementInstanceCustomProvidersCommitsCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersCommitsCreateOutputScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomProvidersCommitsCreateBody:
    message: str
    action: Dict[str, Any]


class mapManagementInstanceCustomProvidersCommitsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsCreateBody:
        return ManagementInstanceCustomProvidersCommitsCreateBody(
        message=data.get('message'),
        action=data.get('action')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

