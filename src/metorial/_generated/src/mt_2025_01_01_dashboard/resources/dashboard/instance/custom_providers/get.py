from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftConfig:
    object: str
    schema: DashboardInstanceCustomProvidersGetOutputDraftConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraft:
    object: str
    config: DashboardInstanceCustomProvidersGetOutputDraftConfig
    container_image: Optional[DashboardInstanceCustomProvidersGetOutputDraftContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersGetOutputDraftRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersGetOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersGetOutputScmRepo:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersGetOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersGetOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersGetOutputProviderCurrentVersion:
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
class DashboardInstanceCustomProvidersGetOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceCustomProvidersGetOutputProviderOauth:
    status: str
    auto_registration: DashboardInstanceCustomProvidersGetOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersGetOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceCustomProvidersGetOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[DashboardInstanceCustomProvidersGetOutputProviderCurrentVersion] = None
    oauth: Optional[DashboardInstanceCustomProvidersGetOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersGetOutputDraftBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersGetOutputDraftBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersGetOutputDraftBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersGetOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: DashboardInstanceCustomProvidersGetOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[DashboardInstanceCustomProvidersGetOutputScmRepo] = None
    provider: Optional[DashboardInstanceCustomProvidersGetOutputProvider] = None
    draft_bucket: Optional[DashboardInstanceCustomProvidersGetOutputDraftBucket] = None


class mapDashboardInstanceCustomProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersGetOutput:
        return DashboardInstanceCustomProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapDashboardInstanceCustomProvidersGetOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapDashboardInstanceCustomProvidersGetOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapDashboardInstanceCustomProvidersGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        draft_bucket=mapDashboardInstanceCustomProvidersGetOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

