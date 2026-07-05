from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: DashboardInstanceConversationsMessagesHandoffResponsesOutputModelProvider
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor] = None
    consumer: Optional[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer] = None
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActor] = None
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: DashboardInstanceConversationsMessagesHandoffResponsesOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[DashboardInstanceConversationsMessagesHandoffResponsesOutputModel] = None


class mapDashboardInstanceConversationsMessagesHandoffResponsesOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutputModelProvider:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutputModel:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapDashboardInstanceConversationsMessagesHandoffResponsesOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActor:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutputRequest:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesOutput:
        return DashboardInstanceConversationsMessagesHandoffResponsesOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapDashboardInstanceConversationsMessagesHandoffResponsesOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapDashboardInstanceConversationsMessagesHandoffResponsesOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesBodyResponses:
    tool_call_id: str
    output: Any
@dataclass
class DashboardInstanceConversationsMessagesHandoffResponsesBody:
    responses: List[DashboardInstanceConversationsMessagesHandoffResponsesBodyResponses]


class mapDashboardInstanceConversationsMessagesHandoffResponsesBodyResponses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesBodyResponses:
        return DashboardInstanceConversationsMessagesHandoffResponsesBodyResponses(
        tool_call_id=data.get('tool_call_id'),
        output=data.get('output')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesBodyResponses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConversationsMessagesHandoffResponsesBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConversationsMessagesHandoffResponsesBody:
        return DashboardInstanceConversationsMessagesHandoffResponsesBody(
        responses=[mapDashboardInstanceConversationsMessagesHandoffResponsesBodyResponses.from_dict(item) for item in data.get('responses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConversationsMessagesHandoffResponsesBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

