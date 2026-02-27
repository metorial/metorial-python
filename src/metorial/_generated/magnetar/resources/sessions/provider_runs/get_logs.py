from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsProviderRunsGetLogsOutputLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class SessionsProviderRunsGetLogsOutput:
    object: str
    logs: List[SessionsProviderRunsGetLogsOutputLogs]


class mapSessionsProviderRunsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProviderRunsGetLogsOutputLogs:
        return SessionsProviderRunsGetLogsOutputLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProviderRunsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProviderRunsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProviderRunsGetLogsOutput:
        return SessionsProviderRunsGetLogsOutput(
        object=data.get('object'),
        logs=[mapSessionsProviderRunsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SessionsProviderRunsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
