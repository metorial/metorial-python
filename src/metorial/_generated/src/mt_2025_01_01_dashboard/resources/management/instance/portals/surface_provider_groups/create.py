from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsCreateOutput:
    object: str
    id: str
    name: str
    index: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstancePortalsSurfaceProviderGroupsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsCreateOutput:
        return ManagementInstancePortalsSurfaceProviderGroupsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsCreateBody:
    name: str
    description: Optional[str] = None


class mapManagementInstancePortalsSurfaceProviderGroupsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsCreateBody:
        return ManagementInstancePortalsSurfaceProviderGroupsCreateBody(
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

