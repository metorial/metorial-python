from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItems:
    object: str
    id: str
    number: float
    definition: ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListOutput:
    object: str
    items: List[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItems]
    pagination: ManagementInstanceAiGatewayVirtualModelsVersionsListOutputPagination


class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinition:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItems:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItemsDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutputPagination:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListOutput:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAiGatewayVirtualModelsVersionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceAiGatewayVirtualModelsVersionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsListQuery:
        return ManagementInstanceAiGatewayVirtualModelsVersionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

