from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsAccessRequestsUpdateOutputConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class ManagementInstancePortalsAccessRequestsUpdateOutput:
    object: str
    id: str
    status: str
    consumer_profile: ManagementInstancePortalsAccessRequestsUpdateOutputConsumerProfile
    target: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    message: Optional[str] = None
    resolution_message: Optional[str] = None
    reviewed_at: Optional[datetime] = None


class mapManagementInstancePortalsAccessRequestsUpdateOutputConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAccessRequestsUpdateOutputConsumerProfile:
        return ManagementInstancePortalsAccessRequestsUpdateOutputConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAccessRequestsUpdateOutputConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAccessRequestsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAccessRequestsUpdateOutput:
        return ManagementInstancePortalsAccessRequestsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        message=data.get('message'),
        resolution_message=data.get('resolution_message'),
        consumer_profile=mapManagementInstancePortalsAccessRequestsUpdateOutputConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        target=data.get('target'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        reviewed_at=datetime.fromisoformat(data.get('reviewed_at').replace('Z', '+00:00')) if data.get('reviewed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAccessRequestsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsAccessRequestsUpdateBody:
    status: str
    resolution_message: Optional[str] = None
    consumer_group_id: Optional[str] = None


class mapManagementInstancePortalsAccessRequestsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAccessRequestsUpdateBody:
        return ManagementInstancePortalsAccessRequestsUpdateBody(
        status=data.get('status'),
        resolution_message=data.get('resolution_message'),
        consumer_group_id=data.get('consumer_group_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAccessRequestsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

