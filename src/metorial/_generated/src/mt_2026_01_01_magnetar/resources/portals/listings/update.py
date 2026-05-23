from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsListingsUpdateOutputGroups:
    id: str
    name: str
    index: float
    description: Optional[str] = None
@dataclass
class PortalsListingsUpdateOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    groups: List[PortalsListingsUpdateOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapPortalsListingsUpdateOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsUpdateOutputGroups:
        return PortalsListingsUpdateOutputGroups(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsUpdateOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListingsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsUpdateOutput:
        return PortalsListingsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        groups=[mapPortalsListingsUpdateOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsListingsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    readme: Optional[str] = None


class mapPortalsListingsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsUpdateBody:
        return PortalsListingsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

