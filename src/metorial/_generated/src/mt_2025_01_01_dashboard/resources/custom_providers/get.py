from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersGetOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersGetOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class CustomProvidersGetOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersGetOutputDraftConfig:
    object: str
    schema: CustomProvidersGetOutputDraftConfigSchema
    transformer: str
@dataclass
class CustomProvidersGetOutputDraft:
    object: str
    config: CustomProvidersGetOutputDraftConfig
    container_image: Optional[CustomProvidersGetOutputDraftContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersGetOutputDraftRemoteMcpServer] = None
@dataclass
class CustomProvidersGetOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersGetOutputScmRepo:
    object: str
    id: str
    provider: CustomProvidersGetOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersGetOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersGetOutputProviderCurrentVersion:
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
class CustomProvidersGetOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersGetOutputProviderOauth:
    status: str
    auto_registration: CustomProvidersGetOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class CustomProvidersGetOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersGetOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[CustomProvidersGetOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersGetOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersGetOutputDraftBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersGetOutputDraftBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersGetOutputDraftBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersGetOutputDraftBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersGetOutputDraftBucketScmRepoLink] = None
@dataclass
class CustomProvidersGetOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: CustomProvidersGetOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersGetOutputScmRepo] = None
    provider: Optional[CustomProvidersGetOutputProvider] = None
    draft_bucket: Optional[CustomProvidersGetOutputDraftBucket] = None


class mapCustomProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutput:
        return CustomProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapCustomProvidersGetOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapCustomProvidersGetOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapCustomProvidersGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        draft_bucket=mapCustomProvidersGetOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

