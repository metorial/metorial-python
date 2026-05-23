from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAssistantsGetOutputDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class DashboardInstanceAssistantsGetOutputDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: DashboardInstanceAssistantsGetOutputDefaultModelProvider
@dataclass
class DashboardInstanceAssistantsGetOutputAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class DashboardInstanceAssistantsGetOutputAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: DashboardInstanceAssistantsGetOutputAvailableModelsProvider
@dataclass
class DashboardInstanceAssistantsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[DashboardInstanceAssistantsGetOutputAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[DashboardInstanceAssistantsGetOutputDefaultModel] = None


class mapDashboardInstanceAssistantsGetOutputDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsGetOutputDefaultModelProvider:
        return DashboardInstanceAssistantsGetOutputDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsGetOutputDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsGetOutputDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsGetOutputDefaultModel:
        return DashboardInstanceAssistantsGetOutputDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapDashboardInstanceAssistantsGetOutputDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsGetOutputDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsGetOutputAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsGetOutputAvailableModelsProvider:
        return DashboardInstanceAssistantsGetOutputAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsGetOutputAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsGetOutputAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsGetOutputAvailableModels:
        return DashboardInstanceAssistantsGetOutputAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapDashboardInstanceAssistantsGetOutputAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsGetOutputAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAssistantsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAssistantsGetOutput:
        return DashboardInstanceAssistantsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapDashboardInstanceAssistantsGetOutputDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapDashboardInstanceAssistantsGetOutputAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAssistantsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

