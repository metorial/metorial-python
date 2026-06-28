from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsListingsCreateOutputGroups:
    id: str
    name: str
    index: float
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsListingsCreateOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    groups: List[DashboardInstancePortalsListingsCreateOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapDashboardInstancePortalsListingsCreateOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListingsCreateOutputGroups:
        return DashboardInstancePortalsListingsCreateOutputGroups(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListingsCreateOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsListingsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListingsCreateOutput:
        return DashboardInstancePortalsListingsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        groups=[mapDashboardInstancePortalsListingsCreateOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListingsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsListingsCreateBody:
    access: Dict[str, Any]
    name: Optional[str] = None
    description: Optional[str] = None
    readme: Optional[str] = None


class mapDashboardInstancePortalsListingsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsListingsCreateBody:
        return DashboardInstancePortalsListingsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsListingsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

