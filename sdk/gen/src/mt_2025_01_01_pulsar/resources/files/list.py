from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class FilesListOutput:
    items: List[Dict[str, Any]]
    pagination: Dict[str, Any]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapFilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FilesListOutput:
        return FilesListOutput(
        items=[{
                "object": item.get('object'),
                "id": item.get('id'),
                "status": item.get('status'),
                "file_name": item.get('file_name'),
                "file_size": item.get('file_size'),
                "file_type": item.get('file_type'),
                "title": item.get('title'),
                "purpose": item.get('purpose') and {
                    "name": item.get('purpose', {}).get('name'),
                    "identifier": item.get('purpose', {}).get('identifier')
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
    def to_dict(value: Union[FilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

FilesListQuery = Any


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapFilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> FilesListQuery:
        data

    @staticmethod
    def to_dict(value: Union[FilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

