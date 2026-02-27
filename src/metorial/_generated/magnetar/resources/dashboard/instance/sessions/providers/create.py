from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsProvidersCreateOutput:
    object: str
    id: str
    session_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None


class mapDashboardInstanceSessionsProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersCreateOutput:
        return DashboardInstanceSessionsProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsProvidersCreateBodyToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class DashboardInstanceSessionsProvidersCreateBody:
    provider_deployment: Union[Dict[str, Any], str]
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_config: Optional[Union[Dict[str, Any], str]] = None
    provider_auth_config: Optional[Union[Dict[str, Any], str]] = None
    tool_filters: Optional[DashboardInstanceSessionsProvidersCreateBodyToolFilters] = None


class mapDashboardInstanceSessionsProvidersCreateBodyToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersCreateBodyToolFilters:
        return DashboardInstanceSessionsProvidersCreateBodyToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersCreateBodyToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersCreateBody:
        return DashboardInstanceSessionsProvidersCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_deployment=data.get('provider_deployment'),
        provider_config=data.get('provider_config'),
        provider_auth_config=data.get('provider_auth_config'),
        tool_filters=mapDashboardInstanceSessionsProvidersCreateBodyToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
