from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOauthAuthorizationRequestsGetOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOauthAuthorizationRequestsGetOutputOauthApplicationScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOauthAuthorizationRequestsGetOutputOauthApplicationClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOauthAuthorizationRequestsGetOutputOauthApplication:
    object: str
    id: str
    status: str
    type: str
    access_level: str
    allow_token_exchange_without_client_secret: bool
    name: str
    scopes: List[DashboardOauthAuthorizationRequestsGetOutputOauthApplicationScopes]
    image_url: str
    redirect_uris: List[str]
    client_id: str
    client_secrets: List[DashboardOauthAuthorizationRequestsGetOutputOauthApplicationClientSecrets]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    website_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    terms_of_service_url: Optional[str] = None
    organization_id: Optional[str] = None
@dataclass
class DashboardOauthAuthorizationRequestsGetOutput:
    object: str
    id: str
    status: str
    type: str
    scopes: List[DashboardOauthAuthorizationRequestsGetOutputScopes]
    created_at: datetime
    oauth_application: DashboardOauthAuthorizationRequestsGetOutputOauthApplication
    user_code: Optional[str] = None
    redirect_uri: Optional[str] = None
    redirect_url: Optional[str] = None


class mapDashboardOauthAuthorizationRequestsGetOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsGetOutputScopes:
        return DashboardOauthAuthorizationRequestsGetOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsGetOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsGetOutputOauthApplicationScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsGetOutputOauthApplicationScopes:
        return DashboardOauthAuthorizationRequestsGetOutputOauthApplicationScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsGetOutputOauthApplicationScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsGetOutputOauthApplicationClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsGetOutputOauthApplicationClientSecrets:
        return DashboardOauthAuthorizationRequestsGetOutputOauthApplicationClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsGetOutputOauthApplicationClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsGetOutputOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsGetOutputOauthApplication:
        return DashboardOauthAuthorizationRequestsGetOutputOauthApplication(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        access_level=data.get('access_level'),
        allow_token_exchange_without_client_secret=data.get('allow_token_exchange_without_client_secret'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOauthAuthorizationRequestsGetOutputOauthApplicationScopes.from_dict(item) for item in data.get('scopes', []) if item],
        image_url=data.get('image_url'),
        website_url=data.get('website_url'),
        privacy_policy_url=data.get('privacy_policy_url'),
        terms_of_service_url=data.get('terms_of_service_url'),
        redirect_uris=data.get('redirect_uris', []),
        client_id=data.get('client_id'),
        client_secrets=[mapDashboardOauthAuthorizationRequestsGetOutputOauthApplicationClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsGetOutputOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsGetOutput:
        return DashboardOauthAuthorizationRequestsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        user_code=data.get('user_code'),
        redirect_uri=data.get('redirect_uri'),
        scopes=[mapDashboardOauthAuthorizationRequestsGetOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        oauth_application=mapDashboardOauthAuthorizationRequestsGetOutputOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

