from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsGetOutputUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsGetOutputProvidersUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsGetOutputProvidersDeployment:
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
class DashboardInstanceSessionsGetOutputProvidersConfig:
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
class DashboardInstanceSessionsGetOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class DashboardInstanceSessionsGetOutputProviders:
    object: str
    id: str
    status: str
    usage: DashboardInstanceSessionsGetOutputProvidersUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: DashboardInstanceSessionsGetOutputProvidersDeployment
    config: DashboardInstanceSessionsGetOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[DashboardInstanceSessionsGetOutputProvidersAuthConfig] = None
@dataclass
class DashboardInstanceSessionsGetOutput:
    object: str
    id: str
    connection_state: str
    connection_url: str
    usage: DashboardInstanceSessionsGetOutputUsage
    providers: List[DashboardInstanceSessionsGetOutputProviders]
    from_templates_ids: List[str]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceSessionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsGetOutputUsage:
        return DashboardInstanceSessionsGetOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsGetOutputProvidersUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsGetOutputProvidersUsage:
        return DashboardInstanceSessionsGetOutputProvidersUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsGetOutputProvidersUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsGetOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsGetOutputProvidersDeployment:
        return DashboardInstanceSessionsGetOutputProvidersDeployment(
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
    def to_dict(value: Union[DashboardInstanceSessionsGetOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsGetOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsGetOutputProvidersConfig:
        return DashboardInstanceSessionsGetOutputProvidersConfig(
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
    def to_dict(value: Union[DashboardInstanceSessionsGetOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsGetOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsGetOutputProvidersAuthConfig:
        return DashboardInstanceSessionsGetOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsGetOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsGetOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsGetOutputProviders:
        return DashboardInstanceSessionsGetOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapDashboardInstanceSessionsGetOutputProvidersUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapDashboardInstanceSessionsGetOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceSessionsGetOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceSessionsGetOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsGetOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsGetOutput:
        return DashboardInstanceSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        connection_state=data.get('connection_state'),
        connection_url=data.get('connection_url'),
        usage=mapDashboardInstanceSessionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        providers=[mapDashboardInstanceSessionsGetOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        from_templates_ids=data.get('from_templates_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
