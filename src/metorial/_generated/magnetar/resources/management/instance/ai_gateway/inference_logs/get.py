from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputModel:
    slug: str
    lab_slug: str
    id: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
    model: str
    reason: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
    code: str
    message: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Any]] = None
    error: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModel:
    id: str
    slug: str
    version_id: str
    version_number: float
    reason: str
    trace: List[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace]
    targets: List[str]
    skipped_targets: List[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets]
    rule_id: Optional[str] = None
    decision: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputRoute:
    provider: str
    connection_owner: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputAttemptsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputAttempts:
    provider: str
    connection_owner: str
    started_at: datetime
    duration_ms: float
    outcome: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
    error: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputAttemptsError] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputUsageInput:
    total: float
    no_cache: float
    cache_read: float
    cache_write: float
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputUsageOutput:
    total: float
    text: float
    reasoning: float
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputUsage:
    input: ManagementInstanceAiGatewayInferenceLogsGetOutputUsageInput
    output: ManagementInstanceAiGatewayInferenceLogsGetOutputUsageOutput
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputCostComponents:
    input: float
    cache_read: float
    cache_write: float
    output: float
    reasoning: float
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputCost:
    currency: str
    priced: bool
    total_usd: float
    components: ManagementInstanceAiGatewayInferenceLogsGetOutputCostComponents
    pricing_source: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputTiming:
    received_at: datetime
    completed_at: datetime
    total_ms: float
    upstream_started_at: Optional[datetime] = None
    first_token_at: Optional[datetime] = None
    upstream_ms: Optional[float] = None
    time_to_first_token_ms: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputRequest:
    message_count: Optional[float] = None
    tool_count: Optional[float] = None
    max_output_tokens: Optional[float] = None
    user_agent: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutputContent:
    request: Dict[str, Any]
    response: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetOutput:
    object: str
    id: str
    token_id: str
    dialect: str
    operation: str
    requested_model: str
    metadata: Dict[str, str]
    attempts: List[ManagementInstanceAiGatewayInferenceLogsGetOutputAttempts]
    status: str
    timing: ManagementInstanceAiGatewayInferenceLogsGetOutputTiming
    request: ManagementInstanceAiGatewayInferenceLogsGetOutputRequest
    has_content: bool
    expires_at: datetime
    created_at: datetime
    consumer: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputConsumer] = None
    request_id: Optional[str] = None
    model: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputModel] = None
    virtual_model: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModel] = None
    route: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputRoute] = None
    finish_reason: Optional[str] = None
    error: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputError] = None
    usage: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputUsage] = None
    cost: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputCost] = None
    content: Optional[ManagementInstanceAiGatewayInferenceLogsGetOutputContent] = None


class mapManagementInstanceAiGatewayInferenceLogsGetOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputConsumer:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputModel:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputModel(
        id=data.get('id'),
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModel:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModel(
        id=data.get('id'),
        slug=data.get('slug'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace.from_dict(item) for item in data.get('trace', []) if item],
        targets=data.get('targets', []),
        skipped_targets=[mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets.from_dict(item) for item in data.get('skipped_targets', []) if item],
        decision=mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputRoute:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputRoute(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputAttemptsError:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputAttempts:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputAttempts(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id'),
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        duration_ms=data.get('duration_ms'),
        outcome=data.get('outcome'),
        error=mapManagementInstanceAiGatewayInferenceLogsGetOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputError:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputUsageInput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputUsageInput:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputUsageInput(
        total=data.get('total'),
        no_cache=data.get('no_cache'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputUsageInput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputUsageOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputUsageOutput:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputUsageOutput(
        total=data.get('total'),
        text=data.get('text'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputUsageOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputUsage:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputUsage(
        input=mapManagementInstanceAiGatewayInferenceLogsGetOutputUsageInput.from_dict(data.get('input')) if data.get('input') else None,
        output=mapManagementInstanceAiGatewayInferenceLogsGetOutputUsageOutput.from_dict(data.get('output')) if data.get('output') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputCostComponents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputCostComponents:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputCostComponents(
        input=data.get('input'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write'),
        output=data.get('output'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputCostComponents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputCost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputCost:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputCost(
        currency=data.get('currency'),
        priced=data.get('priced'),
        total_usd=data.get('total_usd'),
        components=mapManagementInstanceAiGatewayInferenceLogsGetOutputCostComponents.from_dict(data.get('components')) if data.get('components') else None,
        pricing_source=data.get('pricing_source')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputCost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputTiming:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputTiming:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputTiming(
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        upstream_started_at=datetime.fromisoformat(data.get('upstream_started_at').replace('Z', '+00:00')) if data.get('upstream_started_at') else None,
        first_token_at=datetime.fromisoformat(data.get('first_token_at').replace('Z', '+00:00')) if data.get('first_token_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        total_ms=data.get('total_ms'),
        upstream_ms=data.get('upstream_ms'),
        time_to_first_token_ms=data.get('time_to_first_token_ms')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputTiming, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputRequest:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputRequest(
        message_count=data.get('message_count'),
        tool_count=data.get('tool_count'),
        max_output_tokens=data.get('max_output_tokens'),
        user_agent=data.get('user_agent')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutputContent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutputContent:
        return ManagementInstanceAiGatewayInferenceLogsGetOutputContent(
        request=data.get('request'),
        response=data.get('response')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutputContent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetOutput:
        return ManagementInstanceAiGatewayInferenceLogsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        token_id=data.get('token_id'),
        consumer=mapManagementInstanceAiGatewayInferenceLogsGetOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        dialect=data.get('dialect'),
        operation=data.get('operation'),
        request_id=data.get('request_id'),
        requested_model=data.get('requested_model'),
        model=mapManagementInstanceAiGatewayInferenceLogsGetOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        virtual_model=mapManagementInstanceAiGatewayInferenceLogsGetOutputVirtualModel.from_dict(data.get('virtual_model')) if data.get('virtual_model') else None,
        metadata=data.get('metadata'),
        route=mapManagementInstanceAiGatewayInferenceLogsGetOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        attempts=[mapManagementInstanceAiGatewayInferenceLogsGetOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        status=data.get('status'),
        finish_reason=data.get('finish_reason'),
        error=mapManagementInstanceAiGatewayInferenceLogsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        usage=mapManagementInstanceAiGatewayInferenceLogsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        cost=mapManagementInstanceAiGatewayInferenceLogsGetOutputCost.from_dict(data.get('cost')) if data.get('cost') else None,
        timing=mapManagementInstanceAiGatewayInferenceLogsGetOutputTiming.from_dict(data.get('timing')) if data.get('timing') else None,
        request=mapManagementInstanceAiGatewayInferenceLogsGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        has_content=data.get('has_content'),
        content=mapManagementInstanceAiGatewayInferenceLogsGetOutputContent.from_dict(data.get('content')) if data.get('content') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayInferenceLogsGetQuery:
    include_content: Optional[bool] = None


class mapManagementInstanceAiGatewayInferenceLogsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsGetQuery:
        return ManagementInstanceAiGatewayInferenceLogsGetQuery(
        include_content=data.get('include_content')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

