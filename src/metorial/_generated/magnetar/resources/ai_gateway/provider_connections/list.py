from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayProviderConnectionsListOutputItemsProvider:
    id: str
    slug: str
    name: str
@dataclass
class AiGatewayProviderConnectionsListOutputItemsFeatures:
    zdr: bool
@dataclass
class AiGatewayProviderConnectionsListOutputItemsPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class AiGatewayProviderConnectionsListOutputItems:
    object: str
    id: str
    name: str
    priority: float
    provider: AiGatewayProviderConnectionsListOutputItemsProvider
    config: Dict[str, Union[str, float, bool]]
    features: AiGatewayProviderConnectionsListOutputItemsFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[AiGatewayProviderConnectionsListOutputItemsPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
@dataclass
class AiGatewayProviderConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class AiGatewayProviderConnectionsListOutput:
    object: str
    items: List[AiGatewayProviderConnectionsListOutputItems]
    pagination: AiGatewayProviderConnectionsListOutputPagination


class mapAiGatewayProviderConnectionsListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsListOutputItemsProvider:
        return AiGatewayProviderConnectionsListOutputItemsProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsListOutputItemsFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsListOutputItemsFeatures:
        return AiGatewayProviderConnectionsListOutputItemsFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsListOutputItemsFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsListOutputItemsPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsListOutputItemsPricingOverride:
        return AiGatewayProviderConnectionsListOutputItemsPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsListOutputItemsPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsListOutputItems:
        return AiGatewayProviderConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapAiGatewayProviderConnectionsListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapAiGatewayProviderConnectionsListOutputItemsFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapAiGatewayProviderConnectionsListOutputItemsPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[AiGatewayProviderConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsListOutputPagination:
        return AiGatewayProviderConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsListOutput:
        return AiGatewayProviderConnectionsListOutput(
        object=data.get('object'),
        items=[mapAiGatewayProviderConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAiGatewayProviderConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayProviderConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapAiGatewayProviderConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsListQuery:
        return AiGatewayProviderConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider=data.get('provider'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

