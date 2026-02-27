from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsListOutputItemsUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsListOutputItemsProvidersUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsListOutputItemsProvidersDeployment:
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
class DashboardInstanceSessionsListOutputItemsProvidersConfig:
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
class DashboardInstanceSessionsListOutputItemsProvidersAuthConfig:
    object: str
    id: str
@dataclass
class DashboardInstanceSessionsListOutputItemsProviders:
    object: str
    id: str
    status: str
    usage: DashboardInstanceSessionsListOutputItemsProvidersUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: DashboardInstanceSessionsListOutputItemsProvidersDeployment
    config: DashboardInstanceSessionsListOutputItemsProvidersConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[DashboardInstanceSessionsListOutputItemsProvidersAuthConfig] = None
@dataclass
class DashboardInstanceSessionsListOutputItems:
    object: str
    id: str
    connection_state: str
    connection_url: str
    usage: DashboardInstanceSessionsListOutputItemsUsage
    providers: List[DashboardInstanceSessionsListOutputItemsProviders]
    from_templates_ids: List[str]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsListOutput:
    items: List[DashboardInstanceSessionsListOutputItems]
    pagination: DashboardInstanceSessionsListOutputPagination


class mapDashboardInstanceSessionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputItemsUsage:
        return DashboardInstanceSessionsListOutputItemsUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutputItemsProvidersUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputItemsProvidersUsage:
        return DashboardInstanceSessionsListOutputItemsProvidersUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListOutputItemsProvidersUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutputItemsProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputItemsProvidersDeployment:
        return DashboardInstanceSessionsListOutputItemsProvidersDeployment(
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
    def to_dict(value: Union[DashboardInstanceSessionsListOutputItemsProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutputItemsProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputItemsProvidersConfig:
        return DashboardInstanceSessionsListOutputItemsProvidersConfig(
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
    def to_dict(value: Union[DashboardInstanceSessionsListOutputItemsProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutputItemsProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputItemsProvidersAuthConfig:
        return DashboardInstanceSessionsListOutputItemsProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListOutputItemsProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutputItemsProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputItemsProviders:
        return DashboardInstanceSessionsListOutputItemsProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapDashboardInstanceSessionsListOutputItemsProvidersUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapDashboardInstanceSessionsListOutputItemsProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceSessionsListOutputItemsProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceSessionsListOutputItemsProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListOutputItemsProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputItems:
        return DashboardInstanceSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        connection_state=data.get('connection_state'),
        connection_url=data.get('connection_url'),
        usage=mapDashboardInstanceSessionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        providers=[mapDashboardInstanceSessionsListOutputItemsProviders.from_dict(item) for item in data.get('providers', []) if item],
        from_templates_ids=data.get('from_templates_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutputPagination:
        return DashboardInstanceSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListOutput:
        return DashboardInstanceSessionsListOutput(
        items=[mapDashboardInstanceSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    session_template_id: Optional[Union[str, List[str]]] = None
    session_provider_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsListQuery:
        return DashboardInstanceSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        session_template_id=data.get('session_template_id'),
        session_provider_id=data.get('session_provider_id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
