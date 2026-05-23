from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAssistantsListOutputItemsDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class DashboardInstanceAssistantsListOutputItemsDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: DashboardInstanceAssistantsListOutputItemsDefaultModelProvider
@dataclass
class DashboardInstanceAssistantsListOutputItemsAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class DashboardInstanceAssistantsListOutputItemsAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: DashboardInstanceAssistantsListOutputItemsAvailableModelsProvider
@dataclass
class DashboardInstanceAssistantsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[DashboardInstanceAssistantsListOutputItemsAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[DashboardInstanceAssistantsListOutputItemsDefaultModel] = None
@dataclass
class DashboardInstanceAssistantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceAssistantsListOutput:
    items: List[DashboardInstanceAssistantsListOutputItems]
    pagination: DashboardInstanceAssistantsListOutputPagination


class mapDashboardInstanceAssistantsListOutputItemsDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListOutputItemsDefaultModelProvider:
        return DashboardInstanceAssistantsListOutputItemsDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListOutputItemsDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsListOutputItemsDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListOutputItemsDefaultModel:
        return DashboardInstanceAssistantsListOutputItemsDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapDashboardInstanceAssistantsListOutputItemsDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListOutputItemsDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsListOutputItemsAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListOutputItemsAvailableModelsProvider:
        return DashboardInstanceAssistantsListOutputItemsAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListOutputItemsAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsListOutputItemsAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListOutputItemsAvailableModels:
        return DashboardInstanceAssistantsListOutputItemsAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapDashboardInstanceAssistantsListOutputItemsAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListOutputItemsAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListOutputItems:
        return DashboardInstanceAssistantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapDashboardInstanceAssistantsListOutputItemsDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapDashboardInstanceAssistantsListOutputItemsAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListOutputPagination:
        return DashboardInstanceAssistantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListOutput:
        return DashboardInstanceAssistantsListOutput(
        items=[mapDashboardInstanceAssistantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAssistantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAssistantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceAssistantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsListQuery:
        return DashboardInstanceAssistantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

