from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutputModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutputModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsMessagesHandoffResponsesOutputModelProvider
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer] = None
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutputRequest:
    object: str
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    actor: Optional[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActor] = None
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesOutput:
    object: str
    id: str
    conversation_item_id: str
    type: str
    status: str
    request: ManagementInstanceConversationsMessagesHandoffResponsesOutputRequest
    items: List[Dict[str, Any]]
    created_at: datetime
    assistant_id: Optional[str] = None
    parent_message_id: Optional[str] = None
    model: Optional[ManagementInstanceConversationsMessagesHandoffResponsesOutputModel] = None


class mapManagementInstanceConversationsMessagesHandoffResponsesOutputModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutputModelProvider:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutputModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutputModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutputModel:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsMessagesHandoffResponsesOutputModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActor:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutputRequest:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutputRequest(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        actor=mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequestActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesOutput:
        return ManagementInstanceConversationsMessagesHandoffResponsesOutput(
        object=data.get('object'),
        id=data.get('id'),
        conversation_item_id=data.get('conversation_item_id'),
        type=data.get('type'),
        status=data.get('status'),
        assistant_id=data.get('assistant_id'),
        parent_message_id=data.get('parent_message_id'),
        model=mapManagementInstanceConversationsMessagesHandoffResponsesOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        request=mapManagementInstanceConversationsMessagesHandoffResponsesOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        items=data.get('items', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesBodyResponses:
    tool_call_id: str
    output: Any
@dataclass
class ManagementInstanceConversationsMessagesHandoffResponsesBody:
    responses: List[ManagementInstanceConversationsMessagesHandoffResponsesBodyResponses]


class mapManagementInstanceConversationsMessagesHandoffResponsesBodyResponses:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesBodyResponses:
        return ManagementInstanceConversationsMessagesHandoffResponsesBodyResponses(
        tool_call_id=data.get('tool_call_id'),
        output=data.get('output')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesBodyResponses, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsMessagesHandoffResponsesBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsMessagesHandoffResponsesBody:
        return ManagementInstanceConversationsMessagesHandoffResponsesBody(
        responses=[mapManagementInstanceConversationsMessagesHandoffResponsesBodyResponses.from_dict(item) for item in data.get('responses', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsMessagesHandoffResponsesBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

