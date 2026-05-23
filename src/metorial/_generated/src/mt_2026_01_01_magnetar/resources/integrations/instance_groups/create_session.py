from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstanceGroupsCreateSessionOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class IntegrationsInstanceGroupsCreateSessionOutputProvidersUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class IntegrationsInstanceGroupsCreateSessionOutputProvidersDeployment:
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
class IntegrationsInstanceGroupsCreateSessionOutputProvidersConfig:
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
class IntegrationsInstanceGroupsCreateSessionOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class IntegrationsInstanceGroupsCreateSessionOutputProviders:
    object: str
    id: str
    status: str
    usage: IntegrationsInstanceGroupsCreateSessionOutputProvidersUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: IntegrationsInstanceGroupsCreateSessionOutputProvidersDeployment
    config: IntegrationsInstanceGroupsCreateSessionOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[IntegrationsInstanceGroupsCreateSessionOutputProvidersAuthConfig] = None
@dataclass
class IntegrationsInstanceGroupsCreateSessionOutput:
    object: str
    id: str
    status: str
    connection_state: str
    connection_url: str
    usage: IntegrationsInstanceGroupsCreateSessionOutputUsage
    providers: List[IntegrationsInstanceGroupsCreateSessionOutputProviders]
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


class mapIntegrationsInstanceGroupsCreateSessionOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionOutputUsage:
        return IntegrationsInstanceGroupsCreateSessionOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionOutputProvidersUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionOutputProvidersUsage:
        return IntegrationsInstanceGroupsCreateSessionOutputProvidersUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionOutputProvidersUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionOutputProvidersDeployment:
        return IntegrationsInstanceGroupsCreateSessionOutputProvidersDeployment(
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
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionOutputProvidersConfig:
        return IntegrationsInstanceGroupsCreateSessionOutputProvidersConfig(
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
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionOutputProvidersAuthConfig:
        return IntegrationsInstanceGroupsCreateSessionOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionOutputProviders:
        return IntegrationsInstanceGroupsCreateSessionOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapIntegrationsInstanceGroupsCreateSessionOutputProvidersUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapIntegrationsInstanceGroupsCreateSessionOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapIntegrationsInstanceGroupsCreateSessionOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsInstanceGroupsCreateSessionOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateSessionOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionOutput:
        return IntegrationsInstanceGroupsCreateSessionOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        connection_state=data.get('connection_state'),
        connection_url=data.get('connection_url'),
        client_secret=data.get('client_secret'),
        usage=mapIntegrationsInstanceGroupsCreateSessionOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        providers=[mapIntegrationsInstanceGroupsCreateSessionOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        from_templates_ids=data.get('from_templates_ids', []),
        has_errors=data.get('has_errors'),
        has_warnings=data.get('has_warnings'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstanceGroupsCreateSessionBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapIntegrationsInstanceGroupsCreateSessionBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateSessionBody:
        return IntegrationsInstanceGroupsCreateSessionBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateSessionBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

