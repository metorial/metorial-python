from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOutpostsCredentialsCreateOutput:
    object: str
    id: str
    status: str
    outpost_id: str
    name: str
    envelope_preview: str
    created_at: datetime
    updated_at: datetime
    envelope: Optional[str] = None
    expires_at: Optional[datetime] = None


class mapDashboardOrganizationsOutpostsCredentialsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsCredentialsCreateOutput:
        return DashboardOrganizationsOutpostsCredentialsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        outpost_id=data.get('outpost_id'),
        name=data.get('name'),
        envelope_preview=data.get('envelope_preview'),
        envelope=data.get('envelope'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsCredentialsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsOutpostsCredentialsCreateBody:
    name: str
    expires_at: Optional[datetime] = None


class mapDashboardOrganizationsOutpostsCredentialsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsCredentialsCreateBody:
        return DashboardOrganizationsOutpostsCredentialsCreateBody(
        name=data.get('name'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsCredentialsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

