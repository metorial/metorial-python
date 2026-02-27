from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderGroupsAddListingOutput:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapProviderGroupsAddListingOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderGroupsAddListingOutput:
        return ProviderGroupsAddListingOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderGroupsAddListingOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderGroupsAddListingBody:
    provider_listing_id: str


class mapProviderGroupsAddListingBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderGroupsAddListingBody:
        return ProviderGroupsAddListingBody(
        provider_listing_id=data.get('provider_listing_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderGroupsAddListingBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
