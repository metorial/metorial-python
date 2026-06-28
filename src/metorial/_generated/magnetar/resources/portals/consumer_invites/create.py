from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerInvitesCreateOutputConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class PortalsConsumerInvitesCreateOutputInvitedBy:
    object: str
    id: str
    name: str
    email: Optional[str] = None
@dataclass
class PortalsConsumerInvitesCreateOutput:
    object: str
    id: str
    status: str
    consumer_profile: PortalsConsumerInvitesCreateOutputConsumerProfile
    invited_by: PortalsConsumerInvitesCreateOutputInvitedBy
    created_at: datetime
    updated_at: datetime
    portal_url: Optional[str] = None
    message: Optional[str] = None
    accepted_at: Optional[datetime] = None


class mapPortalsConsumerInvitesCreateOutputConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerInvitesCreateOutputConsumerProfile:
        return PortalsConsumerInvitesCreateOutputConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerInvitesCreateOutputConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerInvitesCreateOutputInvitedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerInvitesCreateOutputInvitedBy:
        return PortalsConsumerInvitesCreateOutputInvitedBy(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerInvitesCreateOutputInvitedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerInvitesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerInvitesCreateOutput:
        return PortalsConsumerInvitesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        portal_url=data.get('portal_url'),
        consumer_profile=mapPortalsConsumerInvitesCreateOutputConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        invited_by=mapPortalsConsumerInvitesCreateOutputInvitedBy.from_dict(data.get('invited_by')) if data.get('invited_by') else None,
        message=data.get('message'),
        accepted_at=datetime.fromisoformat(data.get('accepted_at').replace('Z', '+00:00')) if data.get('accepted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerInvitesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsConsumerInvitesCreateBody:
    name: str
    email: str
    message: Optional[str] = None


class mapPortalsConsumerInvitesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerInvitesCreateBody:
        return PortalsConsumerInvitesCreateBody(
        name=data.get('name'),
        email=data.get('email'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerInvitesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

