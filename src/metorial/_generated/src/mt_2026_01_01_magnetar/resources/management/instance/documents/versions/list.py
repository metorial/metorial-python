from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceDocumentsVersionsListOutputItemsEditorsConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsVersionsListOutputItemsEditors:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor] = None
    consumer: Optional[ManagementInstanceDocumentsVersionsListOutputItemsEditorsConsumer] = None
@dataclass
class ManagementInstanceDocumentsVersionsListOutputItems:
    object: str
    id: str
    document_id: str
    version_number: float
    content: str
    editors: List[ManagementInstanceDocumentsVersionsListOutputItemsEditors]
    created_at: datetime
    previous_version_id: Optional[str] = None
    list_edited_at: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceDocumentsVersionsListOutput:
    items: List[ManagementInstanceDocumentsVersionsListOutputItems]
    pagination: ManagementInstanceDocumentsVersionsListOutputPagination


class mapManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
        return ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor:
        return ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsListOutputItemsEditorsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListOutputItemsEditorsConsumer:
        return ManagementInstanceDocumentsVersionsListOutputItemsEditorsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListOutputItemsEditorsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsListOutputItemsEditors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListOutputItemsEditors:
        return ManagementInstanceDocumentsVersionsListOutputItemsEditors(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceDocumentsVersionsListOutputItemsEditorsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListOutputItemsEditors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListOutputItems:
        return ManagementInstanceDocumentsVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        version_number=data.get('version_number'),
        previous_version_id=data.get('previous_version_id'),
        list_edited_at=datetime.fromisoformat(data.get('list_edited_at').replace('Z', '+00:00')) if data.get('list_edited_at') else None,
        content=data.get('content'),
        editors=[mapManagementInstanceDocumentsVersionsListOutputItemsEditors.from_dict(item) for item in data.get('editors', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListOutputPagination:
        return ManagementInstanceDocumentsVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListOutput:
        return ManagementInstanceDocumentsVersionsListOutput(
        items=[mapManagementInstanceDocumentsVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceDocumentsVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceDocumentsVersionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsVersionsListQueryLastEditedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceDocumentsVersionsListQueryCreatedAt] = None
    last_edited_at: Optional[ManagementInstanceDocumentsVersionsListQueryLastEditedAt] = None


class mapManagementInstanceDocumentsVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsVersionsListQuery:
        return ManagementInstanceDocumentsVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        created_at=mapManagementInstanceDocumentsVersionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        last_edited_at=mapManagementInstanceDocumentsVersionsListQueryLastEditedAt.from_dict(data.get('last_edited_at')) if data.get('last_edited_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

