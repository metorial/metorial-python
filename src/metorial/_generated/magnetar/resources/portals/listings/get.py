from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsListingsGetOutputGroups:
    id: str
    name: str
    index: float
    description: Optional[str] = None
@dataclass
class PortalsListingsGetOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    groups: List[PortalsListingsGetOutputGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapPortalsListingsGetOutputGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsGetOutputGroups:
        return PortalsListingsGetOutputGroups(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsGetOutputGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsListingsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsListingsGetOutput:
        return PortalsListingsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        groups=[mapPortalsListingsGetOutputGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsListingsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

