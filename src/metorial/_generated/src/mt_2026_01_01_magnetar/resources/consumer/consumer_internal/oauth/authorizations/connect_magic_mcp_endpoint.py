from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutputOauthClient:
    object: str
    id: str
    name: str
    client_id: str
    redirect_uris: List[str]
    token_endpoint_auth_method: str
    consumer_surface_id: str
    created_at: datetime
    expires_at: datetime
    portal_id: Optional[str] = None
    magic_mcp_server_id: Optional[str] = None
    magic_mcp_endpoint_id: Optional[str] = None
@dataclass
class ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput:
    object: str
    id: str
    status: str
    redirect_uri: str
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    oauth_client: ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutputOauthClient
    redirect_url: Optional[str] = None
    consumer_profile_id: Optional[str] = None
    magic_mcp_endpoint_id: Optional[str] = None
    authorized_at: Optional[datetime] = None
    denied_at: Optional[datetime] = None


class mapConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutputOauthClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutputOauthClient:
        return ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutputOauthClient(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        client_id=data.get('client_id'),
        redirect_uris=data.get('redirect_uris', []),
        token_endpoint_auth_method=data.get('token_endpoint_auth_method'),
        portal_id=data.get('portal_id'),
        consumer_surface_id=data.get('consumer_surface_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutputOauthClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput:
        return ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        redirect_uri=data.get('redirect_uri'),
        redirect_url=data.get('redirect_url'),
        consumer_profile_id=data.get('consumer_profile_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        authorized_at=datetime.fromisoformat(data.get('authorized_at').replace('Z', '+00:00')) if data.get('authorized_at') else None,
        denied_at=datetime.fromisoformat(data.get('denied_at').replace('Z', '+00:00')) if data.get('denied_at') else None,
        oauth_client=mapConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutputOauthClient.from_dict(data.get('oauth_client')) if data.get('oauth_client') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointBody:
    magic_mcp_endpoint_id: str


class mapConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointBody:
        return ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointBody(
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthAuthorizationsConnectMagicMcpEndpointBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

