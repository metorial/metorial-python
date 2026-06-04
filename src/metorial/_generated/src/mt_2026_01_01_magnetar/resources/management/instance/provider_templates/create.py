from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderTemplatesCreateOutput:
    object: str
    id: str
    status: str
    name: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    integration_id: Optional[str] = None


class mapManagementInstanceProviderTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderTemplatesCreateOutput:
        return ManagementInstanceProviderTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderTemplatesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderTemplatesCreateBodyProviders:
    provider_id: str
    provider_deployment_id: Optional[str] = None
    provider_auth_method_id: Optional[str] = None
    provider_auth_credentials_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filters: Optional[Any] = None
@dataclass
class ManagementInstanceProviderTemplatesCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    providers: Optional[List[ManagementInstanceProviderTemplatesCreateBodyProviders]] = None
    integration_id: Optional[str] = None


class mapManagementInstanceProviderTemplatesCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderTemplatesCreateBodyProviders:
        return ManagementInstanceProviderTemplatesCreateBodyProviders(
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        provider_auth_credentials_id=data.get('provider_auth_credentials_id'),
        provider_config_id=data.get('provider_config_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderTemplatesCreateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderTemplatesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderTemplatesCreateBody:
        return ManagementInstanceProviderTemplatesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapManagementInstanceProviderTemplatesCreateBodyProviders.from_dict(item) for item in data.get('providers', []) if item],
        integration_id=data.get('integration_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderTemplatesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

