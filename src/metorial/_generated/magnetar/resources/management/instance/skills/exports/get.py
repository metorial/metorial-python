from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceSkillsExportsGetOutputFileCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsGetOutputFileCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsExportsGetOutputFileCreatedByConsumer] = None
@dataclass
class ManagementInstanceSkillsExportsGetOutputFile:
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
    created_by: Optional[ManagementInstanceSkillsExportsGetOutputFileCreatedBy] = None
@dataclass
class ManagementInstanceSkillsExportsGetOutputFileLink:
    object: str
    id: str
    file_id: str
    url: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceSkillsExportsGetOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsGetOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsExportsGetOutputCreatedByConsumer] = None
@dataclass
class ManagementInstanceSkillsExportsGetOutput:
    object: str
    id: str
    target: str
    status: str
    created_at: datetime
    file: Optional[ManagementInstanceSkillsExportsGetOutputFile] = None
    file_link: Optional[ManagementInstanceSkillsExportsGetOutputFileLink] = None
    created_by: Optional[ManagementInstanceSkillsExportsGetOutputCreatedBy] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActorTeams:
        return ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActor:
        return ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputFileCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputFileCreatedByConsumer:
        return ManagementInstanceSkillsExportsGetOutputFileCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputFileCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputFileCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputFileCreatedBy:
        return ManagementInstanceSkillsExportsGetOutputFileCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsExportsGetOutputFileCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsExportsGetOutputFileCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputFileCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputFile:
        return ManagementInstanceSkillsExportsGetOutputFile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapManagementInstanceSkillsExportsGetOutputFileCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputFileLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputFileLink:
        return ManagementInstanceSkillsExportsGetOutputFileLink(
        object=data.get('object'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputFileLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActorTeams:
        return ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActor:
        return ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputCreatedByConsumer:
        return ManagementInstanceSkillsExportsGetOutputCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutputCreatedBy:
        return ManagementInstanceSkillsExportsGetOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsExportsGetOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsExportsGetOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsGetOutput:
        return ManagementInstanceSkillsExportsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        target=data.get('target'),
        status=data.get('status'),
        file=mapManagementInstanceSkillsExportsGetOutputFile.from_dict(data.get('file')) if data.get('file') else None,
        file_link=mapManagementInstanceSkillsExportsGetOutputFileLink.from_dict(data.get('file_link')) if data.get('file_link') else None,
        created_by=mapManagementInstanceSkillsExportsGetOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

