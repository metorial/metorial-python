from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputError:
    code: str
    message: Optional[str] = None
@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents:
    id: str
    type: str
    metadata: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile:
    object: str
    id: str
    status: str
    sub: str
    connection_id: str
    created_at: datetime
    last_used_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput:
    object: str
    id: str
    status: str
    events: List[DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents]
    connection_id: str
    created_at: datetime
    error: Optional[DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputError] = None
    profile: Optional[DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile] = None


class mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputError:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents(
        id=data.get('id'),
        type=data.get('type'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sub=data.get('sub'),
        name=data.get('name'),
        email=data.get('email'),
        connection_id=data.get('connection_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at')) if data.get('last_used_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        events=[mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents.from_dict(item) for item in data.get('events', []) if item],
        connection_id=data.get('connection_id'),
        profile=mapDashboardInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile.from_dict(data.get('profile')) if data.get('profile') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

