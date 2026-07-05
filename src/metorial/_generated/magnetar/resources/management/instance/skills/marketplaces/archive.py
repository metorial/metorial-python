from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPluginSkills:
    object: str
    id: str
    identifier: str
    status: str
    skill_id: str
    created_at: datetime
    updated_at: datetime
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPlugin:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    skills: List[ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPluginSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMarketplacesArchiveOutputPlugins:
    object: str
    id: str
    status: str
    identifier: str
    created_at: datetime
    updated_at: datetime
    skill_configuration_id: Optional[str] = None
    skill_marketplace_id: Optional[str] = None
    skill_plugin_id: Optional[str] = None
    skill_plugin: Optional[ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPlugin] = None
@dataclass
class ManagementInstanceSkillsMarketplacesArchiveOutput:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    plugins: List[ManagementInstanceSkillsMarketplacesArchiveOutputPlugins]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    skill_configuration_id: Optional[str] = None


class mapManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPluginSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPluginSkills:
        return ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPluginSkills(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        status=data.get('status'),
        client_name=data.get('client_name'),
        client_description=data.get('client_description'),
        client_metadata=data.get('client_metadata'),
        license=data.get('license'),
        compatibility=data.get('compatibility'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skill_id=data.get('skill_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPluginSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPlugin:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPlugin:
        return ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPlugin(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sync_status=data.get('sync_status'),
        image_url=data.get('image_url'),
        name=data.get('name'),
        description=data.get('description'),
        long_description=data.get('long_description'),
        category=data.get('category'),
        slug=data.get('slug'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skills=[mapManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPluginSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPlugin, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMarketplacesArchiveOutputPlugins:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesArchiveOutputPlugins:
        return ManagementInstanceSkillsMarketplacesArchiveOutputPlugins(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        identifier=data.get('identifier'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skill_marketplace_id=data.get('skill_marketplace_id'),
        skill_plugin_id=data.get('skill_plugin_id'),
        skill_plugin=mapManagementInstanceSkillsMarketplacesArchiveOutputPluginsSkillPlugin.from_dict(data.get('skill_plugin')) if data.get('skill_plugin') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesArchiveOutputPlugins, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMarketplacesArchiveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesArchiveOutput:
        return ManagementInstanceSkillsMarketplacesArchiveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sync_status=data.get('sync_status'),
        image_url=data.get('image_url'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        skill_configuration_id=data.get('skill_configuration_id'),
        plugins=[mapManagementInstanceSkillsMarketplacesArchiveOutputPlugins.from_dict(item) for item in data.get('plugins', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesArchiveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

