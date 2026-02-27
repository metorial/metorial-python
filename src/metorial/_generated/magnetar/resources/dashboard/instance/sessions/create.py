from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsCreateOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsCreateOutputProviderDeployments:
    object: str
    id: str
    provider_id: str
    name: Optional[str] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsCreateOutput:
    object: str
    id: str
    connection_status: str
    usage: DashboardInstanceSessionsCreateOutputUsage
    provider_deployments: List[DashboardInstanceSessionsCreateOutputProviderDeployments]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    connection_url: Optional[str] = None
    connection_key: Optional[str] = None


class mapDashboardInstanceSessionsCreateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateOutputUsage:
        return DashboardInstanceSessionsCreateOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsCreateOutputProviderDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateOutputProviderDeployments:
        return DashboardInstanceSessionsCreateOutputProviderDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateOutputProviderDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateOutput:
        return DashboardInstanceSessionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        connection_status=data.get('connection_status'),
        usage=mapDashboardInstanceSessionsCreateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        connection_url=data.get('connection_url'),
        connection_key=data.get('connection_key'),
        provider_deployments=[mapDashboardInstanceSessionsCreateOutputProviderDeployments.from_dict(item) for item in data.get('provider_deployments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsCreateBodyProvidersToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class DashboardInstanceSessionsCreateBodyProviders:
    provider_deployment: Union[Dict[str, Any], str]
    provider_config: Optional[Union[Dict[str, Any], str]] = None
    provider_auth_config: Optional[Union[Dict[str, Any], str]] = None
    session_template_id: Optional[str] = None
    tool_filters: Optional[DashboardInstanceSessionsCreateBodyProvidersToolFilters] = None
@dataclass
class DashboardInstanceSessionsCreateBody:
    providers: List[DashboardInstanceSessionsCreateBodyProviders]
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSessionsCreateBodyProvidersToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateBodyProvidersToolFilters:
        return DashboardInstanceSessionsCreateBodyProvidersToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateBodyProvidersToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateBodyProviders:
        return DashboardInstanceSessionsCreateBodyProviders(
        provider_deployment=data.get('provider_deployment'),
        provider_config=data.get('provider_config'),
        provider_auth_config=data.get('provider_auth_config'),
        session_template_id=data.get('session_template_id'),
        tool_filters=mapDashboardInstanceSessionsCreateBodyProvidersToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateBody:
        return DashboardInstanceSessionsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapDashboardInstanceSessionsCreateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
