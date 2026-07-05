from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsListOutputItemsFileCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class SkillsExportsListOutputItemsFileCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsListOutputItemsFileCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsExportsListOutputItemsFileCreatedByOrganizationActor] = None
    consumer: Optional[SkillsExportsListOutputItemsFileCreatedByConsumer] = None
@dataclass
class SkillsExportsListOutputItemsFile:
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
    created_by: Optional[SkillsExportsListOutputItemsFileCreatedBy] = None
@dataclass
class SkillsExportsListOutputItemsFileLink:
    object: str
    id: str
    file_id: str
    url: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class SkillsExportsListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsExportsListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class SkillsExportsListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsExportsListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsExportsListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[SkillsExportsListOutputItemsCreatedByConsumer] = None
@dataclass
class SkillsExportsListOutputItems:
    object: str
    id: str
    target: str
    status: str
    created_at: datetime
    file: Optional[SkillsExportsListOutputItemsFile] = None
    file_link: Optional[SkillsExportsListOutputItemsFileLink] = None
    created_by: Optional[SkillsExportsListOutputItemsCreatedBy] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class SkillsExportsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsExportsListOutput:
    items: List[SkillsExportsListOutputItems]
    pagination: SkillsExportsListOutputPagination


class mapSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams:
        return SkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsFileCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsFileCreatedByOrganizationActor:
        return SkillsExportsListOutputItemsFileCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapSkillsExportsListOutputItemsFileCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsFileCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsFileCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsFileCreatedByConsumer:
        return SkillsExportsListOutputItemsFileCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsFileCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsFileCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsFileCreatedBy:
        return SkillsExportsListOutputItemsFileCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsExportsListOutputItemsFileCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsExportsListOutputItemsFileCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsFileCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsFile:
        return SkillsExportsListOutputItemsFile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapSkillsExportsListOutputItemsFileCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsFileLink:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsFileLink:
        return SkillsExportsListOutputItemsFileLink(
        object=data.get('object'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsFileLink, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsCreatedByOrganizationActorTeams:
        return SkillsExportsListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsCreatedByOrganizationActor:
        return SkillsExportsListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapSkillsExportsListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsCreatedByConsumer:
        return SkillsExportsListOutputItemsCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItemsCreatedBy:
        return SkillsExportsListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsExportsListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsExportsListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputItems:
        return SkillsExportsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        target=data.get('target'),
        status=data.get('status'),
        file=mapSkillsExportsListOutputItemsFile.from_dict(data.get('file')) if data.get('file') else None,
        file_link=mapSkillsExportsListOutputItemsFileLink.from_dict(data.get('file_link')) if data.get('file_link') else None,
        created_by=mapSkillsExportsListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutputPagination:
        return SkillsExportsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsExportsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListOutput:
        return SkillsExportsListOutput(
        items=[mapSkillsExportsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsExportsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsExportsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsExportsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    target: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapSkillsExportsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsExportsListQuery:
        return SkillsExportsListQuery(
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
    def to_dict(value: Union[SkillsExportsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

