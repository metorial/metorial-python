from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsModel:
    slug: str
    lab_slug: str
    id: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
    model: str
    reason: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
    code: str
    message: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Any]] = None
    error: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel:
    id: str
    slug: str
    version_id: str
    version_number: float
    reason: str
    trace: List[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace]
    targets: List[str]
    skipped_targets: List[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets]
    rule_id: Optional[str] = None
    decision: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsRoute:
    provider: str
    connection_owner: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttempts:
    provider: str
    connection_owner: str
    started_at: datetime
    duration_ms: float
    outcome: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
    error: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageInput:
    total: float
    no_cache: float
    cache_read: float
    cache_write: float
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput:
    total: float
    text: float
    reasoning: float
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsage:
    input: ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageInput
    output: ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsCostComponents:
    input: float
    cache_read: float
    cache_write: float
    output: float
    reasoning: float
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsCost:
    currency: str
    priced: bool
    total_usd: float
    components: ManagementInstanceAiGatewayInferenceLogsListOutputItemsCostComponents
    pricing_source: str
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsTiming:
    received_at: datetime
    completed_at: datetime
    total_ms: float
    upstream_started_at: Optional[datetime] = None
    first_token_at: Optional[datetime] = None
    upstream_ms: Optional[float] = None
    time_to_first_token_ms: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsRequest:
    message_count: Optional[float] = None
    tool_count: Optional[float] = None
    max_output_tokens: Optional[float] = None
    user_agent: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItemsContent:
    request: Dict[str, Any]
    response: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputItems:
    object: str
    id: str
    token_id: str
    dialect: str
    operation: str
    requested_model: str
    metadata: Dict[str, str]
    attempts: List[ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttempts]
    status: str
    timing: ManagementInstanceAiGatewayInferenceLogsListOutputItemsTiming
    request: ManagementInstanceAiGatewayInferenceLogsListOutputItemsRequest
    has_content: bool
    expires_at: datetime
    created_at: datetime
    consumer: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsConsumer] = None
    request_id: Optional[str] = None
    model: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsModel] = None
    virtual_model: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel] = None
    route: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsRoute] = None
    finish_reason: Optional[str] = None
    error: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsError] = None
    usage: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsage] = None
    cost: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsCost] = None
    content: Optional[ManagementInstanceAiGatewayInferenceLogsListOutputItemsContent] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayInferenceLogsListOutput:
    object: str
    items: List[ManagementInstanceAiGatewayInferenceLogsListOutputItems]
    pagination: ManagementInstanceAiGatewayInferenceLogsListOutputPagination


class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsConsumer:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsModel:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsModel(
        id=data.get('id'),
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel(
        id=data.get('id'),
        slug=data.get('slug'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelTrace.from_dict(item) for item in data.get('trace', []) if item],
        targets=data.get('targets', []),
        skipped_targets=[mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets.from_dict(item) for item in data.get('skipped_targets', []) if item],
        decision=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModelDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsRoute:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsRoute(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttempts:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttempts(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id'),
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        duration_ms=data.get('duration_ms'),
        outcome=data.get('outcome'),
        error=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsAttemptsError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsError:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageInput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageInput:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageInput(
        total=data.get('total'),
        no_cache=data.get('no_cache'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageInput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput(
        total=data.get('total'),
        text=data.get('text'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsage:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsage(
        input=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageInput.from_dict(data.get('input')) if data.get('input') else None,
        output=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsUsageOutput.from_dict(data.get('output')) if data.get('output') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsCostComponents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsCostComponents:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsCostComponents(
        input=data.get('input'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write'),
        output=data.get('output'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsCostComponents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsCost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsCost:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsCost(
        currency=data.get('currency'),
        priced=data.get('priced'),
        total_usd=data.get('total_usd'),
        components=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsCostComponents.from_dict(data.get('components')) if data.get('components') else None,
        pricing_source=data.get('pricing_source')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsCost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsTiming:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsTiming:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsTiming(
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        upstream_started_at=datetime.fromisoformat(data.get('upstream_started_at').replace('Z', '+00:00')) if data.get('upstream_started_at') else None,
        first_token_at=datetime.fromisoformat(data.get('first_token_at').replace('Z', '+00:00')) if data.get('first_token_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        total_ms=data.get('total_ms'),
        upstream_ms=data.get('upstream_ms'),
        time_to_first_token_ms=data.get('time_to_first_token_ms')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsTiming, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsRequest:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsRequest(
        message_count=data.get('message_count'),
        tool_count=data.get('tool_count'),
        max_output_tokens=data.get('max_output_tokens'),
        user_agent=data.get('user_agent')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItemsContent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItemsContent:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItemsContent(
        request=data.get('request'),
        response=data.get('response')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItemsContent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputItems:
        return ManagementInstanceAiGatewayInferenceLogsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        token_id=data.get('token_id'),
        consumer=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        dialect=data.get('dialect'),
        operation=data.get('operation'),
        request_id=data.get('request_id'),
        requested_model=data.get('requested_model'),
        model=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        virtual_model=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsVirtualModel.from_dict(data.get('virtual_model')) if data.get('virtual_model') else None,
        metadata=data.get('metadata'),
        route=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsRoute.from_dict(data.get('route')) if data.get('route') else None,
        attempts=[mapManagementInstanceAiGatewayInferenceLogsListOutputItemsAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        status=data.get('status'),
        finish_reason=data.get('finish_reason'),
        error=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        usage=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        cost=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsCost.from_dict(data.get('cost')) if data.get('cost') else None,
        timing=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsTiming.from_dict(data.get('timing')) if data.get('timing') else None,
        request=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        has_content=data.get('has_content'),
        content=mapManagementInstanceAiGatewayInferenceLogsListOutputItemsContent.from_dict(data.get('content')) if data.get('content') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutputPagination:
        return ManagementInstanceAiGatewayInferenceLogsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayInferenceLogsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListOutput:
        return ManagementInstanceAiGatewayInferenceLogsListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceAiGatewayInferenceLogsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAiGatewayInferenceLogsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayInferenceLogsListQuery:
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


class mapManagementInstanceAiGatewayInferenceLogsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayInferenceLogsListQuery:
        return ManagementInstanceAiGatewayInferenceLogsListQuery(
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
    def to_dict(value: Union[ManagementInstanceAiGatewayInferenceLogsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

