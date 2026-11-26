from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsTestDraftOutputRequest:
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
class AiGatewayVirtualModelsTestDraftOutputRouteTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class AiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
    model: str
    reason: str
@dataclass
class AiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
    code: str
    message: str
@dataclass
class AiGatewayVirtualModelsTestDraftOutputRouteDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[AiGatewayVirtualModelsTestDraftOutputRouteDecisionError] = None
@dataclass
class AiGatewayVirtualModelsTestDraftOutputRoute:
    reason: str
    trace: List[AiGatewayVirtualModelsTestDraftOutputRouteTrace]
    models: List[str]
    skipped_models: List[AiGatewayVirtualModelsTestDraftOutputRouteSkippedModels]
    version_id: Optional[str] = None
    version_number: Optional[float] = None
    rule_id: Optional[str] = None
    decision: Optional[AiGatewayVirtualModelsTestDraftOutputRouteDecision] = None
@dataclass
class AiGatewayVirtualModelsTestDraftOutputOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestDraftOutput:
    object: str
    request: AiGatewayVirtualModelsTestDraftOutputRequest
    candidates: List[Dict[str, Any]]
    route: Optional[AiGatewayVirtualModelsTestDraftOutputRoute] = None
    overrides: Optional[AiGatewayVirtualModelsTestDraftOutputOverrides] = None


class mapAiGatewayVirtualModelsTestDraftOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutputRequest:
        return AiGatewayVirtualModelsTestDraftOutputRequest(
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
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftOutputRouteTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutputRouteTrace:
        return AiGatewayVirtualModelsTestDraftOutputRouteTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutputRouteTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
        return AiGatewayVirtualModelsTestDraftOutputRouteSkippedModels(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutputRouteSkippedModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
        return AiGatewayVirtualModelsTestDraftOutputRouteDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutputRouteDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftOutputRouteDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutputRouteDecision:
        return AiGatewayVirtualModelsTestDraftOutputRouteDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapAiGatewayVirtualModelsTestDraftOutputRouteDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutputRouteDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutputRoute:
        return AiGatewayVirtualModelsTestDraftOutputRoute(
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapAiGatewayVirtualModelsTestDraftOutputRouteTrace.from_dict(item) for item in data.get('trace', []) if item],
        models=data.get('models', []),
        skipped_models=[mapAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels.from_dict(item) for item in data.get('skipped_models', []) if item],
        decision=mapAiGatewayVirtualModelsTestDraftOutputRouteDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftOutputOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutputOverrides:
        return AiGatewayVirtualModelsTestDraftOutputOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutputOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftOutput:
        return AiGatewayVirtualModelsTestDraftOutput(
        object=data.get('object'),
        request=mapAiGatewayVirtualModelsTestDraftOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        route=mapAiGatewayVirtualModelsTestDraftOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        overrides=mapAiGatewayVirtualModelsTestDraftOutputOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
    models: List[AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBodyDefinition:
    rules: List[AiGatewayVirtualModelsTestDraftBodyDefinitionRules]
    default: AiGatewayVirtualModelsTestDraftBodyDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsTestDraftBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsTestDraftBodyDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsTestDraftBody:
    definition: AiGatewayVirtualModelsTestDraftBodyDefinition
    dialect: str
    request: Dict[str, Any]
    token_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class mapAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionRules:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionDefault(
        models=[mapAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
        return AiGatewayVirtualModelsTestDraftBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBodyDefinition:
        return AiGatewayVirtualModelsTestDraftBodyDefinition(
        decision=mapAiGatewayVirtualModelsTestDraftBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsTestDraftBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsTestDraftBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsTestDraftBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsTestDraftBody:
        return AiGatewayVirtualModelsTestDraftBody(
        definition=mapAiGatewayVirtualModelsTestDraftBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        token_id=data.get('token_id'),
        dialect=data.get('dialect'),
        request=data.get('request'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsTestDraftBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

