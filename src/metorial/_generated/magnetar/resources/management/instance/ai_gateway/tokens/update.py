from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayTokensUpdateOutputConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class ManagementInstanceAiGatewayTokensUpdateOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class ManagementInstanceAiGatewayTokensUpdateOutput:
    object: str
    id: str
    name: str
    prefix: str
    allowed_models: List[str]
    limits: List[ManagementInstanceAiGatewayTokensUpdateOutputLimits]
    metadata: Dict[str, str]
    created_at: datetime
    secret: Optional[str] = None
    consumer: Optional[ManagementInstanceAiGatewayTokensUpdateOutputConsumer] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayTokensUpdateOutputConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensUpdateOutputConsumer:
        return ManagementInstanceAiGatewayTokensUpdateOutputConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensUpdateOutputConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayTokensUpdateOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensUpdateOutputLimits:
        return ManagementInstanceAiGatewayTokensUpdateOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensUpdateOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayTokensUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensUpdateOutput:
        return ManagementInstanceAiGatewayTokensUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        prefix=data.get('prefix'),
        secret=data.get('secret'),
        consumer=mapManagementInstanceAiGatewayTokensUpdateOutputConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        allowed_models=data.get('allowed_models', []),
        limits=[mapManagementInstanceAiGatewayTokensUpdateOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayTokensUpdateBodyLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class ManagementInstanceAiGatewayTokensUpdateBody:
    name: Optional[str] = None
    allowed_models: Optional[List[str]] = None
    limits: Optional[List[ManagementInstanceAiGatewayTokensUpdateBodyLimits]] = None
    metadata: Optional[Dict[str, str]] = None
    expires_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayTokensUpdateBodyLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensUpdateBodyLimits:
        return ManagementInstanceAiGatewayTokensUpdateBodyLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensUpdateBodyLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayTokensUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayTokensUpdateBody:
        return ManagementInstanceAiGatewayTokensUpdateBody(
        name=data.get('name'),
        allowed_models=data.get('allowed_models', []),
        limits=[mapManagementInstanceAiGatewayTokensUpdateBodyLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayTokensUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

