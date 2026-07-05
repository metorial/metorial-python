from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class StoresItemsListOutputItemsFileCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class StoresItemsListOutputItemsFileCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[StoresItemsListOutputItemsFileCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class StoresItemsListOutputItemsFileCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class StoresItemsListOutputItemsFileCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[StoresItemsListOutputItemsFileCreatedByOrganizationActor] = None
    consumer: Optional[StoresItemsListOutputItemsFileCreatedByConsumer] = None
@dataclass
class StoresItemsListOutputItemsFile:
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
    created_by: Optional[StoresItemsListOutputItemsFileCreatedBy] = None
@dataclass
class StoresItemsListOutputItemsDocumentCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class StoresItemsListOutputItemsDocumentCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[StoresItemsListOutputItemsDocumentCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class StoresItemsListOutputItemsDocumentCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class StoresItemsListOutputItemsDocumentCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[StoresItemsListOutputItemsDocumentCreatedByOrganizationActor] = None
    consumer: Optional[StoresItemsListOutputItemsDocumentCreatedByConsumer] = None
@dataclass
class StoresItemsListOutputItemsDocument:
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
    created_by: Optional[StoresItemsListOutputItemsDocumentCreatedBy] = None
@dataclass
class StoresItemsListOutputItems:
    object: str
    id: str
    kind: str
    path: str
    store_id: str
    created_at: datetime
    updated_at: datetime
    directory_id: Optional[str] = None
    file: Optional[StoresItemsListOutputItemsFile] = None
    document: Optional[StoresItemsListOutputItemsDocument] = None
@dataclass
class StoresItemsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class StoresItemsListOutput:
    items: List[StoresItemsListOutputItems]
    pagination: StoresItemsListOutputPagination


class mapStoresItemsListOutputItemsFileCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsFileCreatedByOrganizationActorTeams:
        return StoresItemsListOutputItemsFileCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsFileCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsFileCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsFileCreatedByOrganizationActor:
        return StoresItemsListOutputItemsFileCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapStoresItemsListOutputItemsFileCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsFileCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsFileCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsFileCreatedByConsumer:
        return StoresItemsListOutputItemsFileCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsFileCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsFileCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsFileCreatedBy:
        return StoresItemsListOutputItemsFileCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapStoresItemsListOutputItemsFileCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapStoresItemsListOutputItemsFileCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsFileCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsFile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsFile:
        return StoresItemsListOutputItemsFile(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapStoresItemsListOutputItemsFileCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsFile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsDocumentCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsDocumentCreatedByOrganizationActorTeams:
        return StoresItemsListOutputItemsDocumentCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsDocumentCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsDocumentCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsDocumentCreatedByOrganizationActor:
        return StoresItemsListOutputItemsDocumentCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapStoresItemsListOutputItemsDocumentCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsDocumentCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsDocumentCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsDocumentCreatedByConsumer:
        return StoresItemsListOutputItemsDocumentCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsDocumentCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsDocumentCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsDocumentCreatedBy:
        return StoresItemsListOutputItemsDocumentCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapStoresItemsListOutputItemsDocumentCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapStoresItemsListOutputItemsDocumentCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsDocumentCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItemsDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItemsDocument:
        return StoresItemsListOutputItemsDocument(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('file_id'),
        parent_document_id=data.get('parent_document_id'),
        current_version_id=data.get('current_version_id'),
        created_by=mapStoresItemsListOutputItemsDocumentCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItemsDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputItems:
        return StoresItemsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        kind=data.get('kind'),
        path=data.get('path'),
        store_id=data.get('store_id'),
        directory_id=data.get('directory_id'),
        file=mapStoresItemsListOutputItemsFile.from_dict(data.get('file')) if data.get('file') else None,
        document=mapStoresItemsListOutputItemsDocument.from_dict(data.get('document')) if data.get('document') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutputPagination:
        return StoresItemsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresItemsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListOutput:
        return StoresItemsListOutput(
        items=[mapStoresItemsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapStoresItemsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class StoresItemsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class StoresItemsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class StoresItemsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    file_id: Optional[Union[str, List[str]]] = None
    document_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    created_at: Optional[StoresItemsListQueryCreatedAt] = None
    updated_at: Optional[StoresItemsListQueryUpdatedAt] = None


class mapStoresItemsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresItemsListQuery:
        return StoresItemsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        type=data.get('type'),
        created_at=mapStoresItemsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapStoresItemsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresItemsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

