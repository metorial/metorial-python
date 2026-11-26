from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDeleteOutputProvider:
    id: str
    slug: str
    name: str
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDeleteOutputFeatures:
    zdr: bool
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDeleteOutputPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayProviderConnectionsDeleteOutput:
    object: str
    id: str
    name: str
    priority: float
    provider: ManagementInstanceAiGatewayProviderConnectionsDeleteOutputProvider
    config: Dict[str, Union[str, float, bool]]
    features: ManagementInstanceAiGatewayProviderConnectionsDeleteOutputFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[ManagementInstanceAiGatewayProviderConnectionsDeleteOutputPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class mapManagementInstanceAiGatewayProviderConnectionsDeleteOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDeleteOutputProvider:
        return ManagementInstanceAiGatewayProviderConnectionsDeleteOutputProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDeleteOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsDeleteOutputFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDeleteOutputFeatures:
        return ManagementInstanceAiGatewayProviderConnectionsDeleteOutputFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDeleteOutputFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsDeleteOutputPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDeleteOutputPricingOverride:
        return ManagementInstanceAiGatewayProviderConnectionsDeleteOutputPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDeleteOutputPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProviderConnectionsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProviderConnectionsDeleteOutput:
        return ManagementInstanceAiGatewayProviderConnectionsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapManagementInstanceAiGatewayProviderConnectionsDeleteOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapManagementInstanceAiGatewayProviderConnectionsDeleteOutputFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapManagementInstanceAiGatewayProviderConnectionsDeleteOutputPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[ManagementInstanceAiGatewayProviderConnectionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

