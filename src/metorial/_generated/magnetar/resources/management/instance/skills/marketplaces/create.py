from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkillsSkill:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    client_name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkills:
    object: str
    id: str
    identifier: str
    status: str
    skill_id: str
    skill: ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkillsSkill
    created_at: datetime
    updated_at: datetime
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPlugin:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    skills: List[ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMarketplacesCreateOutputPlugins:
    object: str
    id: str
    status: str
    identifier: str
    created_at: datetime
    updated_at: datetime
    skill_configuration_id: Optional[str] = None
    skill_marketplace_id: Optional[str] = None
    skill_plugin: Optional[ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPlugin] = None
@dataclass
class ManagementInstanceSkillsMarketplacesCreateOutput:
    object: str
    id: str
    status: str
    repository_access_mode: str
    force_merge_or_push: bool
    merge_before_checks_pass: bool
    sync_status: str
    image_url: str
    name: str
    slug: str
    plugins: List[ManagementInstanceSkillsMarketplacesCreateOutputPlugins]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    skill_configuration_id: Optional[str] = None


class mapManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkillsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkillsSkill:
        return ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkillsSkill(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        client_name=data.get('client_name'),
        client_description=data.get('client_description'),
        client_metadata=data.get('client_metadata'),
        license=data.get('license'),
        compatibility=data.get('compatibility'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkillsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkills:
        return ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkills(
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
        skill=mapManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkillsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPlugin:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPlugin:
        return ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPlugin(
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
        skills=[mapManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPluginSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPlugin, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMarketplacesCreateOutputPlugins:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesCreateOutputPlugins:
        return ManagementInstanceSkillsMarketplacesCreateOutputPlugins(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        identifier=data.get('identifier'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skill_marketplace_id=data.get('skill_marketplace_id'),
        skill_plugin=mapManagementInstanceSkillsMarketplacesCreateOutputPluginsSkillPlugin.from_dict(data.get('skill_plugin')) if data.get('skill_plugin') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesCreateOutputPlugins, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMarketplacesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesCreateOutput:
        return ManagementInstanceSkillsMarketplacesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        repository_access_mode=data.get('repository_access_mode'),
        force_merge_or_push=data.get('force_merge_or_push'),
        merge_before_checks_pass=data.get('merge_before_checks_pass'),
        sync_status=data.get('sync_status'),
        image_url=data.get('image_url'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        skill_configuration_id=data.get('skill_configuration_id'),
        plugins=[mapManagementInstanceSkillsMarketplacesCreateOutputPlugins.from_dict(item) for item in data.get('plugins', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsMarketplacesCreateBody:
    name: str
    description: Optional[str] = None
    image_file_id: Optional[str] = None
    skill_configuration_id: Optional[str] = None
    repository_access_mode: Optional[str] = None
    force_merge_or_push: Optional[bool] = None
    merge_before_checks_pass: Optional[bool] = None


class mapManagementInstanceSkillsMarketplacesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMarketplacesCreateBody:
        return ManagementInstanceSkillsMarketplacesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        image_file_id=data.get('image_file_id'),
        skill_configuration_id=data.get('skill_configuration_id'),
        repository_access_mode=data.get('repository_access_mode'),
        force_merge_or_push=data.get('force_merge_or_push'),
        merge_before_checks_pass=data.get('merge_before_checks_pass')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMarketplacesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

