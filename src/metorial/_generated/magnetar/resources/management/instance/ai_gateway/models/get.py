from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayModelsGetOutputLab:
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceAiGatewayModelsGetOutputModalities:
    input: List[str]
    output: List[str]
@dataclass
class ManagementInstanceAiGatewayModelsGetOutputCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class ManagementInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class ManagementInstanceAiGatewayModelsGetOutputCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[ManagementInstanceAiGatewayModelsGetOutputCapabilitiesReasoning] = None
    prompt_caching: Optional[ManagementInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching] = None
@dataclass
class ManagementInstanceAiGatewayModelsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: ManagementInstanceAiGatewayModelsGetOutputLab
    open_weights: bool
    modalities: ManagementInstanceAiGatewayModelsGetOutputModalities
    capabilities: ManagementInstanceAiGatewayModelsGetOutputCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None


class mapManagementInstanceAiGatewayModelsGetOutputLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsGetOutputLab:
        return ManagementInstanceAiGatewayModelsGetOutputLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsGetOutputLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsGetOutputModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsGetOutputModalities:
        return ManagementInstanceAiGatewayModelsGetOutputModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsGetOutputModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsGetOutputCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsGetOutputCapabilitiesReasoning:
        return ManagementInstanceAiGatewayModelsGetOutputCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsGetOutputCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching:
        return ManagementInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsGetOutputCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsGetOutputCapabilities:
        return ManagementInstanceAiGatewayModelsGetOutputCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapManagementInstanceAiGatewayModelsGetOutputCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapManagementInstanceAiGatewayModelsGetOutputCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsGetOutputCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsGetOutput:
        return ManagementInstanceAiGatewayModelsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapManagementInstanceAiGatewayModelsGetOutputLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapManagementInstanceAiGatewayModelsGetOutputModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapManagementInstanceAiGatewayModelsGetOutputCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

