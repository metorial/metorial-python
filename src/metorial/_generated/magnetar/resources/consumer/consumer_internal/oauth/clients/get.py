from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerConsumerInternalOauthClientsGetOutputSkillPlugin:
    id: str
    name: Optional[str] = None
    slug: Optional[str] = None
@dataclass
class ConsumerConsumerInternalOauthClientsGetOutput:
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
    skill_plugin: Optional[ConsumerConsumerInternalOauthClientsGetOutputSkillPlugin] = None
    magic_mcp_server_id: Optional[str] = None
    magic_mcp_endpoint_id: Optional[str] = None


class mapConsumerConsumerInternalOauthClientsGetOutputSkillPlugin:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthClientsGetOutputSkillPlugin:
        return ConsumerConsumerInternalOauthClientsGetOutputSkillPlugin(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthClientsGetOutputSkillPlugin, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerConsumerInternalOauthClientsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerConsumerInternalOauthClientsGetOutput:
        return ConsumerConsumerInternalOauthClientsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        client_id=data.get('client_id'),
        redirect_uris=data.get('redirect_uris', []),
        token_endpoint_auth_method=data.get('token_endpoint_auth_method'),
        portal_id=data.get('portal_id'),
        consumer_surface_id=data.get('consumer_surface_id'),
        skill_plugin=mapConsumerConsumerInternalOauthClientsGetOutputSkillPlugin.from_dict(data.get('skill_plugin')) if data.get('skill_plugin') else None,
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerConsumerInternalOauthClientsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

