from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayModelsGetOutputLab:
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceAiGatewayModelsGetOutputModalities:
    input: List[str]
    output: List[str]
@dataclass
class DashboardInstanceAiGatewayModelsGetOutputCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class DashboardInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class DashboardInstanceAiGatewayModelsGetOutputCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[DashboardInstanceAiGatewayModelsGetOutputCapabilitiesReasoning] = None
    prompt_caching: Optional[DashboardInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching] = None
@dataclass
class DashboardInstanceAiGatewayModelsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: DashboardInstanceAiGatewayModelsGetOutputLab
    open_weights: bool
    modalities: DashboardInstanceAiGatewayModelsGetOutputModalities
    capabilities: DashboardInstanceAiGatewayModelsGetOutputCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None


class mapDashboardInstanceAiGatewayModelsGetOutputLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsGetOutputLab:
        return DashboardInstanceAiGatewayModelsGetOutputLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsGetOutputLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsGetOutputModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsGetOutputModalities:
        return DashboardInstanceAiGatewayModelsGetOutputModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsGetOutputModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsGetOutputCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsGetOutputCapabilitiesReasoning:
        return DashboardInstanceAiGatewayModelsGetOutputCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsGetOutputCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching:
        return DashboardInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsGetOutputCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsGetOutputCapabilities:
        return DashboardInstanceAiGatewayModelsGetOutputCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapDashboardInstanceAiGatewayModelsGetOutputCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapDashboardInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsGetOutputCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsGetOutput:
        return DashboardInstanceAiGatewayModelsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapDashboardInstanceAiGatewayModelsGetOutputLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapDashboardInstanceAiGatewayModelsGetOutputModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapDashboardInstanceAiGatewayModelsGetOutputCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

