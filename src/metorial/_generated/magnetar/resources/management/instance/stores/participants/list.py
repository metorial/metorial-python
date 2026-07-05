from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceStoresParticipantsListOutputItemsActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceStoresParticipantsListOutputItemsActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceStoresParticipantsListOutputItemsActorConsumer] = None
@dataclass
class ManagementInstanceStoresParticipantsListOutputItems:
    object: str
    id: str
    store_id: str
    permissions: List[str]
    actor: ManagementInstanceStoresParticipantsListOutputItemsActor
    created_at: datetime
@dataclass
class ManagementInstanceStoresParticipantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceStoresParticipantsListOutput:
    items: List[ManagementInstanceStoresParticipantsListOutputItems]
    pagination: ManagementInstanceStoresParticipantsListOutputPagination


class mapManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActorTeams:
        return ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActor:
        return ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresParticipantsListOutputItemsActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListOutputItemsActorConsumer:
        return ManagementInstanceStoresParticipantsListOutputItemsActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListOutputItemsActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresParticipantsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListOutputItemsActor:
        return ManagementInstanceStoresParticipantsListOutputItemsActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceStoresParticipantsListOutputItemsActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceStoresParticipantsListOutputItemsActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresParticipantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListOutputItems:
        return ManagementInstanceStoresParticipantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        store_id=data.get('store_id'),
        permissions=data.get('permissions', []),
        actor=mapManagementInstanceStoresParticipantsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresParticipantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListOutputPagination:
        return ManagementInstanceStoresParticipantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceStoresParticipantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListOutput:
        return ManagementInstanceStoresParticipantsListOutput(
        items=[mapManagementInstanceStoresParticipantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceStoresParticipantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceStoresParticipantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceStoresParticipantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceStoresParticipantsListQuery:
        return ManagementInstanceStoresParticipantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceStoresParticipantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

