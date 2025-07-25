from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ManagementOrganizationInvitesListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapManagementOrganizationInvitesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInvitesListOutput:
        return ManagementOrganizationInvitesListOutput(
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
                "invite_link": item.get('inviteLink') and {
                    "_typename": item.get('inviteLink', {}).get('__typename'),
                    "id": item.get('inviteLink', {}).get('id'),
                    "key": item.get('inviteLink', {}).get('key'),
                    "key_redacted": item.get('inviteLink', {}).get('keyRedacted'),
                    "url": item.get('inviteLink', {}).get('url'),
                    "created_at": item.get('inviteLink', {}).get('created_at') and datetime.fromisoformat(item.get('inviteLink', {}).get('created_at'))
                },
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "updated_at": item.get('updated_at') and datetime.fromisoformat(item.get('updated_at')),
                "deleted_at": item.get('deletedAt') and datetime.fromisoformat(item.get('deletedAt')),
                "expires_at": item.get('expiresAt') and datetime.fromisoformat(item.get('expiresAt')),
                "accepted_at": item.get('acceptedAt') and datetime.fromisoformat(item.get('acceptedAt')),
                "rejected_at": item.get('rejectedAt') and datetime.fromisoformat(item.get('rejectedAt'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationInvitesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ManagementOrganizationInvitesListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapManagementOrganizationInvitesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInvitesListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationInvitesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

