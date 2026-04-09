from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionTemplatesCreateOutputProvidersDeployment:
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
class ManagementInstanceSessionTemplatesCreateOutputProvidersConfig:
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
class ManagementInstanceSessionTemplatesCreateOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionTemplatesCreateOutputProviders:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: ManagementInstanceSessionTemplatesCreateOutputProvidersDeployment
    config: ManagementInstanceSessionTemplatesCreateOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[ManagementInstanceSessionTemplatesCreateOutputProvidersAuthConfig] = None
@dataclass
class ManagementInstanceSessionTemplatesCreateOutput:
    object: str
    id: str
    status: str
    name: str
    providers: List[ManagementInstanceSessionTemplatesCreateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceSessionTemplatesCreateOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateOutputProvidersDeployment:
        return ManagementInstanceSessionTemplatesCreateOutputProvidersDeployment(
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
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesCreateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateOutputProvidersConfig:
        return ManagementInstanceSessionTemplatesCreateOutputProvidersConfig(
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
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesCreateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateOutputProvidersAuthConfig:
        return ManagementInstanceSessionTemplatesCreateOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesCreateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateOutputProviders:
        return ManagementInstanceSessionTemplatesCreateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapManagementInstanceSessionTemplatesCreateOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapManagementInstanceSessionTemplatesCreateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceSessionTemplatesCreateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionTemplatesCreateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateOutput:
        return ManagementInstanceSessionTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapManagementInstanceSessionTemplatesCreateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
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
class ManagementInstanceSessionTemplatesCreateBodyProviders:
    provider_deployment_id: Optional[str] = None
    provider_config_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
@dataclass
class ManagementInstanceSessionTemplatesCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    providers: Optional[List[ManagementInstanceSessionTemplatesCreateBodyProviders]] = None


class mapManagementInstanceSessionTemplatesCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionTemplatesCreateBodyProviders:
        return ManagementInstanceSessionTemplatesCreateBodyProviders(
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        tool_filters=data.get('tool_filters')
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

