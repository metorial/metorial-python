from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConversationsMessagesGetOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsMessagesGetOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsMessagesGetOutputModelProvider
@dataclass
class ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceConversationsMessagesGetOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesGetOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceConversationsMessagesGetOutputRequestActorConsumer] = None
@dataclass
class ManagementInstanceConversationsMessagesGetOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ManagementInstanceConversationsMessagesGetOutputRequestActor] = None
@dataclass
class ManagementInstanceConversationsMessagesGetOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: ManagementInstanceConversationsMessagesGetOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ManagementInstanceConversationsMessagesGetOutputModel] = None


class mapManagementInstanceConversationsMessagesGetOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutputModelProvider:
        return ManagementInstanceConversationsMessagesGetOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesGetOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutputModel:
        return ManagementInstanceConversationsMessagesGetOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsMessagesGetOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams:
        return ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActor:
        return ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesGetOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutputRequestActorConsumer:
        return ManagementInstanceConversationsMessagesGetOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesGetOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutputRequestActor:
        return ManagementInstanceConversationsMessagesGetOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceConversationsMessagesGetOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceConversationsMessagesGetOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutputRequest:
        return ManagementInstanceConversationsMessagesGetOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapManagementInstanceConversationsMessagesGetOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesGetOutput:
        return ManagementInstanceConversationsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapManagementInstanceConversationsMessagesGetOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapManagementInstanceConversationsMessagesGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

