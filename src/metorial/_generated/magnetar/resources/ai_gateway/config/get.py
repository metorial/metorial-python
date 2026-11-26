from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayConfigGetOutputSettingsContentLogging:
    enabled: bool
    retention_days: float
@dataclass
class AiGatewayConfigGetOutputSettingsMetorialProvider:
    enabled: bool
@dataclass
class AiGatewayConfigGetOutputSettingsFallbacks:
    enabled: bool
@dataclass
class AiGatewayConfigGetOutputSettingsZeroDataRetention:
    required: bool
@dataclass
class AiGatewayConfigGetOutputSettings:
    content_logging: AiGatewayConfigGetOutputSettingsContentLogging
    metorial_provider: AiGatewayConfigGetOutputSettingsMetorialProvider
    fallbacks: AiGatewayConfigGetOutputSettingsFallbacks
    zero_data_retention: AiGatewayConfigGetOutputSettingsZeroDataRetention
@dataclass
class AiGatewayConfigGetOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class AiGatewayConfigGetOutputPlanLimits:
    metric: str
    amount: float
    interval_seconds: float
@dataclass
class AiGatewayConfigGetOutputDisabled:
    since: datetime
    reason: Optional[str] = None
@dataclass
class AiGatewayConfigGetOutputBillingRestriction:
    since: datetime
    reason: Optional[str] = None
@dataclass
class AiGatewayConfigGetOutput:
    object: str
    log_retention_days: float
    settings: AiGatewayConfigGetOutputSettings
    limits: List[AiGatewayConfigGetOutputLimits]
    plan_limits: List[AiGatewayConfigGetOutputPlanLimits]
    updated_at: datetime
    disabled: Optional[AiGatewayConfigGetOutputDisabled] = None
    billing_restriction: Optional[AiGatewayConfigGetOutputBillingRestriction] = None


class mapAiGatewayConfigGetOutputSettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputSettingsContentLogging:
        return AiGatewayConfigGetOutputSettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputSettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputSettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputSettingsMetorialProvider:
        return AiGatewayConfigGetOutputSettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputSettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputSettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputSettingsFallbacks:
        return AiGatewayConfigGetOutputSettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputSettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputSettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputSettingsZeroDataRetention:
        return AiGatewayConfigGetOutputSettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputSettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputSettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputSettings:
        return AiGatewayConfigGetOutputSettings(
        content_logging=mapAiGatewayConfigGetOutputSettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapAiGatewayConfigGetOutputSettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapAiGatewayConfigGetOutputSettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapAiGatewayConfigGetOutputSettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputSettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputLimits:
        return AiGatewayConfigGetOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputPlanLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputPlanLimits:
        return AiGatewayConfigGetOutputPlanLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval_seconds=data.get('interval_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputPlanLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputDisabled:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputDisabled:
        return AiGatewayConfigGetOutputDisabled(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputDisabled, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutputBillingRestriction:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutputBillingRestriction:
        return AiGatewayConfigGetOutputBillingRestriction(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutputBillingRestriction, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigGetOutput:
        return AiGatewayConfigGetOutput(
        object=data.get('object'),
        log_retention_days=data.get('log_retention_days'),
        settings=mapAiGatewayConfigGetOutputSettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapAiGatewayConfigGetOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        plan_limits=[mapAiGatewayConfigGetOutputPlanLimits.from_dict(item) for item in data.get('plan_limits', []) if item],
        disabled=mapAiGatewayConfigGetOutputDisabled.from_dict(data.get('disabled')) if data.get('disabled') else None,
        billing_restriction=mapAiGatewayConfigGetOutputBillingRestriction.from_dict(data.get('billing_restriction')) if data.get('billing_restriction') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

