from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules:
    id: str
    when: str
    models: List[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault:
    models: List[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels]
    overrides: Optional[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition:
    rules: List[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules]
    default: AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault
    decision: Optional[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness] = None
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion:
    object: str
    id: str
    number: float
    definition: AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class AiGatewayVirtualModelsCreateFromTemplateOutput:
    object: str
    id: str
    slug: str
    name: str
    warnings: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    current_version: Optional[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion] = None
    deleted_at: Optional[datetime] = None


class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault(
        models=[mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition(
        decision=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion:
        return AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsCreateFromTemplateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateOutput:
        return AiGatewayVirtualModelsCreateFromTemplateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        current_version=mapAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        warnings=data.get('warnings', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsCreateFromTemplateBody:
    template: str
    slug: str
    name: str
    parameters: Dict[str, str]
    description: Optional[str] = None
    decision_connection_id: Optional[str] = None


class mapAiGatewayVirtualModelsCreateFromTemplateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsCreateFromTemplateBody:
        return AiGatewayVirtualModelsCreateFromTemplateBody(
        template=data.get('template'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        parameters=data.get('parameters'),
        decision_connection_id=data.get('decision_connection_id')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsCreateFromTemplateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

