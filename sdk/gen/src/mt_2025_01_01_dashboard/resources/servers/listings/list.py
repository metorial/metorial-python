from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ServersListingsListOutput:
    items: List[Union[Dict[str, Any], Dict[str, Any]]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServersListingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServersListingsListOutput:
        return ServersListingsListOutput(
        items=[                item for item in data.get('items', [])],
        pagination=data.get('pagination') and {
            "has_more_before": data.get('pagination', {}).get('has_more_before'),
            "has_more_after": data.get('pagination', {}).get('has_more_after')
        }
        )

    @staticmethod
    def to_dict(value: Union[ServersListingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

ServersListingsListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapServersListingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ServersListingsListQuery:
        data

    @staticmethod
    def to_dict(value: Union[ServersListingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

