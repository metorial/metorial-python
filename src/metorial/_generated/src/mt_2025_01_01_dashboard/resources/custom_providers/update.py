from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersUpdateOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersUpdateOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class CustomProvidersUpdateOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersUpdateOutputDraftConfig:
    object: str
    schema: CustomProvidersUpdateOutputDraftConfigSchema
    transformer: str
@dataclass
class CustomProvidersUpdateOutputDraft:
    object: str
    config: CustomProvidersUpdateOutputDraftConfig
    container_image: Optional[CustomProvidersUpdateOutputDraftContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersUpdateOutputDraftRemoteMcpServer] = None
@dataclass
class CustomProvidersUpdateOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersUpdateOutputScmRepo:
    object: str
    id: str
    provider: CustomProvidersUpdateOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersUpdateOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersUpdateOutputProviderCurrentVersion:
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
class CustomProvidersUpdateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersUpdateOutputProviderOauth:
    status: str
    auto_registration: CustomProvidersUpdateOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class CustomProvidersUpdateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersUpdateOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[CustomProvidersUpdateOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersUpdateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersUpdateOutputDraftBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersUpdateOutputDraftBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersUpdateOutputDraftBucketScmRepoLink] = None
@dataclass
class CustomProvidersUpdateOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: CustomProvidersUpdateOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersUpdateOutputScmRepo] = None
    provider: Optional[CustomProvidersUpdateOutputProvider] = None
    draft_bucket: Optional[CustomProvidersUpdateOutputDraftBucket] = None


class mapCustomProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutput:
        return CustomProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapCustomProvidersUpdateOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapCustomProvidersUpdateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapCustomProvidersUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        draft_bucket=mapCustomProvidersUpdateOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    readme: Optional[str] = None


class mapCustomProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateBody:
        return CustomProvidersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

