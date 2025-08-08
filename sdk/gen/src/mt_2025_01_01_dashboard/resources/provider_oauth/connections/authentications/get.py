from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthConnectionsAuthenticationsGetOutput:
    object: str
    id: str
    status: str
    events: List[Dict[str, Any]]
    connection_id: str
    profile: Dict[str, Any]
    created_at: datetime
    error: Optional[Dict[str, Any]] = None


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionsAuthenticationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsAuthenticationsGetOutput:
        return ProviderOauthConnectionsAuthenticationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=data.get('error') and {
            "code": data.get('error', {}).get('code'),
            "message": data.get('error', {}).get('message')
        },
        events=[{
                "id": item.get('id'),
                "type": item.get('type'),
                "metadata": item.get('metadata'),
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at'))
            } for item in data.get('events', [])],
        connection_id=data.get('connection_id'),
        profile=data.get('profile') and {
            "object": data.get('profile', {}).get('object'),
            "id": data.get('profile', {}).get('id'),
            "status": data.get('profile', {}).get('status'),
            "sub": data.get('profile', {}).get('sub'),
            "name": data.get('profile', {}).get('name'),
            "email": data.get('profile', {}).get('email'),
            "connection_id": data.get('profile', {}).get('connection_id'),
            "created_at": data.get('profile', {}).get('created_at') and datetime.fromisoformat(data.get('profile', {}).get('created_at')),
            "last_used_at": data.get('profile', {}).get('last_used_at') and datetime.fromisoformat(data.get('profile', {}).get('last_used_at')),
            "updated_at": data.get('profile', {}).get('updated_at') and datetime.fromisoformat(data.get('profile', {}).get('updated_at'))
        },
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at'))
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionsAuthenticationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

