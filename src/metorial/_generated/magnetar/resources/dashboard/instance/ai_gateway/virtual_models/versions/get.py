from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
    id: str
    when: str
    models: List[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
    models: List[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels]
    overrides: Optional[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition:
    rules: List[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules]
    default: DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault
    decision: Optional[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsVersionsGetOutput:
    object: str
    id: str
    number: float
    definition: DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition
    target_models: List[str]
    created_at: datetime


class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault(
        models=[mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition(
        decision=mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsVersionsGetOutput:
        return DashboardInstanceAiGatewayVirtualModelsVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapDashboardInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

