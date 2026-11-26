from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayTokensListOutputItemsConsumer:
    object: str
    id: str
    name: str
    email: str
@dataclass
class DashboardInstanceAiGatewayTokensListOutputItemsLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class DashboardInstanceAiGatewayTokensListOutputItems:
    object: str
    id: str
    name: str
    prefix: str
    allowed_models: List[str]
    limits: List[DashboardInstanceAiGatewayTokensListOutputItemsLimits]
    metadata: Dict[str, str]
    created_at: datetime
    secret: Optional[str] = None
    consumer: Optional[DashboardInstanceAiGatewayTokensListOutputItemsConsumer] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class DashboardInstanceAiGatewayTokensListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayTokensListOutput:
    object: str
    items: List[DashboardInstanceAiGatewayTokensListOutputItems]
    pagination: DashboardInstanceAiGatewayTokensListOutputPagination


class mapDashboardInstanceAiGatewayTokensListOutputItemsConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensListOutputItemsConsumer:
        return DashboardInstanceAiGatewayTokensListOutputItemsConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensListOutputItemsConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayTokensListOutputItemsLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensListOutputItemsLimits:
        return DashboardInstanceAiGatewayTokensListOutputItemsLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensListOutputItemsLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayTokensListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensListOutputItems:
        return DashboardInstanceAiGatewayTokensListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        prefix=data.get('prefix'),
        secret=data.get('secret'),
        consumer=mapDashboardInstanceAiGatewayTokensListOutputItemsConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        allowed_models=data.get('allowed_models', []),
        limits=[mapDashboardInstanceAiGatewayTokensListOutputItemsLimits.from_dict(item) for item in data.get('limits', []) if item],
        metadata=data.get('metadata'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayTokensListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensListOutputPagination:
        return DashboardInstanceAiGatewayTokensListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayTokensListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensListOutput:
        return DashboardInstanceAiGatewayTokensListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceAiGatewayTokensListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAiGatewayTokensListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayTokensListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    consumer_id: Optional[str] = None


class mapDashboardInstanceAiGatewayTokensListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayTokensListQuery:
        return DashboardInstanceAiGatewayTokensListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        consumer_id=data.get('consumer_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayTokensListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

