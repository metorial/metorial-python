from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsCreateOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class SessionsCreateOutputProviderDeployments:
    object: str
    id: str
    provider_id: str
    name: Optional[str] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class SessionsCreateOutput:
    object: str
    id: str
    connection_status: str
    usage: SessionsCreateOutputUsage
    provider_deployments: List[SessionsCreateOutputProviderDeployments]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    connection_url: Optional[str] = None
    connection_key: Optional[str] = None


class mapSessionsCreateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateOutputUsage:
        return SessionsCreateOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[SessionsCreateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsCreateOutputProviderDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateOutputProviderDeployments:
        return SessionsCreateOutputProviderDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsCreateOutputProviderDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateOutput:
        return SessionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        connection_status=data.get('connection_status'),
        usage=mapSessionsCreateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        connection_url=data.get('connection_url'),
        connection_key=data.get('connection_key'),
        provider_deployments=[mapSessionsCreateOutputProviderDeployments.from_dict(item) for item in data.get('provider_deployments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsCreateBodyProvidersToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class SessionsCreateBodyProviders:
    provider_deployment: Union[Dict[str, Any], str]
    provider_config: Optional[Union[Dict[str, Any], str]] = None
    provider_auth_config: Optional[Union[Dict[str, Any], str]] = None
    session_template_id: Optional[str] = None
    tool_filters: Optional[SessionsCreateBodyProvidersToolFilters] = None
@dataclass
class SessionsCreateBody:
    providers: List[SessionsCreateBodyProviders]
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSessionsCreateBodyProvidersToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateBodyProvidersToolFilters:
        return SessionsCreateBodyProvidersToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionsCreateBodyProvidersToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateBodyProviders:
        return SessionsCreateBodyProviders(
        provider_deployment=data.get('provider_deployment'),
        provider_config=data.get('provider_config'),
        provider_auth_config=data.get('provider_auth_config'),
        session_template_id=data.get('session_template_id'),
        tool_filters=mapSessionsCreateBodyProvidersToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsCreateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateBody:
        return SessionsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapSessionsCreateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
