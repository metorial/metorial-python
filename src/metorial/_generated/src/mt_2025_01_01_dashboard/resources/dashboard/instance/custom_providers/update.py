from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftConfig:
    object: str
    schema: DashboardInstanceCustomProvidersUpdateOutputDraftConfigSchema
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraft:
    object: str
    config: DashboardInstanceCustomProvidersUpdateOutputDraftConfig
    container_image: Optional[DashboardInstanceCustomProvidersUpdateOutputDraftContainerImage] = None
    remote_mcp_server: Optional[DashboardInstanceCustomProvidersUpdateOutputDraftRemoteMcpServer] = None
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputScmRepo:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersUpdateOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputProviderCurrentVersion:
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
class DashboardInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputProviderOauth:
    status: str
    auto_registration: DashboardInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceCustomProvidersUpdateOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[DashboardInstanceCustomProvidersUpdateOutputProviderCurrentVersion] = None
    oauth: Optional[DashboardInstanceCustomProvidersUpdateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersUpdateOutputDraftBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersUpdateOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: DashboardInstanceCustomProvidersUpdateOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[DashboardInstanceCustomProvidersUpdateOutputScmRepo] = None
    provider: Optional[DashboardInstanceCustomProvidersUpdateOutputProvider] = None
    draft_bucket: Optional[DashboardInstanceCustomProvidersUpdateOutputDraftBucket] = None


class mapDashboardInstanceCustomProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersUpdateOutput:
        return DashboardInstanceCustomProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapDashboardInstanceCustomProvidersUpdateOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapDashboardInstanceCustomProvidersUpdateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapDashboardInstanceCustomProvidersUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        draft_bucket=mapDashboardInstanceCustomProvidersUpdateOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    readme: Optional[str] = None


class mapDashboardInstanceCustomProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersUpdateBody:
        return DashboardInstanceCustomProvidersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

