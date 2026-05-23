from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConversationsGetOutputCreatedByActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsGetOutputCreatedByActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ConversationsGetOutputCreatedByActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ConversationsGetOutputCreatedByActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ConversationsGetOutputCreatedByActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ConversationsGetOutputCreatedByActorOrganizationActor] = None
    consumer: Optional[ConversationsGetOutputCreatedByActorConsumer] = None
@dataclass
class ConversationsGetOutputAssistantDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsGetOutputAssistantDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsGetOutputAssistantDefaultModelProvider
@dataclass
class ConversationsGetOutputAssistantAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ConversationsGetOutputAssistantAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ConversationsGetOutputAssistantAvailableModelsProvider
@dataclass
class ConversationsGetOutputAssistant:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[ConversationsGetOutputAssistantAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[ConversationsGetOutputAssistantDefaultModel] = None
@dataclass
class ConversationsGetOutput:
    object: str
    id: str
    assistant_id: str
    instance_id: str
    organization_id: str
    created_by_actor: ConversationsGetOutputCreatedByActor
    root_message_id: str
    assistant: ConversationsGetOutputAssistant
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None


class mapConversationsGetOutputCreatedByActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputCreatedByActorOrganizationActorTeams:
        return ConversationsGetOutputCreatedByActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputCreatedByActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputCreatedByActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputCreatedByActorOrganizationActor:
        return ConversationsGetOutputCreatedByActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapConversationsGetOutputCreatedByActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputCreatedByActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputCreatedByActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputCreatedByActorConsumer:
        return ConversationsGetOutputCreatedByActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputCreatedByActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputCreatedByActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputCreatedByActor:
        return ConversationsGetOutputCreatedByActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapConversationsGetOutputCreatedByActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapConversationsGetOutputCreatedByActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputCreatedByActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputAssistantDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputAssistantDefaultModelProvider:
        return ConversationsGetOutputAssistantDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputAssistantDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputAssistantDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputAssistantDefaultModel:
        return ConversationsGetOutputAssistantDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsGetOutputAssistantDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputAssistantDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputAssistantAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputAssistantAvailableModelsProvider:
        return ConversationsGetOutputAssistantAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputAssistantAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputAssistantAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputAssistantAvailableModels:
        return ConversationsGetOutputAssistantAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapConversationsGetOutputAssistantAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputAssistantAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutputAssistant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutputAssistant:
        return ConversationsGetOutputAssistant(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapConversationsGetOutputAssistantDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapConversationsGetOutputAssistantAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutputAssistant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConversationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConversationsGetOutput:
        return ConversationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        title=data.get('title'),
        assistant_id=data.get('assistant_id'),
        instance_id=data.get('instance_id'),
        organization_id=data.get('organization_id'),
        created_by_actor=mapConversationsGetOutputCreatedByActor.from_dict(data.get('created_by_actor')) if data.get('created_by_actor') else None,
        root_message_id=data.get('root_message_id'),
        assistant=mapConversationsGetOutputAssistant.from_dict(data.get('assistant')) if data.get('assistant') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConversationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

