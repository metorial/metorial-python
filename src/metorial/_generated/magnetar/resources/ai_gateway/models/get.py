from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayModelsGetOutputLab:
    id: str
    slug: str
    name: str
@dataclass
class AiGatewayModelsGetOutputModalities:
    input: List[str]
    output: List[str]
@dataclass
class AiGatewayModelsGetOutputCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class AiGatewayModelsGetOutputCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class AiGatewayModelsGetOutputCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[AiGatewayModelsGetOutputCapabilitiesReasoning] = None
    prompt_caching: Optional[AiGatewayModelsGetOutputCapabilitiesPromptCaching] = None
@dataclass
class AiGatewayModelsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: AiGatewayModelsGetOutputLab
    open_weights: bool
    modalities: AiGatewayModelsGetOutputModalities
    capabilities: AiGatewayModelsGetOutputCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None


class mapAiGatewayModelsGetOutputLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsGetOutputLab:
        return AiGatewayModelsGetOutputLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsGetOutputLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsGetOutputModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsGetOutputModalities:
        return AiGatewayModelsGetOutputModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsGetOutputModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsGetOutputCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsGetOutputCapabilitiesReasoning:
        return AiGatewayModelsGetOutputCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsGetOutputCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsGetOutputCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsGetOutputCapabilitiesPromptCaching:
        return AiGatewayModelsGetOutputCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsGetOutputCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsGetOutputCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsGetOutputCapabilities:
        return AiGatewayModelsGetOutputCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapAiGatewayModelsGetOutputCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapAiGatewayModelsGetOutputCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsGetOutputCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsGetOutput:
        return AiGatewayModelsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapAiGatewayModelsGetOutputLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapAiGatewayModelsGetOutputModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapAiGatewayModelsGetOutputCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

