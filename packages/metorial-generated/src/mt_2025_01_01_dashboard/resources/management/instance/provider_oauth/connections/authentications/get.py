from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputError:
    code: str
    message: Optional[str] = None
@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents:
    id: str
    type: str
    metadata: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile:
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
class ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutput:
    object: str
    id: str
    status: str
    events: List[ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents]
    connection_id: str
    created_at: datetime
    error: Optional[ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputError] = None
    profile: Optional[ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile] = None


class mapManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputError:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents(
        id=data.get('id'),
        type=data.get('type'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile(
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
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutput:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        events=[mapManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputEvents.from_dict(item) for item in data.get('events', []) if item],
        connection_id=data.get('connection_id'),
        profile=mapManagementInstanceProviderOauthConnectionsAuthenticationsGetOutputProfile.from_dict(data.get('profile')) if data.get('profile') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

