from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderListingsGetOutputAttributes:
    is_public: bool
    is_customized: bool
    is_metorial: bool
    is_verified: bool
    is_official: bool
@dataclass
class ProviderListingsGetOutputProviderPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderListingsGetOutputProviderCurrentVersion:
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
class ProviderListingsGetOutputProviderOauthAutoRegistration:
    status: str
@dataclass
class ProviderListingsGetOutputProviderOauth:
    status: str
    auto_registration: ProviderListingsGetOutputProviderOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ProviderListingsGetOutputProvider:
    object: str
    id: str
    access: str
    status: str
    publisher: ProviderListingsGetOutputProviderPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    current_version: Optional[ProviderListingsGetOutputProviderCurrentVersion] = None
    oauth: Optional[ProviderListingsGetOutputProviderOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderListingsGetOutputCategories:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProviderListingsGetOutputCollections:
    object: str
    id: str
    name: str
    description: str
    slug: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProviderListingsGetOutputGroups:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderListingsGetOutput:
    object: str
    id: str
    attributes: ProviderListingsGetOutputAttributes
    name: str
    slug: str
    image_url: str
    skills: List[str]
    provider: ProviderListingsGetOutputProvider
    categories: List[ProviderListingsGetOutputCategories]
    collections: List[ProviderListingsGetOutputCollections]
    groups: List[ProviderListingsGetOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapProviderListingsGetOutputAttributes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputAttributes:
        return ProviderListingsGetOutputAttributes(
        is_public=data.get('is_public'),
        is_customized=data.get('is_customized'),
        is_metorial=data.get('is_metorial'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official')
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputAttributes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputProviderPublisher:
        return ProviderListingsGetOutputProviderPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputProviderCurrentVersion:
        return ProviderListingsGetOutputProviderCurrentVersion(
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
    def to_dict(value: Union[ProviderListingsGetOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputProviderOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputProviderOauthAutoRegistration:
        return ProviderListingsGetOutputProviderOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputProviderOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputProviderOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputProviderOauth:
        return ProviderListingsGetOutputProviderOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapProviderListingsGetOutputProviderOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputProviderOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputProvider:
        return ProviderListingsGetOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapProviderListingsGetOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapProviderListingsGetOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapProviderListingsGetOutputProviderOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputCategories:
        return ProviderListingsGetOutputCategories(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputCollections:
        return ProviderListingsGetOutputCollections(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutputGroups:
        return ProviderListingsGetOutputGroups(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderListingsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderListingsGetOutput:
        return ProviderListingsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        attributes=mapProviderListingsGetOutputAttributes.from_dict(data.get('attributes')) if data.get('attributes') else None,
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        readme=data.get('readme'),
        skills=data.get('skills', []),
        provider=mapProviderListingsGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        categories=[mapProviderListingsGetOutputCategories.from_dict(item) for item in data.get('categories', []) if item],
        collections=[mapProviderListingsGetOutputCollections.from_dict(item) for item in data.get('collections', []) if item],
        groups=[mapProviderListingsGetOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderListingsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

