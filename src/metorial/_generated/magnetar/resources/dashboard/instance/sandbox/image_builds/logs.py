from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxImageBuildsLogsOutputLines:
    index: float
    source: str
    timestamp: datetime
    text: str
@dataclass
class DashboardInstanceSandboxImageBuildsLogsOutput:
    object: str
    lines: List[DashboardInstanceSandboxImageBuildsLogsOutputLines]
    has_more: bool
    line_count: float
    status: str
    truncated: bool
    next_cursor: Optional[float] = None


class mapDashboardInstanceSandboxImageBuildsLogsOutputLines:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImageBuildsLogsOutputLines:
        return DashboardInstanceSandboxImageBuildsLogsOutputLines(
        index=data.get('index'),
        source=data.get('source'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        text=data.get('text')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImageBuildsLogsOutputLines, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxImageBuildsLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImageBuildsLogsOutput:
        return DashboardInstanceSandboxImageBuildsLogsOutput(
        object=data.get('object'),
        lines=[mapDashboardInstanceSandboxImageBuildsLogsOutputLines.from_dict(item) for item in data.get('lines', []) if item],
        next_cursor=data.get('next_cursor'),
        has_more=data.get('has_more'),
        line_count=data.get('line_count'),
        status=data.get('status'),
        truncated=data.get('truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImageBuildsLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxImageBuildsLogsQuery:
    direction: Optional[str] = None
    cursor: Optional[float] = None
    limit: Optional[float] = None


class mapDashboardInstanceSandboxImageBuildsLogsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImageBuildsLogsQuery:
        return DashboardInstanceSandboxImageBuildsLogsQuery(
        direction=data.get('direction'),
        cursor=data.get('cursor'),
        limit=data.get('limit')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImageBuildsLogsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

