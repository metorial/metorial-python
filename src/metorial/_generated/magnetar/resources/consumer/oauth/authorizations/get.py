from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerOauthAuthorizationsGetOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ConsumerOauthAuthorizationsGetOutputOauthApplication:
    id: str
    name: str
    image_url: str
    description: Optional[str] = None
    website_url: Optional[str] = None
@dataclass
class ConsumerOauthAuthorizationsGetOutput:
    object: str
    id: str
    status: str
    scopes: List[ConsumerOauthAuthorizationsGetOutputScopes]
    oauth_application: ConsumerOauthAuthorizationsGetOutputOauthApplication
    created_at: datetime
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapConsumerOauthAuthorizationsGetOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsGetOutputScopes:
        return ConsumerOauthAuthorizationsGetOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsGetOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsGetOutputOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsGetOutputOauthApplication:
        return ConsumerOauthAuthorizationsGetOutputOauthApplication(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        website_url=data.get('website_url')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsGetOutputOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsGetOutput:
        return ConsumerOauthAuthorizationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        scopes=[mapConsumerOauthAuthorizationsGetOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        oauth_application=mapConsumerOauthAuthorizationsGetOutputOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

