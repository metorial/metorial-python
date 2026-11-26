from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayInferenceLogsGetOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class AiGatewayInferenceLogsGetOutputModel:
    slug: str
    lab_slug: str
    id: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsGetOutputVirtualModelTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
    model: str
    reason: str
@dataclass
class AiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
    code: str
    message: str
@dataclass
class AiGatewayInferenceLogsGetOutputVirtualModelDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Any]] = None
    error: Optional[AiGatewayInferenceLogsGetOutputVirtualModelDecisionError] = None
@dataclass
class AiGatewayInferenceLogsGetOutputVirtualModel:
    id: str
    slug: str
    version_id: str
    version_number: float
    reason: str
    trace: List[AiGatewayInferenceLogsGetOutputVirtualModelTrace]
    targets: List[str]
    skipped_targets: List[AiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets]
    rule_id: Optional[str] = None
    decision: Optional[AiGatewayInferenceLogsGetOutputVirtualModelDecision] = None
@dataclass
class AiGatewayInferenceLogsGetOutputRoute:
    provider: str
    connection_owner: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsGetOutputAttemptsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsGetOutputAttempts:
    provider: str
    connection_owner: str
    started_at: datetime
    duration_ms: float
    outcome: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
    error: Optional[AiGatewayInferenceLogsGetOutputAttemptsError] = None
@dataclass
class AiGatewayInferenceLogsGetOutputError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsGetOutputUsageInput:
    total: float
    no_cache: float
    cache_read: float
    cache_write: float
@dataclass
class AiGatewayInferenceLogsGetOutputUsageOutput:
    total: float
    text: float
    reasoning: float
@dataclass
class AiGatewayInferenceLogsGetOutputUsage:
    input: AiGatewayInferenceLogsGetOutputUsageInput
    output: AiGatewayInferenceLogsGetOutputUsageOutput
@dataclass
class AiGatewayInferenceLogsGetOutputCostComponents:
    input: float
    cache_read: float
    cache_write: float
    output: float
    reasoning: float
@dataclass
class AiGatewayInferenceLogsGetOutputCost:
    currency: str
    priced: bool
    total_usd: float
    components: AiGatewayInferenceLogsGetOutputCostComponents
    pricing_source: str
@dataclass
class AiGatewayInferenceLogsGetOutputTiming:
    received_at: datetime
    completed_at: datetime
    total_ms: float
    upstream_started_at: Optional[datetime] = None
    first_token_at: Optional[datetime] = None
    upstream_ms: Optional[float] = None
    time_to_first_token_ms: Optional[float] = None
@dataclass
class AiGatewayInferenceLogsGetOutputRequest:
    message_count: Optional[float] = None
    tool_count: Optional[float] = None
    max_output_tokens: Optional[float] = None
    user_agent: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsGetOutputContent:
    request: Dict[str, Any]
    response: Optional[Dict[str, Any]] = None
@dataclass
class AiGatewayInferenceLogsGetOutput:
    object: str
    id: str
    token_id: str
    dialect: str
    operation: str
    requested_model: str
    metadata: Dict[str, str]
    attempts: List[AiGatewayInferenceLogsGetOutputAttempts]
    status: str
    timing: AiGatewayInferenceLogsGetOutputTiming
    request: AiGatewayInferenceLogsGetOutputRequest
    has_content: bool
    expires_at: datetime
    created_at: datetime
    consumer: Optional[AiGatewayInferenceLogsGetOutputConsumer] = None
    request_id: Optional[str] = None
    model: Optional[AiGatewayInferenceLogsGetOutputModel] = None
    virtual_model: Optional[AiGatewayInferenceLogsGetOutputVirtualModel] = None
    route: Optional[AiGatewayInferenceLogsGetOutputRoute] = None
    finish_reason: Optional[str] = None
    error: Optional[AiGatewayInferenceLogsGetOutputError] = None
    usage: Optional[AiGatewayInferenceLogsGetOutputUsage] = None
    cost: Optional[AiGatewayInferenceLogsGetOutputCost] = None
    content: Optional[AiGatewayInferenceLogsGetOutputContent] = None


class mapAiGatewayInferenceLogsGetOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputConsumer:
        return AiGatewayInferenceLogsGetOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputModel:
        return AiGatewayInferenceLogsGetOutputModel(
        id=data.get('id'),
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputVirtualModelTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputVirtualModelTrace:
        return AiGatewayInferenceLogsGetOutputVirtualModelTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputVirtualModelTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
        return AiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
        return AiGatewayInferenceLogsGetOutputVirtualModelDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputVirtualModelDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputVirtualModelDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputVirtualModelDecision:
        return AiGatewayInferenceLogsGetOutputVirtualModelDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapAiGatewayInferenceLogsGetOutputVirtualModelDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputVirtualModelDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputVirtualModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputVirtualModel:
        return AiGatewayInferenceLogsGetOutputVirtualModel(
        id=data.get('id'),
        slug=data.get('slug'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapAiGatewayInferenceLogsGetOutputVirtualModelTrace.from_dict(item) for item in data.get('trace', []) if item],
        targets=data.get('targets', []),
        skipped_targets=[mapAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets.from_dict(item) for item in data.get('skipped_targets', []) if item],
        decision=mapAiGatewayInferenceLogsGetOutputVirtualModelDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputVirtualModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputRoute:
        return AiGatewayInferenceLogsGetOutputRoute(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputAttemptsError:
        return AiGatewayInferenceLogsGetOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputAttempts:
        return AiGatewayInferenceLogsGetOutputAttempts(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id'),
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        duration_ms=data.get('duration_ms'),
        outcome=data.get('outcome'),
        error=mapAiGatewayInferenceLogsGetOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputError:
        return AiGatewayInferenceLogsGetOutputError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputUsageInput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputUsageInput:
        return AiGatewayInferenceLogsGetOutputUsageInput(
        total=data.get('total'),
        no_cache=data.get('no_cache'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputUsageInput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputUsageOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputUsageOutput:
        return AiGatewayInferenceLogsGetOutputUsageOutput(
        total=data.get('total'),
        text=data.get('text'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputUsageOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputUsage:
        return AiGatewayInferenceLogsGetOutputUsage(
        input=mapAiGatewayInferenceLogsGetOutputUsageInput.from_dict(data.get('input')) if data.get('input') else None,
        output=mapAiGatewayInferenceLogsGetOutputUsageOutput.from_dict(data.get('output')) if data.get('output') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputCostComponents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputCostComponents:
        return AiGatewayInferenceLogsGetOutputCostComponents(
        input=data.get('input'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write'),
        output=data.get('output'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputCostComponents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputCost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputCost:
        return AiGatewayInferenceLogsGetOutputCost(
        currency=data.get('currency'),
        priced=data.get('priced'),
        total_usd=data.get('total_usd'),
        components=mapAiGatewayInferenceLogsGetOutputCostComponents.from_dict(data.get('components')) if data.get('components') else None,
        pricing_source=data.get('pricing_source')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputCost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputTiming:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputTiming:
        return AiGatewayInferenceLogsGetOutputTiming(
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        upstream_started_at=datetime.fromisoformat(data.get('upstream_started_at').replace('Z', '+00:00')) if data.get('upstream_started_at') else None,
        first_token_at=datetime.fromisoformat(data.get('first_token_at').replace('Z', '+00:00')) if data.get('first_token_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        total_ms=data.get('total_ms'),
        upstream_ms=data.get('upstream_ms'),
        time_to_first_token_ms=data.get('time_to_first_token_ms')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputTiming, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputRequest:
        return AiGatewayInferenceLogsGetOutputRequest(
        message_count=data.get('message_count'),
        tool_count=data.get('tool_count'),
        max_output_tokens=data.get('max_output_tokens'),
        user_agent=data.get('user_agent')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutputContent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutputContent:
        return AiGatewayInferenceLogsGetOutputContent(
        request=data.get('request'),
        response=data.get('response')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutputContent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetOutput:
        return AiGatewayInferenceLogsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        token_id=data.get('token_id'),
        consumer=mapAiGatewayInferenceLogsGetOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        dialect=data.get('dialect'),
        operation=data.get('operation'),
        request_id=data.get('request_id'),
        requested_model=data.get('requested_model'),
        model=mapAiGatewayInferenceLogsGetOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        virtual_model=mapAiGatewayInferenceLogsGetOutputVirtualModel.from_dict(data.get('virtual_model')) if data.get('virtual_model') else None,
        metadata=data.get('metadata'),
        route=mapAiGatewayInferenceLogsGetOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        attempts=[mapAiGatewayInferenceLogsGetOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        status=data.get('status'),
        finish_reason=data.get('finish_reason'),
        error=mapAiGatewayInferenceLogsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        usage=mapAiGatewayInferenceLogsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        cost=mapAiGatewayInferenceLogsGetOutputCost.from_dict(data.get('cost')) if data.get('cost') else None,
        timing=mapAiGatewayInferenceLogsGetOutputTiming.from_dict(data.get('timing')) if data.get('timing') else None,
        request=mapAiGatewayInferenceLogsGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        has_content=data.get('has_content'),
        content=mapAiGatewayInferenceLogsGetOutputContent.from_dict(data.get('content')) if data.get('content') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayInferenceLogsGetQuery:
    include_content: Optional[bool] = None


class mapAiGatewayInferenceLogsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsGetQuery:
        return AiGatewayInferenceLogsGetQuery(
        include_content=data.get('include_content')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

