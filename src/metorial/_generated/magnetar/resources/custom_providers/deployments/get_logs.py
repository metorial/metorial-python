from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersDeploymentsGetLogsOutputLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class CustomProvidersDeploymentsGetLogsOutputStepsSource:
    provider: Optional[str] = None
    workflow_run_id: Optional[str] = None
    workflow_id: Optional[str] = None
    function_deployment_id: Optional[str] = None
@dataclass
class CustomProvidersDeploymentsGetLogsOutputStepsLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class CustomProvidersDeploymentsGetLogsOutputSteps:
    logs: List[CustomProvidersDeploymentsGetLogsOutputStepsLogs]
    id: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    source: Optional[CustomProvidersDeploymentsGetLogsOutputStepsSource] = None
    created_at: Optional[datetime] = None
@dataclass
class CustomProvidersDeploymentsGetLogsOutput:
    object: str
    logs: List[CustomProvidersDeploymentsGetLogsOutputLogs]
    steps: List[CustomProvidersDeploymentsGetLogsOutputSteps]


class mapCustomProvidersDeploymentsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetLogsOutputLogs:
        return CustomProvidersDeploymentsGetLogsOutputLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetLogsOutputStepsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetLogsOutputStepsSource:
        return CustomProvidersDeploymentsGetLogsOutputStepsSource(
        provider=data.get('provider'),
        workflow_run_id=data.get('workflow_run_id'),
        workflow_id=data.get('workflow_id'),
        function_deployment_id=data.get('function_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetLogsOutputStepsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetLogsOutputStepsLogs:
        return CustomProvidersDeploymentsGetLogsOutputStepsLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetLogsOutputStepsLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetLogsOutputSteps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetLogsOutputSteps:
        return CustomProvidersDeploymentsGetLogsOutputSteps(
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=mapCustomProvidersDeploymentsGetLogsOutputStepsSource.from_dict(data.get('source')) if data.get('source') else None,
        logs=[mapCustomProvidersDeploymentsGetLogsOutputStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetLogsOutputSteps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersDeploymentsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetLogsOutput:
        return CustomProvidersDeploymentsGetLogsOutput(
        object=data.get('object'),
        logs=[mapCustomProvidersDeploymentsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item],
        steps=[mapCustomProvidersDeploymentsGetLogsOutputSteps.from_dict(item) for item in data.get('steps', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersDeploymentsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
