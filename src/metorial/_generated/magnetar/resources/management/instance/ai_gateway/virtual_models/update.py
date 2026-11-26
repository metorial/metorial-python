from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersion:
    object: str
    id: str
    number: float
    definition: ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateOutput:
    object: str
    id: str
    slug: str
    name: str
    warnings: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    current_version: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersion] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersion:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersionDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateOutput:
        return ManagementInstanceAiGatewayVirtualModelsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        current_version=mapManagementInstanceAiGatewayVirtualModelsUpdateOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        warnings=data.get('warnings', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    definition: Optional[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinition] = None


class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinition:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsUpdateBody:
        return ManagementInstanceAiGatewayVirtualModelsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        definition=mapManagementInstanceAiGatewayVirtualModelsUpdateBodyDefinition.from_dict(data.get('definition')) if data.get('definition') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

