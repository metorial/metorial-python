from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsCreateOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsCreateOutputProviderDeployments:
    object: str
    id: str
    provider_id: str
    name: Optional[str] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class ManagementInstanceSessionsCreateOutput:
    object: str
    id: str
    connection_status: str
    usage: ManagementInstanceSessionsCreateOutputUsage
    provider_deployments: List[ManagementInstanceSessionsCreateOutputProviderDeployments]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    connection_url: Optional[str] = None
    connection_key: Optional[str] = None


class mapManagementInstanceSessionsCreateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputUsage:
        return ManagementInstanceSessionsCreateOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
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

class mapManagementInstanceSessionsCreateOutputProviderDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputProviderDeployments:
        return ManagementInstanceSessionsCreateOutputProviderDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputProviderDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
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
        connection_status=data.get('connection_status'),
        usage=mapManagementInstanceSessionsCreateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        connection_url=data.get('connection_url'),
        connection_key=data.get('connection_key'),
        provider_deployments=[mapManagementInstanceSessionsCreateOutputProviderDeployments.from_dict(item) for item in data.get('provider_deployments', []) if item],
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
class ManagementInstanceSessionsCreateBodyProvidersToolFilters:
    tool_keys: Optional[List[str]] = None
@dataclass
class ManagementInstanceSessionsCreateBodyProviders:
    provider_deployment: Union[Dict[str, Any], str]
    provider_config: Optional[Union[Dict[str, Any], str]] = None
    provider_auth_config: Optional[Union[Dict[str, Any], str]] = None
    session_template_id: Optional[str] = None
    tool_filters: Optional[ManagementInstanceSessionsCreateBodyProvidersToolFilters] = None
@dataclass
class ManagementInstanceSessionsCreateBody:
    providers: List[ManagementInstanceSessionsCreateBodyProviders]
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceSessionsCreateBodyProvidersToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateBodyProvidersToolFilters:
        return ManagementInstanceSessionsCreateBodyProvidersToolFilters(
        tool_keys=data.get('tool_keys', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateBodyProvidersToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateBodyProviders:
        return ManagementInstanceSessionsCreateBodyProviders(
        provider_deployment=data.get('provider_deployment'),
        provider_config=data.get('provider_config'),
        provider_auth_config=data.get('provider_auth_config'),
        session_template_id=data.get('session_template_id'),
        tool_filters=mapManagementInstanceSessionsCreateBodyProvidersToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateBody:
        return ManagementInstanceSessionsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapManagementInstanceSessionsCreateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
