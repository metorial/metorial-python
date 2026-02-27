from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderListingsGetOutputAttributes:
    is_public: bool
    is_customized: bool
    is_metorial: bool
    is_verified: bool
    is_official: bool
@dataclass
class ManagementInstanceProviderListingsGetOutputProviderOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class ManagementInstanceProviderListingsGetOutputProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderListingsGetOutputProviderEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProviderListingsGetOutputProviderDefaultVariantCurrentVersion:
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
class ManagementInstanceProviderListingsGetOutputProviderDefaultVariant:
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
    current_version: Optional[ManagementInstanceProviderListingsGetOutputProviderDefaultVariantCurrentVersion] = None
@dataclass
class ManagementInstanceProviderListingsGetOutputProviderCurrentVersion:
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
class ManagementInstanceProviderListingsGetOutputProviderType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceProviderListingsGetOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceProviderListingsGetOutputProviderOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[ManagementInstanceProviderListingsGetOutputProviderOauthAutoRegistration] = None
@dataclass
class ManagementInstanceProviderListingsGetOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceProviderListingsGetOutputProviderPublisher
    entry: ManagementInstanceProviderListingsGetOutputProviderEntry
    type: ManagementInstanceProviderListingsGetOutputProviderType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[ManagementInstanceProviderListingsGetOutputProviderOwnerTenant] = None
    default_variant: Optional[ManagementInstanceProviderListingsGetOutputProviderDefaultVariant] = None
    current_version: Optional[ManagementInstanceProviderListingsGetOutputProviderCurrentVersion] = None
    oauth: Optional[ManagementInstanceProviderListingsGetOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProviderListingsGetOutputCategories:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceProviderListingsGetOutputCollections:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceProviderListingsGetOutputGroups:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderListingsGetOutput:
    object: str
    id: str
    attributes: ManagementInstanceProviderListingsGetOutputAttributes
    name: str
    slug: str
    image_url: str
    skills: List[str]
    provider: ManagementInstanceProviderListingsGetOutputProvider
    categories: List[ManagementInstanceProviderListingsGetOutputCategories]
    collections: List[ManagementInstanceProviderListingsGetOutputCollections]
    groups: List[ManagementInstanceProviderListingsGetOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapManagementInstanceProviderListingsGetOutputAttributes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputAttributes:
        return ManagementInstanceProviderListingsGetOutputAttributes(
        is_public=data.get('is_public'),
        is_customized=data.get('is_customized'),
        is_metorial=data.get('is_metorial'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputAttributes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderOwnerTenant:
        return ManagementInstanceProviderListingsGetOutputProviderOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderPublisher:
        return ManagementInstanceProviderListingsGetOutputProviderPublisher(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderEntry:
        return ManagementInstanceProviderListingsGetOutputProviderEntry(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderDefaultVariantCurrentVersion:
        return ManagementInstanceProviderListingsGetOutputProviderDefaultVariantCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderDefaultVariant:
        return ManagementInstanceProviderListingsGetOutputProviderDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapManagementInstanceProviderListingsGetOutputProviderDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderCurrentVersion:
        return ManagementInstanceProviderListingsGetOutputProviderCurrentVersion(
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
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderType:
        return ManagementInstanceProviderListingsGetOutputProviderType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderOauthAutoRegistration:
        return ManagementInstanceProviderListingsGetOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProviderOauth:
        return ManagementInstanceProviderListingsGetOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapManagementInstanceProviderListingsGetOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputProvider:
        return ManagementInstanceProviderListingsGetOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapManagementInstanceProviderListingsGetOutputProviderOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapManagementInstanceProviderListingsGetOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapManagementInstanceProviderListingsGetOutputProviderEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapManagementInstanceProviderListingsGetOutputProviderDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapManagementInstanceProviderListingsGetOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapManagementInstanceProviderListingsGetOutputProviderType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapManagementInstanceProviderListingsGetOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
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
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputCategories:
        return ManagementInstanceProviderListingsGetOutputCategories(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputCollections:
        return ManagementInstanceProviderListingsGetOutputCollections(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputGroups:
        return ManagementInstanceProviderListingsGetOutputGroups(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderListingsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutput:
        return ManagementInstanceProviderListingsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        attributes=mapManagementInstanceProviderListingsGetOutputAttributes.from_dict(data.get('attributes')) if data.get('attributes') else None,
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        readme=data.get('readme'),
        skills=data.get('skills', []),
        provider=mapManagementInstanceProviderListingsGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        categories=[mapManagementInstanceProviderListingsGetOutputCategories.from_dict(item) for item in data.get('categories', []) if item],
        collections=[mapManagementInstanceProviderListingsGetOutputCollections.from_dict(item) for item in data.get('collections', []) if item],
        groups=[mapManagementInstanceProviderListingsGetOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
