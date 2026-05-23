from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsVersionsListOutputItemsEditorsOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsVersionsListOutputItemsEditorsOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DocumentsVersionsListOutputItemsEditorsConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsVersionsListOutputItemsEditors:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsVersionsListOutputItemsEditorsOrganizationActor] = None
    consumer: Optional[DocumentsVersionsListOutputItemsEditorsConsumer] = None
@dataclass
class DocumentsVersionsListOutputItems:
    object: str
    id: str
    document_id: str
    version_number: float
    content: str
    editors: List[DocumentsVersionsListOutputItemsEditors]
    created_at: datetime
    previous_version_id: Optional[str] = None
    list_edited_at: Optional[datetime] = None
@dataclass
class DocumentsVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DocumentsVersionsListOutput:
    items: List[DocumentsVersionsListOutputItems]
    pagination: DocumentsVersionsListOutputPagination


class mapDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
        return DocumentsVersionsListOutputItemsEditorsOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListOutputItemsEditorsOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsVersionsListOutputItemsEditorsOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListOutputItemsEditorsOrganizationActor:
        return DocumentsVersionsListOutputItemsEditorsOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListOutputItemsEditorsOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsVersionsListOutputItemsEditorsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListOutputItemsEditorsConsumer:
        return DocumentsVersionsListOutputItemsEditorsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListOutputItemsEditorsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsVersionsListOutputItemsEditors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListOutputItemsEditors:
        return DocumentsVersionsListOutputItemsEditors(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsVersionsListOutputItemsEditorsOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsVersionsListOutputItemsEditorsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListOutputItemsEditors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListOutputItems:
        return DocumentsVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        version_number=data.get('version_number'),
        previous_version_id=data.get('previous_version_id'),
        list_edited_at=datetime.fromisoformat(data.get('list_edited_at').replace('Z', '+00:00')) if data.get('list_edited_at') else None,
        content=data.get('content'),
        editors=[mapDocumentsVersionsListOutputItemsEditors.from_dict(item) for item in data.get('editors', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListOutputPagination:
        return DocumentsVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListOutput:
        return DocumentsVersionsListOutput(
        items=[mapDocumentsVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDocumentsVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DocumentsVersionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DocumentsVersionsListQueryLastEditedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DocumentsVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DocumentsVersionsListQueryCreatedAt] = None
    last_edited_at: Optional[DocumentsVersionsListQueryLastEditedAt] = None


class mapDocumentsVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsVersionsListQuery:
        return DocumentsVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        created_at=mapDocumentsVersionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        last_edited_at=mapDocumentsVersionsListQueryLastEditedAt.from_dict(data.get('last_edited_at')) if data.get('last_edited_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

