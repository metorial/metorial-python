from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthConnectionsAuthenticationsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionsAuthenticationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsAuthenticationsListOutput:
        return ProviderOauthConnectionsAuthenticationsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "error": item.get('error') and {
                    "code": item.get('error', {}).get('code'),
                    "message": item.get('error', {}).get('message')
                },
                "events": [{
                        "id": item.get('id'),
                        "type": item.get('type'),
                        "metadata": item.get('metadata'),
                        "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at'))
                    } for item in item.get('events', [])],
                "connection_id": item.get('connection_id'),
                "profile": item.get('profile') and {
                    "object": item.get('profile', {}).get('object'),
                    "id": item.get('profile', {}).get('id'),
                    "status": item.get('profile', {}).get('status'),
                    "sub": item.get('profile', {}).get('sub'),
                    "name": item.get('profile', {}).get('name'),
                    "email": item.get('profile', {}).get('email'),
                    "connection_id": item.get('profile', {}).get('connection_id'),
                    "created_at": item.get('profile', {}).get('created_at') and datetime.fromisoformat(item.get('profile', {}).get('created_at')),
                    "last_used_at": item.get('profile', {}).get('last_used_at') and datetime.fromisoformat(item.get('profile', {}).get('last_used_at')),
                    "updated_at": item.get('profile', {}).get('updated_at') and datetime.fromisoformat(item.get('profile', {}).get('updated_at'))
                },
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionsAuthenticationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ProviderOauthConnectionsAuthenticationsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionsAuthenticationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsAuthenticationsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionsAuthenticationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

