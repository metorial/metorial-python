from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayTokensUpdateOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class AiGatewayTokensUpdateOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class AiGatewayTokensUpdateOutput:
    object: str
    id: str
    name: str
    prefix: str
    allowed_models: List[str]
    limits: List[AiGatewayTokensUpdateOutputLimits]
    metadata: Dict[str, str]
    created_at: datetime
    secret: Optional[str] = None
    consumer: Optional[AiGatewayTokensUpdateOutputConsumer] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapAiGatewayTokensUpdateOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensUpdateOutputConsumer:
        return AiGatewayTokensUpdateOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensUpdateOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayTokensUpdateOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensUpdateOutputLimits:
        return AiGatewayTokensUpdateOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensUpdateOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayTokensUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensUpdateOutput:
        return AiGatewayTokensUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        prefix=data.get('prefix'),
        secret=data.get('secret'),
        consumer=mapAiGatewayTokensUpdateOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        allowed_models=data.get('allowed_models', []),
        limits=[mapAiGatewayTokensUpdateOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayTokensUpdateBodyLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class AiGatewayTokensUpdateBody:
    name: Optional[str] = None
    allowed_models: Optional[List[str]] = None
    limits: Optional[List[AiGatewayTokensUpdateBodyLimits]] = None
    metadata: Optional[Dict[str, str]] = None
    expires_at: Optional[datetime] = None


class mapAiGatewayTokensUpdateBodyLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensUpdateBodyLimits:
        return AiGatewayTokensUpdateBodyLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensUpdateBodyLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayTokensUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayTokensUpdateBody:
        return AiGatewayTokensUpdateBody(
        name=data.get('name'),
        allowed_models=data.get('allowed_models', []),
        limits=[mapAiGatewayTokensUpdateBodyLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayTokensUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

