from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsModel:
    slug: str
    lab_slug: str
    id: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
    model: str
    reason: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
    code: str
    message: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Any]] = None
    error: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel:
    id: str
    slug: str
    version_id: str
    version_number: float
    reason: str
    trace: List[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace]
    targets: List[str]
    skipped_targets: List[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets]
    rule_id: Optional[str] = None
    decision: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsRoute:
    provider: str
    connection_owner: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttempts:
    provider: str
    connection_owner: str
    started_at: datetime
    duration_ms: float
    outcome: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
    error: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageInput:
    total: float
    no_cache: float
    cache_read: float
    cache_write: float
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput:
    total: float
    text: float
    reasoning: float
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsage:
    input: DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageInput
    output: DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsCostComponents:
    input: float
    cache_read: float
    cache_write: float
    output: float
    reasoning: float
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsCost:
    currency: str
    priced: bool
    total_usd: float
    components: DashboardInstanceAiGatewayInferenceLogsListOutputItemsCostComponents
    pricing_source: str
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsTiming:
    received_at: datetime
    completed_at: datetime
    total_ms: float
    upstream_started_at: Optional[datetime] = None
    first_token_at: Optional[datetime] = None
    upstream_ms: Optional[float] = None
    time_to_first_token_ms: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsRequest:
    message_count: Optional[float] = None
    tool_count: Optional[float] = None
    max_output_tokens: Optional[float] = None
    user_agent: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItemsContent:
    request: Dict[str, Any]
    response: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputItems:
    object: str
    id: str
    token_id: str
    dialect: str
    operation: str
    requested_model: str
    metadata: Dict[str, str]
    attempts: List[DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttempts]
    status: str
    timing: DashboardInstanceAiGatewayInferenceLogsListOutputItemsTiming
    request: DashboardInstanceAiGatewayInferenceLogsListOutputItemsRequest
    has_content: bool
    expires_at: datetime
    created_at: datetime
    consumer: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsConsumer] = None
    request_id: Optional[str] = None
    model: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsModel] = None
    virtual_model: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel] = None
    route: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsRoute] = None
    finish_reason: Optional[str] = None
    error: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsError] = None
    usage: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsage] = None
    cost: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsCost] = None
    content: Optional[DashboardInstanceAiGatewayInferenceLogsListOutputItemsContent] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayInferenceLogsListOutput:
    object: str
    items: List[DashboardInstanceAiGatewayInferenceLogsListOutputItems]
    pagination: DashboardInstanceAiGatewayInferenceLogsListOutputPagination


class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsConsumer:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsModel:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsModel(
        id=data.get('id'),
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel(
        id=data.get('id'),
        slug=data.get('slug'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace.from_dict(item) for item in data.get('trace', []) if item],
        targets=data.get('targets', []),
        skipped_targets=[mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets.from_dict(item) for item in data.get('skipped_targets', []) if item],
        decision=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsRoute:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsRoute(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttempts:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttempts(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id'),
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        duration_ms=data.get('duration_ms'),
        outcome=data.get('outcome'),
        error=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsError:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageInput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageInput:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageInput(
        total=data.get('total'),
        no_cache=data.get('no_cache'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageInput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput(
        total=data.get('total'),
        text=data.get('text'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsage:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsage(
        input=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageInput.from_dict(data.get('input')) if data.get('input') else None,
        output=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput.from_dict(data.get('output')) if data.get('output') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsCostComponents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsCostComponents:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsCostComponents(
        input=data.get('input'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write'),
        output=data.get('output'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsCostComponents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsCost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsCost:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsCost(
        currency=data.get('currency'),
        priced=data.get('priced'),
        total_usd=data.get('total_usd'),
        components=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsCostComponents.from_dict(data.get('components')) if data.get('components') else None,
        pricing_source=data.get('pricing_source')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsCost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsTiming:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsTiming:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsTiming(
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        upstream_started_at=datetime.fromisoformat(data.get('upstream_started_at').replace('Z', '+00:00')) if data.get('upstream_started_at') else None,
        first_token_at=datetime.fromisoformat(data.get('first_token_at').replace('Z', '+00:00')) if data.get('first_token_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        total_ms=data.get('total_ms'),
        upstream_ms=data.get('upstream_ms'),
        time_to_first_token_ms=data.get('time_to_first_token_ms')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsTiming, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsRequest:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsRequest(
        message_count=data.get('message_count'),
        tool_count=data.get('tool_count'),
        max_output_tokens=data.get('max_output_tokens'),
        user_agent=data.get('user_agent')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsContent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItemsContent:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItemsContent(
        request=data.get('request'),
        response=data.get('response')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItemsContent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputItems:
        return DashboardInstanceAiGatewayInferenceLogsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        token_id=data.get('token_id'),
        consumer=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        dialect=data.get('dialect'),
        operation=data.get('operation'),
        request_id=data.get('request_id'),
        requested_model=data.get('requested_model'),
        model=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        virtual_model=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel.from_dict(data.get('virtual_model')) if data.get('virtual_model') else None,
        metadata=data.get('metadata'),
        route=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsRoute.from_dict(data.get('route')) if data.get('route') else None,
        attempts=[mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        status=data.get('status'),
        finish_reason=data.get('finish_reason'),
        error=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        usage=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        cost=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsCost.from_dict(data.get('cost')) if data.get('cost') else None,
        timing=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsTiming.from_dict(data.get('timing')) if data.get('timing') else None,
        request=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        has_content=data.get('has_content'),
        content=mapDashboardInstanceAiGatewayInferenceLogsListOutputItemsContent.from_dict(data.get('content')) if data.get('content') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutputPagination:
        return DashboardInstanceAiGatewayInferenceLogsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayInferenceLogsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListOutput:
        return DashboardInstanceAiGatewayInferenceLogsListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceAiGatewayInferenceLogsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAiGatewayInferenceLogsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayInferenceLogsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    token_id: Optional[str] = None
    consumer_id: Optional[str] = None
    model: Optional[str] = None
    virtual_model_id: Optional[str] = None
    status: Optional[str] = None


class mapDashboardInstanceAiGatewayInferenceLogsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayInferenceLogsListQuery:
        return DashboardInstanceAiGatewayInferenceLogsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        token_id=data.get('token_id'),
        consumer_id=data.get('consumer_id'),
        model=data.get('model'),
        virtual_model_id=data.get('virtual_model_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayInferenceLogsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

