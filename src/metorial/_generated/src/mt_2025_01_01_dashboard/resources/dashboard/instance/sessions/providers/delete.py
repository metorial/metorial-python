from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsProvidersDeleteOutputUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsProvidersDeleteOutputDeployment:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSessionsProvidersDeleteOutputConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSessionsProvidersDeleteOutputAuthConfig:
    object: str
    id: str
@dataclass
class DashboardInstanceSessionsProvidersDeleteOutput:
    object: str
    id: str
    status: str
    usage: DashboardInstanceSessionsProvidersDeleteOutputUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: DashboardInstanceSessionsProvidersDeleteOutputDeployment
    config: DashboardInstanceSessionsProvidersDeleteOutputConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[DashboardInstanceSessionsProvidersDeleteOutputAuthConfig] = None


class mapDashboardInstanceSessionsProvidersDeleteOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersDeleteOutputUsage:
        return DashboardInstanceSessionsProvidersDeleteOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersDeleteOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsProvidersDeleteOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersDeleteOutputDeployment:
        return DashboardInstanceSessionsProvidersDeleteOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersDeleteOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsProvidersDeleteOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersDeleteOutputConfig:
        return DashboardInstanceSessionsProvidersDeleteOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersDeleteOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsProvidersDeleteOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersDeleteOutputAuthConfig:
        return DashboardInstanceSessionsProvidersDeleteOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersDeleteOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsProvidersDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsProvidersDeleteOutput:
        return DashboardInstanceSessionsProvidersDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapDashboardInstanceSessionsProvidersDeleteOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapDashboardInstanceSessionsProvidersDeleteOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceSessionsProvidersDeleteOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceSessionsProvidersDeleteOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsProvidersDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
