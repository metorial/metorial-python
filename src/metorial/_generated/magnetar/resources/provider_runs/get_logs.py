from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderRunsGetLogsOutputLogs:
    object: str
    timestamp: datetime
    message: str
    output_type: str
@dataclass
class ProviderRunsGetLogsOutput:
    object: str
    provider_run_id: str
    logs: List[ProviderRunsGetLogsOutputLogs]


class mapProviderRunsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderRunsGetLogsOutputLogs:
        return ProviderRunsGetLogsOutputLogs(
        object=data.get('object'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        message=data.get('message'),
        output_type=data.get('output_type')
        )

    @staticmethod
    def to_dict(value: Union[ProviderRunsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderRunsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderRunsGetLogsOutput:
        return ProviderRunsGetLogsOutput(
        object=data.get('object'),
        provider_run_id=data.get('provider_run_id'),
        logs=[mapProviderRunsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ProviderRunsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

