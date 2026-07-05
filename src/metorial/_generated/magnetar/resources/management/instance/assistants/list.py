from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAssistantsListOutputItemsDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceAssistantsListOutputItemsDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceAssistantsListOutputItemsDefaultModelProvider
@dataclass
class ManagementInstanceAssistantsListOutputItemsAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceAssistantsListOutputItemsAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceAssistantsListOutputItemsAvailableModelsProvider
@dataclass
class ManagementInstanceAssistantsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[ManagementInstanceAssistantsListOutputItemsAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[ManagementInstanceAssistantsListOutputItemsDefaultModel] = None
@dataclass
class ManagementInstanceAssistantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceAssistantsListOutput:
    items: List[ManagementInstanceAssistantsListOutputItems]
    pagination: ManagementInstanceAssistantsListOutputPagination


class mapManagementInstanceAssistantsListOutputItemsDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListOutputItemsDefaultModelProvider:
        return ManagementInstanceAssistantsListOutputItemsDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListOutputItemsDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsListOutputItemsDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListOutputItemsDefaultModel:
        return ManagementInstanceAssistantsListOutputItemsDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceAssistantsListOutputItemsDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListOutputItemsDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsListOutputItemsAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListOutputItemsAvailableModelsProvider:
        return ManagementInstanceAssistantsListOutputItemsAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListOutputItemsAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsListOutputItemsAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListOutputItemsAvailableModels:
        return ManagementInstanceAssistantsListOutputItemsAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceAssistantsListOutputItemsAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListOutputItemsAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListOutputItems:
        return ManagementInstanceAssistantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapManagementInstanceAssistantsListOutputItemsDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapManagementInstanceAssistantsListOutputItemsAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListOutputPagination:
        return ManagementInstanceAssistantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListOutput:
        return ManagementInstanceAssistantsListOutput(
        items=[mapManagementInstanceAssistantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAssistantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAssistantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceAssistantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsListQuery:
        return ManagementInstanceAssistantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

