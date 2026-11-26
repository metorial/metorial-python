from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRequest:
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
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
    model: str
    reason: str
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
    code: str
    message: str
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    error: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRoute:
    reason: str
    trace: List[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace]
    models: List[str]
    skipped_models: List[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels]
    version_id: Optional[str] = None
    version_number: Optional[float] = None
    rule_id: Optional[str] = None
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutputOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftOutput:
    object: str
    request: ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRequest
    candidates: List[Dict[str, Any]]
    route: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRoute] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputOverrides] = None


class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRequest:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRequest(
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
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRoute:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRoute(
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteTrace.from_dict(item) for item in data.get('trace', []) if item],
        models=data.get('models', []),
        skipped_models=[mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteSkippedModels.from_dict(item) for item in data.get('skipped_models', []) if item],
        decision=mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRouteDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutputOverrides:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutputOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutputOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftOutput:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftOutput(
        object=data.get('object'),
        request=mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        route=mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        overrides=mapManagementInstanceAiGatewayVirtualModelsTestDraftOutputOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsTestDraftBody:
    definition: ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinition
    dialect: str
    request: Dict[str, Any]
    token_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinition:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsTestDraftBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsTestDraftBody:
        return ManagementInstanceAiGatewayVirtualModelsTestDraftBody(
        definition=mapManagementInstanceAiGatewayVirtualModelsTestDraftBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        token_id=data.get('token_id'),
        dialect=data.get('dialect'),
        request=data.get('request'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsTestDraftBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

