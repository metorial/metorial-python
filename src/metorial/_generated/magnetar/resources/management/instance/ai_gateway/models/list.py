from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayModelsListOutputItemsLab:
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceAiGatewayModelsListOutputItemsModalities:
    input: List[str]
    output: List[str]
@dataclass
class ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class ManagementInstanceAiGatewayModelsListOutputItemsCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning] = None
    prompt_caching: Optional[ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching] = None
@dataclass
class ManagementInstanceAiGatewayModelsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: ManagementInstanceAiGatewayModelsListOutputItemsLab
    open_weights: bool
    modalities: ManagementInstanceAiGatewayModelsListOutputItemsModalities
    capabilities: ManagementInstanceAiGatewayModelsListOutputItemsCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayModelsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayModelsListOutput:
    object: str
    items: List[ManagementInstanceAiGatewayModelsListOutputItems]
    pagination: ManagementInstanceAiGatewayModelsListOutputPagination


class mapManagementInstanceAiGatewayModelsListOutputItemsLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutputItemsLab:
        return ManagementInstanceAiGatewayModelsListOutputItemsLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutputItemsLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsListOutputItemsModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutputItemsModalities:
        return ManagementInstanceAiGatewayModelsListOutputItemsModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutputItemsModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning:
        return ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
        return ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsListOutputItemsCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutputItemsCapabilities:
        return ManagementInstanceAiGatewayModelsListOutputItemsCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapManagementInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutputItemsCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutputItems:
        return ManagementInstanceAiGatewayModelsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapManagementInstanceAiGatewayModelsListOutputItemsLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapManagementInstanceAiGatewayModelsListOutputItemsModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapManagementInstanceAiGatewayModelsListOutputItemsCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutputPagination:
        return ManagementInstanceAiGatewayModelsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayModelsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListOutput:
        return ManagementInstanceAiGatewayModelsListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceAiGatewayModelsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAiGatewayModelsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayModelsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    lab: Optional[str] = None
    kind: Optional[str] = None
    search: Optional[str] = None


class mapManagementInstanceAiGatewayModelsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayModelsListQuery:
        return ManagementInstanceAiGatewayModelsListQuery(
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
    def to_dict(value: Union[ManagementInstanceAiGatewayModelsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

