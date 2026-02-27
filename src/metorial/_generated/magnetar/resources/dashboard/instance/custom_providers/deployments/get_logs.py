from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutputLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource:
    provider: Optional[str] = None
    workflow_run_id: Optional[str] = None
    workflow_id: Optional[str] = None
    function_deployment_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps:
    logs: List[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs]
    id: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    source: Optional[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource] = None
    created_at: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetLogsOutput:
    object: str
    logs: List[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputLogs]
    steps: List[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputSteps]


class mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetLogsOutputLogs:
        return DashboardInstanceCustomProvidersDeploymentsGetLogsOutputLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource:
        return DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource(
        provider=data.get('provider'),
        workflow_run_id=data.get('workflow_run_id'),
        workflow_id=data.get('workflow_id'),
        function_deployment_id=data.get('function_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
        return DashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
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
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource.from_dict(data.get('source')) if data.get('source') else None,
        logs=[mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
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
        logs=[mapDashboardInstanceCustomProvidersDeploymentsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item],
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
