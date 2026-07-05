from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConversationsMessagesListOutputItemsModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsMessagesListOutputItemsModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsMessagesListOutputItemsModelProvider
@dataclass
class ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceConversationsMessagesListOutputItemsRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesListOutputItemsRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceConversationsMessagesListOutputItemsRequestActorConsumer] = None
@dataclass
class ManagementInstanceConversationsMessagesListOutputItemsRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ManagementInstanceConversationsMessagesListOutputItemsRequestActor] = None
@dataclass
class ManagementInstanceConversationsMessagesListOutputItems:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: ManagementInstanceConversationsMessagesListOutputItemsRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ManagementInstanceConversationsMessagesListOutputItemsModel] = None
@dataclass
class ManagementInstanceConversationsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceConversationsMessagesListOutput:
    items: List[ManagementInstanceConversationsMessagesListOutputItems]
    pagination: ManagementInstanceConversationsMessagesListOutputPagination


class mapManagementInstanceConversationsMessagesListOutputItemsModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItemsModelProvider:
        return ManagementInstanceConversationsMessagesListOutputItemsModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItemsModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItemsModel:
        return ManagementInstanceConversationsMessagesListOutputItemsModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsMessagesListOutputItemsModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams:
        return ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActor:
        return ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputItemsRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItemsRequestActorConsumer:
        return ManagementInstanceConversationsMessagesListOutputItemsRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItemsRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputItemsRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItemsRequestActor:
        return ManagementInstanceConversationsMessagesListOutputItemsRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceConversationsMessagesListOutputItemsRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceConversationsMessagesListOutputItemsRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItemsRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItemsRequest:
        return ManagementInstanceConversationsMessagesListOutputItemsRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapManagementInstanceConversationsMessagesListOutputItemsRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputItems:
        return ManagementInstanceConversationsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapManagementInstanceConversationsMessagesListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapManagementInstanceConversationsMessagesListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutputPagination:
        return ManagementInstanceConversationsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListOutput:
        return ManagementInstanceConversationsMessagesListOutput(
        items=[mapManagementInstanceConversationsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceConversationsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConversationsMessagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceConversationsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesListQuery:
        return ManagementInstanceConversationsMessagesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

