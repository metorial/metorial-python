from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftConfig:
    object: str
    schema: ManagementInstanceCustomProvidersUpdateOutputDraftConfigSchema
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraft:
    object: str
    config: ManagementInstanceCustomProvidersUpdateOutputDraftConfig
    container_image: Optional[ManagementInstanceCustomProvidersUpdateOutputDraftContainerImage] = None
    remote_mcp_server: Optional[ManagementInstanceCustomProvidersUpdateOutputDraftRemoteMcpServer] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputScmRepo:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersUpdateOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion:
    object: str
    id: str
    version: str
    provider_id: str
    is_current: bool
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    specification_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderOauth:
    status: str
    auto_registration: ManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceCustomProvidersUpdateOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion] = None
    oauth: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink:
    object: str
    is_linked: str
    repository: ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputDraftBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: ManagementInstanceCustomProvidersUpdateOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[ManagementInstanceCustomProvidersUpdateOutputScmRepo] = None
    provider: Optional[ManagementInstanceCustomProvidersUpdateOutputProvider] = None
    draft_bucket: Optional[ManagementInstanceCustomProvidersUpdateOutputDraftBucket] = None


class mapManagementInstanceCustomProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutput:
        return ManagementInstanceCustomProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapManagementInstanceCustomProvidersUpdateOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapManagementInstanceCustomProvidersUpdateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapManagementInstanceCustomProvidersUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        draft_bucket=mapManagementInstanceCustomProvidersUpdateOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomProvidersUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    readme: Optional[str] = None


class mapManagementInstanceCustomProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateBody:
        return ManagementInstanceCustomProvidersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

