from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceDocumentsListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceDocumentsListOutputItemsCreatedByConsumer] = None
@dataclass
class ManagementInstanceDocumentsListOutputItems:
    object: str
    id: str
    status: str
    title: str
    content: str
    file_id: str
    created_at: datetime
    updated_at: datetime
    parent_document_id: Optional[str] = None
    current_version_id: Optional[str] = None
    created_by: Optional[ManagementInstanceDocumentsListOutputItemsCreatedBy] = None
@dataclass
class ManagementInstanceDocumentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceDocumentsListOutput:
    items: List[ManagementInstanceDocumentsListOutputItems]
    pagination: ManagementInstanceDocumentsListOutputPagination


class mapManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActorTeams:
        return ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActor:
        return ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListOutputItemsCreatedByConsumer:
        return ManagementInstanceDocumentsListOutputItemsCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListOutputItemsCreatedBy:
        return ManagementInstanceDocumentsListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceDocumentsListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceDocumentsListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListOutputItems:
        return ManagementInstanceDocumentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('file_id'),
        parent_document_id=data.get('parent_document_id'),
        current_version_id=data.get('current_version_id'),
        created_by=mapManagementInstanceDocumentsListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListOutputPagination:
        return ManagementInstanceDocumentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListOutput:
        return ManagementInstanceDocumentsListOutput(
        items=[mapManagementInstanceDocumentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceDocumentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceDocumentsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    file_id: Optional[Union[str, List[str]]] = None
    store_id: Optional[Union[str, List[str]]] = None
    parent_document_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceDocumentsListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceDocumentsListQueryUpdatedAt] = None


class mapManagementInstanceDocumentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsListQuery:
        return ManagementInstanceDocumentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        store_id=data.get('store_id'),
        parent_document_id=data.get('parent_document_id'),
        created_at=mapManagementInstanceDocumentsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceDocumentsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

