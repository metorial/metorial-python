from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayModelsListOutputItemsLab:
    id: str
    slug: str
    name: str
@dataclass
class AiGatewayModelsListOutputItemsModalities:
    input: List[str]
    output: List[str]
@dataclass
class AiGatewayModelsListOutputItemsCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class AiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class AiGatewayModelsListOutputItemsCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[AiGatewayModelsListOutputItemsCapabilitiesReasoning] = None
    prompt_caching: Optional[AiGatewayModelsListOutputItemsCapabilitiesPromptCaching] = None
@dataclass
class AiGatewayModelsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: AiGatewayModelsListOutputItemsLab
    open_weights: bool
    modalities: AiGatewayModelsListOutputItemsModalities
    capabilities: AiGatewayModelsListOutputItemsCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class AiGatewayModelsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class AiGatewayModelsListOutput:
    object: str
    items: List[AiGatewayModelsListOutputItems]
    pagination: AiGatewayModelsListOutputPagination


class mapAiGatewayModelsListOutputItemsLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutputItemsLab:
        return AiGatewayModelsListOutputItemsLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutputItemsLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsListOutputItemsModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutputItemsModalities:
        return AiGatewayModelsListOutputItemsModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutputItemsModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsListOutputItemsCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutputItemsCapabilitiesReasoning:
        return AiGatewayModelsListOutputItemsCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutputItemsCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
        return AiGatewayModelsListOutputItemsCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutputItemsCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsListOutputItemsCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutputItemsCapabilities:
        return AiGatewayModelsListOutputItemsCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapAiGatewayModelsListOutputItemsCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapAiGatewayModelsListOutputItemsCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutputItemsCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutputItems:
        return AiGatewayModelsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapAiGatewayModelsListOutputItemsLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapAiGatewayModelsListOutputItemsModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapAiGatewayModelsListOutputItemsCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutputPagination:
        return AiGatewayModelsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayModelsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListOutput:
        return AiGatewayModelsListOutput(
        object=data.get('object'),
        items=[mapAiGatewayModelsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAiGatewayModelsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayModelsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    lab: Optional[str] = None
    kind: Optional[str] = None
    search: Optional[str] = None


class mapAiGatewayModelsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayModelsListQuery:
        return AiGatewayModelsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        lab=data.get('lab'),
        kind=data.get('kind'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayModelsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

