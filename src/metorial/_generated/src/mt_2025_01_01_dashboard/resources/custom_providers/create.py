from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersCreateOutputDraftContainerImage:
    object: str
    container_registry: str
    container_image_tag: str
    container_image: str
@dataclass
class CustomProvidersCreateOutputDraftRemoteMcpServer:
    object: str
    url: str
    transport: str
@dataclass
class CustomProvidersCreateOutputDraftConfigSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class CustomProvidersCreateOutputDraftConfig:
    object: str
    schema: CustomProvidersCreateOutputDraftConfigSchema
    transformer: str
@dataclass
class CustomProvidersCreateOutputDraft:
    object: str
    config: CustomProvidersCreateOutputDraftConfig
    container_image: Optional[CustomProvidersCreateOutputDraftContainerImage] = None
    remote_mcp_server: Optional[CustomProvidersCreateOutputDraftRemoteMcpServer] = None
@dataclass
class CustomProvidersCreateOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCreateOutputScmRepo:
    object: str
    id: str
    provider: CustomProvidersCreateOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCreateOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersCreateOutputProviderCurrentVersion:
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
class CustomProvidersCreateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersCreateOutputProviderOauth:
    status: str
    auto_registration: CustomProvidersCreateOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class CustomProvidersCreateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersCreateOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[CustomProvidersCreateOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersCreateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class CustomProvidersCreateOutputDraftBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: CustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class CustomProvidersCreateOutputDraftBucketScmRepoLink:
    object: str
    is_linked: str
    repository: CustomProvidersCreateOutputDraftBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class CustomProvidersCreateOutputDraftBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[CustomProvidersCreateOutputDraftBucketScmRepoLink] = None
@dataclass
class CustomProvidersCreateOutput:
    object: str
    id: str
    status: str
    type: str
    name: str
    draft: CustomProvidersCreateOutputDraft
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersCreateOutputScmRepo] = None
    provider: Optional[CustomProvidersCreateOutputProvider] = None
    draft_bucket: Optional[CustomProvidersCreateOutputDraftBucket] = None


class mapCustomProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateOutput:
        return CustomProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        draft=mapCustomProvidersCreateOutputDraft.from_dict(data.get('draft')) if data.get('draft') else None,
        scm_repo=mapCustomProvidersCreateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        provider=mapCustomProvidersCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        draft_bucket=mapCustomProvidersCreateOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class CustomProvidersCreateBody:
    name: str
    from_: Dict[str, Any]
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[CustomProvidersCreateBodyConfig] = None


class mapCustomProvidersCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateBodyConfig:
        return CustomProvidersCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersCreateBody:
        return CustomProvidersCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        from_=data.get('from'),
        config=mapCustomProvidersCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

