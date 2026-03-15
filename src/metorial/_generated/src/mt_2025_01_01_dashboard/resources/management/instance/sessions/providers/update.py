from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsProvidersUpdateOutputUsage:
    total_productive_client_message_count: float
    total_productive_provider_message_count: float
@dataclass
class ManagementInstanceSessionsProvidersUpdateOutputDeployment:
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
class ManagementInstanceSessionsProvidersUpdateOutputConfig:
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
class ManagementInstanceSessionsProvidersUpdateOutputAuthConfig:
    object: str
    id: str
@dataclass
class ManagementInstanceSessionsProvidersUpdateOutput:
    object: str
    id: str
    status: str
    usage: ManagementInstanceSessionsProvidersUpdateOutputUsage
    tool_filter: Dict[str, Any]
    provider_id: str
    session_id: str
    deployment: ManagementInstanceSessionsProvidersUpdateOutputDeployment
    config: ManagementInstanceSessionsProvidersUpdateOutputConfig
    created_at: datetime
    updated_at: datetime
    from_template_id: Optional[str] = None
    from_template_provider_id: Optional[str] = None
    auth_config: Optional[ManagementInstanceSessionsProvidersUpdateOutputAuthConfig] = None


class mapManagementInstanceSessionsProvidersUpdateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProvidersUpdateOutputUsage:
        return ManagementInstanceSessionsProvidersUpdateOutputUsage(
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_provider_message_count=data.get('total_productive_provider_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsProvidersUpdateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsProvidersUpdateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProvidersUpdateOutputDeployment:
        return ManagementInstanceSessionsProvidersUpdateOutputDeployment(
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
    def to_dict(value: Union[ManagementInstanceSessionsProvidersUpdateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsProvidersUpdateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProvidersUpdateOutputConfig:
        return ManagementInstanceSessionsProvidersUpdateOutputConfig(
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
    def to_dict(value: Union[ManagementInstanceSessionsProvidersUpdateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsProvidersUpdateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProvidersUpdateOutputAuthConfig:
        return ManagementInstanceSessionsProvidersUpdateOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsProvidersUpdateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProvidersUpdateOutput:
        return ManagementInstanceSessionsProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        usage=mapManagementInstanceSessionsProvidersUpdateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_id=data.get('session_id'),
        from_template_id=data.get('from_template_id'),
        from_template_provider_id=data.get('from_template_provider_id'),
        deployment=mapManagementInstanceSessionsProvidersUpdateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapManagementInstanceSessionsProvidersUpdateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceSessionsProvidersUpdateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsProvidersUpdateBody:
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None


class mapManagementInstanceSessionsProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsProvidersUpdateBody:
        return ManagementInstanceSessionsProvidersUpdateBody(
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

