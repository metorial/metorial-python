from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

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
class ManagementInstanceCustomProvidersUpdateOutputProviderOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion:
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
class ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariant:
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
    current_version: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion] = None
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
class ManagementInstanceCustomProvidersUpdateOutputProviderType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProviderOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceCustomProvidersUpdateOutputProviderPublisher
    entry: ManagementInstanceCustomProvidersUpdateOutputProviderEntry
    type: ManagementInstanceCustomProvidersUpdateOutputProviderType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderOwnerTenant] = None
    default_variant: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariant] = None
    current_version: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion] = None
    oauth: Optional[ManagementInstanceCustomProvidersUpdateOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceCustomProvidersUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scm_repo: Optional[ManagementInstanceCustomProvidersUpdateOutputScmRepo] = None
    draft_bucket: Optional[ManagementInstanceCustomProvidersUpdateOutputDraftBucket] = None
    provider: Optional[ManagementInstanceCustomProvidersUpdateOutputProvider] = None


class mapManagementInstanceCustomProvidersUpdateOutputScmRepoProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputScmRepoProvider:
        return ManagementInstanceCustomProvidersUpdateOutputScmRepoProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputScmRepoProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputScmRepo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputScmRepo:
        return ManagementInstanceCustomProvidersUpdateOutputScmRepo(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersUpdateOutputScmRepoProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputScmRepo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider:
        return ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        name=data.get('name'),
        owner=data.get('owner')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository:
        return ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository(
        object=data.get('object'),
        id=data.get('id'),
        provider=mapManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepositoryProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        url=data.get('url'),
        is_private=data.get('is_private'),
        default_branch=data.get('default_branch'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink:
        return ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink(
        object=data.get('object'),
        is_linked=data.get('is_linked'),
        path=data.get('path'),
        repository=mapManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLinkRepository.from_dict(data.get('repository')) if data.get('repository') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputDraftBucket:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputDraftBucket:
        return ManagementInstanceCustomProvidersUpdateOutputDraftBucket(
        object=data.get('object'),
        id=data.get('id'),
        is_immutable=data.get('is_immutable'),
        is_read_only=data.get('is_read_only'),
        scm_repo_link=mapManagementInstanceCustomProvidersUpdateOutputDraftBucketScmRepoLink.from_dict(data.get('scm_repo_link')) if data.get('scm_repo_link') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputDraftBucket, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderOwnerTenant:
        return ManagementInstanceCustomProvidersUpdateOutputProviderOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderPublisher:
        return ManagementInstanceCustomProvidersUpdateOutputProviderPublisher(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderEntry:
        return ManagementInstanceCustomProvidersUpdateOutputProviderEntry(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion:
        return ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariant:
        return ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion:
        return ManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderType:
        return ManagementInstanceCustomProvidersUpdateOutputProviderType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration:
        return ManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProviderOauth:
        return ManagementInstanceCustomProvidersUpdateOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapManagementInstanceCustomProvidersUpdateOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutputProvider:
        return ManagementInstanceCustomProvidersUpdateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapManagementInstanceCustomProvidersUpdateOutputProviderOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapManagementInstanceCustomProvidersUpdateOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapManagementInstanceCustomProvidersUpdateOutputProviderEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapManagementInstanceCustomProvidersUpdateOutputProviderDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapManagementInstanceCustomProvidersUpdateOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapManagementInstanceCustomProvidersUpdateOutputProviderType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapManagementInstanceCustomProvidersUpdateOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateOutput:
        return ManagementInstanceCustomProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        scm_repo=mapManagementInstanceCustomProvidersUpdateOutputScmRepo.from_dict(data.get('scm_repo')) if data.get('scm_repo') else None,
        draft_bucket=mapManagementInstanceCustomProvidersUpdateOutputDraftBucket.from_dict(data.get('draft_bucket')) if data.get('draft_bucket') else None,
        provider=mapManagementInstanceCustomProvidersUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
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


class mapManagementInstanceCustomProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersUpdateBody:
        return ManagementInstanceCustomProvidersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
