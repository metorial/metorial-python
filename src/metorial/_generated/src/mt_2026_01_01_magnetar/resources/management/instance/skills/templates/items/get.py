from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsTemplatesItemsGetOutputIntegrationConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceSkillsTemplatesItemsGetOutputIntegration:
    object: str
    id: str
    slug: str
    name: str
    configuration: ManagementInstanceSkillsTemplatesItemsGetOutputIntegrationConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsTemplatesItemsGetOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsTemplatesItemsGetOutput:
    object: str
    id: str
    type: str
    created_at: datetime
    updated_at: datetime
    integration: Optional[ManagementInstanceSkillsTemplatesItemsGetOutputIntegration] = None
    provider: Optional[ManagementInstanceSkillsTemplatesItemsGetOutputProvider] = None


class mapManagementInstanceSkillsTemplatesItemsGetOutputIntegrationConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsGetOutputIntegrationConfiguration:
        return ManagementInstanceSkillsTemplatesItemsGetOutputIntegrationConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsGetOutputIntegrationConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsTemplatesItemsGetOutputIntegration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsGetOutputIntegration:
        return ManagementInstanceSkillsTemplatesItemsGetOutputIntegration(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapManagementInstanceSkillsTemplatesItemsGetOutputIntegrationConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsGetOutputIntegration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsTemplatesItemsGetOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsGetOutputProvider:
        return ManagementInstanceSkillsTemplatesItemsGetOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsGetOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsTemplatesItemsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsTemplatesItemsGetOutput:
        return ManagementInstanceSkillsTemplatesItemsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        integration=mapManagementInstanceSkillsTemplatesItemsGetOutputIntegration.from_dict(data.get('integration')) if data.get('integration') else None,
        provider=mapManagementInstanceSkillsTemplatesItemsGetOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsTemplatesItemsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

