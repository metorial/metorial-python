from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerAccessGetOutputConsumerGroup:
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
class DashboardInstancePortalsConsumerAccessGetOutput:
    object: str
    id: str
    access: Dict[str, Any]
    consumer_group: DashboardInstancePortalsConsumerAccessGetOutputConsumerGroup
    created_at: datetime
    updated_at: datetime


class mapDashboardInstancePortalsConsumerAccessGetOutputConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerAccessGetOutputConsumerGroup:
        return DashboardInstancePortalsConsumerAccessGetOutputConsumerGroup(
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
    def to_dict(value: Union[DashboardInstancePortalsConsumerAccessGetOutputConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerAccessGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerAccessGetOutput:
        return DashboardInstancePortalsConsumerAccessGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        consumer_group=mapDashboardInstancePortalsConsumerAccessGetOutputConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerAccessGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

