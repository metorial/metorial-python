from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDisableOutputProvider:
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDisableOutputFeatures:
    zdr: bool
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDisableOutputPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDisableOutput:
    object: str
    id: str
    name: str
    priority: float
    provider: ManagementInstanceAiGatewayProviderConnectionsDisableOutputProvider
    config: Dict[str, Union[str, float, bool]]
    features: ManagementInstanceAiGatewayProviderConnectionsDisableOutputFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[ManagementInstanceAiGatewayProviderConnectionsDisableOutputPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayProviderConnectionsDisableOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDisableOutputProvider:
        return ManagementInstanceAiGatewayProviderConnectionsDisableOutputProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDisableOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsDisableOutputFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDisableOutputFeatures:
        return ManagementInstanceAiGatewayProviderConnectionsDisableOutputFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDisableOutputFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsDisableOutputPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDisableOutputPricingOverride:
        return ManagementInstanceAiGatewayProviderConnectionsDisableOutputPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDisableOutputPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsDisableOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDisableOutput:
        return ManagementInstanceAiGatewayProviderConnectionsDisableOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapManagementInstanceAiGatewayProviderConnectionsDisableOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapManagementInstanceAiGatewayProviderConnectionsDisableOutputFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapManagementInstanceAiGatewayProviderConnectionsDisableOutputPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDisableOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

