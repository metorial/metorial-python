from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConversationsMessagesGetOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class DashboardInstanceConversationsMessagesGetOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: DashboardInstanceConversationsMessagesGetOutputModelProvider
@dataclass
class DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceConversationsMessagesGetOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceConversationsMessagesGetOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActor] = None
    consumer: Optional[DashboardInstanceConversationsMessagesGetOutputRequestActorConsumer] = None
@dataclass
class DashboardInstanceConversationsMessagesGetOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[DashboardInstanceConversationsMessagesGetOutputRequestActor] = None
@dataclass
class DashboardInstanceConversationsMessagesGetOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: DashboardInstanceConversationsMessagesGetOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[DashboardInstanceConversationsMessagesGetOutputModel] = None


class mapDashboardInstanceConversationsMessagesGetOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutputModelProvider:
        return DashboardInstanceConversationsMessagesGetOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesGetOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutputModel:
        return DashboardInstanceConversationsMessagesGetOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapDashboardInstanceConversationsMessagesGetOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams:
        return DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActor:
        return DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesGetOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutputRequestActorConsumer:
        return DashboardInstanceConversationsMessagesGetOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesGetOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutputRequestActor:
        return DashboardInstanceConversationsMessagesGetOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceConversationsMessagesGetOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceConversationsMessagesGetOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutputRequest:
        return DashboardInstanceConversationsMessagesGetOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapDashboardInstanceConversationsMessagesGetOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesGetOutput:
        return DashboardInstanceConversationsMessagesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapDashboardInstanceConversationsMessagesGetOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapDashboardInstanceConversationsMessagesGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

