from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestOutputRequest:
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
class DashboardInstanceAiGatewayVirtualModelsTestOutputRouteTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels:
    model: str
    reason: str
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError:
    code: str
    message: str
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestOutputRoute:
    reason: str
    trace: List[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteTrace]
    models: List[str]
    skipped_models: List[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels]
    version_id: Optional[str] = None
    version_number: Optional[float] = None
    rule_id: Optional[str] = None
    decision: Optional[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecision] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestOutputOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestOutput:
    object: str
    request: DashboardInstanceAiGatewayVirtualModelsTestOutputRequest
    candidates: List[Dict[str, Any]]
    route: Optional[DashboardInstanceAiGatewayVirtualModelsTestOutputRoute] = None
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsTestOutputOverrides] = None


class mapDashboardInstanceAiGatewayVirtualModelsTestOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutputRequest:
        return DashboardInstanceAiGatewayVirtualModelsTestOutputRequest(
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
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutputRouteTrace:
        return DashboardInstanceAiGatewayVirtualModelsTestOutputRouteTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels:
        return DashboardInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError:
        return DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecision:
        return DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutputRoute:
        return DashboardInstanceAiGatewayVirtualModelsTestOutputRoute(
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteTrace.from_dict(item) for item in data.get('trace', []) if item],
        models=data.get('models', []),
        skipped_models=[mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels.from_dict(item) for item in data.get('skipped_models', []) if item],
        decision=mapDashboardInstanceAiGatewayVirtualModelsTestOutputRouteDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestOutputOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutputOverrides:
        return DashboardInstanceAiGatewayVirtualModelsTestOutputOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutputOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestOutput:
        return DashboardInstanceAiGatewayVirtualModelsTestOutput(
        object=data.get('object'),
        request=mapDashboardInstanceAiGatewayVirtualModelsTestOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        route=mapDashboardInstanceAiGatewayVirtualModelsTestOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        overrides=mapDashboardInstanceAiGatewayVirtualModelsTestOutputOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRules:
    id: str
    when: str
    models: List[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault:
    models: List[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels]
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBodyDefinition:
    rules: List[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRules]
    default: DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault
    decision: Optional[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsTestBody:
    dialect: str
    request: Dict[str, Any]
    definition: Optional[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinition] = None
    token_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRules:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault(
        models=[mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBodyDefinition:
        return DashboardInstanceAiGatewayVirtualModelsTestBodyDefinition(
        decision=mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsTestBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsTestBody:
        return DashboardInstanceAiGatewayVirtualModelsTestBody(
        definition=mapDashboardInstanceAiGatewayVirtualModelsTestBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        token_id=data.get('token_id'),
        dialect=data.get('dialect'),
        request=data.get('request'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsTestBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

