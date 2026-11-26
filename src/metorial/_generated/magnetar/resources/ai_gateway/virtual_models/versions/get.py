from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
    models: List[AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutputDefinition:
    rules: List[AiGatewayVirtualModelsVersionsGetOutputDefinitionRules]
    default: AiGatewayVirtualModelsVersionsGetOutputDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsVersionsGetOutputDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsVersionsGetOutput:
    object: str
    id: str
    number: float
    definition: AiGatewayVirtualModelsVersionsGetOutputDefinition
    target_models: List[str]
    created_at: datetime


class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionDefault(
        models=[mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
        return AiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutputDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutputDefinition:
        return AiGatewayVirtualModelsVersionsGetOutputDefinition(
        decision=mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsVersionsGetOutputDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutputDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsVersionsGetOutput:
        return AiGatewayVirtualModelsVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapAiGatewayVirtualModelsVersionsGetOutputDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

