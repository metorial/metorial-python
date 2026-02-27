from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionTemplatesProvidersCreateOutputDeployment:
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
class SessionTemplatesProvidersCreateOutputConfig:
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
class SessionTemplatesProvidersCreateOutputAuthConfig:
    object: str
    id: str
@dataclass
class SessionTemplatesProvidersCreateOutput:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: SessionTemplatesProvidersCreateOutputDeployment
    config: SessionTemplatesProvidersCreateOutputConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[SessionTemplatesProvidersCreateOutputAuthConfig] = None


class mapSessionTemplatesProvidersCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersCreateOutputDeployment:
        return SessionTemplatesProvidersCreateOutputDeployment(
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
    def to_dict(value: Union[SessionTemplatesProvidersCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersCreateOutputConfig:
        return SessionTemplatesProvidersCreateOutputConfig(
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
    def to_dict(value: Union[SessionTemplatesProvidersCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersCreateOutputAuthConfig:
        return SessionTemplatesProvidersCreateOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersCreateOutput:
        return SessionTemplatesProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapSessionTemplatesProvidersCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionTemplatesProvidersCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionTemplatesProvidersCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionTemplatesProvidersCreateBodyToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class SessionTemplatesProvidersCreateBody:
    session_template_id: str
    provider_deployment_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    tool_filters: Optional[SessionTemplatesProvidersCreateBodyToolFilters] = None


class mapSessionTemplatesProvidersCreateBodyToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersCreateBodyToolFilters:
        return SessionTemplatesProvidersCreateBodyToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersCreateBodyToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersCreateBody:
        return SessionTemplatesProvidersCreateBody(
        session_template_id=data.get('session_template_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        tool_filters=mapSessionTemplatesProvidersCreateBodyToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
