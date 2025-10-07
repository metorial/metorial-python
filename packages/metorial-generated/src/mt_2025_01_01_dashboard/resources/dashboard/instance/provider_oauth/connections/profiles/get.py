from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderOauthConnectionsProfilesGetOutput:
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


class mapDashboardInstanceProviderOauthConnectionsProfilesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsProfilesGetOutput:
        return DashboardInstanceProviderOauthConnectionsProfilesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sub=data.get('sub'),
        name=data.get('name'),
        email=data.get('email'),
        connection_id=data.get('connection_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at')) if data.get('last_used_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsProfilesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

