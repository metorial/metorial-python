from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsSurfaceProviderGroupsUpdateOutput:
    object: str
    id: str
    name: str
    index: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstancePortalsSurfaceProviderGroupsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsSurfaceProviderGroupsUpdateOutput:
        return DashboardInstancePortalsSurfaceProviderGroupsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsSurfaceProviderGroupsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsSurfaceProviderGroupsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    index: Optional[float] = None


class mapDashboardInstancePortalsSurfaceProviderGroupsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsSurfaceProviderGroupsUpdateBody:
        return DashboardInstancePortalsSurfaceProviderGroupsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsSurfaceProviderGroupsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

