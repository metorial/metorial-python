from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsAccessUpdateOutputConsumerGroup:
    object: str
    id: str
    status: str
    name: str
    is_default: bool
    sso_group_ids: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class PortalsAccessUpdateOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    consumer_group: PortalsAccessUpdateOutputConsumerGroup
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None


class mapPortalsAccessUpdateOutputConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAccessUpdateOutputConsumerGroup:
        return PortalsAccessUpdateOutputConsumerGroup(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        is_default=data.get('is_default'),
        sso_group_ids=data.get('sso_group_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsAccessUpdateOutputConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsAccessUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAccessUpdateOutput:
        return PortalsAccessUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        consumer_group=mapPortalsAccessUpdateOutputConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsAccessUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsAccessUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    readme: Optional[str] = None


class mapPortalsAccessUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAccessUpdateBody:
        return PortalsAccessUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme')
        )

    @staticmethod
    def to_dict(value: Union[PortalsAccessUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

