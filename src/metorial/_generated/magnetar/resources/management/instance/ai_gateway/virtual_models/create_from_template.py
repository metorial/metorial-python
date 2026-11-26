from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext:
    prior_turns: Optional[float] = None
    max_chars: Optional[float] = None
    include_system: Optional[bool] = None
    include_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision:
    model: str
    connection_id: Optional[str] = None
    timeout_ms: Optional[float] = None
    on_error: Optional[str] = None
    context: Optional[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules:
    id: str
    when: str
    models: List[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels]
    description: Optional[str] = None
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels:
    model: str
    weight: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides:
    reasoning_effort: Optional[str] = None
    max_output_tokens: Optional[float] = None
    temperature: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault:
    models: List[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels]
    overrides: Optional[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness:
    metadata_key: str
    ttl_seconds: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition:
    rules: List[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules]
    default: ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault
    decision: Optional[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision] = None
    signals: Optional[Dict[str, Dict[str, Any]]] = None
    stickiness: Optional[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion:
    object: str
    id: str
    number: float
    definition: ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition
    target_models: List[str]
    created_at: datetime
@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutput:
    object: str
    id: str
    slug: str
    name: str
    warnings: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    current_version: Optional[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext(
        prior_turns=data.get('prior_turns'),
        max_chars=data.get('max_chars'),
        include_system=data.get('include_system'),
        include_tool_names=data.get('include_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision(
        model=data.get('model'),
        connection_id=data.get('connection_id'),
        timeout_ms=data.get('timeout_ms'),
        on_error=data.get('on_error'),
        context=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecisionContext.from_dict(data.get('context')) if data.get('context') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules(
        id=data.get('id'),
        description=data.get('description'),
        when=data.get('when'),
        models=[mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRulesOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels(
        model=data.get('model'),
        weight=data.get('weight')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides(
        reasoning_effort=data.get('reasoning_effort'),
        max_output_tokens=data.get('max_output_tokens'),
        temperature=data.get('temperature')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault(
        models=[mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultModels.from_dict(item) for item in data.get('models', []) if item],
        overrides=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefaultOverrides.from_dict(data.get('overrides')) if data.get('overrides') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness(
        metadata_key=data.get('metadata_key'),
        ttl_seconds=data.get('ttl_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition(
        decision=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        signals=data.get('signals'),
        rules=[mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionRules.from_dict(item) for item in data.get('rules', []) if item],
        default=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionDefault.from_dict(data.get('default')) if data.get('default') else None,
        stickiness=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinitionStickiness.from_dict(data.get('stickiness')) if data.get('stickiness') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        number=data.get('number'),
        definition=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersionDefinition.from_dict(data.get('definition')) if data.get('definition') else None,
        target_models=data.get('target_models', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutput:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        current_version=mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        warnings=data.get('warnings', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateBody:
    template: str
    slug: str
    name: str
    parameters: Dict[str, str]
    description: Optional[str] = None
    decision_connection_id: Optional[str] = None


class mapManagementInstanceAiGatewayVirtualModelsCreateFromTemplateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateBody:
        return ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateBody(
        template=data.get('template'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        parameters=data.get('parameters'),
        decision_connection_id=data.get('decision_connection_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelsCreateFromTemplateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

