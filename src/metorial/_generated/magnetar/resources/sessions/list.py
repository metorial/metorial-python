from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsListOutputItemsUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsListOutputItemsProvidersUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsListOutputItemsProvidersDeployment:
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
class SessionsListOutputItemsProvidersConfig:
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
class SessionsListOutputItemsProvidersAuthConfig:
    object: str
    id: str
@dataclass
class SessionsListOutputItemsProviders:
    object: str
    id: str
    status: str
    usage: SessionsListOutputItemsProvidersUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: SessionsListOutputItemsProvidersDeployment
    config: SessionsListOutputItemsProvidersConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[SessionsListOutputItemsProvidersAuthConfig] = None
@dataclass
class SessionsListOutputItems:
    object: str
    id: str
    connection_state: str
    connection_url: str
    usage: SessionsListOutputItemsUsage
    providers: List[SessionsListOutputItemsProviders]
    from_templates_ids: List[str]
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    client_secret: Optional[str] = None
@dataclass
class SessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsListOutput:
    items: List[SessionsListOutputItems]
    pagination: SessionsListOutputPagination


class mapSessionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsUsage:
        return SessionsListOutputItemsUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutputItemsProvidersUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsProvidersUsage:
        return SessionsListOutputItemsProvidersUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputItemsProvidersUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutputItemsProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsProvidersDeployment:
        return SessionsListOutputItemsProvidersDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputItemsProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutputItemsProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsProvidersConfig:
        return SessionsListOutputItemsProvidersConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputItemsProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutputItemsProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsProvidersAuthConfig:
        return SessionsListOutputItemsProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputItemsProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutputItemsProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputItemsProviders:
        return SessionsListOutputItemsProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapSessionsListOutputItemsProvidersUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapSessionsListOutputItemsProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionsListOutputItemsProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionsListOutputItemsProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputItemsProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputItems:
        return SessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        connection_state=data.get('connection_state'),
        connection_url=data.get('connection_url'),
        client_secret=data.get('client_secret'),
        usage=mapSessionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        providers=[mapSessionsListOutputItemsProviders.from_dict(item) for item in data.get('providers', []) if item],
        from_templates_ids=data.get('from_templates_ids', []),
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutputPagination:
        return SessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListOutput:
        return SessionsListOutput(
        items=[mapSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsListQuery:
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


class mapSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsListQuery:
        return SessionsListQuery(
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
    def to_dict(value: Union[SessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

