from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayTokensRevokeOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class DashboardInstanceAiGatewayTokensRevokeOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class DashboardInstanceAiGatewayTokensRevokeOutput:
    object: str
    id: str
    name: str
    prefix: str
    allowed_models: List[str]
    limits: List[DashboardInstanceAiGatewayTokensRevokeOutputLimits]
    metadata: Dict[str, str]
    created_at: datetime
    secret: Optional[str] = None
    consumer: Optional[DashboardInstanceAiGatewayTokensRevokeOutputConsumer] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapDashboardInstanceAiGatewayTokensRevokeOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensRevokeOutputConsumer:
        return DashboardInstanceAiGatewayTokensRevokeOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensRevokeOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayTokensRevokeOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensRevokeOutputLimits:
        return DashboardInstanceAiGatewayTokensRevokeOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensRevokeOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayTokensRevokeOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensRevokeOutput:
        return DashboardInstanceAiGatewayTokensRevokeOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        prefix=data.get('prefix'),
        secret=data.get('secret'),
        consumer=mapDashboardInstanceAiGatewayTokensRevokeOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        allowed_models=data.get('allowed_models', []),
        limits=[mapDashboardInstanceAiGatewayTokensRevokeOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensRevokeOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

