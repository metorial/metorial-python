from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SessionsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutput:
        return SessionsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "connection_status": item.get('connection_status'),
                "client_secret": item.get('client_secret') and {
                    "object": item.get('client_secret', {}).get('object'),
                    "type": item.get('client_secret', {}).get('type'),
                    "id": item.get('client_secret', {}).get('id'),
                    "secret": item.get('client_secret', {}).get('secret'),
                    "expires_at": item.get('client_secret', {}).get('expires_at') and datetime.fromisoformat(item.get('client_secret', {}).get('expires_at'))
                },
                "server_deployments": [{
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
                    } for item in item.get('server_deployments', [])],
                "usage": item.get('usage') and {
                    "total_productive_message_count": item.get('usage', {}).get('total_productive_message_count'),
                    "total_productive_client_message_count": item.get('usage', {}).get('total_productive_client_message_count'),
                    "total_productive_server_message_count": item.get('usage', {}).get('total_productive_server_message_count')
                },
                "metadata": item.get('metadata'),
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "updated_at": item.get('updated_at') and datetime.fromisoformat(item.get('updated_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

SessionsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[SessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

