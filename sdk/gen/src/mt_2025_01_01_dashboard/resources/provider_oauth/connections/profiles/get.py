from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthConnectionsProfilesGetOutput:
    object: str
    id: str
    status: str
    sub: str
    connection_id: str
    created_at: datetime
    last_used_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    email: Optional[str] = None


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionsProfilesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsProfilesGetOutput:
        return ProviderOauthConnectionsProfilesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sub=data.get('sub'),
        name=data.get('name'),
        email=data.get('email'),
        connection_id=data.get('connection_id'),
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at')),
        last_used_at=data.get('last_used_at') and datetime.fromisoformat(data.get('last_used_at')),
        updated_at=data.get('updated_at') and datetime.fromisoformat(data.get('updated_at'))
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionsProfilesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

