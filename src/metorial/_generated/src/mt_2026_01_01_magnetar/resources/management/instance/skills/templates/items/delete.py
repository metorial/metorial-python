from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
@dataclass
class ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsTemplatesItemsDeleteOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsTemplatesItemsDeleteOutput:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegration] = None
    provider: Optional[ManagementInstanceSkillsTemplatesItemsDeleteOutputProvider] = None


class mapManagementInstanceSkillsTemplatesItemsDeleteOutputIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegrationConfiguration:
        return ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsTemplatesItemsDeleteOutputIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegration:
        return ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapManagementInstanceSkillsTemplatesItemsDeleteOutputIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsDeleteOutputIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsTemplatesItemsDeleteOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsDeleteOutputProvider:
        return ManagementInstanceSkillsTemplatesItemsDeleteOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsDeleteOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsTemplatesItemsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsDeleteOutput:
        return ManagementInstanceSkillsTemplatesItemsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapManagementInstanceSkillsTemplatesItemsDeleteOutputIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapManagementInstanceSkillsTemplatesItemsDeleteOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

