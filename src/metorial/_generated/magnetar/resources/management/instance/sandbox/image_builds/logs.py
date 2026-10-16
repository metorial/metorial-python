from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxImageBuildsLogsOutputLines:
    index: float
    source: str
    timestamp: datetime
    text: str
@dataclass
class ManagementInstanceSandboxImageBuildsLogsOutput:
    object: str
    lines: List[ManagementInstanceSandboxImageBuildsLogsOutputLines]
    has_more: bool
    line_count: float
    status: str
    truncated: bool
    next_cursor: Optional[float] = None


class mapManagementInstanceSandboxImageBuildsLogsOutputLines:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImageBuildsLogsOutputLines:
        return ManagementInstanceSandboxImageBuildsLogsOutputLines(
        index=data.get('index'),
        source=data.get('source'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        text=data.get('text')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImageBuildsLogsOutputLines, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxImageBuildsLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImageBuildsLogsOutput:
        return ManagementInstanceSandboxImageBuildsLogsOutput(
        object=data.get('object'),
        lines=[mapManagementInstanceSandboxImageBuildsLogsOutputLines.from_dict(item) for item in data.get('lines', []) if item],
        next_cursor=data.get('next_cursor'),
        has_more=data.get('has_more'),
        line_count=data.get('line_count'),
        status=data.get('status'),
        truncated=data.get('truncated')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImageBuildsLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSandboxImageBuildsLogsQuery:
    direction: Optional[str] = None
    cursor: Optional[float] = None
    limit: Optional[float] = None


class mapManagementInstanceSandboxImageBuildsLogsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxImageBuildsLogsQuery:
        return ManagementInstanceSandboxImageBuildsLogsQuery(
        direction=data.get('direction'),
        cursor=data.get('cursor'),
        limit=data.get('limit')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxImageBuildsLogsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

