from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayModelsResolveOutputModelLab:
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceAiGatewayModelsResolveOutputModelModalities:
    input: List[str]
    output: List[str]
@dataclass
class DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class DashboardInstanceAiGatewayModelsResolveOutputModelCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning] = None
    prompt_caching: Optional[DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching] = None
@dataclass
class DashboardInstanceAiGatewayModelsResolveOutputModel:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: DashboardInstanceAiGatewayModelsResolveOutputModelLab
    open_weights: bool
    modalities: DashboardInstanceAiGatewayModelsResolveOutputModelModalities
    capabilities: DashboardInstanceAiGatewayModelsResolveOutputModelCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelsResolveOutput:
    object: str
    requested: str
    request: Dict[str, Any]
    via: str
    model: DashboardInstanceAiGatewayModelsResolveOutputModel


class mapDashboardInstanceAiGatewayModelsResolveOutputModelLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveOutputModelLab:
        return DashboardInstanceAiGatewayModelsResolveOutputModelLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveOutputModelLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsResolveOutputModelModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveOutputModelModalities:
        return DashboardInstanceAiGatewayModelsResolveOutputModelModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveOutputModelModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning:
        return DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching:
        return DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsResolveOutputModelCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveOutputModelCapabilities:
        return DashboardInstanceAiGatewayModelsResolveOutputModelCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapDashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapDashboardInstanceAiGatewayModelsResolveOutputModelCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveOutputModelCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsResolveOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveOutputModel:
        return DashboardInstanceAiGatewayModelsResolveOutputModel(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapDashboardInstanceAiGatewayModelsResolveOutputModelLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapDashboardInstanceAiGatewayModelsResolveOutputModelModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapDashboardInstanceAiGatewayModelsResolveOutputModelCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveOutput:
        return DashboardInstanceAiGatewayModelsResolveOutput(
        object=data.get('object'),
        requested=data.get('requested'),
        request=data.get('request'),
        via=data.get('via'),
        model=mapDashboardInstanceAiGatewayModelsResolveOutputModel.from_dict(data.get('model')) if data.get('model') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayModelsResolveBody:
    model: str


class mapDashboardInstanceAiGatewayModelsResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsResolveBody:
        return DashboardInstanceAiGatewayModelsResolveBody(
        model=data.get('model')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

