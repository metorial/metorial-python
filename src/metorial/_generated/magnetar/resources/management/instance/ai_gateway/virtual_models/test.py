from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestOutputRequest:
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
class ManagementInstanceAiGatewayVirtualModelsTestOutputRouteTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels:
    model: str
    reason: str
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError:
    code: str
    message: str
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestOutputRoute:
    reason: str
    trace: List[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteTrace]
    models: List[str]
    skipped_models: List[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels]
    version_id: Optional[str] = None
    version_number: Optional[float] = None
    rule_id: Optional[str] = None
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecision] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestOutputOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestOutput:
    object: str
    request: ManagementInstanceAiGatewayVirtualModelsTestOutputRequest
    candidates: List[Dict[str, Any]]
    route: Optional[ManagementInstanceAiGatewayVirtualModelsTestOutputRoute] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsTestOutputOverrides] = None


class mapManagementInstanceAiGatewayVirtualModelsTestOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutputRequest:
        return ManagementInstanceAiGatewayVirtualModelsTestOutputRequest(
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
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutputRouteTrace:
        return ManagementInstanceAiGatewayVirtualModelsTestOutputRouteTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels:
        return ManagementInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError:
        return ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecision:
        return ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutputRoute:
        return ManagementInstanceAiGatewayVirtualModelsTestOutputRoute(
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteTrace.from_dict(item) for item in data.get('trace', []) if item],
        models=data.get('models', []),
        skipped_models=[mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteSkippedModels.from_dict(item) for item in data.get('skipped_models', []) if item],
        decision=mapManagementInstanceAiGatewayVirtualModelsTestOutputRouteDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestOutputOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutputOverrides:
        return ManagementInstanceAiGatewayVirtualModelsTestOutputOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutputOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestOutput:
        return ManagementInstanceAiGatewayVirtualModelsTestOutput(
        object=data.get('object'),
        request=mapManagementInstanceAiGatewayVirtualModelsTestOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        route=mapManagementInstanceAiGatewayVirtualModelsTestOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        overrides=mapManagementInstanceAiGatewayVirtualModelsTestOutputOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBodyDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestBody:
    dialect: str
    request: Dict[str, Any]
    definition: Optional[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinition] = None
    token_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBodyDefinition:
        return ManagementInstanceAiGatewayVirtualModelsTestBodyDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestBody:
        return ManagementInstanceAiGatewayVirtualModelsTestBody(
        definition=mapManagementInstanceAiGatewayVirtualModelsTestBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        token_id=data.get('token_id'),
        dialect=data.get('dialect'),
        request=data.get('request'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

