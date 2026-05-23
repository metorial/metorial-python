from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsListingsCreateOutputGroups:
    id: str
    name: str
    index: float
    description: Optional[str] = None
@dataclass
class PortalsListingsCreateOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    groups: List[PortalsListingsCreateOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapPortalsListingsCreateOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsCreateOutputGroups:
        return PortalsListingsCreateOutputGroups(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsCreateOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListingsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsCreateOutput:
        return PortalsListingsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        groups=[mapPortalsListingsCreateOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsListingsCreateBody:
    access: Dict[str, Any]
    name: Optional[str] = None
    description: Optional[str] = None
    readme: Optional[str] = None


class mapPortalsListingsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsCreateBody:
        return PortalsListingsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

