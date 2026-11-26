from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsTestOutputRequest:
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
class AiGatewayVirtualModelsTestOutputRouteTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class AiGatewayVirtualModelsTestOutputRouteSkippedModels:
    model: str
    reason: str
@dataclass
class AiGatewayVirtualModelsTestOutputRouteDecisionError:
    code: str
    message: str
@dataclass
class AiGatewayVirtualModelsTestOutputRouteDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[AiGatewayVirtualModelsTestOutputRouteDecisionError] = None
@dataclass
class AiGatewayVirtualModelsTestOutputRoute:
    reason: str
    trace: List[AiGatewayVirtualModelsTestOutputRouteTrace]
    models: List[str]
    skipped_models: List[AiGatewayVirtualModelsTestOutputRouteSkippedModels]
    version_id: Optional[str] = None
    version_number: Optional[float] = None
    rule_id: Optional[str] = None
    decision: Optional[AiGatewayVirtualModelsTestOutputRouteDecision] = None
@dataclass
class AiGatewayVirtualModelsTestOutputOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestOutput:
    object: str
    request: AiGatewayVirtualModelsTestOutputRequest
    candidates: List[Dict[str, Any]]
    route: Optional[AiGatewayVirtualModelsTestOutputRoute] = None
    overrides: Optional[AiGatewayVirtualModelsTestOutputOverrides] = None


class mapAiGatewayVirtualModelsTestOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutputRequest:
        return AiGatewayVirtualModelsTestOutputRequest(
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
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestOutputRouteTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutputRouteTrace:
        return AiGatewayVirtualModelsTestOutputRouteTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutputRouteTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestOutputRouteSkippedModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutputRouteSkippedModels:
        return AiGatewayVirtualModelsTestOutputRouteSkippedModels(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutputRouteSkippedModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestOutputRouteDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutputRouteDecisionError:
        return AiGatewayVirtualModelsTestOutputRouteDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutputRouteDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestOutputRouteDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutputRouteDecision:
        return AiGatewayVirtualModelsTestOutputRouteDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapAiGatewayVirtualModelsTestOutputRouteDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutputRouteDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutputRoute:
        return AiGatewayVirtualModelsTestOutputRoute(
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapAiGatewayVirtualModelsTestOutputRouteTrace.from_dict(item) for item in data.get('trace', []) if item],
        models=data.get('models', []),
        skipped_models=[mapAiGatewayVirtualModelsTestOutputRouteSkippedModels.from_dict(item) for item in data.get('skipped_models', []) if item],
        decision=mapAiGatewayVirtualModelsTestOutputRouteDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestOutputOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutputOverrides:
        return AiGatewayVirtualModelsTestOutputOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutputOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestOutput:
        return AiGatewayVirtualModelsTestOutput(
        object=data.get('object'),
        request=mapAiGatewayVirtualModelsTestOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        route=mapAiGatewayVirtualModelsTestOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        overrides=mapAiGatewayVirtualModelsTestOutputOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsTestBodyDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsTestBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsTestBodyDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionDefault:
    models: List[AiGatewayVirtualModelsTestBodyDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestBodyDefinition:
    rules: List[AiGatewayVirtualModelsTestBodyDefinitionRules]
    default: AiGatewayVirtualModelsTestBodyDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsTestBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsTestBodyDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsTestBody:
    dialect: str
    request: Dict[str, Any]
    definition: Optional[AiGatewayVirtualModelsTestBodyDefinition] = None
    token_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class mapAiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
        return AiGatewayVirtualModelsTestBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionDecision:
        return AiGatewayVirtualModelsTestBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsTestBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionRulesModels:
        return AiGatewayVirtualModelsTestBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
        return AiGatewayVirtualModelsTestBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionRules:
        return AiGatewayVirtualModelsTestBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsTestBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
        return AiGatewayVirtualModelsTestBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionDefault:
        return AiGatewayVirtualModelsTestBodyDefinitionDefault(
        models=[mapAiGatewayVirtualModelsTestBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinitionStickiness:
        return AiGatewayVirtualModelsTestBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBodyDefinition:
        return AiGatewayVirtualModelsTestBodyDefinition(
        decision=mapAiGatewayVirtualModelsTestBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsTestBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsTestBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsTestBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestBody:
        return AiGatewayVirtualModelsTestBody(
        definition=mapAiGatewayVirtualModelsTestBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        token_id=data.get('token_id'),
        dialect=data.get('dialect'),
        request=data.get('request'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

