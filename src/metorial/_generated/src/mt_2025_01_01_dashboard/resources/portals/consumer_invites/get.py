from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerInvitesGetOutputConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class PortalsConsumerInvitesGetOutputInvitedBy:
    object: str
    id: str
    name: str
    email: Optional[str] = None
@dataclass
class PortalsConsumerInvitesGetOutput:
    object: str
    id: str
    status: str
    consumer_profile: PortalsConsumerInvitesGetOutputConsumerProfile
    invited_by: PortalsConsumerInvitesGetOutputInvitedBy
    created_at: datetime
    updated_at: datetime
    portal_url: Optional[str] = None
    message: Optional[str] = None
    accepted_at: Optional[datetime] = None


class mapPortalsConsumerInvitesGetOutputConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerInvitesGetOutputConsumerProfile:
        return PortalsConsumerInvitesGetOutputConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerInvitesGetOutputConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerInvitesGetOutputInvitedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerInvitesGetOutputInvitedBy:
        return PortalsConsumerInvitesGetOutputInvitedBy(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerInvitesGetOutputInvitedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerInvitesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerInvitesGetOutput:
        return PortalsConsumerInvitesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        portal_url=data.get('portal_url'),
        consumer_profile=mapPortalsConsumerInvitesGetOutputConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        invited_by=mapPortalsConsumerInvitesGetOutputInvitedBy.from_dict(data.get('invited_by')) if data.get('invited_by') else None,
        message=data.get('message'),
        accepted_at=datetime.fromisoformat(data.get('accepted_at').replace('Z', '+00:00')) if data.get('accepted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerInvitesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

