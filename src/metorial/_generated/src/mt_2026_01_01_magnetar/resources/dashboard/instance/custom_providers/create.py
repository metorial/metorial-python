from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersCreateOutputScmRepoProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCreateOutputScmRepo:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCreateOutputScmRepoProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider:
    object: str
    type: str
    id: str
    name: str
    owner: str
@dataclass
class DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepository:
    object: str
    id: str
    provider: DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider
    url: str
    is_private: bool
    default_branch: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLink:
    object: str
    is_linked: str
    repository: DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepository
    path: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutputDraftBucket:
    object: str
    id: str
    is_immutable: bool
    is_read_only: bool
    created_at: datetime
    scm_repo_link: Optional[DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLink] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariantCurrentVersion:
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
class DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariant:
    object: str
    id: str
    tag: str
    identifier: str
    provider_id: str
    is_default: bool
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    current_version: Optional[DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariantCurrentVersion] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion:
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
class DashboardInstanceCustomProvidersCreateOutputProviderType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[DashboardInstanceCustomProvidersCreateOutputProviderOauthAutoRegistration] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceCustomProvidersCreateOutputProviderPublisher
    entry: DashboardInstanceCustomProvidersCreateOutputProviderEntry
    type: DashboardInstanceCustomProvidersCreateOutputProviderType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[DashboardInstanceCustomProvidersCreateOutputProviderOwnerTenant] = None
    default_variant: Optional[DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariant] = None
    current_version: Optional[DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion] = None
    oauth: Optional[DashboardInstanceCustomProvidersCreateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutput:
    object: str
    id: str
    status: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[DashboardInstanceCustomProvidersCreateOutputScmRepo] = None
    draft_bucket: Optional[DashboardInstanceCustomProvidersCreateOutputDraftBucket] = None
    provider: Optional[DashboardInstanceCustomProvidersCreateOutputProvider] = None


class mapDashboardInstanceCustomProvidersCreateOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputScmRepoProvider:
        return DashboardInstanceCustomProvidersCreateOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputScmRepo:
        return DashboardInstanceCustomProvidersCreateOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCreateOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider:
        return DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepository:
        return DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapDashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLink:
        return DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapDashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputDraftBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputDraftBucket:
        return DashboardInstanceCustomProvidersCreateOutputDraftBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapDashboardInstanceCustomProvidersCreateOutputDraftBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputDraftBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderOwnerTenant:
        return DashboardInstanceCustomProvidersCreateOutputProviderOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderPublisher:
        return DashboardInstanceCustomProvidersCreateOutputProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderEntry:
        return DashboardInstanceCustomProvidersCreateOutputProviderEntry(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariantCurrentVersion:
        return DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariantCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariant:
        return DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapDashboardInstanceCustomProvidersCreateOutputProviderDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion:
        return DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderType:
        return DashboardInstanceCustomProvidersCreateOutputProviderType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderOauthAutoRegistration:
        return DashboardInstanceCustomProvidersCreateOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderOauth:
        return DashboardInstanceCustomProvidersCreateOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapDashboardInstanceCustomProvidersCreateOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProvider:
        return DashboardInstanceCustomProvidersCreateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapDashboardInstanceCustomProvidersCreateOutputProviderOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapDashboardInstanceCustomProvidersCreateOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapDashboardInstanceCustomProvidersCreateOutputProviderEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapDashboardInstanceCustomProvidersCreateOutputProviderDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapDashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapDashboardInstanceCustomProvidersCreateOutputProviderType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapDashboardInstanceCustomProvidersCreateOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        tag=data.get('tag'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutput:
        return DashboardInstanceCustomProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        scm_repo=mapDashboardInstanceCustomProvidersCreateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        draft_bucket=mapDashboardInstanceCustomProvidersCreateOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None,
        provider=mapDashboardInstanceCustomProvidersCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersCreateBody:
    name: str
    from_: Dict[str, Any]
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[DashboardInstanceCustomProvidersCreateBodyConfig] = None


class mapDashboardInstanceCustomProvidersCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateBodyConfig:
        return DashboardInstanceCustomProvidersCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateBody:
        return DashboardInstanceCustomProvidersCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        from_=data.get('from'),
        config=mapDashboardInstanceCustomProvidersCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
