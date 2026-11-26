from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayProviderConnectionsCreateOutputProvider:
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsCreateOutputFeatures:
    zdr: bool
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsCreateOutput:
    object: str
    id: str
    name: str
    priority: float
    provider: ManagementInstanceAiGatewayProviderConnectionsCreateOutputProvider
    config: Dict[str, Union[str, float, bool]]
    features: ManagementInstanceAiGatewayProviderConnectionsCreateOutputFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[ManagementInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayProviderConnectionsCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsCreateOutputProvider:
        return ManagementInstanceAiGatewayProviderConnectionsCreateOutputProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsCreateOutputFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsCreateOutputFeatures:
        return ManagementInstanceAiGatewayProviderConnectionsCreateOutputFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsCreateOutputFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride:
        return ManagementInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsCreateOutput:
        return ManagementInstanceAiGatewayProviderConnectionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapManagementInstanceAiGatewayProviderConnectionsCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapManagementInstanceAiGatewayProviderConnectionsCreateOutputFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapManagementInstanceAiGatewayProviderConnectionsCreateOutputPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayProviderConnectionsCreateBodyFeatures:
    zdr: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride:
    multiplier: Optional[float] = None
    models: Optional[Dict[str, Dict[str, Any]]] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsCreateBody:
    provider: str
    name: str
    credentials: Dict[str, str]
    description: Optional[str] = None
    priority: Optional[float] = None
    config: Optional[Dict[str, Union[str, float, bool]]] = None
    features: Optional[ManagementInstanceAiGatewayProviderConnectionsCreateBodyFeatures] = None
    pricing_override: Optional[ManagementInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride] = None


class mapManagementInstanceAiGatewayProviderConnectionsCreateBodyFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsCreateBodyFeatures:
        return ManagementInstanceAiGatewayProviderConnectionsCreateBodyFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsCreateBodyFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride:
        return ManagementInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsCreateBody:
        return ManagementInstanceAiGatewayProviderConnectionsCreateBody(
        provider=data.get('provider'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        credentials=data.get('credentials'),
        config=data.get('config'),
        features=mapManagementInstanceAiGatewayProviderConnectionsCreateBodyFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapManagementInstanceAiGatewayProviderConnectionsCreateBodyPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

