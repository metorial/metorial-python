from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsReplayOutputResultsOriginal:
    rule_id: Optional[str] = None
    model: Optional[str] = None
@dataclass
class AiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class AiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
    code: str
    message: str
@dataclass
class AiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[AiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError] = None
@dataclass
class AiGatewayVirtualModelsReplayOutputResultsReplayed:
    trace: List[AiGatewayVirtualModelsReplayOutputResultsReplayedTrace]
    rule_id: Optional[str] = None
    model: Optional[str] = None
    decision: Optional[AiGatewayVirtualModelsReplayOutputResultsReplayedDecision] = None
@dataclass
class AiGatewayVirtualModelsReplayOutputResults:
    inference_log_id: str
    received_at: datetime
    original: AiGatewayVirtualModelsReplayOutputResultsOriginal
    changed: bool
    replayed: Optional[AiGatewayVirtualModelsReplayOutputResultsReplayed] = None
    error: Optional[str] = None
@dataclass
class AiGatewayVirtualModelsReplayOutputSummary:
    replayed: float
    changed: float
    decision_cost_usd: float
@dataclass
class AiGatewayVirtualModelsReplayOutput:
    object: str
    results: List[AiGatewayVirtualModelsReplayOutputResults]
    summary: AiGatewayVirtualModelsReplayOutputSummary


class mapAiGatewayVirtualModelsReplayOutputResultsOriginal:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutputResultsOriginal:
        return AiGatewayVirtualModelsReplayOutputResultsOriginal(
        rule_id=data.get('rule_id'),
        model=data.get('model')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutputResultsOriginal, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
        return AiGatewayVirtualModelsReplayOutputResultsReplayedTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutputResultsReplayedTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
        return AiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
        return AiGatewayVirtualModelsReplayOutputResultsReplayedDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutputResultsReplayedDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayOutputResultsReplayed:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutputResultsReplayed:
        return AiGatewayVirtualModelsReplayOutputResultsReplayed(
        rule_id=data.get('rule_id'),
        model=data.get('model'),
        trace=[mapAiGatewayVirtualModelsReplayOutputResultsReplayedTrace.from_dict(item) for item in data.get('trace', []) if item],
        decision=mapAiGatewayVirtualModelsReplayOutputResultsReplayedDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutputResultsReplayed, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayOutputResults:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutputResults:
        return AiGatewayVirtualModelsReplayOutputResults(
        inference_log_id=data.get('inference_log_id'),
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        original=mapAiGatewayVirtualModelsReplayOutputResultsOriginal.from_dict(data.get('original')) if data.get('original') else None,
        replayed=mapAiGatewayVirtualModelsReplayOutputResultsReplayed.from_dict(data.get('replayed')) if data.get('replayed') else None,
        changed=data.get('changed'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutputResults, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayOutputSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutputSummary:
        return AiGatewayVirtualModelsReplayOutputSummary(
        replayed=data.get('replayed'),
        changed=data.get('changed'),
        decision_cost_usd=data.get('decision_cost_usd')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutputSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayOutput:
        return AiGatewayVirtualModelsReplayOutput(
        object=data.get('object'),
        results=[mapAiGatewayVirtualModelsReplayOutputResults.from_dict(item) for item in data.get('results', []) if item],
        summary=mapAiGatewayVirtualModelsReplayOutputSummary.from_dict(data.get('summary')) if data.get('summary') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsReplayBodyDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsReplayBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionDefault:
    models: List[AiGatewayVirtualModelsReplayBodyDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsReplayBodyDefinition:
    rules: List[AiGatewayVirtualModelsReplayBodyDefinitionRules]
    default: AiGatewayVirtualModelsReplayBodyDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsReplayBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsReplayBodyDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsReplayBody:
    definition: Optional[AiGatewayVirtualModelsReplayBodyDefinition] = None
    limit: Optional[float] = None


class mapAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
        return AiGatewayVirtualModelsReplayBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionDecision:
        return AiGatewayVirtualModelsReplayBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
        return AiGatewayVirtualModelsReplayBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
        return AiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionRules:
        return AiGatewayVirtualModelsReplayBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsReplayBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
        return AiGatewayVirtualModelsReplayBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionDefault:
        return AiGatewayVirtualModelsReplayBodyDefinitionDefault(
        models=[mapAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinitionStickiness:
        return AiGatewayVirtualModelsReplayBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBodyDefinition:
        return AiGatewayVirtualModelsReplayBodyDefinition(
        decision=mapAiGatewayVirtualModelsReplayBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsReplayBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsReplayBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsReplayBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsReplayBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsReplayBody:
        return AiGatewayVirtualModelsReplayBody(
        definition=mapAiGatewayVirtualModelsReplayBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        limit=data.get('limit')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsReplayBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

