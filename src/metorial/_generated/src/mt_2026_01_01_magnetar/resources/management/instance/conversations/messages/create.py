from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConversationsMessagesCreateOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsMessagesCreateOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsMessagesCreateOutputModelProvider
@dataclass
class ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceConversationsMessagesCreateOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesCreateOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceConversationsMessagesCreateOutputRequestActorConsumer] = None
@dataclass
class ManagementInstanceConversationsMessagesCreateOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ManagementInstanceConversationsMessagesCreateOutputRequestActor] = None
@dataclass
class ManagementInstanceConversationsMessagesCreateOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    request: ManagementInstanceConversationsMessagesCreateOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ManagementInstanceConversationsMessagesCreateOutputModel] = None


class mapManagementInstanceConversationsMessagesCreateOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutputModelProvider:
        return ManagementInstanceConversationsMessagesCreateOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutputModel:
        return ManagementInstanceConversationsMessagesCreateOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsMessagesCreateOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
        return ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor:
        return ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutputRequestActorConsumer:
        return ManagementInstanceConversationsMessagesCreateOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutputRequestActor:
        return ManagementInstanceConversationsMessagesCreateOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceConversationsMessagesCreateOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutputRequest:
        return ManagementInstanceConversationsMessagesCreateOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapManagementInstanceConversationsMessagesCreateOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateOutput:
        return ManagementInstanceConversationsMessagesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapManagementInstanceConversationsMessagesCreateOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapManagementInstanceConversationsMessagesCreateOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConversationsMessagesCreateBodyMessage:
    parts: List[Dict[str, Any]]
@dataclass
class ManagementInstanceConversationsMessagesCreateBody:
    message: ManagementInstanceConversationsMessagesCreateBodyMessage
    parent_message_id: Optional[str] = None
    model_id: Optional[str] = None


class mapManagementInstanceConversationsMessagesCreateBodyMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateBodyMessage:
        return ManagementInstanceConversationsMessagesCreateBodyMessage(
        parts=data.get('parts', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateBodyMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesCreateBody:
        return ManagementInstanceConversationsMessagesCreateBody(
        message=mapManagementInstanceConversationsMessagesCreateBodyMessage.from_dict(data.get('message')) if data.get('message') else None,
        parent_message_id=data.get('parent_message_id'),
        model_id=data.get('model_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

