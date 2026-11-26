from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayProviderConnectionsCreateOutputProvider:
    id: str
    slug: str
    name: str
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsCreateOutputFeatures:
    zdr: bool
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsCreateOutput:
    object: str
    id: str
    name: str
    priority: float
    provider: DashboardInstanceAiGatewayProviderConnectionsCreateOutputProvider
    config: Dict[str, Union[str, float, bool]]
    features: DashboardInstanceAiGatewayProviderConnectionsCreateOutputFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[DashboardInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class mapDashboardInstanceAiGatewayProviderConnectionsCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsCreateOutputProvider:
        return DashboardInstanceAiGatewayProviderConnectionsCreateOutputProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsCreateOutputFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsCreateOutputFeatures:
        return DashboardInstanceAiGatewayProviderConnectionsCreateOutputFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsCreateOutputFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride:
        return DashboardInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsCreateOutput:
        return DashboardInstanceAiGatewayProviderConnectionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapDashboardInstanceAiGatewayProviderConnectionsCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapDashboardInstanceAiGatewayProviderConnectionsCreateOutputFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapDashboardInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayProviderConnectionsCreateBodyFeatures:
    zdr: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride:
    multiplier: Optional[float] = None
    models: Optional[Dict[str, Dict[str, Any]]] = None
@dataclass
class DashboardInstanceAiGatewayProviderConnectionsCreateBody:
    provider: str
    name: str
    credentials: Dict[str, str]
    description: Optional[str] = None
    priority: Optional[float] = None
    config: Optional[Dict[str, Union[str, float, bool]]] = None
    features: Optional[DashboardInstanceAiGatewayProviderConnectionsCreateBodyFeatures] = None
    pricing_override: Optional[DashboardInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride] = None


class mapDashboardInstanceAiGatewayProviderConnectionsCreateBodyFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsCreateBodyFeatures:
        return DashboardInstanceAiGatewayProviderConnectionsCreateBodyFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsCreateBodyFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride:
        return DashboardInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProviderConnectionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProviderConnectionsCreateBody:
        return DashboardInstanceAiGatewayProviderConnectionsCreateBody(
        provider=data.get('provider'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        credentials=data.get('credentials'),
        config=data.get('config'),
        features=mapDashboardInstanceAiGatewayProviderConnectionsCreateBodyFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapDashboardInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProviderConnectionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

