from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerConsumerInternalOauthAuthorizationsGetOutputSkillPlugin:
    id: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClientSkillPlugin:
    id: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClient:
    object: str
    id: str
    name: str
    client_id: str
    redirect_uris: List[str]
    token_endpoint_auth_method: str
    created_at: datetime
    expires_at: datetime
    portal_id: Optional[str] = None
    consumer_surface_id: Optional[str] = None
    skill_plugin: Optional[ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClientSkillPlugin] = None
    magic_mcp_server_id: Optional[str] = None
    magic_mcp_endpoint_id: Optional[str] = None
@dataclass
class ConsumerConsumerInternalOauthAuthorizationsGetOutput:
    object: str
    id: str
    status: str
    redirect_uri: str
    skill_plugin_supported_provider_ids: List[str]
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    oauth_client: ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClient
    redirect_url: Optional[str] = None
    consumer_profile_id: Optional[str] = None
    magic_mcp_endpoint_id: Optional[str] = None
    skill_plugin: Optional[ConsumerConsumerInternalOauthAuthorizationsGetOutputSkillPlugin] = None
    authorized_at: Optional[datetime] = None
    denied_at: Optional[datetime] = None


class mapConsumerConsumerInternalOauthAuthorizationsGetOutputSkillPlugin:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthAuthorizationsGetOutputSkillPlugin:
        return ConsumerConsumerInternalOauthAuthorizationsGetOutputSkillPlugin(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthAuthorizationsGetOutputSkillPlugin, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClientSkillPlugin:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClientSkillPlugin:
        return ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClientSkillPlugin(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClientSkillPlugin, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClient:
        return ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClient(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        client_id=data.get('client_id'),
        redirect_uris=data.get('redirect_uris', []),
        token_endpoint_auth_method=data.get('token_endpoint_auth_method'),
        portal_id=data.get('portal_id'),
        consumer_surface_id=data.get('consumer_surface_id'),
        skill_plugin=mapConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClientSkillPlugin.from_dict(data.get('skill_plugin')) if data.get('skill_plugin') else None,
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerConsumerInternalOauthAuthorizationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthAuthorizationsGetOutput:
        return ConsumerConsumerInternalOauthAuthorizationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        redirect_uri=data.get('redirect_uri'),
        redirect_url=data.get('redirect_url'),
        consumer_profile_id=data.get('consumer_profile_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id'),
        skill_plugin=mapConsumerConsumerInternalOauthAuthorizationsGetOutputSkillPlugin.from_dict(data.get('skill_plugin')) if data.get('skill_plugin') else None,
        skill_plugin_supported_provider_ids=data.get('skill_plugin_supported_provider_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        authorized_at=datetime.fromisoformat(data.get('authorized_at').replace('Z', '+00:00')) if data.get('authorized_at') else None,
        denied_at=datetime.fromisoformat(data.get('denied_at').replace('Z', '+00:00')) if data.get('denied_at') else None,
        oauth_client=mapConsumerConsumerInternalOauthAuthorizationsGetOutputOauthClient.from_dict(data.get('oauth_client')) if data.get('oauth_client') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthAuthorizationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

