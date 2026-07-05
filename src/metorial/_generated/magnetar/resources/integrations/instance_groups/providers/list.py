from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstanceGroupsProvidersListOutputItems:
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
class IntegrationsInstanceGroupsProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IntegrationsInstanceGroupsProvidersListOutput:
    items: List[IntegrationsInstanceGroupsProvidersListOutputItems]
    pagination: IntegrationsInstanceGroupsProvidersListOutputPagination


class mapIntegrationsInstanceGroupsProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsProvidersListOutputItems:
        return IntegrationsInstanceGroupsProvidersListOutputItems(
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
    def to_dict(value: Union[IntegrationsInstanceGroupsProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsProvidersListOutputPagination:
        return IntegrationsInstanceGroupsProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstanceGroupsProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsProvidersListOutput:
        return IntegrationsInstanceGroupsProvidersListOutput(
        items=[mapIntegrationsInstanceGroupsProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIntegrationsInstanceGroupsProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstanceGroupsProvidersListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IntegrationsInstanceGroupsProvidersListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IntegrationsInstanceGroupsProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    integration_instance_group_id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_instance_id: Optional[Union[str, List[str]]] = None
    integration_instance_provider_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    integration_provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    session_template_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[IntegrationsInstanceGroupsProvidersListQueryCreatedAt] = None
    updated_at: Optional[IntegrationsInstanceGroupsProvidersListQueryUpdatedAt] = None


class mapIntegrationsInstanceGroupsProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstanceGroupsProvidersListQuery:
        return IntegrationsInstanceGroupsProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        integration_instance_group_id=data.get('integration_instance_group_id'),
        integration_id=data.get('integration_id'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        provider_id=data.get('provider_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        session_template_id=data.get('session_template_id'),
        created_at=mapIntegrationsInstanceGroupsProvidersListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapIntegrationsInstanceGroupsProvidersListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstanceGroupsProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

