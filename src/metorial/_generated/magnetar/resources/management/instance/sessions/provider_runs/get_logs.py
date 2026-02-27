from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsProviderRunsGetLogsOutputLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsProviderRunsGetLogsOutput:
    object: str
    logs: List[ManagementInstanceSessionsProviderRunsGetLogsOutputLogs]


class mapManagementInstanceSessionsProviderRunsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProviderRunsGetLogsOutputLogs:
        return ManagementInstanceSessionsProviderRunsGetLogsOutputLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsProviderRunsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsProviderRunsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProviderRunsGetLogsOutput:
        return ManagementInstanceSessionsProviderRunsGetLogsOutput(
        object=data.get('object'),
        logs=[mapManagementInstanceSessionsProviderRunsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsProviderRunsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
