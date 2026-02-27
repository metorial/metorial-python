from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

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
class CustomProvidersUpdateOutputProviderOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class CustomProvidersUpdateOutputProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class CustomProvidersUpdateOutputProviderEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion:
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
class CustomProvidersUpdateOutputProviderDefaultVariant:
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
    current_version: Optional[CustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion] = None
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
class CustomProvidersUpdateOutputProviderType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class CustomProvidersUpdateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class CustomProvidersUpdateOutputProviderOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[CustomProvidersUpdateOutputProviderOauthAutoRegistration] = None
@dataclass
class CustomProvidersUpdateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: CustomProvidersUpdateOutputProviderPublisher
    entry: CustomProvidersUpdateOutputProviderEntry
    type: CustomProvidersUpdateOutputProviderType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[CustomProvidersUpdateOutputProviderOwnerTenant] = None
    default_variant: Optional[CustomProvidersUpdateOutputProviderDefaultVariant] = None
    current_version: Optional[CustomProvidersUpdateOutputProviderCurrentVersion] = None
    oauth: Optional[CustomProvidersUpdateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class CustomProvidersUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[CustomProvidersUpdateOutputScmRepo] = None
    draft_bucket: Optional[CustomProvidersUpdateOutputDraftBucket] = None
    provider: Optional[CustomProvidersUpdateOutputProvider] = None


class mapCustomProvidersUpdateOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputScmRepoProvider:
        return CustomProvidersUpdateOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputScmRepo:
        return CustomProvidersUpdateOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersUpdateOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider:
        return CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository:
        return CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraftBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftBucketScmRepoLink:
        return CustomProvidersUpdateOutputDraftBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputDraftBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputDraftBucket:
        return CustomProvidersUpdateOutputDraftBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapCustomProvidersUpdateOutputDraftBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputDraftBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderOwnerTenant:
        return CustomProvidersUpdateOutputProviderOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderPublisher:
        return CustomProvidersUpdateOutputProviderPublisher(
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
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderEntry:
        return CustomProvidersUpdateOutputProviderEntry(
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
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion:
        return CustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion(
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
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderDefaultVariant:
        return CustomProvidersUpdateOutputProviderDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderCurrentVersion:
        return CustomProvidersUpdateOutputProviderCurrentVersion(
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
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderType:
        return CustomProvidersUpdateOutputProviderType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderOauthAutoRegistration:
        return CustomProvidersUpdateOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProviderOauth:
        return CustomProvidersUpdateOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapCustomProvidersUpdateOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutputProvider:
        return CustomProvidersUpdateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapCustomProvidersUpdateOutputProviderOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapCustomProvidersUpdateOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapCustomProvidersUpdateOutputProviderEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapCustomProvidersUpdateOutputProviderDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapCustomProvidersUpdateOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapCustomProvidersUpdateOutputProviderType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapCustomProvidersUpdateOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
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
    def to_dict(value: Union[CustomProvidersUpdateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateOutput:
        return CustomProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        scm_repo=mapCustomProvidersUpdateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        draft_bucket=mapCustomProvidersUpdateOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None,
        provider=mapCustomProvidersUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
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


class mapCustomProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersUpdateBody:
        return CustomProvidersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
