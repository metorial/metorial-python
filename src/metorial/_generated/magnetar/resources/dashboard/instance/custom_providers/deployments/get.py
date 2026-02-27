from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputCommit:
    id: str
    created_at: datetime
    type: Optional[str] = None
    message: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutputActor:
    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    organization_actor_id: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersDeploymentsGetOutput:
    object: str
    id: str
    custom_provider_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    trigger: Optional[str] = None
    provider_id: Optional[str] = None
    custom_provider_version_id: Optional[str] = None
    commit: Optional[DashboardInstanceCustomProvidersDeploymentsGetOutputCommit] = None
    actor: Optional[DashboardInstanceCustomProvidersDeploymentsGetOutputActor] = None


class mapDashboardInstanceCustomProvidersDeploymentsGetOutputCommit:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetOutputCommit:
        return DashboardInstanceCustomProvidersDeploymentsGetOutputCommit(
        id=data.get('id'),
        type=data.get('type'),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetOutputCommit, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetOutputActor:
        return DashboardInstanceCustomProvidersDeploymentsGetOutputActor(
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        organization_actor_id=data.get('organization_actor_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersDeploymentsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersDeploymentsGetOutput:
        return DashboardInstanceCustomProvidersDeploymentsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        trigger=data.get('trigger'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        commit=mapDashboardInstanceCustomProvidersDeploymentsGetOutputCommit.from_dict(data.get('commit')) if data.get('commit') else None,
        actor=mapDashboardInstanceCustomProvidersDeploymentsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersDeploymentsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
