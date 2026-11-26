from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayUsageTimelineOutputBuckets:
    start: datetime
    requests: float
    succeeded: float
    failed: float
    cancelled: float
    rejected: float
    input_tokens: float
    cached_input_tokens: float
    output_tokens: float
    cost_usd: float
    metorial_cost_usd: float
    average_latency_ms: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayUsageTimelineOutput:
    object: str
    interval: str
    from_: datetime
    to: datetime
    buckets: List[DashboardInstanceAiGatewayUsageTimelineOutputBuckets]


class mapDashboardInstanceAiGatewayUsageTimelineOutputBuckets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayUsageTimelineOutputBuckets:
        return DashboardInstanceAiGatewayUsageTimelineOutputBuckets(
        start=datetime.fromisoformat(data.get('start').replace('Z', '+00:00')) if data.get('start') else None,
        requests=data.get('requests'),
        succeeded=data.get('succeeded'),
        failed=data.get('failed'),
        cancelled=data.get('cancelled'),
        rejected=data.get('rejected'),
        input_tokens=data.get('input_tokens'),
        cached_input_tokens=data.get('cached_input_tokens'),
        output_tokens=data.get('output_tokens'),
        cost_usd=data.get('cost_usd'),
        metorial_cost_usd=data.get('metorial_cost_usd'),
        average_latency_ms=data.get('average_latency_ms')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayUsageTimelineOutputBuckets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayUsageTimelineOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayUsageTimelineOutput:
        return DashboardInstanceAiGatewayUsageTimelineOutput(
        object=data.get('object'),
        interval=data.get('interval'),
        from_=datetime.fromisoformat(data.get('from').replace('Z', '+00:00')) if data.get('from') else None,
        to=datetime.fromisoformat(data.get('to').replace('Z', '+00:00')) if data.get('to') else None,
        buckets=[mapDashboardInstanceAiGatewayUsageTimelineOutputBuckets.from_dict(item) for item in data.get('buckets', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayUsageTimelineOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayUsageTimelineQuery:
    from_: datetime
    to: datetime
    interval: Optional[str] = None
    token_id: Optional[str] = None
    consumer_id: Optional[str] = None
    model: Optional[str] = None
    virtual_model_id: Optional[str] = None


class mapDashboardInstanceAiGatewayUsageTimelineQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayUsageTimelineQuery:
        return DashboardInstanceAiGatewayUsageTimelineQuery(
        from_=datetime.fromisoformat(data.get('from').replace('Z', '+00:00')) if data.get('from') else None,
        to=datetime.fromisoformat(data.get('to').replace('Z', '+00:00')) if data.get('to') else None,
        interval=data.get('interval'),
        token_id=data.get('token_id'),
        consumer_id=data.get('consumer_id'),
        model=data.get('model'),
        virtual_model_id=data.get('virtual_model_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayUsageTimelineQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

