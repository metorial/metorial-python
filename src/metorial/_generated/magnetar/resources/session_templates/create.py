from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionTemplatesCreateOutput:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSessionTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesCreateOutput:
        return SessionTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionTemplatesCreateBodyProvidersToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class SessionTemplatesCreateBodyProviders:
    provider_deployment: Union[Dict[str, Any], str]
    provider_config: Optional[Union[Dict[str, Any], str]] = None
    provider_auth_config: Optional[Union[Dict[str, Any], str]] = None
    tool_filters: Optional[SessionTemplatesCreateBodyProvidersToolFilters] = None
@dataclass
class SessionTemplatesCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    providers: Optional[List[SessionTemplatesCreateBodyProviders]] = None


class mapSessionTemplatesCreateBodyProvidersToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesCreateBodyProvidersToolFilters:
        return SessionTemplatesCreateBodyProvidersToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesCreateBodyProvidersToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesCreateBodyProviders:
        return SessionTemplatesCreateBodyProviders(
        provider_deployment=data.get('provider_deployment'),
        provider_config=data.get('provider_config'),
        provider_auth_config=data.get('provider_auth_config'),
        tool_filters=mapSessionTemplatesCreateBodyProvidersToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesCreateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesCreateBody:
        return SessionTemplatesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapSessionTemplatesCreateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
