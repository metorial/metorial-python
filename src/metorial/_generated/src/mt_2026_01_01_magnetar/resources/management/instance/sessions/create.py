from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsCreateOutputUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsCreateOutputProvidersUsage:
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsCreateOutputProvidersDeployment:
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
class ManagementInstanceSessionsCreateOutputProvidersConfig:
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
class ManagementInstanceSessionsCreateOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionsCreateOutputProviders:
    object: str
    id: str
    status: str
    usage: ManagementInstanceSessionsCreateOutputProvidersUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: ManagementInstanceSessionsCreateOutputProvidersDeployment
    config: ManagementInstanceSessionsCreateOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[ManagementInstanceSessionsCreateOutputProvidersAuthConfig] = None
@dataclass
class ManagementInstanceSessionsCreateOutput:
    object: str
    id: str
    connection_state: str
    connection_url: str
    usage: ManagementInstanceSessionsCreateOutputUsage
    providers: List[ManagementInstanceSessionsCreateOutputProviders]
    from_templates_ids: List[str]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceSessionsCreateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputUsage:
        return ManagementInstanceSessionsCreateOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputProvidersUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputProvidersUsage:
        return ManagementInstanceSessionsCreateOutputProvidersUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputProvidersUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputProvidersDeployment:
        return ManagementInstanceSessionsCreateOutputProvidersDeployment(
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
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputProvidersConfig:
        return ManagementInstanceSessionsCreateOutputProvidersConfig(
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
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputProvidersAuthConfig:
        return ManagementInstanceSessionsCreateOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputProviders:
        return ManagementInstanceSessionsCreateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapManagementInstanceSessionsCreateOutputProvidersUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapManagementInstanceSessionsCreateOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapManagementInstanceSessionsCreateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceSessionsCreateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutput:
        return ManagementInstanceSessionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        connection_state=data.get('connection_state'),
        connection_url=data.get('connection_url'),
        usage=mapManagementInstanceSessionsCreateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        providers=[mapManagementInstanceSessionsCreateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        from_templates_ids=data.get('from_templates_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsCreateBody:
    providers: List[Dict[str, Any]]
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateBody:
        return ManagementInstanceSessionsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=data.get('providers', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
