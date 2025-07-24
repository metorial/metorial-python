from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SessionsMessagesGetOutput:
    object: str
    id: str
    type: str
    sender: Dict[str, Any]
    mcp_message: Dict[str, Any]
    session_id: str
    server_session_id: str
    created_at: datetime


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsMessagesGetOutput:
        return SessionsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        sender=data.get('sender') and {
            "object": data.get('sender', {}).get('object'),
            "type": data.get('sender', {}).get('type'),
            "id": data.get('sender', {}).get('id')
        },
        mcp_message=data.get('mcp_message') and {
            "object": data.get('mcp_message', {}).get('object'),
            "id": data.get('mcp_message', {}).get('id'),
            "method": data.get('mcp_message', {}).get('method'),
            "payload": data.get('mcp_message', {}).get('payload')
        },
        session_id=data.get('session_id'),
        server_session_id=data.get('server_session_id'),
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at'))
        )

    @staticmethod
    def to_dict(value: Union[SessionsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

