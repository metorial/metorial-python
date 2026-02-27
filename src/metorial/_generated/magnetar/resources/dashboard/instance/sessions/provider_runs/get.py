from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsProviderRunsGetOutput:
    object: str
    id: str
    session_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    session_provider_id: Optional[str] = None
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    provider_version_id: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapDashboardInstanceSessionsProviderRunsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProviderRunsGetOutput:
        return DashboardInstanceSessionsProviderRunsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_version_id=data.get('provider_version_id'),
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProviderRunsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
