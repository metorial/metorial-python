from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesInstancesLogsOutputLines:
    index: float
    source: str
    timestamp: datetime
    text: str
@dataclass
class SandboxMachinesInstancesLogsOutput:
    object: str
    lines: List[SandboxMachinesInstancesLogsOutputLines]
    has_more: bool
    line_count: float
    status: str
    truncated: bool
    next_cursor: Optional[float] = None


class mapSandboxMachinesInstancesLogsOutputLines:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesLogsOutputLines:
        return SandboxMachinesInstancesLogsOutputLines(
        index=data.get('index'),
        source=data.get('source'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        text=data.get('text')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesLogsOutputLines, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxMachinesInstancesLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesLogsOutput:
        return SandboxMachinesInstancesLogsOutput(
        object=data.get('object'),
        lines=[mapSandboxMachinesInstancesLogsOutputLines.from_dict(item) for item in data.get('lines', []) if item],
        next_cursor=data.get('next_cursor'),
        has_more=data.get('has_more'),
        line_count=data.get('line_count'),
        status=data.get('status'),
        truncated=data.get('truncated')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesInstancesLogsQuery:
    direction: Optional[str] = None
    cursor: Optional[float] = None
    limit: Optional[float] = None


class mapSandboxMachinesInstancesLogsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesInstancesLogsQuery:
        return SandboxMachinesInstancesLogsQuery(
        direction=data.get('direction'),
        cursor=data.get('cursor'),
        limit=data.get('limit')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesInstancesLogsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

