from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOutpostsDisableOutput:
    object: str
    id: str
    status: str
    connection_status: str
    organization_id: str
    name: str
    instance_count: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    last_seen_at: Optional[datetime] = None


class mapDashboardOrganizationsOutpostsDisableOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsDisableOutput:
        return DashboardOrganizationsOutpostsDisableOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        description=data.get('description'),
        instance_count=data.get('instance_count'),
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsDisableOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

