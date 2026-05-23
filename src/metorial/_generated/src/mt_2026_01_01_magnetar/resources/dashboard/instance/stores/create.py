from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceStoresCreateOutput:
    object: str
    id: str
    name: str
    access: str
    item_count: float
    created_at: datetime
    updated_at: datetime


class mapDashboardInstanceStoresCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresCreateOutput:
        return DashboardInstanceStoresCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        access=data.get('access'),
        item_count=data.get('item_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceStoresCreateBody:
    name: str
    access: Optional[str] = None
    template_id: Optional[str] = None
    parent_id: Optional[str] = None


class mapDashboardInstanceStoresCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresCreateBody:
        return DashboardInstanceStoresCreateBody(
        name=data.get('name'),
        access=data.get('access'),
        template_id=data.get('template_id'),
        parent_id=data.get('parent_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

