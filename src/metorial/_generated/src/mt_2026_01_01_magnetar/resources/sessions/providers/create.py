from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsProvidersCreateOutputUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class SessionsProvidersCreateOutputDeployment:
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
class SessionsProvidersCreateOutputConfig:
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
class SessionsProvidersCreateOutputAuthConfig:
    object: str
    id: str
@dataclass
class SessionsProvidersCreateOutput:
    object: str
    id: str
    status: str
    usage: SessionsProvidersCreateOutputUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: SessionsProvidersCreateOutputDeployment
    config: SessionsProvidersCreateOutputConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[SessionsProvidersCreateOutputAuthConfig] = None


class mapSessionsProvidersCreateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersCreateOutputUsage:
        return SessionsProvidersCreateOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersCreateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersCreateOutputDeployment:
        return SessionsProvidersCreateOutputDeployment(
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
    def to_dict(value: Union[SessionsProvidersCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersCreateOutputConfig:
        return SessionsProvidersCreateOutputConfig(
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
    def to_dict(value: Union[SessionsProvidersCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersCreateOutputAuthConfig:
        return SessionsProvidersCreateOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersCreateOutput:
        return SessionsProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapSessionsProvidersCreateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapSessionsProvidersCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionsProvidersCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionsProvidersCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsProvidersCreateBody:
    session_id: str
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None


class mapSessionsProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersCreateBody:
        return SessionsProvidersCreateBody(
        session_id=data.get('session_id'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
