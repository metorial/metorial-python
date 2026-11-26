from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsVersionsGetOutput:
    object: str
    id: str
    number: float
    definition: ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition
    target_models: List[str]
    created_at: datetime


class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsVersionsGetOutput:
        return ManagementInstanceAiGatewayVirtualModelsVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapManagementInstanceAiGatewayVirtualModelsVersionsGetOutputDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

