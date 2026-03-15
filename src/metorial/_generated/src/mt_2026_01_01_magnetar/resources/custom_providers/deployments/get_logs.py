from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersDeploymentsGetLogsOutputStepsLogs:
    object: str
    timestamp: datetime
    message: str
@dataclass
class CustomProvidersDeploymentsGetLogsOutputSteps:
    object: str
    id: str
    name: str
    type: str
    status: str
    logs: List[CustomProvidersDeploymentsGetLogsOutputStepsLogs]
    created_at: datetime
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class CustomProvidersDeploymentsGetLogsOutput:
    object: str
    custom_provider_deployment_id: str
    steps: List[CustomProvidersDeploymentsGetLogsOutputSteps]


class mapCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersDeploymentsGetLogsOutputStepsLogs:
        return CustomProvidersDeploymentsGetLogsOutputStepsLogs(
        object=data.get('object'),
        timestamp=datetime.fromisoformat(data.get('timestamp').replace('Z', '+00:00')) if data.get('timestamp') else None,
        message=data.get('message')
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
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        status=data.get('status'),
        logs=[mapCustomProvidersDeploymentsGetLogsOutputStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at').replace('Z', '+00:00')) if data.get('ended_at') else None
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
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
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

