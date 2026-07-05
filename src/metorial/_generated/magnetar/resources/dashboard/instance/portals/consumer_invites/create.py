from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerInvitesCreateOutputConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class DashboardInstancePortalsConsumerInvitesCreateOutputInvitedBy:
    object: str
    id: str
    name: str
    email: Optional[str] = None
@dataclass
class DashboardInstancePortalsConsumerInvitesCreateOutput:
    object: str
    id: str
    status: str
    consumer_profile: DashboardInstancePortalsConsumerInvitesCreateOutputConsumerProfile
    invited_by: DashboardInstancePortalsConsumerInvitesCreateOutputInvitedBy
    created_at: datetime
    updated_at: datetime
    portal_url: Optional[str] = None
    message: Optional[str] = None
    accepted_at: Optional[datetime] = None


class mapDashboardInstancePortalsConsumerInvitesCreateOutputConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesCreateOutputConsumerProfile:
        return DashboardInstancePortalsConsumerInvitesCreateOutputConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesCreateOutputConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerInvitesCreateOutputInvitedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesCreateOutputInvitedBy:
        return DashboardInstancePortalsConsumerInvitesCreateOutputInvitedBy(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesCreateOutputInvitedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerInvitesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesCreateOutput:
        return DashboardInstancePortalsConsumerInvitesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        portal_url=data.get('portal_url'),
        consumer_profile=mapDashboardInstancePortalsConsumerInvitesCreateOutputConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        invited_by=mapDashboardInstancePortalsConsumerInvitesCreateOutputInvitedBy.from_dict(data.get('invited_by')) if data.get('invited_by') else None,
        message=data.get('message'),
        accepted_at=datetime.fromisoformat(data.get('accepted_at').replace('Z', '+00:00')) if data.get('accepted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsConsumerInvitesCreateBody:
    name: str
    email: str
    message: Optional[str] = None


class mapDashboardInstancePortalsConsumerInvitesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesCreateBody:
        return DashboardInstancePortalsConsumerInvitesCreateBody(
        name=data.get('name'),
        email=data.get('email'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

