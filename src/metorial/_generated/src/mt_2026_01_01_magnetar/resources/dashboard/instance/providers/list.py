from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProvidersListOutputItemsOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class DashboardInstanceProvidersListOutputItemsPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProvidersListOutputItemsEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceProvidersListOutputItemsDefaultVariantCurrentVersion:
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
class DashboardInstanceProvidersListOutputItemsDefaultVariant:
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
    current_version: Optional[DashboardInstanceProvidersListOutputItemsDefaultVariantCurrentVersion] = None
@dataclass
class DashboardInstanceProvidersListOutputItemsCurrentVersion:
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
class DashboardInstanceProvidersListOutputItemsType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceProvidersListOutputItemsOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceProvidersListOutputItemsOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[DashboardInstanceProvidersListOutputItemsOauthAutoRegistration] = None
@dataclass
class DashboardInstanceProvidersListOutputItems:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceProvidersListOutputItemsPublisher
    entry: DashboardInstanceProvidersListOutputItemsEntry
    type: DashboardInstanceProvidersListOutputItemsType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[DashboardInstanceProvidersListOutputItemsOwnerTenant] = None
    default_variant: Optional[DashboardInstanceProvidersListOutputItemsDefaultVariant] = None
    current_version: Optional[DashboardInstanceProvidersListOutputItemsCurrentVersion] = None
    oauth: Optional[DashboardInstanceProvidersListOutputItemsOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProvidersListOutput:
    items: List[DashboardInstanceProvidersListOutputItems]
    pagination: DashboardInstanceProvidersListOutputPagination


class mapDashboardInstanceProvidersListOutputItemsOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsOwnerTenant:
        return DashboardInstanceProvidersListOutputItemsOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsPublisher:
        return DashboardInstanceProvidersListOutputItemsPublisher(
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
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsEntry:
        return DashboardInstanceProvidersListOutputItemsEntry(
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
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsDefaultVariantCurrentVersion:
        return DashboardInstanceProvidersListOutputItemsDefaultVariantCurrentVersion(
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
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsDefaultVariant:
        return DashboardInstanceProvidersListOutputItemsDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapDashboardInstanceProvidersListOutputItemsDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsCurrentVersion:
        return DashboardInstanceProvidersListOutputItemsCurrentVersion(
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
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsType:
        return DashboardInstanceProvidersListOutputItemsType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsOauthAutoRegistration:
        return DashboardInstanceProvidersListOutputItemsOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItemsOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItemsOauth:
        return DashboardInstanceProvidersListOutputItemsOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapDashboardInstanceProvidersListOutputItemsOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItemsOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputItems:
        return DashboardInstanceProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapDashboardInstanceProvidersListOutputItemsOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapDashboardInstanceProvidersListOutputItemsPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapDashboardInstanceProvidersListOutputItemsEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapDashboardInstanceProvidersListOutputItemsDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapDashboardInstanceProvidersListOutputItemsCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapDashboardInstanceProvidersListOutputItemsType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapDashboardInstanceProvidersListOutputItemsOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
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
    def to_dict(value: Union[DashboardInstanceProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutputPagination:
        return DashboardInstanceProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListOutput:
        return DashboardInstanceProvidersListOutput(
        items=[mapDashboardInstanceProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersListQuery:
        return DashboardInstanceProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
