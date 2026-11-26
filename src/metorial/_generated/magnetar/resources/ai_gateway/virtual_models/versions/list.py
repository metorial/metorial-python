from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault:
    models: List[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItemsDefinition:
    rules: List[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules]
    default: AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutputItems:
    object: str
    id: str
    number: float
    definition: AiGatewayVirtualModelsVersionsListOutputItemsDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class AiGatewayVirtualModelsVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class AiGatewayVirtualModelsVersionsListOutput:
    object: str
    items: List[AiGatewayVirtualModelsVersionsListOutputItems]
    pagination: AiGatewayVirtualModelsVersionsListOutputPagination


class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault(
        models=[mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItemsDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItemsDefinition:
        return AiGatewayVirtualModelsVersionsListOutputItemsDefinition(
        decision=mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItemsDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputItems:
        return AiGatewayVirtualModelsVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapAiGatewayVirtualModelsVersionsListOutputItemsDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutputPagination:
        return AiGatewayVirtualModelsVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListOutput:
        return AiGatewayVirtualModelsVersionsListOutput(
        object=data.get('object'),
        items=[mapAiGatewayVirtualModelsVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAiGatewayVirtualModelsVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapAiGatewayVirtualModelsVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsListQuery:
        return AiGatewayVirtualModelsVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

