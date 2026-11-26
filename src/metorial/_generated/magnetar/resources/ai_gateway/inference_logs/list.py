from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayInferenceLogsListOutputItemsConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class AiGatewayInferenceLogsListOutputItemsModel:
    slug: str
    lab_slug: str
    id: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
    rule_id: str
    outcome: str
    error: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
    model: str
    reason: str
@dataclass
class AiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
    code: str
    message: str
@dataclass
class AiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
    model: str
    cached: bool
    latency_ms: float
    input_tokens: float
    cost_usd: float
    source: Optional[str] = None
    signals: Optional[Dict[str, Any]] = None
    error: Optional[AiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsVirtualModel:
    id: str
    slug: str
    version_id: str
    version_number: float
    reason: str
    trace: List[AiGatewayInferenceLogsListOutputItemsVirtualModelTrace]
    targets: List[str]
    skipped_targets: List[AiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets]
    rule_id: Optional[str] = None
    decision: Optional[AiGatewayInferenceLogsListOutputItemsVirtualModelDecision] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsRoute:
    provider: str
    connection_owner: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsAttemptsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsAttempts:
    provider: str
    connection_owner: str
    started_at: datetime
    duration_ms: float
    outcome: str
    connection_id: Optional[str] = None
    vendor_model_id: Optional[str] = None
    error: Optional[AiGatewayInferenceLogsListOutputItemsAttemptsError] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsError:
    code: str
    message: str
    stage: Optional[str] = None
    param: Optional[str] = None
    http_status: Optional[float] = None
    provider_code: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsUsageInput:
    total: float
    no_cache: float
    cache_read: float
    cache_write: float
@dataclass
class AiGatewayInferenceLogsListOutputItemsUsageOutput:
    total: float
    text: float
    reasoning: float
@dataclass
class AiGatewayInferenceLogsListOutputItemsUsage:
    input: AiGatewayInferenceLogsListOutputItemsUsageInput
    output: AiGatewayInferenceLogsListOutputItemsUsageOutput
@dataclass
class AiGatewayInferenceLogsListOutputItemsCostComponents:
    input: float
    cache_read: float
    cache_write: float
    output: float
    reasoning: float
@dataclass
class AiGatewayInferenceLogsListOutputItemsCost:
    currency: str
    priced: bool
    total_usd: float
    components: AiGatewayInferenceLogsListOutputItemsCostComponents
    pricing_source: str
@dataclass
class AiGatewayInferenceLogsListOutputItemsTiming:
    received_at: datetime
    completed_at: datetime
    total_ms: float
    upstream_started_at: Optional[datetime] = None
    first_token_at: Optional[datetime] = None
    upstream_ms: Optional[float] = None
    time_to_first_token_ms: Optional[float] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsRequest:
    message_count: Optional[float] = None
    tool_count: Optional[float] = None
    max_output_tokens: Optional[float] = None
    user_agent: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsListOutputItemsContent:
    request: Dict[str, Any]
    response: Optional[Dict[str, Any]] = None
@dataclass
class AiGatewayInferenceLogsListOutputItems:
    object: str
    id: str
    token_id: str
    dialect: str
    operation: str
    requested_model: str
    metadata: Dict[str, str]
    attempts: List[AiGatewayInferenceLogsListOutputItemsAttempts]
    status: str
    timing: AiGatewayInferenceLogsListOutputItemsTiming
    request: AiGatewayInferenceLogsListOutputItemsRequest
    has_content: bool
    expires_at: datetime
    created_at: datetime
    consumer: Optional[AiGatewayInferenceLogsListOutputItemsConsumer] = None
    request_id: Optional[str] = None
    model: Optional[AiGatewayInferenceLogsListOutputItemsModel] = None
    virtual_model: Optional[AiGatewayInferenceLogsListOutputItemsVirtualModel] = None
    route: Optional[AiGatewayInferenceLogsListOutputItemsRoute] = None
    finish_reason: Optional[str] = None
    error: Optional[AiGatewayInferenceLogsListOutputItemsError] = None
    usage: Optional[AiGatewayInferenceLogsListOutputItemsUsage] = None
    cost: Optional[AiGatewayInferenceLogsListOutputItemsCost] = None
    content: Optional[AiGatewayInferenceLogsListOutputItemsContent] = None
@dataclass
class AiGatewayInferenceLogsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class AiGatewayInferenceLogsListOutput:
    object: str
    items: List[AiGatewayInferenceLogsListOutputItems]
    pagination: AiGatewayInferenceLogsListOutputPagination


class mapAiGatewayInferenceLogsListOutputItemsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsConsumer:
        return AiGatewayInferenceLogsListOutputItemsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsModel:
        return AiGatewayInferenceLogsListOutputItemsModel(
        id=data.get('id'),
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsVirtualModelTrace:
        return AiGatewayInferenceLogsListOutputItemsVirtualModelTrace(
        rule_id=data.get('rule_id'),
        outcome=data.get('outcome'),
        error=data.get('error')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsVirtualModelTrace, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets:
        return AiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets(
        model=data.get('model'),
        reason=data.get('reason')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError:
        return AiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsVirtualModelDecision:
        return AiGatewayInferenceLogsListOutputItemsVirtualModelDecision(
        model=data.get('model'),
        source=data.get('source'),
        cached=data.get('cached'),
        latency_ms=data.get('latency_ms'),
        input_tokens=data.get('input_tokens'),
        cost_usd=data.get('cost_usd'),
        signals=data.get('signals'),
        error=mapAiGatewayInferenceLogsListOutputItemsVirtualModelDecisionError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsVirtualModelDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsVirtualModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsVirtualModel:
        return AiGatewayInferenceLogsListOutputItemsVirtualModel(
        id=data.get('id'),
        slug=data.get('slug'),
        version_id=data.get('version_id'),
        version_number=data.get('version_number'),
        rule_id=data.get('rule_id'),
        reason=data.get('reason'),
        trace=[mapAiGatewayInferenceLogsListOutputItemsVirtualModelTrace.from_dict(item) for item in data.get('trace', []) if item],
        targets=data.get('targets', []),
        skipped_targets=[mapAiGatewayInferenceLogsListOutputItemsVirtualModelSkippedTargets.from_dict(item) for item in data.get('skipped_targets', []) if item],
        decision=mapAiGatewayInferenceLogsListOutputItemsVirtualModelDecision.from_dict(data.get('decision')) if data.get('decision') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsVirtualModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsRoute:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsRoute:
        return AiGatewayInferenceLogsListOutputItemsRoute(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsRoute, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsAttemptsError:
        return AiGatewayInferenceLogsListOutputItemsAttemptsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsAttempts:
        return AiGatewayInferenceLogsListOutputItemsAttempts(
        provider=data.get('provider'),
        connection_owner=data.get('connection_owner'),
        connection_id=data.get('connection_id'),
        vendor_model_id=data.get('vendor_model_id'),
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        duration_ms=data.get('duration_ms'),
        outcome=data.get('outcome'),
        error=mapAiGatewayInferenceLogsListOutputItemsAttemptsError.from_dict(data.get('error')) if data.get('error') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsError:
        return AiGatewayInferenceLogsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message'),
        stage=data.get('stage'),
        param=data.get('param'),
        http_status=data.get('http_status'),
        provider_code=data.get('provider_code')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsUsageInput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsUsageInput:
        return AiGatewayInferenceLogsListOutputItemsUsageInput(
        total=data.get('total'),
        no_cache=data.get('no_cache'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsUsageInput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsUsageOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsUsageOutput:
        return AiGatewayInferenceLogsListOutputItemsUsageOutput(
        total=data.get('total'),
        text=data.get('text'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsUsageOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsUsage:
        return AiGatewayInferenceLogsListOutputItemsUsage(
        input=mapAiGatewayInferenceLogsListOutputItemsUsageInput.from_dict(data.get('input')) if data.get('input') else None,
        output=mapAiGatewayInferenceLogsListOutputItemsUsageOutput.from_dict(data.get('output')) if data.get('output') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsCostComponents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsCostComponents:
        return AiGatewayInferenceLogsListOutputItemsCostComponents(
        input=data.get('input'),
        cache_read=data.get('cache_read'),
        cache_write=data.get('cache_write'),
        output=data.get('output'),
        reasoning=data.get('reasoning')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsCostComponents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsCost:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsCost:
        return AiGatewayInferenceLogsListOutputItemsCost(
        currency=data.get('currency'),
        priced=data.get('priced'),
        total_usd=data.get('total_usd'),
        components=mapAiGatewayInferenceLogsListOutputItemsCostComponents.from_dict(data.get('components')) if data.get('components') else None,
        pricing_source=data.get('pricing_source')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsCost, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsTiming:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsTiming:
        return AiGatewayInferenceLogsListOutputItemsTiming(
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None,
        upstream_started_at=datetime.fromisoformat(data.get('upstream_started_at').replace('Z', '+00:00')) if data.get('upstream_started_at') else None,
        first_token_at=datetime.fromisoformat(data.get('first_token_at').replace('Z', '+00:00')) if data.get('first_token_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        total_ms=data.get('total_ms'),
        upstream_ms=data.get('upstream_ms'),
        time_to_first_token_ms=data.get('time_to_first_token_ms')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsTiming, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsRequest:
        return AiGatewayInferenceLogsListOutputItemsRequest(
        message_count=data.get('message_count'),
        tool_count=data.get('tool_count'),
        max_output_tokens=data.get('max_output_tokens'),
        user_agent=data.get('user_agent')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItemsContent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItemsContent:
        return AiGatewayInferenceLogsListOutputItemsContent(
        request=data.get('request'),
        response=data.get('response')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItemsContent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputItems:
        return AiGatewayInferenceLogsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        token_id=data.get('token_id'),
        consumer=mapAiGatewayInferenceLogsListOutputItemsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        dialect=data.get('dialect'),
        operation=data.get('operation'),
        request_id=data.get('request_id'),
        requested_model=data.get('requested_model'),
        model=mapAiGatewayInferenceLogsListOutputItemsModel.from_dict(data.get('model')) if data.get('model') else None,
        virtual_model=mapAiGatewayInferenceLogsListOutputItemsVirtualModel.from_dict(data.get('virtual_model')) if data.get('virtual_model') else None,
        metadata=data.get('metadata'),
        route=mapAiGatewayInferenceLogsListOutputItemsRoute.from_dict(data.get('route')) if data.get('route') else None,
        attempts=[mapAiGatewayInferenceLogsListOutputItemsAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        status=data.get('status'),
        finish_reason=data.get('finish_reason'),
        error=mapAiGatewayInferenceLogsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        usage=mapAiGatewayInferenceLogsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        cost=mapAiGatewayInferenceLogsListOutputItemsCost.from_dict(data.get('cost')) if data.get('cost') else None,
        timing=mapAiGatewayInferenceLogsListOutputItemsTiming.from_dict(data.get('timing')) if data.get('timing') else None,
        request=mapAiGatewayInferenceLogsListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        has_content=data.get('has_content'),
        content=mapAiGatewayInferenceLogsListOutputItemsContent.from_dict(data.get('content')) if data.get('content') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutputPagination:
        return AiGatewayInferenceLogsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayInferenceLogsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListOutput:
        return AiGatewayInferenceLogsListOutput(
        object=data.get('object'),
        items=[mapAiGatewayInferenceLogsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAiGatewayInferenceLogsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayInferenceLogsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayInferenceLogsListQuery:
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


class mapAiGatewayInferenceLogsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayInferenceLogsListQuery:
        return AiGatewayInferenceLogsListQuery(
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
    def to_dict(value: Union[AiGatewayInferenceLogsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

