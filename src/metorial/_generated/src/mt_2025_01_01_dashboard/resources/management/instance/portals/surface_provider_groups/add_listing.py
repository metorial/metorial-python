from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsAddListingOutput:
    object: str
    id: str
    name: str
    index: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsSurfaceProviderGroupsAddListingOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsAddListingOutput:
        return ManagementInstancePortalsSurfaceProviderGroupsAddListingOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsAddListingOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsAddListingBody:
    consumer_access_listing_id: str


class mapManagementInstancePortalsSurfaceProviderGroupsAddListingBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsAddListingBody:
        return ManagementInstancePortalsSurfaceProviderGroupsAddListingBody(
        consumer_access_listing_id=data.get('consumer_access_listing_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsAddListingBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

