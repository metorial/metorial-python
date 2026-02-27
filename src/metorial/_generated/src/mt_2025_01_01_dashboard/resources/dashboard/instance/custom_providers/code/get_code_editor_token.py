from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
    object: str
    id: str
    url: str
    expires_at: datetime


class mapDashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput:
        return DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput(
        object=data.get('object'),
        id=data.get('id'),
        url=data.get('url'),
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCodeGetCodeEditorTokenOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
