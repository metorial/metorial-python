from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsFileCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsFileCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsExportsListOutputItemsFileCreatedByConsumer] = None
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsFile:
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
    created_by: Optional[ManagementInstanceSkillsExportsListOutputItemsFileCreatedBy] = None
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsFileLink:
    object: str
    id: str
    file_id: str
    url: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsExportsListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsExportsListOutputItemsCreatedByConsumer] = None
@dataclass
class ManagementInstanceSkillsExportsListOutputItems:
    object: str
    id: str
    target: str
    status: str
    created_at: datetime
    file: Optional[ManagementInstanceSkillsExportsListOutputItemsFile] = None
    file_link: Optional[ManagementInstanceSkillsExportsListOutputItemsFileLink] = None
    created_by: Optional[ManagementInstanceSkillsExportsListOutputItemsCreatedBy] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsExportsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsExportsListOutput:
    items: List[ManagementInstanceSkillsExportsListOutputItems]
    pagination: ManagementInstanceSkillsExportsListOutputPagination


class mapManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams:
        return ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActor:
        return ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsFileCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsFileCreatedByConsumer:
        return ManagementInstanceSkillsExportsListOutputItemsFileCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsFileCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsFileCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsFileCreatedBy:
        return ManagementInstanceSkillsExportsListOutputItemsFileCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsExportsListOutputItemsFileCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsExportsListOutputItemsFileCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsFileCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsFile:
        return ManagementInstanceSkillsExportsListOutputItemsFile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapManagementInstanceSkillsExportsListOutputItemsFileCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsFileLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsFileLink:
        return ManagementInstanceSkillsExportsListOutputItemsFileLink(
        object=data.get('object'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsFileLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActorTeams:
        return ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActor:
        return ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsCreatedByConsumer:
        return ManagementInstanceSkillsExportsListOutputItemsCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItemsCreatedBy:
        return ManagementInstanceSkillsExportsListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsExportsListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsExportsListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputItems:
        return ManagementInstanceSkillsExportsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target=data.get('target'),
        status=data.get('status'),
        file=mapManagementInstanceSkillsExportsListOutputItemsFile.from_dict(data.get('file')) if data.get('file') else None,
        file_link=mapManagementInstanceSkillsExportsListOutputItemsFileLink.from_dict(data.get('file_link')) if data.get('file_link') else None,
        created_by=mapManagementInstanceSkillsExportsListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutputPagination:
        return ManagementInstanceSkillsExportsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsExportsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListOutput:
        return ManagementInstanceSkillsExportsListOutput(
        items=[mapManagementInstanceSkillsExportsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsExportsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsExportsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    target: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSkillsExportsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsExportsListQuery:
        return ManagementInstanceSkillsExportsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        target=data.get('target'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsExportsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

