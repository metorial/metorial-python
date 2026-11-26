from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayModelsResolveOutputModelLab:
    id: str
    slug: str
    name: str
@dataclass
class AiGatewayModelsResolveOutputModelModalities:
    input: List[str]
    output: List[str]
@dataclass
class AiGatewayModelsResolveOutputModelCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class AiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class AiGatewayModelsResolveOutputModelCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[AiGatewayModelsResolveOutputModelCapabilitiesReasoning] = None
    prompt_caching: Optional[AiGatewayModelsResolveOutputModelCapabilitiesPromptCaching] = None
@dataclass
class AiGatewayModelsResolveOutputModel:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: AiGatewayModelsResolveOutputModelLab
    open_weights: bool
    modalities: AiGatewayModelsResolveOutputModelModalities
    capabilities: AiGatewayModelsResolveOutputModelCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class AiGatewayModelsResolveOutput:
    object: str
    requested: str
    request: Dict[str, Any]
    via: str
    model: AiGatewayModelsResolveOutputModel


class mapAiGatewayModelsResolveOutputModelLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveOutputModelLab:
        return AiGatewayModelsResolveOutputModelLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveOutputModelLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsResolveOutputModelModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveOutputModelModalities:
        return AiGatewayModelsResolveOutputModelModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveOutputModelModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsResolveOutputModelCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveOutputModelCapabilitiesReasoning:
        return AiGatewayModelsResolveOutputModelCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveOutputModelCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
        return AiGatewayModelsResolveOutputModelCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveOutputModelCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsResolveOutputModelCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveOutputModelCapabilities:
        return AiGatewayModelsResolveOutputModelCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapAiGatewayModelsResolveOutputModelCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveOutputModelCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsResolveOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveOutputModel:
        return AiGatewayModelsResolveOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapAiGatewayModelsResolveOutputModelLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapAiGatewayModelsResolveOutputModelModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapAiGatewayModelsResolveOutputModelCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveOutput:
        return AiGatewayModelsResolveOutput(
        object=data.get('object'),
        requested=data.get('requested'),
        request=data.get('request'),
        via=data.get('via'),
        model=mapAiGatewayModelsResolveOutputModel.from_dict(data.get('model')) if data.get('model') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayModelsResolveBody:
    model: str


class mapAiGatewayModelsResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsResolveBody:
        return AiGatewayModelsResolveBody(
        model=data.get('model')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

