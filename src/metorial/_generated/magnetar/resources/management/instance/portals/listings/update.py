from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsListingsUpdateOutputGroups:
    id: str
    name: str
    index: float
    description: Optional[str] = None
@dataclass
class ManagementInstancePortalsListingsUpdateOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    groups: List[ManagementInstancePortalsListingsUpdateOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapManagementInstancePortalsListingsUpdateOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListingsUpdateOutputGroups:
        return ManagementInstancePortalsListingsUpdateOutputGroups(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListingsUpdateOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsListingsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListingsUpdateOutput:
        return ManagementInstancePortalsListingsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        groups=[mapManagementInstancePortalsListingsUpdateOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListingsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsListingsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    readme: Optional[str] = None


class mapManagementInstancePortalsListingsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsListingsUpdateBody:
        return ManagementInstancePortalsListingsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsListingsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

