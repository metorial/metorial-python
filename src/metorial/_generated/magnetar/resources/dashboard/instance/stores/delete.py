from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceStoresDeleteOutput:
    object: str
    id: str
    name: str
    access: str
    item_count: float
    created_at: datetime
    updated_at: datetime


class mapDashboardInstanceStoresDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresDeleteOutput:
        return DashboardInstanceStoresDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        access=data.get('access'),
        item_count=data.get('item_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

