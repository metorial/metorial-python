from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionErrorGroupsGetOutput:
    object: str
    id: str
    code: str
    message: str
    data: Dict[str, Any]
    occurrence_count: float
    created_at: datetime
    provider_id: Optional[str] = None


class mapManagementInstanceSessionErrorGroupsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionErrorGroupsGetOutput:
        return ManagementInstanceSessionErrorGroupsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        data=data.get('data'),
        provider_id=data.get('provider_id'),
        occurrence_count=data.get('occurrence_count'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionErrorGroupsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
