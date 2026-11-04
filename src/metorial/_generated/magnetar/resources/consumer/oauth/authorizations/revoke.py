from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerOauthAuthorizationsRevokeOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ConsumerOauthAuthorizationsRevokeOutputOauthApplication:
    id: str
    name: str
    image_url: str
    description: Optional[str] = None
    website_url: Optional[str] = None
@dataclass
class ConsumerOauthAuthorizationsRevokeOutput:
    object: str
    id: str
    status: str
    scopes: List[ConsumerOauthAuthorizationsRevokeOutputScopes]
    oauth_application: ConsumerOauthAuthorizationsRevokeOutputOauthApplication
    created_at: datetime
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapConsumerOauthAuthorizationsRevokeOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsRevokeOutputScopes:
        return ConsumerOauthAuthorizationsRevokeOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsRevokeOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsRevokeOutputOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsRevokeOutputOauthApplication:
        return ConsumerOauthAuthorizationsRevokeOutputOauthApplication(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        website_url=data.get('website_url')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsRevokeOutputOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsRevokeOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsRevokeOutput:
        return ConsumerOauthAuthorizationsRevokeOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        scopes=[mapConsumerOauthAuthorizationsRevokeOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        oauth_application=mapConsumerOauthAuthorizationsRevokeOutputOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsRevokeOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

