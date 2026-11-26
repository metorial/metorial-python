from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelsInsightsGetOutputRoutes:
    requests: float
    failed: float
    billed_usd: float
    input_tokens: float
    output_tokens: float
    rule_id: Optional[str] = None
    model: Optional[str] = None
    avg_total_ms: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsInsightsGetOutputDecision:
    calls: float
    cached: float
    failed: float
    cost_usd: float
    avg_latency_ms: Optional[float] = None
@dataclass
class AiGatewayVirtualModelsInsightsGetOutputSavings:
    baseline_model: str
    baseline_usd: float
    spent_usd: float
    saved_usd: float
    priced: bool
@dataclass
class AiGatewayVirtualModelsInsightsGetOutput:
    object: str
    since: datetime
    days: float
    routes: List[AiGatewayVirtualModelsInsightsGetOutputRoutes]
    decision: AiGatewayVirtualModelsInsightsGetOutputDecision
    billed_usd: float
    savings: Optional[AiGatewayVirtualModelsInsightsGetOutputSavings] = None


class mapAiGatewayVirtualModelsInsightsGetOutputRoutes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsInsightsGetOutputRoutes:
        return AiGatewayVirtualModelsInsightsGetOutputRoutes(
        rule_id=data.get('rule_id'),
        model=data.get('model'),
        requests=data.get('requests'),
        failed=data.get('failed'),
        billed_usd=data.get('billed_usd'),
        input_tokens=data.get('input_tokens'),
        output_tokens=data.get('output_tokens'),
        avg_total_ms=data.get('avg_total_ms')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsInsightsGetOutputRoutes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsInsightsGetOutputDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsInsightsGetOutputDecision:
        return AiGatewayVirtualModelsInsightsGetOutputDecision(
        calls=data.get('calls'),
        cached=data.get('cached'),
        failed=data.get('failed'),
        cost_usd=data.get('cost_usd'),
        avg_latency_ms=data.get('avg_latency_ms')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsInsightsGetOutputDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsInsightsGetOutputSavings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsInsightsGetOutputSavings:
        return AiGatewayVirtualModelsInsightsGetOutputSavings(
        baseline_model=data.get('baseline_model'),
        baseline_usd=data.get('baseline_usd'),
        spent_usd=data.get('spent_usd'),
        saved_usd=data.get('saved_usd'),
        priced=data.get('priced')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsInsightsGetOutputSavings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelsInsightsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsInsightsGetOutput:
        return AiGatewayVirtualModelsInsightsGetOutput(
        object=data.get('object'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None,
        days=data.get('days'),
        routes=[mapAiGatewayVirtualModelsInsightsGetOutputRoutes.from_dict(item) for item in data.get('routes', []) if item],
        decision=mapAiGatewayVirtualModelsInsightsGetOutputDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        billed_usd=data.get('billed_usd'),
        savings=mapAiGatewayVirtualModelsInsightsGetOutputSavings.from_dict(data.get('savings')) if data.get('savings') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsInsightsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayVirtualModelsInsightsGetQuery:
    days: Optional[float] = None
    baseline_model: Optional[str] = None


class mapAiGatewayVirtualModelsInsightsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelsInsightsGetQuery:
        return AiGatewayVirtualModelsInsightsGetQuery(
        days=data.get('days'),
        baseline_model=data.get('baseline_model')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelsInsightsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

