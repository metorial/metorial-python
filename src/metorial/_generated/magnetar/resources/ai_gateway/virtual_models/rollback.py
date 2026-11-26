from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefault:
    models: List[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinition:
    rules: List[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRules]
    default: AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsRollbackOutputCurrentVersion:
    object: str
    id: str
    number: float
    definition: AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class AiGatewayVirtualModelsRollbackOutput:
    object: str
    id: str
    slug: str
    name: str
    warnings: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    current_version: Optional[AiGatewayVirtualModelsRollbackOutputCurrentVersion] = None
    deleted_at: Optional[datetime] = None


class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecisionContext:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecision:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesModels:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesOverrides:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRules:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultModels:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefault:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefault(
        models=[mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionStickiness:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinition:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinition(
        decision=mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersionDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutputCurrentVersion:
        return AiGatewayVirtualModelsRollbackOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapAiGatewayVirtualModelsRollbackOutputCurrentVersionDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsRollbackOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackOutput:
        return AiGatewayVirtualModelsRollbackOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        current_version=mapAiGatewayVirtualModelsRollbackOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        warnings=data.get('warnings', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsRollbackBody:
    version_id: str


class mapAiGatewayVirtualModelsRollbackBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsRollbackBody:
        return AiGatewayVirtualModelsRollbackBody(
        version_id=data.get('version_id')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsRollbackBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

