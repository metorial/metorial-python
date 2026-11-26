from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal:
    rule_id: Optional[str] = None
    model: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
    code: str
    message: str
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed:
    trace: List[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace]
    rule_id: Optional[str] = None
    model: Optional[str] = None
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutputResults:
    inference_log_id: str
    received_at: datetime
    original: ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal
    changed: bool
    replayed: Optional[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed] = None
    error: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutputSummary:
    replayed: float
    changed: float
    decision_cost_usd: float
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayOutput:
    object: str
    results: List[ManagementInstanceAiGatewayVirtualModelsReplayOutputResults]
    summary: ManagementInstanceAiGatewayVirtualModelsReplayOutputSummary


class mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal(
        rule_id=data.get('rule_id'),
        model=data.get('model')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed(
        rule_id=data.get('rule_id'),
        model=data.get('model'),
        trace=[mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedTrace.from_dict(item) for item in data.get('trace', []) if item],
        decision=mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayedDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayOutputResults:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutputResults:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutputResults(
        inference_log_id=data.get('inference_log_id'),
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        original=mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsOriginal.from_dict(data.get('original')) if data.get('original') else None,
        replayed=mapManagementInstanceAiGatewayVirtualModelsReplayOutputResultsReplayed.from_dict(data.get('replayed')) if data.get('replayed') else None,
        changed=data.get('changed'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutputResults, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayOutputSummary:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutputSummary:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutputSummary(
        replayed=data.get('replayed'),
        changed=data.get('changed'),
        decision_cost_usd=data.get('decision_cost_usd')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutputSummary, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayOutput:
        return ManagementInstanceAiGatewayVirtualModelsReplayOutput(
        object=data.get('object'),
        results=[mapManagementInstanceAiGatewayVirtualModelsReplayOutputResults.from_dict(item) for item in data.get('results', []) if item],
        summary=mapManagementInstanceAiGatewayVirtualModelsReplayOutputSummary.from_dict(data.get('summary')) if data.get('summary') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsReplayBody:
    definition: Optional[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinition] = None
    limit: Optional[float] = None


class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinition:
        return ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsReplayBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsReplayBody:
        return ManagementInstanceAiGatewayVirtualModelsReplayBody(
        definition=mapManagementInstanceAiGatewayVirtualModelsReplayBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        limit=data.get('limit')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsReplayBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

