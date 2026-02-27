from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionTemplatesCreateOutput:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceSessionTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateOutput:
        return ManagementInstanceSessionTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionTemplatesCreateBodyProvidersToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class ManagementInstanceSessionTemplatesCreateBodyProviders:
    provider_deployment: Union[Dict[str, Any], str]
    provider_config: Optional[Union[Dict[str, Any], str]] = None
    provider_auth_config: Optional[Union[Dict[str, Any], str]] = None
    tool_filters: Optional[ManagementInstanceSessionTemplatesCreateBodyProvidersToolFilters] = None
@dataclass
class ManagementInstanceSessionTemplatesCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    providers: Optional[List[ManagementInstanceSessionTemplatesCreateBodyProviders]] = None


class mapManagementInstanceSessionTemplatesCreateBodyProvidersToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateBodyProvidersToolFilters:
        return ManagementInstanceSessionTemplatesCreateBodyProvidersToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateBodyProvidersToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateBodyProviders:
        return ManagementInstanceSessionTemplatesCreateBodyProviders(
        provider_deployment=data.get('provider_deployment'),
        provider_config=data.get('provider_config'),
        provider_auth_config=data.get('provider_auth_config'),
        tool_filters=mapManagementInstanceSessionTemplatesCreateBodyProvidersToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateBody:
        return ManagementInstanceSessionTemplatesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapManagementInstanceSessionTemplatesCreateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
