from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsItemsCreateOutputIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
@dataclass
class SkillsItemsCreateOutputIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: SkillsItemsCreateOutputIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class SkillsItemsCreateOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class SkillsItemsCreateOutput:
    object: str
    id: str
    status: str
    type: str
    skill_id: str
    created_at: datetime
    integration: Optional[SkillsItemsCreateOutputIntegration] = None
    provider: Optional[SkillsItemsCreateOutputProvider] = None


class mapSkillsItemsCreateOutputIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsItemsCreateOutputIntegrationConfiguration:
        return SkillsItemsCreateOutputIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[SkillsItemsCreateOutputIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsItemsCreateOutputIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsItemsCreateOutputIntegration:
        return SkillsItemsCreateOutputIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapSkillsItemsCreateOutputIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsItemsCreateOutputIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsItemsCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsItemsCreateOutputProvider:
        return SkillsItemsCreateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsItemsCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsItemsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsItemsCreateOutput:
        return SkillsItemsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        skill_id=data.get('skill_id'),
        integration=mapSkillsItemsCreateOutputIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapSkillsItemsCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsItemsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

SkillsItemsCreateBody = Dict[str, Any]


class mapSkillsItemsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsItemsCreateBody:
        data

    @staticmethod
    def to_dict(value: Union[SkillsItemsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

