from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerGroupsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    is_default: bool
    sso_group_ids: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapPortalsConsumerGroupsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerGroupsCreateOutput:
        return PortalsConsumerGroupsCreateOutput(
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
    def to_dict(value: Union[PortalsConsumerGroupsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsConsumerGroupsCreateBody:
    name: str
    description: Optional[str] = None
    sso_group_ids: Optional[List[str]] = None
    is_default: Optional[bool] = None


class mapPortalsConsumerGroupsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerGroupsCreateBody:
        return PortalsConsumerGroupsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        sso_group_ids=data.get('sso_group_ids', []),
        is_default=data.get('is_default')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerGroupsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

