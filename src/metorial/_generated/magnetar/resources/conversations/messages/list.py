from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConversationsMessagesListOutputItemsModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsMessagesListOutputItemsModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsMessagesListOutputItemsModelProvider
@dataclass
class ConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsMessagesListOutputItemsRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ConversationsMessagesListOutputItemsRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsMessagesListOutputItemsRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ConversationsMessagesListOutputItemsRequestActorOrganizationActor] = None
    consumer: Optional[ConversationsMessagesListOutputItemsRequestActorConsumer] = None
@dataclass
class ConversationsMessagesListOutputItemsRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ConversationsMessagesListOutputItemsRequestActor] = None
@dataclass
class ConversationsMessagesListOutputItems:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: ConversationsMessagesListOutputItemsRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ConversationsMessagesListOutputItemsModel] = None
@dataclass
class ConversationsMessagesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConversationsMessagesListOutput:
    items: List[ConversationsMessagesListOutputItems]
    pagination: ConversationsMessagesListOutputPagination


class mapConversationsMessagesListOutputItemsModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItemsModelProvider:
        return ConversationsMessagesListOutputItemsModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItemsModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItemsModel:
        return ConversationsMessagesListOutputItemsModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsMessagesListOutputItemsModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams:
        return ConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputItemsRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItemsRequestActorOrganizationActor:
        return ConversationsMessagesListOutputItemsRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapConversationsMessagesListOutputItemsRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItemsRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputItemsRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItemsRequestActorConsumer:
        return ConversationsMessagesListOutputItemsRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItemsRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputItemsRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItemsRequestActor:
        return ConversationsMessagesListOutputItemsRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapConversationsMessagesListOutputItemsRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapConversationsMessagesListOutputItemsRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItemsRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItemsRequest:
        return ConversationsMessagesListOutputItemsRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapConversationsMessagesListOutputItemsRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputItems:
        return ConversationsMessagesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapConversationsMessagesListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapConversationsMessagesListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutputPagination:
        return ConversationsMessagesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsMessagesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListOutput:
        return ConversationsMessagesListOutput(
        items=[mapConversationsMessagesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConversationsMessagesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConversationsMessagesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapConversationsMessagesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsMessagesListQuery:
        return ConversationsMessagesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsMessagesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

