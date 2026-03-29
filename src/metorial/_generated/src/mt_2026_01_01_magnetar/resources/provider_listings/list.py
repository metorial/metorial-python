from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderListingsListOutputItemsAttributes:
    is_public: bool
    is_customized: bool
    is_metorial: bool
    is_verified: bool
    is_official: bool
@dataclass
class ProviderListingsListOutputItemsProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderListingsListOutputItemsProviderCurrentVersion:
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
class ProviderListingsListOutputItemsProviderOauthAutoRegistration:
    status: str
@dataclass
class ProviderListingsListOutputItemsProviderOauth:
    status: str
    auto_registration: ProviderListingsListOutputItemsProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ProviderListingsListOutputItemsProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ProviderListingsListOutputItemsProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[ProviderListingsListOutputItemsProviderCurrentVersion] = None
    oauth: Optional[ProviderListingsListOutputItemsProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderListingsListOutputItemsCategories:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProviderListingsListOutputItemsCollections:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProviderListingsListOutputItemsGroups:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderListingsListOutputItems:
    object: str
    id: str
    attributes: ProviderListingsListOutputItemsAttributes
    name: str
    slug: str
    image_url: str
    skills: List[str]
    provider: ProviderListingsListOutputItemsProvider
    categories: List[ProviderListingsListOutputItemsCategories]
    collections: List[ProviderListingsListOutputItemsCollections]
    groups: List[ProviderListingsListOutputItemsGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
@dataclass
class ProviderListingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderListingsListOutput:
    items: List[ProviderListingsListOutputItems]
    pagination: ProviderListingsListOutputPagination


class mapProviderListingsListOutputItemsAttributes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsAttributes:
        return ProviderListingsListOutputItemsAttributes(
        is_public=data.get('is_public'),
        is_customized=data.get('is_customized'),
        is_metorial=data.get('is_metorial'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official')
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsAttributes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsProviderPublisher:
        return ProviderListingsListOutputItemsProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsProviderCurrentVersion:
        return ProviderListingsListOutputItemsProviderCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsProviderOauthAutoRegistration:
        return ProviderListingsListOutputItemsProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsProviderOauth:
        return ProviderListingsListOutputItemsProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapProviderListingsListOutputItemsProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsProvider:
        return ProviderListingsListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapProviderListingsListOutputItemsProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapProviderListingsListOutputItemsProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapProviderListingsListOutputItemsProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsCategories:
        return ProviderListingsListOutputItemsCategories(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsCollections:
        return ProviderListingsListOutputItemsCollections(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItemsGroups:
        return ProviderListingsListOutputItemsGroups(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputItems:
        return ProviderListingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        attributes=mapProviderListingsListOutputItemsAttributes.from_dict(data.get('attributes')) if data.get('attributes') else None,
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        readme=data.get('readme'),
        skills=data.get('skills', []),
        provider=mapProviderListingsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        categories=[mapProviderListingsListOutputItemsCategories.from_dict(item) for item in data.get('categories', []) if item],
        collections=[mapProviderListingsListOutputItemsCollections.from_dict(item) for item in data.get('collections', []) if item],
        groups=[mapProviderListingsListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutputPagination:
        return ProviderListingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListOutput:
        return ProviderListingsListOutput(
        items=[mapProviderListingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderListingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderListingsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProviderListingsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProviderListingsListQuery:
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
    is_owner: Optional[bool] = None
    is_public: Optional[bool] = None
    is_verified: Optional[bool] = None
    is_official: Optional[bool] = None
    is_metorial: Optional[bool] = None
    created_at: Optional[ProviderListingsListQueryCreatedAt] = None
    updated_at: Optional[ProviderListingsListQueryUpdatedAt] = None


class mapProviderListingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsListQuery:
        return ProviderListingsListQuery(
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
        is_owner=data.get('is_owner'),
        is_public=data.get('is_public'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official'),
        is_metorial=data.get('is_metorial'),
        created_at=mapProviderListingsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapProviderListingsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

