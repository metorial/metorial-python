from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOauthAuthorizationRequestsRejectOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOauthAuthorizationRequestsRejectOutputOauthApplication:
    object: str
    id: str
    status: str
    type: str
    access_level: str
    allow_token_exchange_without_client_secret: bool
    name: str
    scopes: List[DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationScopes]
    image_url: str
    redirect_uris: List[str]
    client_id: str
    client_secrets: List[DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationClientSecrets]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    website_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    terms_of_service_url: Optional[str] = None
    organization_id: Optional[str] = None
@dataclass
class DashboardOauthAuthorizationRequestsRejectOutput:
    object: str
    id: str
    status: str
    type: str
    scopes: List[DashboardOauthAuthorizationRequestsRejectOutputScopes]
    created_at: datetime
    oauth_application: DashboardOauthAuthorizationRequestsRejectOutputOauthApplication
    user_code: Optional[str] = None
    redirect_uri: Optional[str] = None
    redirect_url: Optional[str] = None


class mapDashboardOauthAuthorizationRequestsRejectOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsRejectOutputScopes:
        return DashboardOauthAuthorizationRequestsRejectOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsRejectOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsRejectOutputOauthApplicationScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationScopes:
        return DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsRejectOutputOauthApplicationClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationClientSecrets:
        return DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsRejectOutputOauthApplicationClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsRejectOutputOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsRejectOutputOauthApplication:
        return DashboardOauthAuthorizationRequestsRejectOutputOauthApplication(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        access_level=data.get('access_level'),
        allow_token_exchange_without_client_secret=data.get('allow_token_exchange_without_client_secret'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOauthAuthorizationRequestsRejectOutputOauthApplicationScopes.from_dict(item) for item in data.get('scopes', []) if item],
        image_url=data.get('image_url'),
        website_url=data.get('website_url'),
        privacy_policy_url=data.get('privacy_policy_url'),
        terms_of_service_url=data.get('terms_of_service_url'),
        redirect_uris=data.get('redirect_uris', []),
        client_id=data.get('client_id'),
        client_secrets=[mapDashboardOauthAuthorizationRequestsRejectOutputOauthApplicationClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsRejectOutputOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOauthAuthorizationRequestsRejectOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsRejectOutput:
        return DashboardOauthAuthorizationRequestsRejectOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        user_code=data.get('user_code'),
        redirect_uri=data.get('redirect_uri'),
        scopes=[mapDashboardOauthAuthorizationRequestsRejectOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        oauth_application=mapDashboardOauthAuthorizationRequestsRejectOutputOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsRejectOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOauthAuthorizationRequestsRejectBody:
    organization_id: Optional[str] = None


class mapDashboardOauthAuthorizationRequestsRejectBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOauthAuthorizationRequestsRejectBody:
        return DashboardOauthAuthorizationRequestsRejectBody(
        organization_id=data.get('organization_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOauthAuthorizationRequestsRejectBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

