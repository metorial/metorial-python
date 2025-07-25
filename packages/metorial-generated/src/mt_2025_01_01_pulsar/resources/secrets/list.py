from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SecretsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSecretsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SecretsListOutput:
        return SecretsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "type": item.get('type') and {
                    "identifier": item.get('type', {}).get('identifier'),
                    "name": item.get('type', {}).get('name')
                },
                "description": item.get('description'),
                "metadata": item.get('metadata'),
                "organization_id": item.get('organization_id'),
                "instance_id": item.get('instance_id'),
                "fingerprint": item.get('fingerprint'),
                "last_used_at": item.get('last_used_at') and datetime.fromisoformat(item.get('last_used_at')),
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[SecretsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

SecretsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSecretsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SecretsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[SecretsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

