from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault:
    models: List[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition:
    rules: List[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules]
    default: AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsUpdateOutputCurrentVersion:
    object: str
    id: str
    number: float
    definition: AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class AiGatewayVirtualModelsUpdateOutput:
    object: str
    id: str
    slug: str
    name: str
    warnings: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    current_version: Optional[AiGatewayVirtualModelsUpdateOutputCurrentVersion] = None
    deleted_at: Optional[datetime] = None


class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault(
        models=[mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition(
        decision=mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutputCurrentVersion:
        return AiGatewayVirtualModelsUpdateOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateOutput:
        return AiGatewayVirtualModelsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        current_version=mapAiGatewayVirtualModelsUpdateOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        warnings=data.get('warnings', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsUpdateBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionDefault:
    models: List[AiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsUpdateBodyDefinition:
    rules: List[AiGatewayVirtualModelsUpdateBodyDefinitionRules]
    default: AiGatewayVirtualModelsUpdateBodyDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsUpdateBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsUpdateBodyDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[AiGatewayVirtualModelsUpdateBodyDefinition] = None


class mapAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext:
        return AiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionDecision:
        return AiGatewayVirtualModelsUpdateBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionRulesModels:
        return AiGatewayVirtualModelsUpdateBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides:
        return AiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionRules:
        return AiGatewayVirtualModelsUpdateBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels:
        return AiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionDefault:
        return AiGatewayVirtualModelsUpdateBodyDefinitionDefault(
        models=[mapAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinitionStickiness:
        return AiGatewayVirtualModelsUpdateBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBodyDefinition:
        return AiGatewayVirtualModelsUpdateBodyDefinition(
        decision=mapAiGatewayVirtualModelsUpdateBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsUpdateBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsUpdateBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsUpdateBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsUpdateBody:
        return AiGatewayVirtualModelsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        definition=mapAiGatewayVirtualModelsUpdateBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

