from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ServersListingsCategoriesListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServersListingsCategoriesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServersListingsCategoriesListOutput:
        return ServersListingsCategoriesListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "name": item.get('name'),
                "slug": item.get('slug'),
                "description": item.get('description'),
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at')),
                "updated_at": item.get('updated_at') and datetime.fromisoformat(item.get('updated_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ServersListingsCategoriesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ServersListingsCategoriesListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServersListingsCategoriesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServersListingsCategoriesListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ServersListingsCategoriesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

