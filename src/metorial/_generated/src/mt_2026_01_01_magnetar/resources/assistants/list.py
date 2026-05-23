from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AssistantsListOutputItemsDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class AssistantsListOutputItemsDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: AssistantsListOutputItemsDefaultModelProvider
@dataclass
class AssistantsListOutputItemsAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class AssistantsListOutputItemsAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: AssistantsListOutputItemsAvailableModelsProvider
@dataclass
class AssistantsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[AssistantsListOutputItemsAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[AssistantsListOutputItemsDefaultModel] = None
@dataclass
class AssistantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class AssistantsListOutput:
    items: List[AssistantsListOutputItems]
    pagination: AssistantsListOutputPagination


class mapAssistantsListOutputItemsDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListOutputItemsDefaultModelProvider:
        return AssistantsListOutputItemsDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListOutputItemsDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsListOutputItemsDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListOutputItemsDefaultModel:
        return AssistantsListOutputItemsDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapAssistantsListOutputItemsDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListOutputItemsDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsListOutputItemsAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListOutputItemsAvailableModelsProvider:
        return AssistantsListOutputItemsAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListOutputItemsAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsListOutputItemsAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListOutputItemsAvailableModels:
        return AssistantsListOutputItemsAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapAssistantsListOutputItemsAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListOutputItemsAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListOutputItems:
        return AssistantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapAssistantsListOutputItemsDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapAssistantsListOutputItemsAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListOutputPagination:
        return AssistantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListOutput:
        return AssistantsListOutput(
        items=[mapAssistantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAssistantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AssistantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapAssistantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsListQuery:
        return AssistantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[AssistantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

