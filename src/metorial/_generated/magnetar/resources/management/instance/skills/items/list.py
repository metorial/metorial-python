from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsItemsListOutputItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceSkillsItemsListOutputItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: ManagementInstanceSkillsItemsListOutputItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsItemsListOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsItemsListOutputItems:
    object: str
    id: str
    status: str
    type: str
    skill_id: str
    created_at: datetime
    integration: Optional[ManagementInstanceSkillsItemsListOutputItemsIntegration] = None
    provider: Optional[ManagementInstanceSkillsItemsListOutputItemsProvider] = None
@dataclass
class ManagementInstanceSkillsItemsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsItemsListOutput:
    items: List[ManagementInstanceSkillsItemsListOutputItems]
    pagination: ManagementInstanceSkillsItemsListOutputPagination


class mapManagementInstanceSkillsItemsListOutputItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsItemsListOutputItemsIntegrationConfiguration:
        return ManagementInstanceSkillsItemsListOutputItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsItemsListOutputItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsItemsListOutputItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsItemsListOutputItemsIntegration:
        return ManagementInstanceSkillsItemsListOutputItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapManagementInstanceSkillsItemsListOutputItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsItemsListOutputItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsItemsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsItemsListOutputItemsProvider:
        return ManagementInstanceSkillsItemsListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsItemsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsItemsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsItemsListOutputItems:
        return ManagementInstanceSkillsItemsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        skill_id=data.get('skill_id'),
        integration=mapManagementInstanceSkillsItemsListOutputItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapManagementInstanceSkillsItemsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsItemsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsItemsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsItemsListOutputPagination:
        return ManagementInstanceSkillsItemsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsItemsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsItemsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsItemsListOutput:
        return ManagementInstanceSkillsItemsListOutput(
        items=[mapManagementInstanceSkillsItemsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsItemsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsItemsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsItemsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsItemsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceSkillsItemsListQueryCreatedAt] = None


class mapManagementInstanceSkillsItemsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsItemsListQuery:
        return ManagementInstanceSkillsItemsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        type=data.get('type'),
        id=data.get('id'),
        integration_id=data.get('integration_id'),
        provider_id=data.get('provider_id'),
        created_at=mapManagementInstanceSkillsItemsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsItemsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

