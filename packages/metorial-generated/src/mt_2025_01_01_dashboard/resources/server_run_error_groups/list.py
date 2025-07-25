from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ServerRunErrorGroupsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServerRunErrorGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsListOutput:
        return ServerRunErrorGroupsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "code": item.get('code'),
                "message": item.get('message'),
                "fingerprint": item.get('fingerprint'),
                "count": item.get('count'),
                "default_error": item.get('default_error') and {
                    "object": item.get('default_error', {}).get('object'),
                    "id": item.get('default_error', {}).get('id'),
                    "code": item.get('default_error', {}).get('code'),
                    "message": item.get('default_error', {}).get('message'),
                    "metadata": item.get('default_error', {}).get('metadata'),
                    "server_run": item.get('default_error', {}).get('server_run') and {
                        "object": item.get('default_error', {}).get('server_run', {}).get('object'),
                        "id": item.get('default_error', {}).get('server_run', {}).get('id'),
                        "type": item.get('default_error', {}).get('server_run', {}).get('type'),
                        "status": item.get('default_error', {}).get('server_run', {}).get('status'),
                        "server_version_id": item.get('default_error', {}).get('server_run', {}).get('server_version_id'),
                        "server": item.get('default_error', {}).get('server_run', {}).get('server') and {
                            "object": item.get('default_error', {}).get('server_run', {}).get('server', {}).get('object'),
                            "id": item.get('default_error', {}).get('server_run', {}).get('server', {}).get('id'),
                            "name": item.get('default_error', {}).get('server_run', {}).get('server', {}).get('name'),
                            "description": item.get('default_error', {}).get('server_run', {}).get('server', {}).get('description'),
                            "type": item.get('default_error', {}).get('server_run', {}).get('server', {}).get('type'),
                            "created_at": item.get('default_error', {}).get('server_run', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('server', {}).get('created_at')),
                            "updated_at": item.get('default_error', {}).get('server_run', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('server', {}).get('updated_at'))
                        },
                        "server_deployment": item.get('default_error', {}).get('server_run', {}).get('server_deployment') and {
                            "object": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('object'),
                            "id": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('id'),
                            "name": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('name'),
                            "description": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('description'),
                            "metadata": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('metadata'),
                            "created_at": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('created_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('created_at')),
                            "updated_at": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('updated_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('updated_at')),
                            "server": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server') and {
                                "object": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('object'),
                                "id": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('id'),
                                "name": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('name'),
                                "description": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('description'),
                                "type": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('type'),
                                "created_at": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('created_at')),
                                "updated_at": item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('updated_at'))
                            }
                        },
                        "server_session": item.get('default_error', {}).get('server_run', {}).get('server_session') and {
                            "object": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('object'),
                            "id": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('id'),
                            "status": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('status'),
                            "mcp": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp') and {
                                "object": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('object'),
                                "version": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('version'),
                                "connection_type": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('connection_type'),
                                "client": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client') and {
                                    "object": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('object'),
                                    "name": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('name'),
                                    "version": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('version'),
                                    "capabilities": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('capabilities')
                                },
                                "server": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server') and {
                                    "object": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('object'),
                                    "name": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('name'),
                                    "version": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('version'),
                                    "capabilities": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('capabilities')
                                }
                            },
                            "usage": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('usage') and {
                                "total_productive_message_count": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_message_count'),
                                "total_productive_client_message_count": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_client_message_count'),
                                "total_productive_server_message_count": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_server_message_count')
                            },
                            "session_id": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('session_id'),
                            "created_at": item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('created_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('server_session', {}).get('created_at'))
                        },
                        "created_at": item.get('default_error', {}).get('server_run', {}).get('created_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('created_at')),
                        "updated_at": item.get('default_error', {}).get('server_run', {}).get('updated_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('updated_at')),
                        "started_at": item.get('default_error', {}).get('server_run', {}).get('started_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('started_at')),
                        "stopped_at": item.get('default_error', {}).get('server_run', {}).get('stopped_at') and datetime.fromisoformat(item.get('default_error', {}).get('server_run', {}).get('stopped_at'))
                    },
                    "created_at": item.get('default_error', {}).get('created_at') and datetime.fromisoformat(item.get('default_error', {}).get('created_at'))
                },
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "first_seen_at": item.get('first_seen_at') and datetime.fromisoformat(item.get('first_seen_at')),
                "last_seen_at": item.get('last_seen_at') and datetime.fromisoformat(item.get('last_seen_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ServerRunErrorGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ServerRunErrorGroupsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServerRunErrorGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServerRunErrorGroupsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ServerRunErrorGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

