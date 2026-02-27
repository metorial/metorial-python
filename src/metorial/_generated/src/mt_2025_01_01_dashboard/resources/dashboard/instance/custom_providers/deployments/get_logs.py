from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    object: str
    timestamp: datetime
    message: str
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps:
    object: str
    id: str
    name: str
    type: str
    status: str
    logs: List[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs]
    created_at: datetime
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutput:
    object: str
    custom_provider_deployment_id: str
    steps: List[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps]


class mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
        return DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs(
        object=data.get('object'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None,
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps:
        return DashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        status=data.get('status'),
        logs=[mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetLogsOutput:
        return DashboardInstanceCustomProvidersDeploymentsGetLogsOutput(
        object=data.get('object'),
        custom_provider_deployment_id=data.get('custom_provider_deployment_id'),
        steps=[mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps.from_dict(item) for item in data.get('steps', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
