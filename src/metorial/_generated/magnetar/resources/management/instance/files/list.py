from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFilesListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceFilesListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceFilesListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceFilesListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceFilesListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceFilesListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceFilesListOutputItemsCreatedByConsumer] = None
@dataclass
class ManagementInstanceFilesListOutputItems:
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
    created_by: Optional[ManagementInstanceFilesListOutputItemsCreatedBy] = None
@dataclass
class ManagementInstanceFilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceFilesListOutput:
    items: List[ManagementInstanceFilesListOutputItems]
    pagination: ManagementInstanceFilesListOutputPagination


class mapManagementInstanceFilesListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputItemsCreatedByOrganizationActorTeams:
        return ManagementInstanceFilesListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputItemsCreatedByOrganizationActor:
        return ManagementInstanceFilesListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceFilesListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputItemsCreatedByConsumer:
        return ManagementInstanceFilesListOutputItemsCreatedByConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputItemsCreatedBy:
        return ManagementInstanceFilesListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceFilesListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceFilesListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputItems:
        return ManagementInstanceFilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        file_name=data.get('file_name'),
        file_size=data.get('file_size'),
        file_type=data.get('file_type'),
        title=data.get('title'),
        purpose=data.get('purpose'),
        created_by=mapManagementInstanceFilesListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutputPagination:
        return ManagementInstanceFilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListOutput:
        return ManagementInstanceFilesListOutput(
        items=[mapManagementInstanceFilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceFilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFilesListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceFilesListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceFilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    purpose: Optional[Union[str, List[str]]] = None
    store_id: Optional[Union[str, List[str]]] = None
    document_id: Optional[Union[str, List[str]]] = None
    file_link_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceFilesListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceFilesListQueryUpdatedAt] = None


class mapManagementInstanceFilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFilesListQuery:
        return ManagementInstanceFilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        purpose=data.get('purpose'),
        store_id=data.get('store_id'),
        document_id=data.get('document_id'),
        file_link_id=data.get('file_link_id'),
        created_at=mapManagementInstanceFilesListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceFilesListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

