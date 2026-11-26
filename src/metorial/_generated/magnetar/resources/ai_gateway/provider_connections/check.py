from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayProviderConnectionsCheckOutputProvider:
    id: str
    slug: str
    name: str
@dataclass
class AiGatewayProviderConnectionsCheckOutputFeatures:
    zdr: bool
@dataclass
class AiGatewayProviderConnectionsCheckOutputPricingOverride:
    models: Dict[str, Dict[str, Any]]
    multiplier: Optional[float] = None
@dataclass
class AiGatewayProviderConnectionsCheckOutput:
    object: str
    id: str
    name: str
    priority: float
    provider: AiGatewayProviderConnectionsCheckOutputProvider
    config: Dict[str, Union[str, float, bool]]
    features: AiGatewayProviderConnectionsCheckOutputFeatures
    status: str
    consecutive_failures: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    pricing_override: Optional[AiGatewayProviderConnectionsCheckOutputPricingOverride] = None
    credential_hint: Optional[str] = None
    status_message: Optional[str] = None
    last_checked_at: Optional[datetime] = None
    last_valid_at: Optional[datetime] = None
    next_check_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class mapAiGatewayProviderConnectionsCheckOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsCheckOutputProvider:
        return AiGatewayProviderConnectionsCheckOutputProvider(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsCheckOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsCheckOutputFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsCheckOutputFeatures:
        return AiGatewayProviderConnectionsCheckOutputFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsCheckOutputFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsCheckOutputPricingOverride:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsCheckOutputPricingOverride:
        return AiGatewayProviderConnectionsCheckOutputPricingOverride(
        multiplier=data.get('multiplier'),
        models=data.get('models')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProviderConnectionsCheckOutputPricingOverride, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProviderConnectionsCheckOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProviderConnectionsCheckOutput:
        return AiGatewayProviderConnectionsCheckOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        priority=data.get('priority'),
        provider=mapAiGatewayProviderConnectionsCheckOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        config=data.get('config'),
        features=mapAiGatewayProviderConnectionsCheckOutputFeatures.from_dict(data.get('features')) if data.get('features') else None,
        pricing_override=mapAiGatewayProviderConnectionsCheckOutputPricingOverride.from_dict(data.get('pricing_override')) if data.get('pricing_override') else None,
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
    def to_dict(value: Union[AiGatewayProviderConnectionsCheckOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

