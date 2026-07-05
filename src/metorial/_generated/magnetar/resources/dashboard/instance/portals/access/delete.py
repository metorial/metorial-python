from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAccessDeleteOutputListing:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsAccessDeleteOutputConsumerGroup:
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
class DashboardInstancePortalsAccessDeleteOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    consumer_group: DashboardInstancePortalsAccessDeleteOutputConsumerGroup
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
    listing: Optional[DashboardInstancePortalsAccessDeleteOutputListing] = None


class mapDashboardInstancePortalsAccessDeleteOutputListing:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessDeleteOutputListing:
        return DashboardInstancePortalsAccessDeleteOutputListing(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessDeleteOutputListing, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessDeleteOutputConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessDeleteOutputConsumerGroup:
        return DashboardInstancePortalsAccessDeleteOutputConsumerGroup(
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
    def to_dict(value: Union[DashboardInstancePortalsAccessDeleteOutputConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessDeleteOutput:
        return DashboardInstancePortalsAccessDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        listing=mapDashboardInstancePortalsAccessDeleteOutputListing.from_dict(data.get('listing')) if data.get('listing') else None,
        access=data.get('access'),
        consumer_group=mapDashboardInstancePortalsAccessDeleteOutputConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

