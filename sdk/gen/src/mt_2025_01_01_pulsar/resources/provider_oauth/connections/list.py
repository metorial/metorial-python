from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthConnectionsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsListOutput:
        return ProviderOauthConnectionsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "name": item.get('name'),
                "provider": item.get('provider') and {
                    "id": item.get('provider', {}).get('id'),
                    "name": item.get('provider', {}).get('name'),
                    "url": item.get('provider', {}).get('url')
                },
                "config": item.get('config'),
                "scopes": [                        item for item in item.get('scopes', [])],
                "client_id": item.get('client_id'),
                "instance_id": item.get('instance_id'),
                "template_id": item.get('template_id'),
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "updated_at": item.get('updated_at') and datetime.fromisoformat(item.get('updated_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ProviderOauthConnectionsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

