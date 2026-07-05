from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsVersionsListOutputItemsEditorsConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsVersionsListOutputItemsEditors:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor] = None
    consumer: Optional[DashboardInstanceDocumentsVersionsListOutputItemsEditorsConsumer] = None
@dataclass
class DashboardInstanceDocumentsVersionsListOutputItems:
    object: str
    id: str
    document_id: str
    version_number: float
    content: str
    editors: List[DashboardInstanceDocumentsVersionsListOutputItemsEditors]
    created_at: datetime
    previous_version_id: Optional[str] = None
    list_edited_at: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceDocumentsVersionsListOutput:
    items: List[DashboardInstanceDocumentsVersionsListOutputItems]
    pagination: DashboardInstanceDocumentsVersionsListOutputPagination


class mapDashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams:
        return DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor:
        return DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsListOutputItemsEditorsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListOutputItemsEditorsConsumer:
        return DashboardInstanceDocumentsVersionsListOutputItemsEditorsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListOutputItemsEditorsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsListOutputItemsEditors:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListOutputItemsEditors:
        return DashboardInstanceDocumentsVersionsListOutputItemsEditors(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceDocumentsVersionsListOutputItemsEditorsOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceDocumentsVersionsListOutputItemsEditorsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListOutputItemsEditors, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListOutputItems:
        return DashboardInstanceDocumentsVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        version_number=data.get('version_number'),
        previous_version_id=data.get('previous_version_id'),
        list_edited_at=datetime.fromisoformat(data.get('list_edited_at').replace('Z', '+00:00')) if data.get('list_edited_at') else None,
        content=data.get('content'),
        editors=[mapDashboardInstanceDocumentsVersionsListOutputItemsEditors.from_dict(item) for item in data.get('editors', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListOutputPagination:
        return DashboardInstanceDocumentsVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListOutput:
        return DashboardInstanceDocumentsVersionsListOutput(
        items=[mapDashboardInstanceDocumentsVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceDocumentsVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceDocumentsVersionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsVersionsListQueryLastEditedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceDocumentsVersionsListQueryCreatedAt] = None
    last_edited_at: Optional[DashboardInstanceDocumentsVersionsListQueryLastEditedAt] = None


class mapDashboardInstanceDocumentsVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsVersionsListQuery:
        return DashboardInstanceDocumentsVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        created_at=mapDashboardInstanceDocumentsVersionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        last_edited_at=mapDashboardInstanceDocumentsVersionsListQueryLastEditedAt.from_dict(data.get('last_edited_at')) if data.get('last_edited_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

