from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SessionsGetOutput:
    object: str
    id: str
    status: str
    connection_status: str
    client_secret: Dict[str, Any]
    server_deployments: List[Dict[str, Any]]
    usage: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsGetOutput:
        return SessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        client_secret=data.get('client_secret') and {
            "object": data.get('client_secret', {}).get('object'),
            "type": data.get('client_secret', {}).get('type'),
            "id": data.get('client_secret', {}).get('id'),
            "secret": data.get('client_secret', {}).get('secret'),
            "expires_at": data.get('client_secret', {}).get('expires_at') and datetime.fromisoformat(data.get('client_secret', {}).get('expires_at'))
        },
        server_deployments=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "name": item.get('name'),
                "description": item.get('description'),
                "metadata": item.get('metadata'),
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "updated_at": item.get('updated_at') and datetime.fromisoformat(item.get('updated_at')),
                "server": item.get('server') and {
                    "object": item.get('server', {}).get('object'),
                    "id": item.get('server', {}).get('id'),
                    "name": item.get('server', {}).get('name'),
                    "description": item.get('server', {}).get('description'),
                    "type": item.get('server', {}).get('type'),
                    "created_at": item.get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server', {}).get('created_at')),
                    "updated_at": item.get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server', {}).get('updated_at'))
                },
                "connection_urls": item.get('connection_urls') and {
                    "sse": item.get('connection_urls', {}).get('sse'),
                    "streamable_http": item.get('connection_urls', {}).get('streamable_http'),
                    "websocket": item.get('connection_urls', {}).get('websocket')
                }
            } for item in data.get('server_deployments', [])],
        usage=data.get('usage') and {
            "total_productive_message_count": data.get('usage', {}).get('total_productive_message_count'),
            "total_productive_client_message_count": data.get('usage', {}).get('total_productive_client_message_count'),
            "total_productive_server_message_count": data.get('usage', {}).get('total_productive_server_message_count')
        },
        metadata=data.get('metadata'),
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at')),
        updated_at=data.get('updated_at') and datetime.fromisoformat(data.get('updated_at'))
        )

    @staticmethod
    def to_dict(value: Union[SessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

