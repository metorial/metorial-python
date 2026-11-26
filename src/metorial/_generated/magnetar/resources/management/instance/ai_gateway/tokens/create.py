from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayTokensCreateOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class ManagementInstanceAiGatewayTokensCreateOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class ManagementInstanceAiGatewayTokensCreateOutput:
    object: str
    id: str
    name: str
    prefix: str
    allowed_models: List[str]
    limits: List[ManagementInstanceAiGatewayTokensCreateOutputLimits]
    metadata: Dict[str, str]
    created_at: datetime
    secret: Optional[str] = None
    consumer: Optional[ManagementInstanceAiGatewayTokensCreateOutputConsumer] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayTokensCreateOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensCreateOutputConsumer:
        return ManagementInstanceAiGatewayTokensCreateOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensCreateOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayTokensCreateOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensCreateOutputLimits:
        return ManagementInstanceAiGatewayTokensCreateOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensCreateOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayTokensCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensCreateOutput:
        return ManagementInstanceAiGatewayTokensCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        prefix=data.get('prefix'),
        secret=data.get('secret'),
        consumer=mapManagementInstanceAiGatewayTokensCreateOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        allowed_models=data.get('allowed_models', []),
        limits=[mapManagementInstanceAiGatewayTokensCreateOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayTokensCreateBodyLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class ManagementInstanceAiGatewayTokensCreateBody:
    name: str
    consumer_id: Optional[str] = None
    allowed_models: Optional[List[str]] = None
    limits: Optional[List[ManagementInstanceAiGatewayTokensCreateBodyLimits]] = None
    metadata: Optional[Dict[str, str]] = None
    expires_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayTokensCreateBodyLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensCreateBodyLimits:
        return ManagementInstanceAiGatewayTokensCreateBodyLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensCreateBodyLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayTokensCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensCreateBody:
        return ManagementInstanceAiGatewayTokensCreateBody(
        name=data.get('name'),
        consumer_id=data.get('consumer_id'),
        allowed_models=data.get('allowed_models', []),
        limits=[mapManagementInstanceAiGatewayTokensCreateBodyLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

