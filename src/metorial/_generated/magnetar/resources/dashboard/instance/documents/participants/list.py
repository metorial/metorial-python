from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsParticipantsListOutputItemsActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsParticipantsListOutputItemsActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActor] = None
    consumer: Optional[DashboardInstanceDocumentsParticipantsListOutputItemsActorConsumer] = None
@dataclass
class DashboardInstanceDocumentsParticipantsListOutputItems:
    object: str
    id: str
    role: str
    edit_count: float
    actor: DashboardInstanceDocumentsParticipantsListOutputItemsActor
    created_at: datetime
    last_edited_at: Optional[datetime] = None
    last_viewed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsParticipantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceDocumentsParticipantsListOutput:
    items: List[DashboardInstanceDocumentsParticipantsListOutputItems]
    pagination: DashboardInstanceDocumentsParticipantsListOutputPagination


class mapDashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActorTeams:
        return DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActor:
        return DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsParticipantsListOutputItemsActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListOutputItemsActorConsumer:
        return DashboardInstanceDocumentsParticipantsListOutputItemsActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListOutputItemsActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsParticipantsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListOutputItemsActor:
        return DashboardInstanceDocumentsParticipantsListOutputItemsActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceDocumentsParticipantsListOutputItemsActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceDocumentsParticipantsListOutputItemsActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsParticipantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListOutputItems:
        return DashboardInstanceDocumentsParticipantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        role=data.get('role'),
        edit_count=data.get('edit_count'),
        last_edited_at=datetime.fromisoformat(data.get('last_edited_at').replace('Z', '+00:00')) if data.get('last_edited_at') else None,
        last_viewed_at=datetime.fromisoformat(data.get('last_viewed_at').replace('Z', '+00:00')) if data.get('last_viewed_at') else None,
        actor=mapDashboardInstanceDocumentsParticipantsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsParticipantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListOutputPagination:
        return DashboardInstanceDocumentsParticipantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsParticipantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListOutput:
        return DashboardInstanceDocumentsParticipantsListOutput(
        items=[mapDashboardInstanceDocumentsParticipantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceDocumentsParticipantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceDocumentsParticipantsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsParticipantsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsParticipantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceDocumentsParticipantsListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceDocumentsParticipantsListQueryUpdatedAt] = None


class mapDashboardInstanceDocumentsParticipantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsParticipantsListQuery:
        return DashboardInstanceDocumentsParticipantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        created_at=mapDashboardInstanceDocumentsParticipantsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceDocumentsParticipantsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsParticipantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

