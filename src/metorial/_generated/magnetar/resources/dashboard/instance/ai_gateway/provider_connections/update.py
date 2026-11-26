from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayProviderConnectionsUpdateOutputProvider:
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsUpdateOutputFeatures:
    zdr: bool
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsUpdateOutput:
    object: str
    id: str
    name: str
    priority: float
    provider: DashboardInstanceAiGatewayProviderConnectionsUpdateOutputProvider
    config: Dict[str, Union[str, float, bool]]
    features: DashboardInstanceAiGatewayProviderConnectionsUpdateOutputFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[DashboardInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsUpdateOutputProvider:
        return DashboardInstanceAiGatewayProviderConnectionsUpdateOutputProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsUpdateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutputFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsUpdateOutputFeatures:
        return DashboardInstanceAiGatewayProviderConnectionsUpdateOutputFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsUpdateOutputFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride:
        return DashboardInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsUpdateOutput:
        return DashboardInstanceAiGatewayProviderConnectionsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutputFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapDashboardInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayProviderConnectionsUpdateBodyFeatures:
    zdr: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride:
    multiplier: Optional[float] = None
    models: Optional[Dict[str, Dict[str, Any]]] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[float] = None
    credentials: Optional[Dict[str, str]] = None
    config: Optional[Dict[str, Union[str, float, bool]]] = None
    features: Optional[DashboardInstanceAiGatewayProviderConnectionsUpdateBodyFeatures] = None
    pricing_override: Optional[DashboardInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride] = None


class mapDashboardInstanceAiGatewayProviderConnectionsUpdateBodyFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsUpdateBodyFeatures:
        return DashboardInstanceAiGatewayProviderConnectionsUpdateBodyFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsUpdateBodyFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride:
        return DashboardInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsUpdateBody:
        return DashboardInstanceAiGatewayProviderConnectionsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        credentials=data.get('credentials'),
        config=data.get('config'),
        features=mapDashboardInstanceAiGatewayProviderConnectionsUpdateBodyFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapDashboardInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

