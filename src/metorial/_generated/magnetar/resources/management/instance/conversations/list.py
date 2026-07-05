from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceConversationsListOutputItemsCreatedByActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConversationsListOutputItemsCreatedByActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceConversationsListOutputItemsCreatedByActorConsumer] = None
@dataclass
class ManagementInstanceConversationsListOutputItemsAssistantDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsListOutputItemsAssistantDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsListOutputItemsAssistantDefaultModelProvider
@dataclass
class ManagementInstanceConversationsListOutputItemsAssistantAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceConversationsListOutputItemsAssistantAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceConversationsListOutputItemsAssistantAvailableModelsProvider
@dataclass
class ManagementInstanceConversationsListOutputItemsAssistant:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[ManagementInstanceConversationsListOutputItemsAssistantAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[ManagementInstanceConversationsListOutputItemsAssistantDefaultModel] = None
@dataclass
class ManagementInstanceConversationsListOutputItems:
    object: str
    id: str
    assistant_id: str
    instance_id: str
    organization_id: str
    created_by_actor: ManagementInstanceConversationsListOutputItemsCreatedByActor
    root_message_id: str
    assistant: ManagementInstanceConversationsListOutputItemsAssistant
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
@dataclass
class ManagementInstanceConversationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceConversationsListOutput:
    items: List[ManagementInstanceConversationsListOutputItems]
    pagination: ManagementInstanceConversationsListOutputPagination


class mapManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActorTeams:
        return ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActor:
        return ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsCreatedByActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsCreatedByActorConsumer:
        return ManagementInstanceConversationsListOutputItemsCreatedByActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsCreatedByActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsCreatedByActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsCreatedByActor:
        return ManagementInstanceConversationsListOutputItemsCreatedByActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceConversationsListOutputItemsCreatedByActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceConversationsListOutputItemsCreatedByActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsCreatedByActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsAssistantDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsAssistantDefaultModelProvider:
        return ManagementInstanceConversationsListOutputItemsAssistantDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsAssistantDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsAssistantDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsAssistantDefaultModel:
        return ManagementInstanceConversationsListOutputItemsAssistantDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsListOutputItemsAssistantDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsAssistantDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsAssistantAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsAssistantAvailableModelsProvider:
        return ManagementInstanceConversationsListOutputItemsAssistantAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsAssistantAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsAssistantAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsAssistantAvailableModels:
        return ManagementInstanceConversationsListOutputItemsAssistantAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceConversationsListOutputItemsAssistantAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsAssistantAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItemsAssistant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItemsAssistant:
        return ManagementInstanceConversationsListOutputItemsAssistant(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapManagementInstanceConversationsListOutputItemsAssistantDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapManagementInstanceConversationsListOutputItemsAssistantAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItemsAssistant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputItems:
        return ManagementInstanceConversationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        title=data.get('title'),
        assistant_id=data.get('assistant_id'),
        instance_id=data.get('instance_id'),
        organization_id=data.get('organization_id'),
        created_by_actor=mapManagementInstanceConversationsListOutputItemsCreatedByActor.from_dict(data.get('created_by_actor')) if data.get('created_by_actor') else None,
        root_message_id=data.get('root_message_id'),
        assistant=mapManagementInstanceConversationsListOutputItemsAssistant.from_dict(data.get('assistant')) if data.get('assistant') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutputPagination:
        return ManagementInstanceConversationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConversationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListOutput:
        return ManagementInstanceConversationsListOutput(
        items=[mapManagementInstanceConversationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceConversationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConversationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    assistant_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceConversationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConversationsListQuery:
        return ManagementInstanceConversationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        assistant_id=data.get('assistant_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConversationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

