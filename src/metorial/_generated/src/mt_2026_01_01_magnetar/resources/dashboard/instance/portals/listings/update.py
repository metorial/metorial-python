from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsListingsUpdateOutputGroups:
    id: str
    name: str
    index: float
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsListingsUpdateOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    groups: List[DashboardInstancePortalsListingsUpdateOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapDashboardInstancePortalsListingsUpdateOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListingsUpdateOutputGroups:
        return DashboardInstancePortalsListingsUpdateOutputGroups(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListingsUpdateOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListingsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListingsUpdateOutput:
        return DashboardInstancePortalsListingsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        groups=[mapDashboardInstancePortalsListingsUpdateOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListingsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsListingsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    readme: Optional[str] = None


class mapDashboardInstancePortalsListingsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListingsUpdateBody:
        return DashboardInstancePortalsListingsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListingsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

