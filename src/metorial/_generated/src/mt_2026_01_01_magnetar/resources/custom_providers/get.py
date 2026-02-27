from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

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
class CustomProvidersGetOutputProviderOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class CustomProvidersGetOutputProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersGetOutputProviderEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersGetOutputProviderDefaultVariantCurrentVersion:
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
class CustomProvidersGetOutputProviderDefaultVariant:
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
    current_version: Optional[CustomProvidersGetOutputProviderDefaultVariantCurrentVersion] = None
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
class CustomProvidersGetOutputProviderType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class CustomProvidersGetOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersGetOutputProviderOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[CustomProvidersGetOutputProviderOauthAutoRegistration] = None
@dataclass
class CustomProvidersGetOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersGetOutputProviderPublisher
    entry: CustomProvidersGetOutputProviderEntry
    type: CustomProvidersGetOutputProviderType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[CustomProvidersGetOutputProviderOwnerTenant] = None
    default_variant: Optional[CustomProvidersGetOutputProviderDefaultVariant] = None
    current_version: Optional[CustomProvidersGetOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersGetOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersGetOutput:
    object: str
    id: str
    status: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersGetOutputScmRepo] = None
    draft_bucket: Optional[CustomProvidersGetOutputDraftBucket] = None
    provider: Optional[CustomProvidersGetOutputProvider] = None


class mapCustomProvidersGetOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputScmRepoProvider:
        return CustomProvidersGetOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputScmRepo:
        return CustomProvidersGetOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersGetOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputDraftBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputDraftBucketScmRepoLinkRepository:
        return CustomProvidersGetOutputDraftBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersGetOutputDraftBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputDraftBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputDraftBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputDraftBucketScmRepoLink:
        return CustomProvidersGetOutputDraftBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersGetOutputDraftBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputDraftBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputDraftBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputDraftBucket:
        return CustomProvidersGetOutputDraftBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersGetOutputDraftBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputDraftBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderOwnerTenant:
        return CustomProvidersGetOutputProviderOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputProviderOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderPublisher:
        return CustomProvidersGetOutputProviderPublisher(
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
    def to_dict(value: Union[CustomProvidersGetOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderEntry:
        return CustomProvidersGetOutputProviderEntry(
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
    def to_dict(value: Union[CustomProvidersGetOutputProviderEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderDefaultVariantCurrentVersion:
        return CustomProvidersGetOutputProviderDefaultVariantCurrentVersion(
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
    def to_dict(value: Union[CustomProvidersGetOutputProviderDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderDefaultVariant:
        return CustomProvidersGetOutputProviderDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapCustomProvidersGetOutputProviderDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputProviderDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderCurrentVersion:
        return CustomProvidersGetOutputProviderCurrentVersion(
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
    def to_dict(value: Union[CustomProvidersGetOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderType:
        return CustomProvidersGetOutputProviderType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputProviderType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderOauthAutoRegistration:
        return CustomProvidersGetOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProviderOauth:
        return CustomProvidersGetOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapCustomProvidersGetOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutputProvider:
        return CustomProvidersGetOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapCustomProvidersGetOutputProviderOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapCustomProvidersGetOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapCustomProvidersGetOutputProviderEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapCustomProvidersGetOutputProviderDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapCustomProvidersGetOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapCustomProvidersGetOutputProviderType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapCustomProvidersGetOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
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
    def to_dict(value: Union[CustomProvidersGetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersGetOutput:
        return CustomProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        scm_repo=mapCustomProvidersGetOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        draft_bucket=mapCustomProvidersGetOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None,
        provider=mapCustomProvidersGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
