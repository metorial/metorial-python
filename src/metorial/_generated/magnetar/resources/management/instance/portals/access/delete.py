from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsAccessDeleteOutputListing:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstancePortalsAccessDeleteOutputConsumerGroup:
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
class ManagementInstancePortalsAccessDeleteOutput:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    consumer_group: ManagementInstancePortalsAccessDeleteOutputConsumerGroup
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
    listing: Optional[ManagementInstancePortalsAccessDeleteOutputListing] = None


class mapManagementInstancePortalsAccessDeleteOutputListing:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAccessDeleteOutputListing:
        return ManagementInstancePortalsAccessDeleteOutputListing(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAccessDeleteOutputListing, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAccessDeleteOutputConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAccessDeleteOutputConsumerGroup:
        return ManagementInstancePortalsAccessDeleteOutputConsumerGroup(
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
    def to_dict(value: Union[ManagementInstancePortalsAccessDeleteOutputConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAccessDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAccessDeleteOutput:
        return ManagementInstancePortalsAccessDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        listing=mapManagementInstancePortalsAccessDeleteOutputListing.from_dict(data.get('listing')) if data.get('listing') else None,
        access=data.get('access'),
        consumer_group=mapManagementInstancePortalsAccessDeleteOutputConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAccessDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

