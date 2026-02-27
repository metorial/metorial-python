from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderListingsListOutputItemsAttributes:
    is_public: bool
    is_customized: bool
    is_metorial: bool
    is_verified: bool
    is_official: bool
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProviderOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProviderEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariantCurrentVersion:
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
class ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariant:
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
    current_version: Optional[ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariantCurrentVersion] = None
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProviderCurrentVersion:
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
class ManagementInstanceProviderListingsListOutputItemsProviderType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProviderOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[ManagementInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration] = None
@dataclass
class ManagementInstanceProviderListingsListOutputItemsProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceProviderListingsListOutputItemsProviderPublisher
    entry: ManagementInstanceProviderListingsListOutputItemsProviderEntry
    type: ManagementInstanceProviderListingsListOutputItemsProviderType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[ManagementInstanceProviderListingsListOutputItemsProviderOwnerTenant] = None
    default_variant: Optional[ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariant] = None
    current_version: Optional[ManagementInstanceProviderListingsListOutputItemsProviderCurrentVersion] = None
    oauth: Optional[ManagementInstanceProviderListingsListOutputItemsProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProviderListingsListOutputItemsCategories:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceProviderListingsListOutputItemsCollections:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceProviderListingsListOutputItemsGroups:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderListingsListOutputItems:
    object: str
    id: str
    attributes: ManagementInstanceProviderListingsListOutputItemsAttributes
    name: str
    slug: str
    image_url: str
    skills: List[str]
    provider: ManagementInstanceProviderListingsListOutputItemsProvider
    categories: List[ManagementInstanceProviderListingsListOutputItemsCategories]
    collections: List[ManagementInstanceProviderListingsListOutputItemsCollections]
    groups: List[ManagementInstanceProviderListingsListOutputItemsGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
@dataclass
class ManagementInstanceProviderListingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderListingsListOutput:
    items: List[ManagementInstanceProviderListingsListOutputItems]
    pagination: ManagementInstanceProviderListingsListOutputPagination


class mapManagementInstanceProviderListingsListOutputItemsAttributes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsAttributes:
        return ManagementInstanceProviderListingsListOutputItemsAttributes(
        is_public=data.get('is_public'),
        is_customized=data.get('is_customized'),
        is_metorial=data.get('is_metorial'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsAttributes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderOwnerTenant:
        return ManagementInstanceProviderListingsListOutputItemsProviderOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderPublisher:
        return ManagementInstanceProviderListingsListOutputItemsProviderPublisher(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderEntry:
        return ManagementInstanceProviderListingsListOutputItemsProviderEntry(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariantCurrentVersion:
        return ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariantCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariant:
        return ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapManagementInstanceProviderListingsListOutputItemsProviderDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderCurrentVersion:
        return ManagementInstanceProviderListingsListOutputItemsProviderCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderType:
        return ManagementInstanceProviderListingsListOutputItemsProviderType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration:
        return ManagementInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProviderOauth:
        return ManagementInstanceProviderListingsListOutputItemsProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapManagementInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsProvider:
        return ManagementInstanceProviderListingsListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapManagementInstanceProviderListingsListOutputItemsProviderOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapManagementInstanceProviderListingsListOutputItemsProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapManagementInstanceProviderListingsListOutputItemsProviderEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapManagementInstanceProviderListingsListOutputItemsProviderDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapManagementInstanceProviderListingsListOutputItemsProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapManagementInstanceProviderListingsListOutputItemsProviderType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapManagementInstanceProviderListingsListOutputItemsProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
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
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsCategories:
        return ManagementInstanceProviderListingsListOutputItemsCategories(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsCollections:
        return ManagementInstanceProviderListingsListOutputItemsCollections(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItemsGroups:
        return ManagementInstanceProviderListingsListOutputItemsGroups(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputItems:
        return ManagementInstanceProviderListingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        attributes=mapManagementInstanceProviderListingsListOutputItemsAttributes.from_dict(data.get('attributes')) if data.get('attributes') else None,
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        readme=data.get('readme'),
        skills=data.get('skills', []),
        provider=mapManagementInstanceProviderListingsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        categories=[mapManagementInstanceProviderListingsListOutputItemsCategories.from_dict(item) for item in data.get('categories', []) if item],
        collections=[mapManagementInstanceProviderListingsListOutputItemsCollections.from_dict(item) for item in data.get('collections', []) if item],
        groups=[mapManagementInstanceProviderListingsListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutputPagination:
        return ManagementInstanceProviderListingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListOutput:
        return ManagementInstanceProviderListingsListOutput(
        items=[mapManagementInstanceProviderListingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderListingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderListingsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    provider_category_id: Optional[Union[str, List[str]]] = None
    provider_collection_id: Optional[Union[str, List[str]]] = None
    provider_group_id: Optional[Union[str, List[str]]] = None
    publisher_id: Optional[Union[str, List[str]]] = None
    is_public: Optional[bool] = None
    only_from_tenant: Optional[bool] = None
    is_verified: Optional[bool] = None
    is_official: Optional[bool] = None
    is_metorial: Optional[bool] = None
    order_by_rank: Optional[bool] = None


class mapManagementInstanceProviderListingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsListQuery:
        return ManagementInstanceProviderListingsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        provider_category_id=data.get('provider_category_id'),
        provider_collection_id=data.get('provider_collection_id'),
        provider_group_id=data.get('provider_group_id'),
        publisher_id=data.get('publisher_id'),
        is_public=data.get('is_public'),
        only_from_tenant=data.get('only_from_tenant'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official'),
        is_metorial=data.get('is_metorial'),
        order_by_rank=data.get('order_by_rank')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
