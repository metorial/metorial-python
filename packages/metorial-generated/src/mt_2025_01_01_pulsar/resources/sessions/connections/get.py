from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SessionsConnectionsGetOutput:
    object: str
    id: str
    status: str
    mcp: Dict[str, Any]
    usage: Dict[str, Any]
    server: Dict[str, Any]
    session: Dict[str, Any]
    server_deployment: Dict[str, Any]
    created_at: datetime
    started_at: datetime
    ended_at: Optional[datetime] = None


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutput:
        return SessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=data.get('mcp') and {
            "object": data.get('mcp', {}).get('object'),
            "version": data.get('mcp', {}).get('version'),
            "connection_type": data.get('mcp', {}).get('connection_type'),
            "client": data.get('mcp', {}).get('client') and {
                "object": data.get('mcp', {}).get('client', {}).get('object'),
                "name": data.get('mcp', {}).get('client', {}).get('name'),
                "version": data.get('mcp', {}).get('client', {}).get('version'),
                "capabilities": data.get('mcp', {}).get('client', {}).get('capabilities')
            },
            "server": data.get('mcp', {}).get('server') and {
                "object": data.get('mcp', {}).get('server', {}).get('object'),
                "name": data.get('mcp', {}).get('server', {}).get('name'),
                "version": data.get('mcp', {}).get('server', {}).get('version'),
                "capabilities": data.get('mcp', {}).get('server', {}).get('capabilities')
            }
        },
        usage=data.get('usage') and {
            "total_productive_message_count": data.get('usage', {}).get('total_productive_message_count'),
            "total_productive_client_message_count": data.get('usage', {}).get('total_productive_client_message_count'),
            "total_productive_server_message_count": data.get('usage', {}).get('total_productive_server_message_count')
        },
        server=data.get('server') and {
            "object": data.get('server', {}).get('object'),
            "id": data.get('server', {}).get('id'),
            "name": data.get('server', {}).get('name'),
            "description": data.get('server', {}).get('description'),
            "type": data.get('server', {}).get('type'),
            "created_at": data.get('server', {}).get('created_at') and datetime.fromisoformat(data.get('server', {}).get('created_at')),
            "updated_at": data.get('server', {}).get('updated_at') and datetime.fromisoformat(data.get('server', {}).get('updated_at'))
        },
        session=data.get('session') and {
            "object": data.get('session', {}).get('object'),
            "id": data.get('session', {}).get('id'),
            "status": data.get('session', {}).get('status'),
            "connection_status": data.get('session', {}).get('connection_status'),
            "usage": data.get('session', {}).get('usage') and {
                "total_productive_message_count": data.get('session', {}).get('usage', {}).get('total_productive_message_count'),
                "total_productive_client_message_count": data.get('session', {}).get('usage', {}).get('total_productive_client_message_count'),
                "total_productive_server_message_count": data.get('session', {}).get('usage', {}).get('total_productive_server_message_count')
            },
            "metadata": data.get('session', {}).get('metadata'),
            "created_at": data.get('session', {}).get('created_at') and datetime.fromisoformat(data.get('session', {}).get('created_at')),
            "updated_at": data.get('session', {}).get('updated_at') and datetime.fromisoformat(data.get('session', {}).get('updated_at'))
        },
        server_deployment=data.get('server_deployment') and {
            "object": data.get('server_deployment', {}).get('object'),
            "id": data.get('server_deployment', {}).get('id'),
            "name": data.get('server_deployment', {}).get('name'),
            "description": data.get('server_deployment', {}).get('description'),
            "metadata": data.get('server_deployment', {}).get('metadata'),
            "created_at": data.get('server_deployment', {}).get('created_at') and datetime.fromisoformat(data.get('server_deployment', {}).get('created_at')),
            "updated_at": data.get('server_deployment', {}).get('updated_at') and datetime.fromisoformat(data.get('server_deployment', {}).get('updated_at')),
            "server": data.get('server_deployment', {}).get('server') and {
                "object": data.get('server_deployment', {}).get('server', {}).get('object'),
                "id": data.get('server_deployment', {}).get('server', {}).get('id'),
                "name": data.get('server_deployment', {}).get('server', {}).get('name'),
                "description": data.get('server_deployment', {}).get('server', {}).get('description'),
                "type": data.get('server_deployment', {}).get('server', {}).get('type'),
                "created_at": data.get('server_deployment', {}).get('server', {}).get('created_at') and datetime.fromisoformat(data.get('server_deployment', {}).get('server', {}).get('created_at')),
                "updated_at": data.get('server_deployment', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(data.get('server_deployment', {}).get('server', {}).get('updated_at'))
            }
        },
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at')),
        started_at=data.get('started_at') and datetime.fromisoformat(data.get('started_at')),
        ended_at=data.get('ended_at') and datetime.fromisoformat(data.get('ended_at'))
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

