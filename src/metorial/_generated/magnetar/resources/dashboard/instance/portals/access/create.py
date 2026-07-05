from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAccessCreateOutputListing:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsAccessCreateOutputConsumerGroup:
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
class DashboardInstancePortalsAccessCreateOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    consumer_group: DashboardInstancePortalsAccessCreateOutputConsumerGroup
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
    listing: Optional[DashboardInstancePortalsAccessCreateOutputListing] = None


class mapDashboardInstancePortalsAccessCreateOutputListing:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessCreateOutputListing:
        return DashboardInstancePortalsAccessCreateOutputListing(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessCreateOutputListing, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessCreateOutputConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessCreateOutputConsumerGroup:
        return DashboardInstancePortalsAccessCreateOutputConsumerGroup(
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
    def to_dict(value: Union[DashboardInstancePortalsAccessCreateOutputConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessCreateOutput:
        return DashboardInstancePortalsAccessCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        listing=mapDashboardInstancePortalsAccessCreateOutputListing.from_dict(data.get('listing')) if data.get('listing') else None,
        access=data.get('access'),
        consumer_group=mapDashboardInstancePortalsAccessCreateOutputConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsAccessCreateBody:
    consumer_group_id: str
    access: Dict[str, Any]
    name: Optional[str] = None
    description: Optional[str] = None
    readme: Optional[str] = None


class mapDashboardInstancePortalsAccessCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessCreateBody:
        return DashboardInstancePortalsAccessCreateBody(
        consumer_group_id=data.get('consumer_group_id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

