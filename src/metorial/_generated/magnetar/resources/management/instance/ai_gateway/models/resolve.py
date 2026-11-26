from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayModelsResolveOutputModelLab:
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceAiGatewayModelsResolveOutputModelModalities:
    input: List[str]
    output: List[str]
@dataclass
class ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class ManagementInstanceAiGatewayModelsResolveOutputModelCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning] = None
    prompt_caching: Optional[ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching] = None
@dataclass
class ManagementInstanceAiGatewayModelsResolveOutputModel:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: ManagementInstanceAiGatewayModelsResolveOutputModelLab
    open_weights: bool
    modalities: ManagementInstanceAiGatewayModelsResolveOutputModelModalities
    capabilities: ManagementInstanceAiGatewayModelsResolveOutputModelCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelsResolveOutput:
    object: str
    requested: str
    request: Dict[str, Any]
    via: str
    model: ManagementInstanceAiGatewayModelsResolveOutputModel


class mapManagementInstanceAiGatewayModelsResolveOutputModelLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveOutputModelLab:
        return ManagementInstanceAiGatewayModelsResolveOutputModelLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveOutputModelLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsResolveOutputModelModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveOutputModelModalities:
        return ManagementInstanceAiGatewayModelsResolveOutputModelModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveOutputModelModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning:
        return ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
        return ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsResolveOutputModelCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveOutputModelCapabilities:
        return ManagementInstanceAiGatewayModelsResolveOutputModelCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapManagementInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveOutputModelCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsResolveOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveOutputModel:
        return ManagementInstanceAiGatewayModelsResolveOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapManagementInstanceAiGatewayModelsResolveOutputModelLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapManagementInstanceAiGatewayModelsResolveOutputModelModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapManagementInstanceAiGatewayModelsResolveOutputModelCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveOutput:
        return ManagementInstanceAiGatewayModelsResolveOutput(
        object=data.get('object'),
        requested=data.get('requested'),
        request=data.get('request'),
        via=data.get('via'),
        model=mapManagementInstanceAiGatewayModelsResolveOutputModel.from_dict(data.get('model')) if data.get('model') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayModelsResolveBody:
    model: str


class mapManagementInstanceAiGatewayModelsResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsResolveBody:
        return ManagementInstanceAiGatewayModelsResolveBody(
        model=data.get('model')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

