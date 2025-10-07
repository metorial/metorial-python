from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomServersDeploymentsGetOutputCreatorActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceCustomServersDeploymentsGetOutputStepsLogs:
    timestamp: datetime
    line: str
    type: str
@dataclass
class DashboardInstanceCustomServersDeploymentsGetOutputSteps:
    object: str
    id: str
    index: float
    status: str
    type: str
    logs: List[DashboardInstanceCustomServersDeploymentsGetOutputStepsLogs]
    created_at: datetime
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class DashboardInstanceCustomServersDeploymentsGetOutput:
    object: str
    id: str
    status: str
    trigger: str
    creator_actor: DashboardInstanceCustomServersDeploymentsGetOutputCreatorActor
    custom_server_id: str
    created_at: datetime
    updated_at: datetime
    steps: List[DashboardInstanceCustomServersDeploymentsGetOutputSteps]
    custom_server_version_id: Optional[str] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None


class mapDashboardInstanceCustomServersDeploymentsGetOutputCreatorActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsGetOutputCreatorActor:
        return DashboardInstanceCustomServersDeploymentsGetOutputCreatorActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsGetOutputCreatorActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsGetOutputStepsLogs:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsGetOutputStepsLogs:
        return DashboardInstanceCustomServersDeploymentsGetOutputStepsLogs(
        timestamp=datetime.fromisoformat(data.get('timestamp')) if data.get('timestamp') else None,
        line=data.get('line'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsGetOutputStepsLogs, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsGetOutputSteps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsGetOutputSteps:
        return DashboardInstanceCustomServersDeploymentsGetOutputSteps(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index'),
        status=data.get('status'),
        type=data.get('type'),
        logs=[mapDashboardInstanceCustomServersDeploymentsGetOutputStepsLogs.from_dict(item) for item in data.get('logs', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsGetOutputSteps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomServersDeploymentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomServersDeploymentsGetOutput:
        return DashboardInstanceCustomServersDeploymentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        creator_actor=mapDashboardInstanceCustomServersDeploymentsGetOutputCreatorActor.from_dict(data.get('creator_actor')) if data.get('creator_actor') else None,
        custom_server_id=data.get('custom_server_id'),
        custom_server_version_id=data.get('custom_server_version_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        steps=[mapDashboardInstanceCustomServersDeploymentsGetOutputSteps.from_dict(item) for item in data.get('steps', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomServersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

