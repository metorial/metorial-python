from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputError:
    code: str
    message: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputToEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputFromEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig:
    object: str
    schema: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor
    commit: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit
    repository: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment
    environments: List[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig:
    object: str
    schema: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit:
    object: str
    id: str
    type: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    object: str
    is_linked: str
    repository: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor
    commit: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit
    repository: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit] = None
    immutable_bucket: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket] = None
    scm_push: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments:
    object: str
    id: str
    is_current_version_for_environment: bool
    environment: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage:
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer:
    url: str
    transport: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion:
    object: str
    id: str
    status: str
    index: float
    identifier: str
    deployment: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment
    environments: List[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments]
    custom_provider_id: str
    actor: ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor
    created_at: datetime
    updated_at: datetime
    config: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig] = None
    provider_id: Optional[str] = None
    container_image: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage] = None
    remote_mcp_server: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputActor:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    created_at: datetime
    organization_actor_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputScmPushActor:
    object: str
    id: str
    external_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputScmPushCommit:
    object: str
    id: str
    sha: str
    branch: str
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutputScmPush:
    object: str
    id: str
    actor: ManagementInstanceCustomProvidersCommitsGetOutputScmPushActor
    commit: ManagementInstanceCustomProvidersCommitsGetOutputScmPushCommit
    repository: ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepository
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCommitsGetOutput:
    object: str
    id: str
    status: str
    trigger: str
    custom_provider_id: str
    to_environment: ManagementInstanceCustomProvidersCommitsGetOutputToEnvironment
    target_custom_provider_version: ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion
    actor: ManagementInstanceCustomProvidersCommitsGetOutputActor
    created_at: datetime
    error: Optional[ManagementInstanceCustomProvidersCommitsGetOutputError] = None
    provider_id: Optional[str] = None
    custom_provider_deployment_id: Optional[str] = None
    from_environment: Optional[ManagementInstanceCustomProvidersCommitsGetOutputFromEnvironment] = None
    previous_custom_provider_version: Optional[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion] = None
    scm_push: Optional[ManagementInstanceCustomProvidersCommitsGetOutputScmPush] = None
    applied_at: Optional[datetime] = None


class mapManagementInstanceCustomProvidersCommitsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputError:
        return ManagementInstanceCustomProvidersCommitsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputToEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputToEnvironment:
        return ManagementInstanceCustomProvidersCommitsGetOutputToEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputToEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputFromEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputFromEnvironment:
        return ManagementInstanceCustomProvidersCommitsGetOutputFromEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputFromEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion:
        return ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig(
        object=data.get('object'),
        schema=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfigSchema.from_dict(data.get('schema')) if data.get('schema') else None,
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        immutable_bucket=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentImmutableBucket.from_dict(data.get('immutable_bucket')) if data.get('immutable_bucket') else None,
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeploymentScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments(
        object=data.get('object'),
        id=data.get('id'),
        is_current_version_for_environment=data.get('is_current_version_for_environment'),
        environment=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironmentsEnvironment.from_dict(data.get('environment')) if data.get('environment') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage(
        container_registry=data.get('container_registry'),
        container_image_tag=data.get('container_image_tag'),
        container_image=data.get('container_image')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer(
        url=data.get('url'),
        transport=data.get('transport')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion:
        return ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        config=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionConfig.from_dict(data.get('config')) if data.get('config') else None,
        index=data.get('index'),
        identifier=data.get('identifier'),
        deployment=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        environments=[mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionEnvironments.from_dict(item) for item in data.get('environments', []) if item],
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionActor.from_dict(data.get('actor')) if data.get('actor') else None,
        container_image=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionContainerImage.from_dict(data.get('container_image')) if data.get('container_image') else None,
        remote_mcp_server=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersionRemoteMcpServer.from_dict(data.get('remote_mcp_server')) if data.get('remote_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        organization_actor_id=data.get('organization_actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputScmPushActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputScmPushActor:
        return ManagementInstanceCustomProvidersCommitsGetOutputScmPushActor(
        object=data.get('object'),
        id=data.get('id'),
        external_id=data.get('external_id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputScmPushActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputScmPushCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputScmPushCommit:
        return ManagementInstanceCustomProvidersCommitsGetOutputScmPushCommit(
        object=data.get('object'),
        id=data.get('id'),
        sha=data.get('sha'),
        branch=data.get('branch'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputScmPushCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider:
        return ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputScmPushRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepository:
        return ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersCommitsGetOutputScmPushRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputScmPushRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutputScmPush:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutputScmPush:
        return ManagementInstanceCustomProvidersCommitsGetOutputScmPush(
        object=data.get('object'),
        id=data.get('id'),
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputScmPushActor.from_dict(data.get('actor')) if data.get('actor') else None,
        commit=mapManagementInstanceCustomProvidersCommitsGetOutputScmPushCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        repository=mapManagementInstanceCustomProvidersCommitsGetOutputScmPushRepository.from_dict(data.get('repository')) if data.get('repository') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutputScmPush, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCommitsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCommitsGetOutput:
        return ManagementInstanceCustomProvidersCommitsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        error=mapManagementInstanceCustomProvidersCommitsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        to_environment=mapManagementInstanceCustomProvidersCommitsGetOutputToEnvironment.from_dict(data.get('to_environment')) if data.get('to_environment') else None,
        from_environment=mapManagementInstanceCustomProvidersCommitsGetOutputFromEnvironment.from_dict(data.get('from_environment')) if data.get('from_environment') else None,
        target_custom_provider_version=mapManagementInstanceCustomProvidersCommitsGetOutputTargetCustomProviderVersion.from_dict(data.get('target_custom_provider_version')) if data.get('target_custom_provider_version') else None,
        previous_custom_provider_version=mapManagementInstanceCustomProvidersCommitsGetOutputPreviousCustomProviderVersion.from_dict(data.get('previous_custom_provider_version')) if data.get('previous_custom_provider_version') else None,
        actor=mapManagementInstanceCustomProvidersCommitsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        scm_push=mapManagementInstanceCustomProvidersCommitsGetOutputScmPush.from_dict(data.get('scm_push')) if data.get('scm_push') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCommitsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

