from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SessionsEventsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListOutput:
        return SessionsEventsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "type": item.get('type'),
                "session_id": item.get('session_id'),
                "server_run": item.get('server_run') and {
                    "object": item.get('server_run', {}).get('object'),
                    "id": item.get('server_run', {}).get('id'),
                    "type": item.get('server_run', {}).get('type'),
                    "status": item.get('server_run', {}).get('status'),
                    "server_version_id": item.get('server_run', {}).get('server_version_id'),
                    "server": item.get('server_run', {}).get('server') and {
                        "object": item.get('server_run', {}).get('server', {}).get('object'),
                        "id": item.get('server_run', {}).get('server', {}).get('id'),
                        "name": item.get('server_run', {}).get('server', {}).get('name'),
                        "description": item.get('server_run', {}).get('server', {}).get('description'),
                        "type": item.get('server_run', {}).get('server', {}).get('type'),
                        "created_at": item.get('server_run', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server_run', {}).get('server', {}).get('created_at')),
                        "updated_at": item.get('server_run', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run', {}).get('server', {}).get('updated_at'))
                    },
                    "server_deployment": item.get('server_run', {}).get('server_deployment') and {
                        "object": item.get('server_run', {}).get('server_deployment', {}).get('object'),
                        "id": item.get('server_run', {}).get('server_deployment', {}).get('id'),
                        "name": item.get('server_run', {}).get('server_deployment', {}).get('name'),
                        "description": item.get('server_run', {}).get('server_deployment', {}).get('description'),
                        "metadata": item.get('server_run', {}).get('server_deployment', {}).get('metadata'),
                        "created_at": item.get('server_run', {}).get('server_deployment', {}).get('created_at') and datetime.fromisoformat(item.get('server_run', {}).get('server_deployment', {}).get('created_at')),
                        "updated_at": item.get('server_run', {}).get('server_deployment', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run', {}).get('server_deployment', {}).get('updated_at')),
                        "server": item.get('server_run', {}).get('server_deployment', {}).get('server') and {
                            "object": item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('object'),
                            "id": item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('id'),
                            "name": item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('name'),
                            "description": item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('description'),
                            "type": item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('type'),
                            "created_at": item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('created_at')),
                            "updated_at": item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run', {}).get('server_deployment', {}).get('server', {}).get('updated_at'))
                        }
                    },
                    "server_session": item.get('server_run', {}).get('server_session') and {
                        "object": item.get('server_run', {}).get('server_session', {}).get('object'),
                        "id": item.get('server_run', {}).get('server_session', {}).get('id'),
                        "status": item.get('server_run', {}).get('server_session', {}).get('status'),
                        "mcp": item.get('server_run', {}).get('server_session', {}).get('mcp') and {
                            "object": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('object'),
                            "version": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('version'),
                            "connection_type": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('connection_type'),
                            "client": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client') and {
                                "object": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('object'),
                                "name": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('name'),
                                "version": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('version'),
                                "capabilities": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('capabilities')
                            },
                            "server": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server') and {
                                "object": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('object'),
                                "name": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('name'),
                                "version": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('version'),
                                "capabilities": item.get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('capabilities')
                            }
                        },
                        "usage": item.get('server_run', {}).get('server_session', {}).get('usage') and {
                            "total_productive_message_count": item.get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_message_count'),
                            "total_productive_client_message_count": item.get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_client_message_count'),
                            "total_productive_server_message_count": item.get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_server_message_count')
                        },
                        "session_id": item.get('server_run', {}).get('server_session', {}).get('session_id'),
                        "created_at": item.get('server_run', {}).get('server_session', {}).get('created_at') and datetime.fromisoformat(item.get('server_run', {}).get('server_session', {}).get('created_at'))
                    },
                    "created_at": item.get('server_run', {}).get('created_at') and datetime.fromisoformat(item.get('server_run', {}).get('created_at')),
                    "updated_at": item.get('server_run', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run', {}).get('updated_at')),
                    "started_at": item.get('server_run', {}).get('started_at') and datetime.fromisoformat(item.get('server_run', {}).get('started_at')),
                    "stopped_at": item.get('server_run', {}).get('stopped_at') and datetime.fromisoformat(item.get('server_run', {}).get('stopped_at'))
                },
                "server_run_error": item.get('server_run_error') and {
                    "object": item.get('server_run_error', {}).get('object'),
                    "id": item.get('server_run_error', {}).get('id'),
                    "code": item.get('server_run_error', {}).get('code'),
                    "message": item.get('server_run_error', {}).get('message'),
                    "metadata": item.get('server_run_error', {}).get('metadata'),
                    "server_run": item.get('server_run_error', {}).get('server_run') and {
                        "object": item.get('server_run_error', {}).get('server_run', {}).get('object'),
                        "id": item.get('server_run_error', {}).get('server_run', {}).get('id'),
                        "type": item.get('server_run_error', {}).get('server_run', {}).get('type'),
                        "status": item.get('server_run_error', {}).get('server_run', {}).get('status'),
                        "server_version_id": item.get('server_run_error', {}).get('server_run', {}).get('server_version_id'),
                        "server": item.get('server_run_error', {}).get('server_run', {}).get('server') and {
                            "object": item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('object'),
                            "id": item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('id'),
                            "name": item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('name'),
                            "description": item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('description'),
                            "type": item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('type'),
                            "created_at": item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('created_at')),
                            "updated_at": item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('server', {}).get('updated_at'))
                        },
                        "server_deployment": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment') and {
                            "object": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('object'),
                            "id": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('id'),
                            "name": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('name'),
                            "description": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('description'),
                            "metadata": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('metadata'),
                            "created_at": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('created_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('created_at')),
                            "updated_at": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('updated_at')),
                            "server": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server') and {
                                "object": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('object'),
                                "id": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('id'),
                                "name": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('name'),
                                "description": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('description'),
                                "type": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('type'),
                                "created_at": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('created_at')),
                                "updated_at": item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('server_deployment', {}).get('server', {}).get('updated_at'))
                            }
                        },
                        "server_session": item.get('server_run_error', {}).get('server_run', {}).get('server_session') and {
                            "object": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('object'),
                            "id": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('id'),
                            "status": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('status'),
                            "mcp": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp') and {
                                "object": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('object'),
                                "version": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('version'),
                                "connection_type": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('connection_type'),
                                "client": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client') and {
                                    "object": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('object'),
                                    "name": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('name'),
                                    "version": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('version'),
                                    "capabilities": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('client', {}).get('capabilities')
                                },
                                "server": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server') and {
                                    "object": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('object'),
                                    "name": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('name'),
                                    "version": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('version'),
                                    "capabilities": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('mcp', {}).get('server', {}).get('capabilities')
                                }
                            },
                            "usage": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('usage') and {
                                "total_productive_message_count": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_message_count'),
                                "total_productive_client_message_count": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_client_message_count'),
                                "total_productive_server_message_count": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('usage', {}).get('total_productive_server_message_count')
                            },
                            "session_id": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('session_id'),
                            "created_at": item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('created_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('server_session', {}).get('created_at'))
                        },
                        "created_at": item.get('server_run_error', {}).get('server_run', {}).get('created_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('created_at')),
                        "updated_at": item.get('server_run_error', {}).get('server_run', {}).get('updated_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('updated_at')),
                        "started_at": item.get('server_run_error', {}).get('server_run', {}).get('started_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('started_at')),
                        "stopped_at": item.get('server_run_error', {}).get('server_run', {}).get('stopped_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('server_run', {}).get('stopped_at'))
                    },
                    "created_at": item.get('server_run_error', {}).get('created_at') and datetime.fromisoformat(item.get('server_run_error', {}).get('created_at'))
                },
                "log_lines": [{
                        "type": item.get('type'),
                        "line": item.get('line')
                    } for item in item.get('log_lines', [])],
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[SessionsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

SessionsEventsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsEventsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[SessionsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

