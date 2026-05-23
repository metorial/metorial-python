from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AssistantsGetOutputDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class AssistantsGetOutputDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: AssistantsGetOutputDefaultModelProvider
@dataclass
class AssistantsGetOutputAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class AssistantsGetOutputAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: AssistantsGetOutputAvailableModelsProvider
@dataclass
class AssistantsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[AssistantsGetOutputAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[AssistantsGetOutputDefaultModel] = None


class mapAssistantsGetOutputDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsGetOutputDefaultModelProvider:
        return AssistantsGetOutputDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[AssistantsGetOutputDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsGetOutputDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsGetOutputDefaultModel:
        return AssistantsGetOutputDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapAssistantsGetOutputDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[AssistantsGetOutputDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsGetOutputAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsGetOutputAvailableModelsProvider:
        return AssistantsGetOutputAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[AssistantsGetOutputAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsGetOutputAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsGetOutputAvailableModels:
        return AssistantsGetOutputAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapAssistantsGetOutputAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[AssistantsGetOutputAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAssistantsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AssistantsGetOutput:
        return AssistantsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapAssistantsGetOutputDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapAssistantsGetOutputAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AssistantsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

