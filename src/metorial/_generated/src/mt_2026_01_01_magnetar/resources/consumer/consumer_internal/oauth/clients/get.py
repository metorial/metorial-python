from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerConsumerInternalOauthClientsGetOutput:
    object: str
    id: str
    name: str
    client_id: str
    redirect_uris: List[str]
    token_endpoint_auth_method: str
    portal_id: str
    magic_mcp_server_id: str
    created_at: datetime
    expires_at: datetime


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
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
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

