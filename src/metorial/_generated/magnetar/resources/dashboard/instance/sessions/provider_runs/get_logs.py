from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsProviderRunsGetLogsOutputLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class DashboardInstanceSessionsProviderRunsGetLogsOutput:
    object: str
    logs: List[DashboardInstanceSessionsProviderRunsGetLogsOutputLogs]


class mapDashboardInstanceSessionsProviderRunsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProviderRunsGetLogsOutputLogs:
        return DashboardInstanceSessionsProviderRunsGetLogsOutputLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProviderRunsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsProviderRunsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProviderRunsGetLogsOutput:
        return DashboardInstanceSessionsProviderRunsGetLogsOutput(
        object=data.get('object'),
        logs=[mapDashboardInstanceSessionsProviderRunsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProviderRunsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
