from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayTokensCreateOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class AiGatewayTokensCreateOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class AiGatewayTokensCreateOutput:
    object: str
    id: str
    name: str
    prefix: str
    allowed_models: List[str]
    limits: List[AiGatewayTokensCreateOutputLimits]
    metadata: Dict[str, str]
    created_at: datetime
    secret: Optional[str] = None
    consumer: Optional[AiGatewayTokensCreateOutputConsumer] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapAiGatewayTokensCreateOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensCreateOutputConsumer:
        return AiGatewayTokensCreateOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensCreateOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayTokensCreateOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensCreateOutputLimits:
        return AiGatewayTokensCreateOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensCreateOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayTokensCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensCreateOutput:
        return AiGatewayTokensCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        prefix=data.get('prefix'),
        secret=data.get('secret'),
        consumer=mapAiGatewayTokensCreateOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        allowed_models=data.get('allowed_models', []),
        limits=[mapAiGatewayTokensCreateOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayTokensCreateBodyLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class AiGatewayTokensCreateBody:
    name: str
    consumer_id: Optional[str] = None
    allowed_models: Optional[List[str]] = None
    limits: Optional[List[AiGatewayTokensCreateBodyLimits]] = None
    metadata: Optional[Dict[str, str]] = None
    expires_at: Optional[datetime] = None


class mapAiGatewayTokensCreateBodyLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensCreateBodyLimits:
        return AiGatewayTokensCreateBodyLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensCreateBodyLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayTokensCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensCreateBody:
        return AiGatewayTokensCreateBody(
        name=data.get('name'),
        consumer_id=data.get('consumer_id'),
        allowed_models=data.get('allowed_models', []),
        limits=[mapAiGatewayTokensCreateBodyLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

