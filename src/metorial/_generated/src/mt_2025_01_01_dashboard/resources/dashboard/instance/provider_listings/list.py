from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderListingsListOutputItemsAttributes:
    is_public: bool
    is_customized: bool
    is_metorial: bool
    is_verified: bool
    is_official: bool
@dataclass
class DashboardInstanceProviderListingsListOutputItemsProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderListingsListOutputItemsProviderCurrentVersion:
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
class DashboardInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceProviderListingsListOutputItemsProviderOauth:
    status: str
    auto_registration: DashboardInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class DashboardInstanceProviderListingsListOutputItemsProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceProviderListingsListOutputItemsProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[DashboardInstanceProviderListingsListOutputItemsProviderCurrentVersion] = None
    oauth: Optional[DashboardInstanceProviderListingsListOutputItemsProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceProviderListingsListOutputItemsCategories:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceProviderListingsListOutputItemsCollections:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceProviderListingsListOutputItemsGroups:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderListingsListOutputItems:
    object: str
    id: str
    attributes: DashboardInstanceProviderListingsListOutputItemsAttributes
    name: str
    slug: str
    image_url: str
    skills: List[str]
    provider: DashboardInstanceProviderListingsListOutputItemsProvider
    categories: List[DashboardInstanceProviderListingsListOutputItemsCategories]
    collections: List[DashboardInstanceProviderListingsListOutputItemsCollections]
    groups: List[DashboardInstanceProviderListingsListOutputItemsGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
@dataclass
class DashboardInstanceProviderListingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderListingsListOutput:
    items: List[DashboardInstanceProviderListingsListOutputItems]
    pagination: DashboardInstanceProviderListingsListOutputPagination


class mapDashboardInstanceProviderListingsListOutputItemsAttributes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsAttributes:
        return DashboardInstanceProviderListingsListOutputItemsAttributes(
        is_public=data.get('is_public'),
        is_customized=data.get('is_customized'),
        is_metorial=data.get('is_metorial'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsAttributes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsProviderPublisher:
        return DashboardInstanceProviderListingsListOutputItemsProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsProviderCurrentVersion:
        return DashboardInstanceProviderListingsListOutputItemsProviderCurrentVersion(
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
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration:
        return DashboardInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsProviderOauth:
        return DashboardInstanceProviderListingsListOutputItemsProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapDashboardInstanceProviderListingsListOutputItemsProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsProvider:
        return DashboardInstanceProviderListingsListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapDashboardInstanceProviderListingsListOutputItemsProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapDashboardInstanceProviderListingsListOutputItemsProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapDashboardInstanceProviderListingsListOutputItemsProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsCategories:
        return DashboardInstanceProviderListingsListOutputItemsCategories(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsCollections:
        return DashboardInstanceProviderListingsListOutputItemsCollections(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItemsGroups:
        return DashboardInstanceProviderListingsListOutputItemsGroups(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputItems:
        return DashboardInstanceProviderListingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        attributes=mapDashboardInstanceProviderListingsListOutputItemsAttributes.from_dict(data.get('attributes')) if data.get('attributes') else None,
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        readme=data.get('readme'),
        skills=data.get('skills', []),
        provider=mapDashboardInstanceProviderListingsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        categories=[mapDashboardInstanceProviderListingsListOutputItemsCategories.from_dict(item) for item in data.get('categories', []) if item],
        collections=[mapDashboardInstanceProviderListingsListOutputItemsCollections.from_dict(item) for item in data.get('collections', []) if item],
        groups=[mapDashboardInstanceProviderListingsListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutputPagination:
        return DashboardInstanceProviderListingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListOutput:
        return DashboardInstanceProviderListingsListOutput(
        items=[mapDashboardInstanceProviderListingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderListingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderListingsListQueryCapabilities:
    supports_config: Optional[bool] = None
    supports_auth: Optional[bool] = None
    supports_oauth: Optional[bool] = None
    supports_callbacks: Optional[bool] = None
    supports_oauth_auto_registration: Optional[bool] = None
    supports_auth_export: Optional[bool] = None
    supports_auth_import: Optional[bool] = None
@dataclass
class DashboardInstanceProviderListingsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceProviderListingsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceProviderListingsListQuery:
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
    capabilities: Optional[DashboardInstanceProviderListingsListQueryCapabilities] = None
    is_public: Optional[bool] = None
    only_from_tenant: Optional[bool] = None
    is_verified: Optional[bool] = None
    is_official: Optional[bool] = None
    is_metorial: Optional[bool] = None
    order_by_rank: Optional[bool] = None
    order_by_use: Optional[str] = None
    created_at: Optional[DashboardInstanceProviderListingsListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceProviderListingsListQueryUpdatedAt] = None


class mapDashboardInstanceProviderListingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsListQuery:
        return DashboardInstanceProviderListingsListQuery(
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
        capabilities=mapDashboardInstanceProviderListingsListQueryCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None,
        is_public=data.get('is_public'),
        only_from_tenant=data.get('only_from_tenant'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official'),
        is_metorial=data.get('is_metorial'),
        order_by_rank=data.get('order_by_rank'),
        order_by_use=data.get('order_by_use'),
        created_at=mapDashboardInstanceProviderListingsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceProviderListingsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

