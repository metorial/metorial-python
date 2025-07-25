from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SessionsConnectionsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutput:
        return SessionsConnectionsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "mcp": item.get('mcp') and {
                    "object": item.get('mcp', {}).get('object'),
                    "version": item.get('mcp', {}).get('version'),
                    "connection_type": item.get('mcp', {}).get('connection_type'),
                    "client": item.get('mcp', {}).get('client') and {
                        "object": item.get('mcp', {}).get('client', {}).get('object'),
                        "name": item.get('mcp', {}).get('client', {}).get('name'),
                        "version": item.get('mcp', {}).get('client', {}).get('version'),
                        "capabilities": item.get('mcp', {}).get('client', {}).get('capabilities')
                    },
                    "server": item.get('mcp', {}).get('server') and {
                        "object": item.get('mcp', {}).get('server', {}).get('object'),
                        "name": item.get('mcp', {}).get('server', {}).get('name'),
                        "version": item.get('mcp', {}).get('server', {}).get('version'),
                        "capabilities": item.get('mcp', {}).get('server', {}).get('capabilities')
                    }
                },
                "usage": item.get('usage') and {
                    "total_productive_message_count": item.get('usage', {}).get('total_productive_message_count'),
                    "total_productive_client_message_count": item.get('usage', {}).get('total_productive_client_message_count'),
                    "total_productive_server_message_count": item.get('usage', {}).get('total_productive_server_message_count')
                },
                "server": item.get('server') and {
                    "object": item.get('server', {}).get('object'),
                    "id": item.get('server', {}).get('id'),
                    "name": item.get('server', {}).get('name'),
                    "description": item.get('server', {}).get('description'),
                    "type": item.get('server', {}).get('type'),
                    "created_at": item.get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server', {}).get('created_at')),
                    "updated_at": item.get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server', {}).get('updated_at'))
                },
                "session": item.get('session') and {
                    "object": item.get('session', {}).get('object'),
                    "id": item.get('session', {}).get('id'),
                    "status": item.get('session', {}).get('status'),
                    "connection_status": item.get('session', {}).get('connection_status'),
                    "usage": item.get('session', {}).get('usage') and {
                        "total_productive_message_count": item.get('session', {}).get('usage', {}).get('total_productive_message_count'),
                        "total_productive_client_message_count": item.get('session', {}).get('usage', {}).get('total_productive_client_message_count'),
                        "total_productive_server_message_count": item.get('session', {}).get('usage', {}).get('total_productive_server_message_count')
                    },
                    "metadata": item.get('session', {}).get('metadata'),
                    "created_at": item.get('session', {}).get('created_at') and datetime.fromisoformat(item.get('session', {}).get('created_at')),
                    "updated_at": item.get('session', {}).get('updated_at') and datetime.fromisoformat(item.get('session', {}).get('updated_at'))
                },
                "server_deployment": item.get('server_deployment') and {
                    "object": item.get('server_deployment', {}).get('object'),
                    "id": item.get('server_deployment', {}).get('id'),
                    "name": item.get('server_deployment', {}).get('name'),
                    "description": item.get('server_deployment', {}).get('description'),
                    "metadata": item.get('server_deployment', {}).get('metadata'),
                    "created_at": item.get('server_deployment', {}).get('created_at') and datetime.fromisoformat(item.get('server_deployment', {}).get('created_at')),
                    "updated_at": item.get('server_deployment', {}).get('updated_at') and datetime.fromisoformat(item.get('server_deployment', {}).get('updated_at')),
                    "server": item.get('server_deployment', {}).get('server') and {
                        "object": item.get('server_deployment', {}).get('server', {}).get('object'),
                        "id": item.get('server_deployment', {}).get('server', {}).get('id'),
                        "name": item.get('server_deployment', {}).get('server', {}).get('name'),
                        "description": item.get('server_deployment', {}).get('server', {}).get('description'),
                        "type": item.get('server_deployment', {}).get('server', {}).get('type'),
                        "created_at": item.get('server_deployment', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server_deployment', {}).get('server', {}).get('created_at')),
                        "updated_at": item.get('server_deployment', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server_deployment', {}).get('server', {}).get('updated_at'))
                    }
                },
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "started_at": item.get('started_at') and datetime.fromisoformat(item.get('started_at')),
                "ended_at": item.get('ended_at') and datetime.fromisoformat(item.get('ended_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

SessionsConnectionsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

