from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRequest:
    dialect: str
    input_tokens: float
    message_count: float
    user_turns: float
    is_continuation: bool
    has_images: bool
    has_files: bool
    has_audio: bool
    tool_count: float
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
    model: str
    reason: str
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
    code: str
    message: str
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRoute:
    reason: str
    trace: List[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace]
    models: List[str]
    skipped_models: List[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels]
    version_id: Optional[str] = None
    version_number: Optional[float] = None
    rule_id: Optional[str] = None
    decision: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutputOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftOutput:
    object: str
    request: DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRequest
    candidates: List[Dict[str, Any]]
    route: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRoute] = None
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputOverrides] = None


class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRequest:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRequest(
        dialect=data.get('dialect'),
        input_tokens=data.get('input_tokens'),
        message_count=data.get('message_count'),
        user_turns=data.get('user_turns'),
        is_continuation=data.get('is_continuation'),
        has_images=data.get('has_images'),
        has_files=data.get('has_files'),
        has_audio=data.get('has_audio'),
        tool_count=data.get('tool_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRoute:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRoute(
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace.from_dict(item) for item in data.get('trace', []) if item],
        models=data.get('models', []),
        skipped_models=[mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels.from_dict(item) for item in data.get('skipped_models', []) if item],
        decision=mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutputOverrides:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutputOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutputOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftOutput:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftOutput(
        object=data.get('object'),
        request=mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        route=mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        overrides=mapDashboardInstanceAiGatewayVirtualModelsTestDraftOutputOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules:
    id: str
    when: str
    models: List[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
    models: List[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels]
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinition:
    rules: List[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules]
    default: DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault
    decision: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestDraftBody:
    definition: DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinition
    dialect: str
    request: Dict[str, Any]
    token_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault(
        models=[mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinition:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinition(
        decision=mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestDraftBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestDraftBody:
        return DashboardInstanceAiGatewayVirtualModelsTestDraftBody(
        definition=mapDashboardInstanceAiGatewayVirtualModelsTestDraftBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        token_id=data.get('token_id'),
        dialect=data.get('dialect'),
        request=data.get('request'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestDraftBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

