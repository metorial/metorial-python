from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsUpdateOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsUpdateOutputProviderDeployments:
    object: str
    id: str
    provider_id: str
    name: Optional[str] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class DashboardInstanceSessionsUpdateOutput:
    object: str
    id: str
    connection_status: str
    usage: DashboardInstanceSessionsUpdateOutputUsage
    provider_deployments: List[DashboardInstanceSessionsUpdateOutputProviderDeployments]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    connection_url: Optional[str] = None
    connection_key: Optional[str] = None


class mapDashboardInstanceSessionsUpdateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsUpdateOutputUsage:
        return DashboardInstanceSessionsUpdateOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsUpdateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsUpdateOutputProviderDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsUpdateOutputProviderDeployments:
        return DashboardInstanceSessionsUpdateOutputProviderDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsUpdateOutputProviderDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsUpdateOutput:
        return DashboardInstanceSessionsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        connection_status=data.get('connection_status'),
        usage=mapDashboardInstanceSessionsUpdateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        connection_url=data.get('connection_url'),
        connection_key=data.get('connection_key'),
        provider_deployments=[mapDashboardInstanceSessionsUpdateOutputProviderDeployments.from_dict(item) for item in data.get('provider_deployments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSessionsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsUpdateBody:
        return DashboardInstanceSessionsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
