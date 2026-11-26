from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayModelsListOutputItemsLab:
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceAiGatewayModelsListOutputItemsModalities:
    input: List[str]
    output: List[str]
@dataclass
class DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning:
    toggle: bool
    effort: Optional[List[str]] = None
@dataclass
class DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
    implicit: bool
    explicit: bool
    ttls: List[str]
@dataclass
class DashboardInstanceAiGatewayModelsListOutputItemsCapabilities:
    tools: bool
    structured_output: bool
    temperature: bool
    attachments: bool
    tool_choice: Optional[List[str]] = None
    reasoning: Optional[DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning] = None
    prompt_caching: Optional[DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching] = None
@dataclass
class DashboardInstanceAiGatewayModelsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    lab: DashboardInstanceAiGatewayModelsListOutputItemsLab
    open_weights: bool
    modalities: DashboardInstanceAiGatewayModelsListOutputItemsModalities
    capabilities: DashboardInstanceAiGatewayModelsListOutputItemsCapabilities
    description: Optional[str] = None
    family_slug: Optional[str] = None
    release_date: Optional[datetime] = None
    context_window: Optional[float] = None
    max_output_tokens: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayModelsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayModelsListOutput:
    object: str
    items: List[DashboardInstanceAiGatewayModelsListOutputItems]
    pagination: DashboardInstanceAiGatewayModelsListOutputPagination


class mapDashboardInstanceAiGatewayModelsListOutputItemsLab:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutputItemsLab:
        return DashboardInstanceAiGatewayModelsListOutputItemsLab(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutputItemsLab, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsListOutputItemsModalities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutputItemsModalities:
        return DashboardInstanceAiGatewayModelsListOutputItemsModalities(
        input=data.get('input', []),
        output=data.get('output', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutputItemsModalities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning:
        return DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning(
        toggle=data.get('toggle'),
        effort=data.get('effort', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching:
        return DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching(
        implicit=data.get('implicit'),
        explicit=data.get('explicit'),
        ttls=data.get('ttls', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsListOutputItemsCapabilities:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutputItemsCapabilities:
        return DashboardInstanceAiGatewayModelsListOutputItemsCapabilities(
        tools=data.get('tools'),
        tool_choice=data.get('tool_choice', []),
        structured_output=data.get('structured_output'),
        reasoning=mapDashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesReasoning.from_dict(data.get('reasoning')) if data.get('reasoning') else None,
        temperature=data.get('temperature'),
        prompt_caching=mapDashboardInstanceAiGatewayModelsListOutputItemsCapabilitiesPromptCaching.from_dict(data.get('prompt_caching')) if data.get('prompt_caching') else None,
        attachments=data.get('attachments')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutputItemsCapabilities, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutputItems:
        return DashboardInstanceAiGatewayModelsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        kind=data.get('kind'),
        status=data.get('status'),
        lab=mapDashboardInstanceAiGatewayModelsListOutputItemsLab.from_dict(data.get('lab')) if data.get('lab') else None,
        family_slug=data.get('family_slug'),
        release_date=datetime.fromisoformat(data.get('release_date').replace('Z', '+00:00')) if data.get('release_date') else None,
        open_weights=data.get('open_weights'),
        context_window=data.get('context_window'),
        max_output_tokens=data.get('max_output_tokens'),
        modalities=mapDashboardInstanceAiGatewayModelsListOutputItemsModalities.from_dict(data.get('modalities')) if data.get('modalities') else None,
        capabilities=mapDashboardInstanceAiGatewayModelsListOutputItemsCapabilities.from_dict(data.get('capabilities')) if data.get('capabilities') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutputPagination:
        return DashboardInstanceAiGatewayModelsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayModelsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListOutput:
        return DashboardInstanceAiGatewayModelsListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceAiGatewayModelsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAiGatewayModelsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayModelsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    lab: Optional[str] = None
    kind: Optional[str] = None
    search: Optional[str] = None


class mapDashboardInstanceAiGatewayModelsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayModelsListQuery:
        return DashboardInstanceAiGatewayModelsListQuery(
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
    def to_dict(value: Union[DashboardInstanceAiGatewayModelsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

