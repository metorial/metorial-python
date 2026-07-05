from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsTemplatesCreateOutputItemsIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class SkillsTemplatesCreateOutputItemsIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: SkillsTemplatesCreateOutputItemsIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class SkillsTemplatesCreateOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class SkillsTemplatesCreateOutputItems:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[SkillsTemplatesCreateOutputItemsIntegration] = None
    provider: Optional[SkillsTemplatesCreateOutputItemsProvider] = None
@dataclass
class SkillsTemplatesCreateOutput:
    object: str
    id: str
    status: str
    owner: str
    slug: str
    name: str
    metadata: Dict[str, Any]
    store_id: str
    items: List[SkillsTemplatesCreateOutputItems]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapSkillsTemplatesCreateOutputItemsIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesCreateOutputItemsIntegrationConfiguration:
        return SkillsTemplatesCreateOutputItemsIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesCreateOutputItemsIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesCreateOutputItemsIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesCreateOutputItemsIntegration:
        return SkillsTemplatesCreateOutputItemsIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapSkillsTemplatesCreateOutputItemsIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesCreateOutputItemsIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesCreateOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesCreateOutputItemsProvider:
        return SkillsTemplatesCreateOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesCreateOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesCreateOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesCreateOutputItems:
        return SkillsTemplatesCreateOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapSkillsTemplatesCreateOutputItemsIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapSkillsTemplatesCreateOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesCreateOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsTemplatesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesCreateOutput:
        return SkillsTemplatesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        owner=data.get('owner'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        store_id=data.get('store_id'),
        items=[mapSkillsTemplatesCreateOutputItems.from_dict(item) for item in data.get('items', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsTemplatesCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    from_skill_id: Optional[str] = None


class mapSkillsTemplatesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsTemplatesCreateBody:
        return SkillsTemplatesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        from_skill_id=data.get('from_skill_Id')
        )

    @staticmethod
    def to_dict(value: Union[SkillsTemplatesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

