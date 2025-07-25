from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ManagementOrganizationInstancesListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapManagementOrganizationInstancesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInstancesListOutput:
        return ManagementOrganizationInstancesListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "slug": item.get('slug'),
                "name": item.get('name'),
                "type": item.get('type'),
                "organization_id": item.get('organization_id'),
                "project": item.get('project') and {
                    "object": item.get('project', {}).get('object'),
                    "id": item.get('project', {}).get('id'),
                    "status": item.get('project', {}).get('status'),
                    "slug": item.get('project', {}).get('slug'),
                    "name": item.get('project', {}).get('name'),
                    "organization_id": item.get('project', {}).get('organization_id'),
                    "created_at": item.get('project', {}).get('created_at') and datetime.fromisoformat(item.get('project', {}).get('created_at')),
                    "updated_at": item.get('project', {}).get('updated_at') and datetime.fromisoformat(item.get('project', {}).get('updated_at'))
                },
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "updated_at": item.get('updated_at') and datetime.fromisoformat(item.get('updated_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationInstancesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ManagementOrganizationInstancesListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapManagementOrganizationInstancesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInstancesListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationInstancesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

