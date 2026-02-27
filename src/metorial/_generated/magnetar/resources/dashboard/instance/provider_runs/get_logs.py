from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderRunsGetLogsOutputLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class DashboardInstanceProviderRunsGetLogsOutput:
    object: str
    logs: List[DashboardInstanceProviderRunsGetLogsOutputLogs]


class mapDashboardInstanceProviderRunsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderRunsGetLogsOutputLogs:
        return DashboardInstanceProviderRunsGetLogsOutputLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderRunsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderRunsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderRunsGetLogsOutput:
        return DashboardInstanceProviderRunsGetLogsOutput(
        object=data.get('object'),
        logs=[mapDashboardInstanceProviderRunsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderRunsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
