from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderListingsGetOutputFlags:
    is_public: bool
    is_customized: bool
    is_metorial: bool
    is_verified: bool
    is_official: bool
@dataclass
class DashboardInstanceProviderListingsGetOutputCategories:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderListingsGetOutputCollections:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderListingsGetOutputGroups:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderListingsGetOutput:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    skills: List[str]
    flags: DashboardInstanceProviderListingsGetOutputFlags
    categories: List[DashboardInstanceProviderListingsGetOutputCategories]
    collections: List[DashboardInstanceProviderListingsGetOutputCollections]
    groups: List[DashboardInstanceProviderListingsGetOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
    provider_id: Optional[str] = None


class mapDashboardInstanceProviderListingsGetOutputFlags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsGetOutputFlags:
        return DashboardInstanceProviderListingsGetOutputFlags(
        is_public=data.get('is_public'),
        is_customized=data.get('is_customized'),
        is_metorial=data.get('is_metorial'),
        is_verified=data.get('is_verified'),
        is_official=data.get('is_official')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsGetOutputFlags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsGetOutputCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsGetOutputCategories:
        return DashboardInstanceProviderListingsGetOutputCategories(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsGetOutputCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsGetOutputCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsGetOutputCollections:
        return DashboardInstanceProviderListingsGetOutputCollections(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsGetOutputCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsGetOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsGetOutputGroups:
        return DashboardInstanceProviderListingsGetOutputGroups(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsGetOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderListingsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderListingsGetOutput:
        return DashboardInstanceProviderListingsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        readme=data.get('readme'),
        skills=data.get('skills', []),
        flags=mapDashboardInstanceProviderListingsGetOutputFlags.from_dict(data.get('flags')) if data.get('flags') else None,
        provider_id=data.get('provider_id'),
        categories=[mapDashboardInstanceProviderListingsGetOutputCategories.from_dict(item) for item in data.get('categories', []) if item],
        collections=[mapDashboardInstanceProviderListingsGetOutputCollections.from_dict(item) for item in data.get('collections', []) if item],
        groups=[mapDashboardInstanceProviderListingsGetOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderListingsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
