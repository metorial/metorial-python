from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsUpdateOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsUpdateOutputProvidersUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsUpdateOutputProvidersDeployment:
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
class SessionsUpdateOutputProvidersConfig:
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
class SessionsUpdateOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class SessionsUpdateOutputProviders:
    object: str
    id: str
    status: str
    usage: SessionsUpdateOutputProvidersUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: SessionsUpdateOutputProvidersDeployment
    config: SessionsUpdateOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[SessionsUpdateOutputProvidersAuthConfig] = None
@dataclass
class SessionsUpdateOutput:
    object: str
    id: str
    connection_state: str
    connection_url: str
    usage: SessionsUpdateOutputUsage
    providers: List[SessionsUpdateOutputProviders]
    from_templates_ids: List[str]
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    client_secret: Optional[str] = None


class mapSessionsUpdateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateOutputUsage:
        return SessionsUpdateOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsUpdateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsUpdateOutputProvidersUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateOutputProvidersUsage:
        return SessionsUpdateOutputProvidersUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsUpdateOutputProvidersUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsUpdateOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateOutputProvidersDeployment:
        return SessionsUpdateOutputProvidersDeployment(
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
    def to_dict(value: Union[SessionsUpdateOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsUpdateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateOutputProvidersConfig:
        return SessionsUpdateOutputProvidersConfig(
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
    def to_dict(value: Union[SessionsUpdateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsUpdateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateOutputProvidersAuthConfig:
        return SessionsUpdateOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsUpdateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsUpdateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateOutputProviders:
        return SessionsUpdateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapSessionsUpdateOutputProvidersUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapSessionsUpdateOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionsUpdateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionsUpdateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsUpdateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateOutput:
        return SessionsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        connection_state=data.get('connection_state'),
        connection_url=data.get('connection_url'),
        client_secret=data.get('client_secret'),
        usage=mapSessionsUpdateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        providers=[mapSessionsUpdateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        from_templates_ids=data.get('from_templates_ids', []),
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSessionsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsUpdateBody:
        return SessionsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[SessionsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

