from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsExportsCreateOutputFileCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsCreateOutputFileCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsExportsCreateOutputFileCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class SkillsExportsCreateOutputFileCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsCreateOutputFileCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsExportsCreateOutputFileCreatedByOrganizationActor] = None
    consumer: Optional[SkillsExportsCreateOutputFileCreatedByConsumer] = None
@dataclass
class SkillsExportsCreateOutputFile:
    object: str
    id: str
    status: str
    file_name: str
    file_size: float
    file_type: str
    title: str
    purpose: str
    created_at: datetime
    updated_at: datetime
    created_by: Optional[SkillsExportsCreateOutputFileCreatedBy] = None
@dataclass
class SkillsExportsCreateOutputFileLink:
    object: str
    id: str
    file_id: str
    url: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class SkillsExportsCreateOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsCreateOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsExportsCreateOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class SkillsExportsCreateOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsCreateOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsExportsCreateOutputCreatedByOrganizationActor] = None
    consumer: Optional[SkillsExportsCreateOutputCreatedByConsumer] = None
@dataclass
class SkillsExportsCreateOutput:
    object: str
    id: str
    target: str
    status: str
    created_at: datetime
    file: Optional[SkillsExportsCreateOutputFile] = None
    file_link: Optional[SkillsExportsCreateOutputFileLink] = None
    created_by: Optional[SkillsExportsCreateOutputCreatedBy] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapSkillsExportsCreateOutputFileCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputFileCreatedByOrganizationActorTeams:
        return SkillsExportsCreateOutputFileCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputFileCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputFileCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputFileCreatedByOrganizationActor:
        return SkillsExportsCreateOutputFileCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapSkillsExportsCreateOutputFileCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputFileCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputFileCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputFileCreatedByConsumer:
        return SkillsExportsCreateOutputFileCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputFileCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputFileCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputFileCreatedBy:
        return SkillsExportsCreateOutputFileCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsExportsCreateOutputFileCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsExportsCreateOutputFileCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputFileCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputFile:
        return SkillsExportsCreateOutputFile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapSkillsExportsCreateOutputFileCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputFileLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputFileLink:
        return SkillsExportsCreateOutputFileLink(
        object=data.get('object'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputFileLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputCreatedByOrganizationActorTeams:
        return SkillsExportsCreateOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputCreatedByOrganizationActor:
        return SkillsExportsCreateOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapSkillsExportsCreateOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputCreatedByConsumer:
        return SkillsExportsCreateOutputCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutputCreatedBy:
        return SkillsExportsCreateOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsExportsCreateOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsExportsCreateOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateOutput:
        return SkillsExportsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        target=data.get('target'),
        status=data.get('status'),
        file=mapSkillsExportsCreateOutputFile.from_dict(data.get('file')) if data.get('file') else None,
        file_link=mapSkillsExportsCreateOutputFileLink.from_dict(data.get('file_link')) if data.get('file_link') else None,
        created_by=mapSkillsExportsCreateOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsExportsCreateBody:
    target: str
    skill_id: Optional[str] = None
    skill_plugin_id: Optional[str] = None
    skill_marketplace_id: Optional[str] = None


class mapSkillsExportsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsCreateBody:
        return SkillsExportsCreateBody(
        target=data.get('target'),
        skill_id=data.get('skill_id'),
        skill_plugin_id=data.get('skill_plugin_id'),
        skill_marketplace_id=data.get('skill_marketplace_id')
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

