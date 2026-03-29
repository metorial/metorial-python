from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderRunsGetLogsOutputLogs:
    object: str
    timestamp: datetime
    message: str
    output_type: str
@dataclass
class DashboardInstanceProviderRunsGetLogsOutput:
    object: str
    provider_run_id: str
    logs: List[DashboardInstanceProviderRunsGetLogsOutputLogs]


class mapDashboardInstanceProviderRunsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderRunsGetLogsOutputLogs:
        return DashboardInstanceProviderRunsGetLogsOutputLogs(
        object=data.get('object'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        message=data.get('message'),
        output_type=data.get('output_type')
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
        provider_run_id=data.get('provider_run_id'),
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

