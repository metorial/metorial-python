from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersion:
    object: str
    id: str
    number: float
    definition: ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceAiGatewayVirtualModelsGetOutput:
    object: str
    id: str
    slug: str
    name: str
    warnings: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    current_version: Optional[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersion] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinition:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersion:
        return ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersionDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsGetOutput:
        return ManagementInstanceAiGatewayVirtualModelsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        current_version=mapManagementInstanceAiGatewayVirtualModelsGetOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        warnings=data.get('warnings', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

