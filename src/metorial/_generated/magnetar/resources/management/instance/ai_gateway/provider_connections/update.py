from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayProviderConnectionsUpdateOutputProvider:
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsUpdateOutputFeatures:
    zdr: bool
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsUpdateOutput:
    object: str
    id: str
    name: str
    priority: float
    provider: ManagementInstanceAiGatewayProviderConnectionsUpdateOutputProvider
    config: Dict[str, Union[str, float, bool]]
    features: ManagementInstanceAiGatewayProviderConnectionsUpdateOutputFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[ManagementInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayProviderConnectionsUpdateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsUpdateOutputProvider:
        return ManagementInstanceAiGatewayProviderConnectionsUpdateOutputProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsUpdateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsUpdateOutputFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsUpdateOutputFeatures:
        return ManagementInstanceAiGatewayProviderConnectionsUpdateOutputFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsUpdateOutputFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride:
        return ManagementInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsUpdateOutput:
        return ManagementInstanceAiGatewayProviderConnectionsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapManagementInstanceAiGatewayProviderConnectionsUpdateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapManagementInstanceAiGatewayProviderConnectionsUpdateOutputFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapManagementInstanceAiGatewayProviderConnectionsUpdateOutputPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayProviderConnectionsUpdateBodyFeatures:
    zdr: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride:
    multiplier: Optional[float] = None
    models: Optional[Dict[str, Dict[str, Any]]] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[float] = None
    credentials: Optional[Dict[str, str]] = None
    config: Optional[Dict[str, Union[str, float, bool]]] = None
    features: Optional[ManagementInstanceAiGatewayProviderConnectionsUpdateBodyFeatures] = None
    pricing_override: Optional[ManagementInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride] = None


class mapManagementInstanceAiGatewayProviderConnectionsUpdateBodyFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsUpdateBodyFeatures:
        return ManagementInstanceAiGatewayProviderConnectionsUpdateBodyFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsUpdateBodyFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride:
        return ManagementInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsUpdateBody:
        return ManagementInstanceAiGatewayProviderConnectionsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        credentials=data.get('credentials'),
        config=data.get('config'),
        features=mapManagementInstanceAiGatewayProviderConnectionsUpdateBodyFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapManagementInstanceAiGatewayProviderConnectionsUpdateBodyPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

