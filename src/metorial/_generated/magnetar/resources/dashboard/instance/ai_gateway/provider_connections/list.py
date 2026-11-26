from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayProviderConnectionsListOutputItemsProvider:
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsListOutputItemsFeatures:
    zdr: bool
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsListOutputItemsPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsListOutputItems:
    object: str
    id: str
    name: str
    priority: float
    provider: DashboardInstanceAiGatewayProviderConnectionsListOutputItemsProvider
    config: Dict[str, Union[str, float, bool]]
    features: DashboardInstanceAiGatewayProviderConnectionsListOutputItemsFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[DashboardInstanceAiGatewayProviderConnectionsListOutputItemsPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsListOutput:
    object: str
    items: List[DashboardInstanceAiGatewayProviderConnectionsListOutputItems]
    pagination: DashboardInstanceAiGatewayProviderConnectionsListOutputPagination


class mapDashboardInstanceAiGatewayProviderConnectionsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsListOutputItemsProvider:
        return DashboardInstanceAiGatewayProviderConnectionsListOutputItemsProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsListOutputItemsFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsListOutputItemsFeatures:
        return DashboardInstanceAiGatewayProviderConnectionsListOutputItemsFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsListOutputItemsFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsListOutputItemsPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsListOutputItemsPricingOverride:
        return DashboardInstanceAiGatewayProviderConnectionsListOutputItemsPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsListOutputItemsPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsListOutputItems:
        return DashboardInstanceAiGatewayProviderConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapDashboardInstanceAiGatewayProviderConnectionsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapDashboardInstanceAiGatewayProviderConnectionsListOutputItemsFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapDashboardInstanceAiGatewayProviderConnectionsListOutputItemsPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
        credential_hint=data.get('credential_hint'),
        status=data.get('status'),
        status_message=data.get('status_message'),
        consecutive_failures=data.get('consecutive_failures'),
        last_checked_at=datetime.fromisoformat(data.get('last_checked_at').replace('Z', '+00:00')) if data.get('last_checked_at') else None,
        last_valid_at=datetime.fromisoformat(data.get('last_valid_at').replace('Z', '+00:00')) if data.get('last_valid_at') else None,
        next_check_at=datetime.fromisoformat(data.get('next_check_at').replace('Z', '+00:00')) if data.get('next_check_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsListOutputPagination:
        return DashboardInstanceAiGatewayProviderConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsListOutput:
        return DashboardInstanceAiGatewayProviderConnectionsListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceAiGatewayProviderConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAiGatewayProviderConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayProviderConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceAiGatewayProviderConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsListQuery:
        return DashboardInstanceAiGatewayProviderConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider=data.get('provider'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

