from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetLogsOutputLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource:
    provider: Optional[str] = None
    workflow_run_id: Optional[str] = None
    workflow_id: Optional[str] = None
    function_deployment_id: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    type: str
    line: str
    timestamp: Optional[datetime] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetLogsOutputSteps:
    logs: List[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs]
    id: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    source: Optional[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource] = None
    created_at: Optional[datetime] = None
@dataclass
class ManagementInstanceCustomProvidersDeploymentsGetLogsOutput:
    object: str
    logs: List[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputLogs]
    steps: List[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputSteps]


class mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersDeploymentsGetLogsOutputLogs:
        return ManagementInstanceCustomProvidersDeploymentsGetLogsOutputLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource:
        return ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource(
        provider=data.get('provider'),
        workflow_run_id=data.get('workflow_run_id'),
        workflow_id=data.get('workflow_id'),
        function_deployment_id=data.get('function_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs:
        return ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs(
        type=data.get('type'),
        line=data.get('line'),
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputSteps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersDeploymentsGetLogsOutputSteps:
        return ManagementInstanceCustomProvidersDeploymentsGetLogsOutputSteps(
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        source=mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsSource.from_dict(data.get('source')) if data.get('source') else None,
        logs=[mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersDeploymentsGetLogsOutputSteps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersDeploymentsGetLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersDeploymentsGetLogsOutput:
        return ManagementInstanceCustomProvidersDeploymentsGetLogsOutput(
        object=data.get('object'),
        logs=[mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputLogs.from_dict(item) for item in data.get('logs', []) if item],
        steps=[mapManagementInstanceCustomProvidersDeploymentsGetLogsOutputSteps.from_dict(item) for item in data.get('steps', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersDeploymentsGetLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
