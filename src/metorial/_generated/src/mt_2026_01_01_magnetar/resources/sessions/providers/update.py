from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsProvidersUpdateOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class SessionsProvidersUpdateOutputDeployment:
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
class SessionsProvidersUpdateOutputConfig:
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
class SessionsProvidersUpdateOutputAuthConfig:
    object: str
    id: str
@dataclass
class SessionsProvidersUpdateOutput:
    object: str
    id: str
    status: str
    usage: SessionsProvidersUpdateOutputUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: SessionsProvidersUpdateOutputDeployment
    config: SessionsProvidersUpdateOutputConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[SessionsProvidersUpdateOutputAuthConfig] = None


class mapSessionsProvidersUpdateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersUpdateOutputUsage:
        return SessionsProvidersUpdateOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersUpdateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersUpdateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersUpdateOutputDeployment:
        return SessionsProvidersUpdateOutputDeployment(
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
    def to_dict(value: Union[SessionsProvidersUpdateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersUpdateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersUpdateOutputConfig:
        return SessionsProvidersUpdateOutputConfig(
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
    def to_dict(value: Union[SessionsProvidersUpdateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersUpdateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersUpdateOutputAuthConfig:
        return SessionsProvidersUpdateOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersUpdateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersUpdateOutput:
        return SessionsProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapSessionsProvidersUpdateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapSessionsProvidersUpdateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionsProvidersUpdateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionsProvidersUpdateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsProvidersUpdateBody:
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None


class mapSessionsProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsProvidersUpdateBody:
        return SessionsProvidersUpdateBody(
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[SessionsProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

