from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class DashboardOrganizationsInvitesListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapDashboardOrganizationsInvitesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsInvitesListOutput:
        return DashboardOrganizationsInvitesListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "role": item.get('role'),
                "type": item.get('type'),
                "email": item.get('email'),
                "organization": item.get('organization') and {
                    "object": item.get('organization', {}).get('object'),
                    "id": item.get('organization', {}).get('id'),
                    "status": item.get('organization', {}).get('status'),
                    "type": item.get('organization', {}).get('type'),
                    "slug": item.get('organization', {}).get('slug'),
                    "name": item.get('organization', {}).get('name'),
                    "organization_id": item.get('organization', {}).get('organization_id'),
                    "image_url": item.get('organization', {}).get('image_url'),
                    "created_at": item.get('organization', {}).get('created_at') and datetime.fromisoformat(item.get('organization', {}).get('created_at')),
                    "updated_at": item.get('organization', {}).get('updated_at') and datetime.fromisoformat(item.get('organization', {}).get('updated_at'))
                },
                "invited_by": item.get('invited_by') and {
                    "object": item.get('invited_by', {}).get('object'),
                    "id": item.get('invited_by', {}).get('id'),
                    "type": item.get('invited_by', {}).get('type'),
                    "organization_id": item.get('invited_by', {}).get('organization_id'),
                    "actor_id": item.get('invited_by', {}).get('actor_id'),
                    "name": item.get('invited_by', {}).get('name'),
                    "email": item.get('invited_by', {}).get('email'),
                    "image_url": item.get('invited_by', {}).get('image_url'),
                    "created_at": item.get('invited_by', {}).get('created_at') and datetime.fromisoformat(item.get('invited_by', {}).get('created_at')),
                    "updated_at": item.get('invited_by', {}).get('updated_at') and datetime.fromisoformat(item.get('invited_by', {}).get('updated_at'))
                },
                "invite_link": item.get('invite_link') and {
                    "object": item.get('invite_link', {}).get('object'),
                    "id": item.get('invite_link', {}).get('id'),
                    "key": item.get('invite_link', {}).get('key'),
                    "key_redacted": item.get('invite_link', {}).get('key_redacted'),
                    "url": item.get('invite_link', {}).get('url'),
                    "created_at": item.get('invite_link', {}).get('created_at') and datetime.fromisoformat(item.get('invite_link', {}).get('created_at'))
                },
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "updated_at": item.get('updated_at') and datetime.fromisoformat(item.get('updated_at')),
                "deleted_at": item.get('deleted_at') and datetime.fromisoformat(item.get('deleted_at')),
                "expires_at": item.get('expires_at') and datetime.fromisoformat(item.get('expires_at')),
                "accepted_at": item.get('accepted_at') and datetime.fromisoformat(item.get('accepted_at')),
                "rejected_at": item.get('rejected_at') and datetime.fromisoformat(item.get('rejected_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsInvitesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

DashboardOrganizationsInvitesListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapDashboardOrganizationsInvitesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsInvitesListQuery:
        data

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsInvitesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

