from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ServersVariantsListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServersVariantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServersVariantsListOutput:
        return ServersVariantsListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "identifier": item.get('identifier'),
                "server": item.get('server') and {
                    "object": item.get('server', {}).get('object'),
                    "id": item.get('server', {}).get('id'),
                    "name": item.get('server', {}).get('name'),
                    "description": item.get('server', {}).get('description'),
                    "type": item.get('server', {}).get('type'),
                    "created_at": item.get('server', {}).get('created_at') and datetime.fromisoformat(item.get('server', {}).get('created_at')),
                    "updated_at": item.get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('server', {}).get('updated_at'))
                },
                "current_version": item.get('current_version') and {
                    "object": item.get('current_version', {}).get('object'),
                    "id": item.get('current_version', {}).get('id'),
                    "identifier": item.get('current_version', {}).get('identifier'),
                    "server_id": item.get('current_version', {}).get('server_id'),
                    "server_variant_id": item.get('current_version', {}).get('server_variant_id'),
                    "get_launch_params": item.get('current_version', {}).get('get_launch_params'),
                    "source": item.get('current_version', {}).get('source'),
                    "schema": item.get('current_version', {}).get('schema') and {
                        "id": item.get('current_version', {}).get('schema', {}).get('id'),
                        "fingerprint": item.get('current_version', {}).get('schema', {}).get('fingerprint'),
                        "schema": item.get('current_version', {}).get('schema', {}).get('schema'),
                        "server_id": item.get('current_version', {}).get('schema', {}).get('server_id'),
                        "server_variant_id": item.get('current_version', {}).get('schema', {}).get('server_variant_id'),
                        "server_version_id": item.get('current_version', {}).get('schema', {}).get('server_version_id'),
                        "created_at": item.get('current_version', {}).get('schema', {}).get('created_at') and datetime.fromisoformat(item.get('current_version', {}).get('schema', {}).get('created_at'))
                    },
                    "server": item.get('current_version', {}).get('server') and {
                        "object": item.get('current_version', {}).get('server', {}).get('object'),
                        "id": item.get('current_version', {}).get('server', {}).get('id'),
                        "name": item.get('current_version', {}).get('server', {}).get('name'),
                        "description": item.get('current_version', {}).get('server', {}).get('description'),
                        "type": item.get('current_version', {}).get('server', {}).get('type'),
                        "created_at": item.get('current_version', {}).get('server', {}).get('created_at') and datetime.fromisoformat(item.get('current_version', {}).get('server', {}).get('created_at')),
                        "updated_at": item.get('current_version', {}).get('server', {}).get('updated_at') and datetime.fromisoformat(item.get('current_version', {}).get('server', {}).get('updated_at'))
                    },
                    "created_at": item.get('current_version', {}).get('created_at') and datetime.fromisoformat(item.get('current_version', {}).get('created_at'))
                },
                "source": item.get('source'),
                "created_at": item.get('created_at') and datetime.fromisoformat(item.get('created_at'))
            } for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ServersVariantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ServersVariantsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServersVariantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServersVariantsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ServersVariantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

