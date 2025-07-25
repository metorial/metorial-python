from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class DashboardOrganizationsInstancesGetOutput:
    object: str
    id: str
    status: str
    slug: str
    name: str
    type: str
    organization_id: str
    project: Dict[str, Any]
    created_at: datetime
    updated_at: datetime


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapDashboardOrganizationsInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsInstancesGetOutput:
        return DashboardOrganizationsInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        project=data.get('project') and {
            "object": data.get('project', {}).get('object'),
            "id": data.get('project', {}).get('id'),
            "status": data.get('project', {}).get('status'),
            "slug": data.get('project', {}).get('slug'),
            "name": data.get('project', {}).get('name'),
            "organization_id": data.get('project', {}).get('organization_id'),
            "created_at": data.get('project', {}).get('created_at') and datetime.fromisoformat(data.get('project', {}).get('created_at')),
            "updated_at": data.get('project', {}).get('updated_at') and datetime.fromisoformat(data.get('project', {}).get('updated_at'))
        },
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at')),
        updated_at=data.get('updated_at') and datetime.fromisoformat(data.get('updated_at'))
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

