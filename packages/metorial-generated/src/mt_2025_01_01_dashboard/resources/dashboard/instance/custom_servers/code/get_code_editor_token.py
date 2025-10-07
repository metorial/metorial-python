from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput:
    object: str
    id: str
    token: str
    expires_at: datetime


class mapDashboardInstanceCustomServersCodeGetCodeEditorTokenOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput:
        return DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput(
        object=data.get('object'),
        id=data.get('id'),
        token=data.get('token'),
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersCodeGetCodeEditorTokenOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

