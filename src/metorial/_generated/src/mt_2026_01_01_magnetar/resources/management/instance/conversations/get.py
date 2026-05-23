from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceConversationsGetOutputCreatedByActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsGetOutputCreatedByActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceConversationsGetOutputCreatedByActorConsumer] = None
@dataclass
class ManagementInstanceConversationsGetOutputAssistantDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsGetOutputAssistantDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsGetOutputAssistantDefaultModelProvider
@dataclass
class ManagementInstanceConversationsGetOutputAssistantAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsGetOutputAssistantAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsGetOutputAssistantAvailableModelsProvider
@dataclass
class ManagementInstanceConversationsGetOutputAssistant:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[ManagementInstanceConversationsGetOutputAssistantAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[ManagementInstanceConversationsGetOutputAssistantDefaultModel] = None
@dataclass
class ManagementInstanceConversationsGetOutput:
    object: str
    id: str
    assistant_id: str
    instance_id: str
    organization_id: str
    created_by_actor: ManagementInstanceConversationsGetOutputCreatedByActor
    root_message_id: str
    assistant: ManagementInstanceConversationsGetOutputAssistant
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None


class mapManagementInstanceConversationsGetOutputCreatedByActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActorTeams:
        return ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputCreatedByActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActor:
        return ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceConversationsGetOutputCreatedByActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputCreatedByActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputCreatedByActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputCreatedByActorConsumer:
        return ManagementInstanceConversationsGetOutputCreatedByActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputCreatedByActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputCreatedByActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputCreatedByActor:
        return ManagementInstanceConversationsGetOutputCreatedByActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceConversationsGetOutputCreatedByActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceConversationsGetOutputCreatedByActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputCreatedByActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputAssistantDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputAssistantDefaultModelProvider:
        return ManagementInstanceConversationsGetOutputAssistantDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputAssistantDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputAssistantDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputAssistantDefaultModel:
        return ManagementInstanceConversationsGetOutputAssistantDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsGetOutputAssistantDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputAssistantDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputAssistantAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputAssistantAvailableModelsProvider:
        return ManagementInstanceConversationsGetOutputAssistantAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputAssistantAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputAssistantAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputAssistantAvailableModels:
        return ManagementInstanceConversationsGetOutputAssistantAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsGetOutputAssistantAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputAssistantAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutputAssistant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutputAssistant:
        return ManagementInstanceConversationsGetOutputAssistant(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapManagementInstanceConversationsGetOutputAssistantDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapManagementInstanceConversationsGetOutputAssistantAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutputAssistant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsGetOutput:
        return ManagementInstanceConversationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        title=data.get('title'),
        assistant_id=data.get('assistant_id'),
        instance_id=data.get('instance_id'),
        organization_id=data.get('organization_id'),
        created_by_actor=mapManagementInstanceConversationsGetOutputCreatedByActor.from_dict(data.get('created_by_actor')) if data.get('created_by_actor') else None,
        root_message_id=data.get('root_message_id'),
        assistant=mapManagementInstanceConversationsGetOutputAssistant.from_dict(data.get('assistant')) if data.get('assistant') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

