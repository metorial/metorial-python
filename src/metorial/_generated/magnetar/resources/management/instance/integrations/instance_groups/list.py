from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationsInstanceGroupsListOutputItemsImplementation:
    type: str
    magic_mcp_endpoint_id: str
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsListOutputItemsProviders:
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
class ManagementInstanceIntegrationsInstanceGroupsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    providers: List[ManagementInstanceIntegrationsInstanceGroupsListOutputItemsProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    implementation: Optional[ManagementInstanceIntegrationsInstanceGroupsListOutputItemsImplementation] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsListOutput:
    items: List[ManagementInstanceIntegrationsInstanceGroupsListOutputItems]
    pagination: ManagementInstanceIntegrationsInstanceGroupsListOutputPagination


class mapManagementInstanceIntegrationsInstanceGroupsListOutputItemsImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsListOutputItemsImplementation:
        return ManagementInstanceIntegrationsInstanceGroupsListOutputItemsImplementation(
        type=data.get('type'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsListOutputItemsImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsListOutputItemsProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsListOutputItemsProviders:
        return ManagementInstanceIntegrationsInstanceGroupsListOutputItemsProviders(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsListOutputItemsProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsListOutputItems:
        return ManagementInstanceIntegrationsInstanceGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        implementation=mapManagementInstanceIntegrationsInstanceGroupsListOutputItemsImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapManagementInstanceIntegrationsInstanceGroupsListOutputItemsProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsListOutputPagination:
        return ManagementInstanceIntegrationsInstanceGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstanceGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsListOutput:
        return ManagementInstanceIntegrationsInstanceGroupsListOutput(
        items=[mapManagementInstanceIntegrationsInstanceGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceIntegrationsInstanceGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationsInstanceGroupsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsInstanceGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_instance_id: Optional[Union[str, List[str]]] = None
    integration_instance_provider_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    integration_provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    session_template_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceIntegrationsInstanceGroupsListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceIntegrationsInstanceGroupsListQueryUpdatedAt] = None


class mapManagementInstanceIntegrationsInstanceGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstanceGroupsListQuery:
        return ManagementInstanceIntegrationsInstanceGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        integration_id=data.get('integration_id'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        provider_id=data.get('provider_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        session_template_id=data.get('session_template_id'),
        created_at=mapManagementInstanceIntegrationsInstanceGroupsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceIntegrationsInstanceGroupsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstanceGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

