from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderRunsGetLogsOutputLogs:
    object: str
    timestamp: datetime
    message: str
    output_type: str
@dataclass
class ManagementInstanceProviderRunsGetLogsOutput:
    object: str
    provider_run_id: str
    logs: List[ManagementInstanceProviderRunsGetLogsOutputLogs]


class mapManagementInstanceProviderRunsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderRunsGetLogsOutputLogs:
        return ManagementInstanceProviderRunsGetLogsOutputLogs(
        object=data.get('object'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        message=data.get('message'),
        output_type=data.get('output_type')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderRunsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderRunsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderRunsGetLogsOutput:
        return ManagementInstanceProviderRunsGetLogsOutput(
        object=data.get('object'),
        provider_run_id=data.get('provider_run_id'),
        logs=[mapManagementInstanceProviderRunsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderRunsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

