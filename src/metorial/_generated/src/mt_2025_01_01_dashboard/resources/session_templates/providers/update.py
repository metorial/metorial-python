from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionTemplatesProvidersUpdateOutputDeployment:
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
class SessionTemplatesProvidersUpdateOutputConfig:
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
class SessionTemplatesProvidersUpdateOutputAuthConfig:
    object: str
    id: str
@dataclass
class SessionTemplatesProvidersUpdateOutput:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: SessionTemplatesProvidersUpdateOutputDeployment
    config: SessionTemplatesProvidersUpdateOutputConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[SessionTemplatesProvidersUpdateOutputAuthConfig] = None


class mapSessionTemplatesProvidersUpdateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersUpdateOutputDeployment:
        return SessionTemplatesProvidersUpdateOutputDeployment(
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
    def to_dict(value: Union[SessionTemplatesProvidersUpdateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersUpdateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersUpdateOutputConfig:
        return SessionTemplatesProvidersUpdateOutputConfig(
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
    def to_dict(value: Union[SessionTemplatesProvidersUpdateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersUpdateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersUpdateOutputAuthConfig:
        return SessionTemplatesProvidersUpdateOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersUpdateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersUpdateOutput:
        return SessionTemplatesProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapSessionTemplatesProvidersUpdateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionTemplatesProvidersUpdateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionTemplatesProvidersUpdateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionTemplatesProvidersUpdateBodyToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class SessionTemplatesProvidersUpdateBody:
    tool_filters: Optional[SessionTemplatesProvidersUpdateBodyToolFilters] = None


class mapSessionTemplatesProvidersUpdateBodyToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersUpdateBodyToolFilters:
        return SessionTemplatesProvidersUpdateBodyToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersUpdateBodyToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesProvidersUpdateBody:
        return SessionTemplatesProvidersUpdateBody(
        tool_filters=mapSessionTemplatesProvidersUpdateBodyToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

