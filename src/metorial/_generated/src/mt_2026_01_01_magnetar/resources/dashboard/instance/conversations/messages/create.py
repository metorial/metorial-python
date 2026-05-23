from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConversationsMessagesCreateOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class DashboardInstanceConversationsMessagesCreateOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: DashboardInstanceConversationsMessagesCreateOutputModelProvider
@dataclass
class DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceConversationsMessagesCreateOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceConversationsMessagesCreateOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor] = None
    consumer: Optional[DashboardInstanceConversationsMessagesCreateOutputRequestActorConsumer] = None
@dataclass
class DashboardInstanceConversationsMessagesCreateOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[DashboardInstanceConversationsMessagesCreateOutputRequestActor] = None
@dataclass
class DashboardInstanceConversationsMessagesCreateOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    request: DashboardInstanceConversationsMessagesCreateOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[DashboardInstanceConversationsMessagesCreateOutputModel] = None


class mapDashboardInstanceConversationsMessagesCreateOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutputModelProvider:
        return DashboardInstanceConversationsMessagesCreateOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutputModel:
        return DashboardInstanceConversationsMessagesCreateOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapDashboardInstanceConversationsMessagesCreateOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams:
        return DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor:
        return DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutputRequestActorConsumer:
        return DashboardInstanceConversationsMessagesCreateOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutputRequestActor:
        return DashboardInstanceConversationsMessagesCreateOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceConversationsMessagesCreateOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceConversationsMessagesCreateOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutputRequest:
        return DashboardInstanceConversationsMessagesCreateOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapDashboardInstanceConversationsMessagesCreateOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateOutput:
        return DashboardInstanceConversationsMessagesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapDashboardInstanceConversationsMessagesCreateOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapDashboardInstanceConversationsMessagesCreateOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceConversationsMessagesCreateBodyMessage:
    parts: List[Dict[str, Any]]
@dataclass
class DashboardInstanceConversationsMessagesCreateBody:
    message: DashboardInstanceConversationsMessagesCreateBodyMessage
    parent_message_id: Optional[str] = None
    model_id: Optional[str] = None


class mapDashboardInstanceConversationsMessagesCreateBodyMessage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateBodyMessage:
        return DashboardInstanceConversationsMessagesCreateBodyMessage(
        parts=data.get('parts', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateBodyMessage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesCreateBody:
        return DashboardInstanceConversationsMessagesCreateBody(
        message=mapDashboardInstanceConversationsMessagesCreateBodyMessage.from_dict(data.get('message')) if data.get('message') else None,
        parent_message_id=data.get('parent_message_id'),
        model_id=data.get('model_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

