from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsProvidersUpdateOutputConfig:
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
class IntegrationsProvidersUpdateOutputCallbacks:
    object: str
    status: str
    callback_id: Optional[str] = None
@dataclass
class IntegrationsProvidersUpdateOutput:
    object: str
    id: str
    status: str
    integration_id: str
    name: str
    provider_id: str
    deployment_id: str
    callbacks: IntegrationsProvidersUpdateOutputCallbacks
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method_id: Optional[str] = None
    auth_credentials_id: Optional[str] = None
    config: Optional[IntegrationsProvidersUpdateOutputConfig] = None
    archived_at: Optional[datetime] = None


class mapIntegrationsProvidersUpdateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsProvidersUpdateOutputConfig:
        return IntegrationsProvidersUpdateOutputConfig(
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
    def to_dict(value: Union[IntegrationsProvidersUpdateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsProvidersUpdateOutputCallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsProvidersUpdateOutputCallbacks:
        return IntegrationsProvidersUpdateOutputCallbacks(
        object=data.get('object'),
        status=data.get('status'),
        callback_id=data.get('callback_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsProvidersUpdateOutputCallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsProvidersUpdateOutput:
        return IntegrationsProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        integration_id=data.get('integration_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapIntegrationsProvidersUpdateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        callbacks=mapIntegrationsProvidersUpdateOutputCallbacks.from_dict(data.get('callbacks')) if data.get('callbacks') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsProvidersUpdateBodyCallbacks:
    status: str
@dataclass
class IntegrationsProvidersUpdateBody:
    provider_deployment_id: Optional[str] = None
    provider_auth_method_id: Optional[str] = None
    provider_auth_credentials_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
    callbacks: Optional[IntegrationsProvidersUpdateBodyCallbacks] = None


class mapIntegrationsProvidersUpdateBodyCallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsProvidersUpdateBodyCallbacks:
        return IntegrationsProvidersUpdateBodyCallbacks(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsProvidersUpdateBodyCallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsProvidersUpdateBody:
        return IntegrationsProvidersUpdateBody(
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        provider_auth_credentials_id=data.get('provider_auth_credentials_id'),
        provider_config_id=data.get('provider_config_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filters=data.get('tool_filters'),
        callbacks=mapIntegrationsProvidersUpdateBodyCallbacks.from_dict(data.get('callbacks')) if data.get('callbacks') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

