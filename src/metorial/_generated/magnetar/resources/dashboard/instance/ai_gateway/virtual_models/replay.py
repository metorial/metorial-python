from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal:
    rule_id: Optional[str] = None
    model: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
    code: str
    message: str
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed:
    trace: List[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace]
    rule_id: Optional[str] = None
    model: Optional[str] = None
    decision: Optional[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutputResults:
    inference_log_id: str
    received_at: datetime
    original: DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal
    changed: bool
    replayed: Optional[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed] = None
    error: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutputSummary:
    replayed: float
    changed: float
    decision_cost_usd: float
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayOutput:
    object: str
    results: List[DashboardInstanceAiGatewayVirtualModelsReplayOutputResults]
    summary: DashboardInstanceAiGatewayVirtualModelsReplayOutputSummary


class mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal(
        rule_id=data.get('rule_id'),
        model=data.get('model')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed(
        rule_id=data.get('rule_id'),
        model=data.get('model'),
        trace=[mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace.from_dict(item) for item in data.get('trace', []) if item],
        decision=mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResults:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutputResults:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutputResults(
        inference_log_id=data.get('inference_log_id'),
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        original=mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal.from_dict(data.get('original')) if data.get('original') else None,
        replayed=mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed.from_dict(data.get('replayed')) if data.get('replayed') else None,
        changed=data.get('changed'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutputResults, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayOutputSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutputSummary:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutputSummary(
        replayed=data.get('replayed'),
        changed=data.get('changed'),
        decision_cost_usd=data.get('decision_cost_usd')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutputSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayOutput:
        return DashboardInstanceAiGatewayVirtualModelsReplayOutput(
        object=data.get('object'),
        results=[mapDashboardInstanceAiGatewayVirtualModelsReplayOutputResults.from_dict(item) for item in data.get('results', []) if item],
        summary=mapDashboardInstanceAiGatewayVirtualModelsReplayOutputSummary.from_dict(data.get('summary')) if data.get('summary') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules:
    id: str
    when: str
    models: List[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault:
    models: List[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels]
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinition:
    rules: List[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules]
    default: DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault
    decision: Optional[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsReplayBody:
    definition: Optional[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinition] = None
    limit: Optional[float] = None


class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault(
        models=[mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinition:
        return DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinition(
        decision=mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsReplayBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsReplayBody:
        return DashboardInstanceAiGatewayVirtualModelsReplayBody(
        definition=mapDashboardInstanceAiGatewayVirtualModelsReplayBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        limit=data.get('limit')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsReplayBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

