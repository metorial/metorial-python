from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthConnectionTemplateGetOutput:
    object: str
    id: str
    status: str
    slug: str
    name: str
    provider: Dict[str, Any]
    scopes: List[Dict[str, Any]]
    variables: List[Dict[str, Any]]
    profile: Dict[str, Any]
    created_at: datetime
    updated_at: datetime


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthConnectionTemplateGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateGetOutput:
        return ProviderOauthConnectionTemplateGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        provider=data.get('provider') and {
            "name": data.get('provider', {}).get('name'),
            "url": data.get('provider', {}).get('url')
        },
        scopes=[{
                "id": item.get('id'),
                "identifier": item.get('identifier'),
                "description": item.get('description')
            } for item in data.get('scopes', [])],
        variables=[{
                "id": item.get('id'),
                "key": item.get('key'),
                "type": item.get('type'),
                "label": item.get('label'),
                "description": item.get('description')
            } for item in data.get('variables', [])],
        profile=data.get('profile') and {
            "object": data.get('profile', {}).get('object'),
            "id": data.get('profile', {}).get('id'),
            "name": data.get('profile', {}).get('name'),
            "description": data.get('profile', {}).get('description'),
            "slug": data.get('profile', {}).get('slug'),
            "image_url": data.get('profile', {}).get('image_url'),
            "is_official": data.get('profile', {}).get('is_official'),
            "is_metorial": data.get('profile', {}).get('is_metorial'),
            "is_verified": data.get('profile', {}).get('is_verified'),
            "badges": [{
                    "type": item.get('type'),
                    "name": item.get('name')
                } for item in data.get('profile', {}).get('badges', [])],
            "created_at": data.get('profile', {}).get('created_at') and datetime.fromisoformat(data.get('profile', {}).get('created_at')),
            "updated_at": data.get('profile', {}).get('updated_at') and datetime.fromisoformat(data.get('profile', {}).get('updated_at'))
        },
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at')),
        updated_at=data.get('updated_at') and datetime.fromisoformat(data.get('updated_at'))
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthConnectionTemplateGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

