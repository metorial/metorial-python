from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthConnectionTemplateListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionTemplateListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateListOutput:
        return ProviderOauthConnectionTemplateListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "slug": item.get('slug'),
                "name": item.get('name'),
                "provider": item.get('provider') and {
                    "name": item.get('provider', {}).get('name'),
                    "url": item.get('provider', {}).get('url')
                },
                "scopes": [{
                        "id": item.get('id'),
                        "identifier": item.get('identifier'),
                        "description": item.get('description')
                    } for item in item.get('scopes', [])],
                "variables": [{
                        "id": item.get('id'),
                        "key": item.get('key'),
                        "type": item.get('type'),
                        "label": item.get('label'),
                        "description": item.get('description')
                    } for item in item.get('variables', [])],
                "profile": item.get('profile') and {
                    "object": item.get('profile', {}).get('object'),
                    "id": item.get('profile', {}).get('id'),
                    "name": item.get('profile', {}).get('name'),
                    "description": item.get('profile', {}).get('description'),
                    "slug": item.get('profile', {}).get('slug'),
                    "image_url": item.get('profile', {}).get('image_url'),
                    "is_official": item.get('profile', {}).get('is_official'),
                    "is_metorial": item.get('profile', {}).get('is_metorial'),
                    "is_verified": item.get('profile', {}).get('is_verified'),
                    "badges": [{
                            "type": item.get('type'),
                            "name": item.get('name')
                        } for item in item.get('profile', {}).get('badges', [])],
                    "created_at": item.get('profile', {}).get('created_at') and datetime.fromisoformat(item.get('profile', {}).get('created_at')),
                    "updated_at": item.get('profile', {}).get('updated_at') and datetime.fromisoformat(item.get('profile', {}).get('updated_at'))
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
    def to_dict(value: Union[ProviderOauthConnectionTemplateListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ProviderOauthConnectionTemplateListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionTemplateListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionTemplateListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

