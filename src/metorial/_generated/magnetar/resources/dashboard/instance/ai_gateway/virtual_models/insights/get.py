from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputRoutes:
    requests: float
    failed: float
    billed_usd: float
    input_tokens: float
    output_tokens: float
    rule_id: Optional[str] = None
    model: Optional[str] = None
    avg_total_ms: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputDecision:
    calls: float
    cached: float
    failed: float
    cost_usd: float
    avg_latency_ms: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputSavings:
    baseline_model: str
    baseline_usd: float
    spent_usd: float
    saved_usd: float
    priced: bool
@dataclass
class DashboardInstanceAiGatewayVirtualModelsInsightsGetOutput:
    object: str
    since: datetime
    days: float
    routes: List[DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputRoutes]
    decision: DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputDecision
    billed_usd: float
    savings: Optional[DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputSavings] = None


class mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutputRoutes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputRoutes:
        return DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputRoutes(
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
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputRoutes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutputDecision:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputDecision:
        return DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputDecision(
        calls=data.get('calls'),
        cached=data.get('cached'),
        failed=data.get('failed'),
        cost_usd=data.get('cost_usd'),
        avg_latency_ms=data.get('avg_latency_ms')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputDecision, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutputSavings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputSavings:
        return DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputSavings(
        baseline_model=data.get('baseline_model'),
        baseline_usd=data.get('baseline_usd'),
        spent_usd=data.get('spent_usd'),
        saved_usd=data.get('saved_usd'),
        priced=data.get('priced')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsInsightsGetOutputSavings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsInsightsGetOutput:
        return DashboardInstanceAiGatewayVirtualModelsInsightsGetOutput(
        object=data.get('object'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None,
        days=data.get('days'),
        routes=[mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutputRoutes.from_dict(item) for item in data.get('routes', []) if item],
        decision=mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutputDecision.from_dict(data.get('decision')) if data.get('decision') else None,
        billed_usd=data.get('billed_usd'),
        savings=mapDashboardInstanceAiGatewayVirtualModelsInsightsGetOutputSavings.from_dict(data.get('savings')) if data.get('savings') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsInsightsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayVirtualModelsInsightsGetQuery:
    days: Optional[float] = None
    baseline_model: Optional[str] = None


class mapDashboardInstanceAiGatewayVirtualModelsInsightsGetQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelsInsightsGetQuery:
        return DashboardInstanceAiGatewayVirtualModelsInsightsGetQuery(
        days=data.get('days'),
        baseline_model=data.get('baseline_model')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelsInsightsGetQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

