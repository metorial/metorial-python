from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthConnectionsDeleteOutput:
    object: str
    id: str
    status: str
    name: str
    provider: Dict[str, Any]
    config: Dict[str, Any]
    scopes: List[str]
    client_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    template_id: Optional[str] = None


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsDeleteOutput:
        return ProviderOauthConnectionsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        provider=data.get('provider') and {
            "id": data.get('provider', {}).get('id'),
            "name": data.get('provider', {}).get('name'),
            "url": data.get('provider', {}).get('url')
        },
        config=data.get('config'),
        scopes=[                item for item in data.get('scopes', [])],
        client_id=data.get('client_id'),
        instance_id=data.get('instance_id'),
        template_id=data.get('template_id'),
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at')),
        updated_at=data.get('updated_at') and datetime.fromisoformat(data.get('updated_at'))
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

