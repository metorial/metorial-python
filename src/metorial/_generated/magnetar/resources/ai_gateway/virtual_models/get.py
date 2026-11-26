from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault:
    models: List[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersionDefinition:
    rules: List[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules]
    default: AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsGetOutputCurrentVersion:
    object: str
    id: str
    number: float
    definition: AiGatewayVirtualModelsGetOutputCurrentVersionDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class AiGatewayVirtualModelsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    warnings: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    current_version: Optional[AiGatewayVirtualModelsGetOutputCurrentVersion] = None
    deleted_at: Optional[datetime] = None


class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault(
        models=[mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersionDefinition:
        return AiGatewayVirtualModelsGetOutputCurrentVersionDefinition(
        decision=mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersionDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutputCurrentVersion:
        return AiGatewayVirtualModelsGetOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapAiGatewayVirtualModelsGetOutputCurrentVersionDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsGetOutput:
        return AiGatewayVirtualModelsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        current_version=mapAiGatewayVirtualModelsGetOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        warnings=data.get('warnings', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

