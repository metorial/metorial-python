from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputModel:
    slug: str
    lab_slug: str
    id: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
    model: str
    reason: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
    code: str
    message: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Any]] = None
    error: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModel:
    id: str
    slug: str
    version_id: str
    version_number: float
    reason: str
    trace: List[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace]
    targets: List[str]
    skipped_targets: List[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets]
    rule_id: Optional[str] = None
    decision: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputRoute:
    provider: str
    connection_owner: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputAttemptsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputAttempts:
    provider: str
    connection_owner: str
    started_at: datetime
    duration_ms: float
    outcome: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
    error: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputAttemptsError] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputUsageInput:
    total: float
    no_cache: float
    cache_read: float
    cache_write: float
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputUsageOutput:
    total: float
    text: float
    reasoning: float
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputUsage:
    input: DashboardInstanceAiGatewayInferenceLogsGetOutputUsageInput
    output: DashboardInstanceAiGatewayInferenceLogsGetOutputUsageOutput
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputCostComponents:
    input: float
    cache_read: float
    cache_write: float
    output: float
    reasoning: float
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputCost:
    currency: str
    priced: bool
    total_usd: float
    components: DashboardInstanceAiGatewayInferenceLogsGetOutputCostComponents
    pricing_source: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputTiming:
    received_at: datetime
    completed_at: datetime
    total_ms: float
    upstream_started_at: Optional[datetime] = None
    first_token_at: Optional[datetime] = None
    upstream_ms: Optional[float] = None
    time_to_first_token_ms: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputRequest:
    message_count: Optional[float] = None
    tool_count: Optional[float] = None
    max_output_tokens: Optional[float] = None
    user_agent: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutputContent:
    request: Dict[str, Any]
    response: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetOutput:
    object: str
    id: str
    token_id: str
    dialect: str
    operation: str
    requested_model: str
    metadata: Dict[str, str]
    attempts: List[DashboardInstanceAiGatewayInferenceLogsGetOutputAttempts]
    status: str
    timing: DashboardInstanceAiGatewayInferenceLogsGetOutputTiming
    request: DashboardInstanceAiGatewayInferenceLogsGetOutputRequest
    has_content: bool
    expires_at: datetime
    created_at: datetime
    consumer: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputConsumer] = None
    request_id: Optional[str] = None
    model: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputModel] = None
    virtual_model: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModel] = None
    route: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputRoute] = None
    finish_reason: Optional[str] = None
    error: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputError] = None
    usage: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputUsage] = None
    cost: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputCost] = None
    content: Optional[DashboardInstanceAiGatewayInferenceLogsGetOutputContent] = None


class mapDashboardInstanceAiGatewayInferenceLogsGetOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputConsumer:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputModel:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputModel(
        id=data.get('id'),
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModel:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModel(
        id=data.get('id'),
        slug=data.get('slug'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelTrace.from_dict(item) for item in data.get('trace', []) if item],
        targets=data.get('targets', []),
        skipped_targets=[mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelSkippedTargets.from_dict(item) for item in data.get('skipped_targets', []) if item],
        decision=mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModelDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputRoute:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputRoute(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputAttemptsError:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputAttempts:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputAttempts(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id'),
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        duration_ms=data.get('duration_ms'),
        outcome=data.get('outcome'),
        error=mapDashboardInstanceAiGatewayInferenceLogsGetOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputError:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputUsageInput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputUsageInput:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputUsageInput(
        total=data.get('total'),
        no_cache=data.get('no_cache'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputUsageInput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputUsageOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputUsageOutput:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputUsageOutput(
        total=data.get('total'),
        text=data.get('text'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputUsageOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputUsage:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputUsage(
        input=mapDashboardInstanceAiGatewayInferenceLogsGetOutputUsageInput.from_dict(data.get('input')) if data.get('input') else None,
        output=mapDashboardInstanceAiGatewayInferenceLogsGetOutputUsageOutput.from_dict(data.get('output')) if data.get('output') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputCostComponents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputCostComponents:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputCostComponents(
        input=data.get('input'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write'),
        output=data.get('output'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputCostComponents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputCost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputCost:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputCost(
        currency=data.get('currency'),
        priced=data.get('priced'),
        total_usd=data.get('total_usd'),
        components=mapDashboardInstanceAiGatewayInferenceLogsGetOutputCostComponents.from_dict(data.get('components')) if data.get('components') else None,
        pricing_source=data.get('pricing_source')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputCost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputTiming:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputTiming:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputTiming(
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        upstream_started_at=datetime.fromisoformat(data.get('upstream_started_at').replace('Z', '+00:00')) if data.get('upstream_started_at') else None,
        first_token_at=datetime.fromisoformat(data.get('first_token_at').replace('Z', '+00:00')) if data.get('first_token_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        total_ms=data.get('total_ms'),
        upstream_ms=data.get('upstream_ms'),
        time_to_first_token_ms=data.get('time_to_first_token_ms')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputTiming, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputRequest:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputRequest(
        message_count=data.get('message_count'),
        tool_count=data.get('tool_count'),
        max_output_tokens=data.get('max_output_tokens'),
        user_agent=data.get('user_agent')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutputContent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutputContent:
        return DashboardInstanceAiGatewayInferenceLogsGetOutputContent(
        request=data.get('request'),
        response=data.get('response')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutputContent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetOutput:
        return DashboardInstanceAiGatewayInferenceLogsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        token_id=data.get('token_id'),
        consumer=mapDashboardInstanceAiGatewayInferenceLogsGetOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        dialect=data.get('dialect'),
        operation=data.get('operation'),
        request_id=data.get('request_id'),
        requested_model=data.get('requested_model'),
        model=mapDashboardInstanceAiGatewayInferenceLogsGetOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        virtual_model=mapDashboardInstanceAiGatewayInferenceLogsGetOutputVirtualModel.from_dict(data.get('virtual_model')) if data.get('virtual_model') else None,
        metadata=data.get('metadata'),
        route=mapDashboardInstanceAiGatewayInferenceLogsGetOutputRoute.from_dict(data.get('route')) if data.get('route') else None,
        attempts=[mapDashboardInstanceAiGatewayInferenceLogsGetOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        status=data.get('status'),
        finish_reason=data.get('finish_reason'),
        error=mapDashboardInstanceAiGatewayInferenceLogsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        usage=mapDashboardInstanceAiGatewayInferenceLogsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        cost=mapDashboardInstanceAiGatewayInferenceLogsGetOutputCost.from_dict(data.get('cost')) if data.get('cost') else None,
        timing=mapDashboardInstanceAiGatewayInferenceLogsGetOutputTiming.from_dict(data.get('timing')) if data.get('timing') else None,
        request=mapDashboardInstanceAiGatewayInferenceLogsGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        has_content=data.get('has_content'),
        content=mapDashboardInstanceAiGatewayInferenceLogsGetOutputContent.from_dict(data.get('content')) if data.get('content') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayInferenceLogsGetQuery:
    include_content: Optional[bool] = None


class mapDashboardInstanceAiGatewayInferenceLogsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsGetQuery:
        return DashboardInstanceAiGatewayInferenceLogsGetQuery(
        include_content=data.get('include_content')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

