from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderListingsGetOutputFlags:
    is_public: bool
    is_customized: bool
    is_metorial: bool
    is_verified: bool
    is_official: bool
@dataclass
class ManagementInstanceProviderListingsGetOutputCategories:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderListingsGetOutputCollections:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
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
    name: str
    slug: str
    image_url: str
    skills: List[str]
    flags: ManagementInstanceProviderListingsGetOutputFlags
    categories: List[ManagementInstanceProviderListingsGetOutputCategories]
    collections: List[ManagementInstanceProviderListingsGetOutputCollections]
    groups: List[ManagementInstanceProviderListingsGetOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
    provider_id: Optional[str] = None


class mapManagementInstanceProviderListingsGetOutputFlags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderListingsGetOutputFlags:
        return ManagementInstanceProviderListingsGetOutputFlags(
        is_public=data.get('is_public'),
        is_customized=data.get('is_customized'),
        is_metorial=data.get('is_metorial'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderListingsGetOutputFlags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        readme=data.get('readme'),
        skills=data.get('skills', []),
        flags=mapManagementInstanceProviderListingsGetOutputFlags.from_dict(data.get('flags')) if data.get('flags') else None,
        provider_id=data.get('provider_id'),
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
