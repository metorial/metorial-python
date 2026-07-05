from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAssistantsGetOutputDefaultModelProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceAssistantsGetOutputDefaultModel:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceAssistantsGetOutputDefaultModelProvider
@dataclass
class ManagementInstanceAssistantsGetOutputAvailableModelsProvider:
    object: str
    id: str
    slug: str
    name: str
    image_url: str
@dataclass
class ManagementInstanceAssistantsGetOutputAvailableModels:
    object: str
    id: str
    slug: str
    name: str
    context_window: float
    provider: ManagementInstanceAssistantsGetOutputAvailableModelsProvider
@dataclass
class ManagementInstanceAssistantsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    owner_type: str
    available_models: List[ManagementInstanceAssistantsGetOutputAvailableModels]
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str] = None
    default_model: Optional[ManagementInstanceAssistantsGetOutputDefaultModel] = None


class mapManagementInstanceAssistantsGetOutputDefaultModelProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsGetOutputDefaultModelProvider:
        return ManagementInstanceAssistantsGetOutputDefaultModelProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsGetOutputDefaultModelProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsGetOutputDefaultModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsGetOutputDefaultModel:
        return ManagementInstanceAssistantsGetOutputDefaultModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceAssistantsGetOutputDefaultModelProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsGetOutputDefaultModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsGetOutputAvailableModelsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsGetOutputAvailableModelsProvider:
        return ManagementInstanceAssistantsGetOutputAvailableModelsProvider(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsGetOutputAvailableModelsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsGetOutputAvailableModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsGetOutputAvailableModels:
        return ManagementInstanceAssistantsGetOutputAvailableModels(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        context_window=data.get('context_window'),
        provider=mapManagementInstanceAssistantsGetOutputAvailableModelsProvider.from_dict(data.get('provider')) if data.get('provider') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsGetOutputAvailableModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAssistantsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAssistantsGetOutput:
        return ManagementInstanceAssistantsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        owner_type=data.get('owner_type'),
        organization_id=data.get('organization_id'),
        default_model=mapManagementInstanceAssistantsGetOutputDefaultModel.from_dict(data.get('default_model')) if data.get('default_model') else None,
        available_models=[mapManagementInstanceAssistantsGetOutputAvailableModels.from_dict(item) for item in data.get('available_models', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAssistantsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

