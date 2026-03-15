from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
    object: str
    id: str
    url: str
    expires_at: datetime


class mapManagementInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
        return ManagementInstanceCustomProvidersCodeGetCodeEditorTokenOutput(
        object=data.get('object'),
        id=data.get('id'),
        url=data.get('url'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCodeGetCodeEditorTokenOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

