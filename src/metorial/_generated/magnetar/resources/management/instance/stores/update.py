from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceStoresUpdateOutput:
    object: str
    id: str
    name: str
    access: str
    item_count: float
    created_at: datetime
    updated_at: datetime


class mapManagementInstanceStoresUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresUpdateOutput:
        return ManagementInstanceStoresUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        access=data.get('access'),
        item_count=data.get('item_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceStoresUpdateBody:
    name: Optional[str] = None
    access: Optional[str] = None


class mapManagementInstanceStoresUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresUpdateBody:
        return ManagementInstanceStoresUpdateBody(
        name=data.get('name'),
        access=data.get('access')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

