from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstancesCreateSessionOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class IntegrationsInstancesCreateSessionOutputProvidersUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class IntegrationsInstancesCreateSessionOutputProvidersDeployment:
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
class IntegrationsInstancesCreateSessionOutputProvidersConfig:
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
class IntegrationsInstancesCreateSessionOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class IntegrationsInstancesCreateSessionOutputProviders:
    object: str
    id: str
    status: str
    usage: IntegrationsInstancesCreateSessionOutputProvidersUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: IntegrationsInstancesCreateSessionOutputProvidersDeployment
    config: IntegrationsInstancesCreateSessionOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[IntegrationsInstancesCreateSessionOutputProvidersAuthConfig] = None
@dataclass
class IntegrationsInstancesCreateSessionOutput:
    object: str
    id: str
    status: str
    connection_state: str
    connection_url: str
    usage: IntegrationsInstancesCreateSessionOutputUsage
    providers: List[IntegrationsInstancesCreateSessionOutputProviders]
    from_templates_ids: List[str]
    has_errors: bool
    has_warnings: bool
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    client_secret: Optional[str] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None


class mapIntegrationsInstancesCreateSessionOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionOutputUsage:
        return IntegrationsInstancesCreateSessionOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionOutputProvidersUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionOutputProvidersUsage:
        return IntegrationsInstancesCreateSessionOutputProvidersUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionOutputProvidersUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionOutputProvidersDeployment:
        return IntegrationsInstancesCreateSessionOutputProvidersDeployment(
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
    def to_dict(value: Union[IntegrationsInstancesCreateSessionOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionOutputProvidersConfig:
        return IntegrationsInstancesCreateSessionOutputProvidersConfig(
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
    def to_dict(value: Union[IntegrationsInstancesCreateSessionOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionOutputProvidersAuthConfig:
        return IntegrationsInstancesCreateSessionOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionOutputProviders:
        return IntegrationsInstancesCreateSessionOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapIntegrationsInstancesCreateSessionOutputProvidersUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapIntegrationsInstancesCreateSessionOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapIntegrationsInstancesCreateSessionOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsInstancesCreateSessionOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesCreateSessionOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionOutput:
        return IntegrationsInstancesCreateSessionOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        connection_state=data.get('connection_state'),
        connection_url=data.get('connection_url'),
        client_secret=data.get('client_secret'),
        usage=mapIntegrationsInstancesCreateSessionOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        providers=[mapIntegrationsInstancesCreateSessionOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        from_templates_ids=data.get('from_templates_ids', []),
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstancesCreateSessionBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapIntegrationsInstancesCreateSessionBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesCreateSessionBody:
        return IntegrationsInstancesCreateSessionBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesCreateSessionBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

