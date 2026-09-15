from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsMarketplacesUpdateOutputPluginsSkillPluginSkillsSkill:
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
class SkillsMarketplacesUpdateOutputPluginsSkillPluginSkills:
    object: str
    id: str
    identifier: str
    status: str
    skill_id: str
    skill: SkillsMarketplacesUpdateOutputPluginsSkillPluginSkillsSkill
    created_at: datetime
    updated_at: datetime
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class SkillsMarketplacesUpdateOutputPluginsSkillPlugin:
    object: str
    id: str
    status: str
    sync_status: str
    image_url: str
    name: str
    slug: str
    skills: List[SkillsMarketplacesUpdateOutputPluginsSkillPluginSkills]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    long_description: Optional[str] = None
    category: Optional[str] = None
    skill_configuration_id: Optional[str] = None
@dataclass
class SkillsMarketplacesUpdateOutputPlugins:
    object: str
    id: str
    status: str
    identifier: str
    created_at: datetime
    updated_at: datetime
    skill_configuration_id: Optional[str] = None
    skill_marketplace_id: Optional[str] = None
    skill_plugin: Optional[SkillsMarketplacesUpdateOutputPluginsSkillPlugin] = None
@dataclass
class SkillsMarketplacesUpdateOutput:
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
    plugins: List[SkillsMarketplacesUpdateOutputPlugins]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    skill_configuration_id: Optional[str] = None


class mapSkillsMarketplacesUpdateOutputPluginsSkillPluginSkillsSkill:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesUpdateOutputPluginsSkillPluginSkillsSkill:
        return SkillsMarketplacesUpdateOutputPluginsSkillPluginSkillsSkill(
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
    def to_dict(value: Union[SkillsMarketplacesUpdateOutputPluginsSkillPluginSkillsSkill, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesUpdateOutputPluginsSkillPluginSkills:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesUpdateOutputPluginsSkillPluginSkills:
        return SkillsMarketplacesUpdateOutputPluginsSkillPluginSkills(
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
        skill=mapSkillsMarketplacesUpdateOutputPluginsSkillPluginSkillsSkill.from_dict(data.get('skill')) if data.get('skill') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesUpdateOutputPluginsSkillPluginSkills, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesUpdateOutputPluginsSkillPlugin:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesUpdateOutputPluginsSkillPlugin:
        return SkillsMarketplacesUpdateOutputPluginsSkillPlugin(
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
        skills=[mapSkillsMarketplacesUpdateOutputPluginsSkillPluginSkills.from_dict(item) for item in data.get('skills', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesUpdateOutputPluginsSkillPlugin, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesUpdateOutputPlugins:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesUpdateOutputPlugins:
        return SkillsMarketplacesUpdateOutputPlugins(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        identifier=data.get('identifier'),
        skill_configuration_id=data.get('skill_configuration_id'),
        skill_marketplace_id=data.get('skill_marketplace_id'),
        skill_plugin=mapSkillsMarketplacesUpdateOutputPluginsSkillPlugin.from_dict(data.get('skill_plugin')) if data.get('skill_plugin') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesUpdateOutputPlugins, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMarketplacesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesUpdateOutput:
        return SkillsMarketplacesUpdateOutput(
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
        plugins=[mapSkillsMarketplacesUpdateOutputPlugins.from_dict(item) for item in data.get('plugins', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsMarketplacesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    image_file_id: Optional[str] = None
    skill_configuration_id: Optional[str] = None
    repository_access_mode: Optional[str] = None
    force_merge_or_push: Optional[bool] = None
    merge_before_checks_pass: Optional[bool] = None


class mapSkillsMarketplacesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMarketplacesUpdateBody:
        return SkillsMarketplacesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        image_file_id=data.get('image_file_id'),
        skill_configuration_id=data.get('skill_configuration_id'),
        repository_access_mode=data.get('repository_access_mode'),
        force_merge_or_push=data.get('force_merge_or_push'),
        merge_before_checks_pass=data.get('merge_before_checks_pass')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMarketplacesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

