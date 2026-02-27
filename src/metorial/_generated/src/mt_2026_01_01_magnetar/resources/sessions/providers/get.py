from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsProvidersGetOutputUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class SessionsProvidersGetOutputDeployment:
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
class SessionsProvidersGetOutputConfig:
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
class SessionsProvidersGetOutputAuthConfig:
    object: str
    id: str
@dataclass
class SessionsProvidersGetOutput:
    object: str
    id: str
    status: str
    usage: SessionsProvidersGetOutputUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: SessionsProvidersGetOutputDeployment
    config: SessionsProvidersGetOutputConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[SessionsProvidersGetOutputAuthConfig] = None


class mapSessionsProvidersGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersGetOutputUsage:
        return SessionsProvidersGetOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersGetOutputDeployment:
        return SessionsProvidersGetOutputDeployment(
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
    def to_dict(value: Union[SessionsProvidersGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersGetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersGetOutputConfig:
        return SessionsProvidersGetOutputConfig(
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
    def to_dict(value: Union[SessionsProvidersGetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersGetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersGetOutputAuthConfig:
        return SessionsProvidersGetOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersGetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersGetOutput:
        return SessionsProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapSessionsProvidersGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapSessionsProvidersGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionsProvidersGetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionsProvidersGetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
