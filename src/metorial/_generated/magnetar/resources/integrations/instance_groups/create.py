from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstanceGroupsCreateOutputImplementation:
    type: str
    magic_mcp_endpoint_id: str
@dataclass
class IntegrationsInstanceGroupsCreateOutputProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_group_id: str
    integration_instance_id: str
    integration_instance_provider_id: str
    is_override_tool_filter: bool
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    integration_provider_id: Optional[str] = None
    tool_filter: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsInstanceGroupsCreateOutput:
    object: str
    id: str
    status: str
    name: str
    providers: List[IntegrationsInstanceGroupsCreateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    implementation: Optional[IntegrationsInstanceGroupsCreateOutputImplementation] = None
    archived_at: Optional[datetime] = None


class mapIntegrationsInstanceGroupsCreateOutputImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateOutputImplementation:
        return IntegrationsInstanceGroupsCreateOutputImplementation(
        type=data.get('type'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateOutputImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateOutputProviders:
        return IntegrationsInstanceGroupsCreateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        integration_instance_group_id=data.get('integration_instance_group_id'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_provider_id=data.get('integration_provider_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        tool_filter=data.get('tool_filter'),
        is_override_tool_filter=data.get('is_override_tool_filter'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateOutput:
        return IntegrationsInstanceGroupsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        implementation=mapIntegrationsInstanceGroupsCreateOutputImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapIntegrationsInstanceGroupsCreateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstanceGroupsCreateBodyProviders:
    integration_instance_provider_id: str
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
@dataclass
class IntegrationsInstanceGroupsCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    providers: Optional[List[IntegrationsInstanceGroupsCreateBodyProviders]] = None


class mapIntegrationsInstanceGroupsCreateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateBodyProviders:
        return IntegrationsInstanceGroupsCreateBodyProviders(
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        tool_filters=data.get('tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsCreateBody:
        return IntegrationsInstanceGroupsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapIntegrationsInstanceGroupsCreateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

