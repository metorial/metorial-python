from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayConfigUpdateOutputSettingsContentLogging:
    enabled: bool
    retention_days: float
@dataclass
class AiGatewayConfigUpdateOutputSettingsMetorialProvider:
    enabled: bool
@dataclass
class AiGatewayConfigUpdateOutputSettingsFallbacks:
    enabled: bool
@dataclass
class AiGatewayConfigUpdateOutputSettingsZeroDataRetention:
    required: bool
@dataclass
class AiGatewayConfigUpdateOutputSettings:
    content_logging: AiGatewayConfigUpdateOutputSettingsContentLogging
    metorial_provider: AiGatewayConfigUpdateOutputSettingsMetorialProvider
    fallbacks: AiGatewayConfigUpdateOutputSettingsFallbacks
    zero_data_retention: AiGatewayConfigUpdateOutputSettingsZeroDataRetention
@dataclass
class AiGatewayConfigUpdateOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class AiGatewayConfigUpdateOutputPlanLimits:
    metric: str
    amount: float
    interval_seconds: float
@dataclass
class AiGatewayConfigUpdateOutputDisabled:
    since: datetime
    reason: Optional[str] = None
@dataclass
class AiGatewayConfigUpdateOutputBillingRestriction:
    since: datetime
    reason: Optional[str] = None
@dataclass
class AiGatewayConfigUpdateOutput:
    object: str
    log_retention_days: float
    settings: AiGatewayConfigUpdateOutputSettings
    limits: List[AiGatewayConfigUpdateOutputLimits]
    plan_limits: List[AiGatewayConfigUpdateOutputPlanLimits]
    updated_at: datetime
    disabled: Optional[AiGatewayConfigUpdateOutputDisabled] = None
    billing_restriction: Optional[AiGatewayConfigUpdateOutputBillingRestriction] = None


class mapAiGatewayConfigUpdateOutputSettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputSettingsContentLogging:
        return AiGatewayConfigUpdateOutputSettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputSettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputSettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputSettingsMetorialProvider:
        return AiGatewayConfigUpdateOutputSettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputSettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputSettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputSettingsFallbacks:
        return AiGatewayConfigUpdateOutputSettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputSettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputSettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputSettingsZeroDataRetention:
        return AiGatewayConfigUpdateOutputSettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputSettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputSettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputSettings:
        return AiGatewayConfigUpdateOutputSettings(
        content_logging=mapAiGatewayConfigUpdateOutputSettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapAiGatewayConfigUpdateOutputSettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapAiGatewayConfigUpdateOutputSettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapAiGatewayConfigUpdateOutputSettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputSettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputLimits:
        return AiGatewayConfigUpdateOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputPlanLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputPlanLimits:
        return AiGatewayConfigUpdateOutputPlanLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval_seconds=data.get('interval_seconds')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputPlanLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputDisabled:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputDisabled:
        return AiGatewayConfigUpdateOutputDisabled(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputDisabled, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutputBillingRestriction:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutputBillingRestriction:
        return AiGatewayConfigUpdateOutputBillingRestriction(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutputBillingRestriction, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateOutput:
        return AiGatewayConfigUpdateOutput(
        object=data.get('object'),
        log_retention_days=data.get('log_retention_days'),
        settings=mapAiGatewayConfigUpdateOutputSettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapAiGatewayConfigUpdateOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        plan_limits=[mapAiGatewayConfigUpdateOutputPlanLimits.from_dict(item) for item in data.get('plan_limits', []) if item],
        disabled=mapAiGatewayConfigUpdateOutputDisabled.from_dict(data.get('disabled')) if data.get('disabled') else None,
        billing_restriction=mapAiGatewayConfigUpdateOutputBillingRestriction.from_dict(data.get('billing_restriction')) if data.get('billing_restriction') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayConfigUpdateBodySettingsContentLogging:
    enabled: Optional[bool] = None
    retention_days: Optional[float] = None
@dataclass
class AiGatewayConfigUpdateBodySettingsMetorialProvider:
    enabled: Optional[bool] = None
@dataclass
class AiGatewayConfigUpdateBodySettingsFallbacks:
    enabled: Optional[bool] = None
@dataclass
class AiGatewayConfigUpdateBodySettingsZeroDataRetention:
    required: Optional[bool] = None
@dataclass
class AiGatewayConfigUpdateBodySettings:
    content_logging: Optional[AiGatewayConfigUpdateBodySettingsContentLogging] = None
    metorial_provider: Optional[AiGatewayConfigUpdateBodySettingsMetorialProvider] = None
    fallbacks: Optional[AiGatewayConfigUpdateBodySettingsFallbacks] = None
    zero_data_retention: Optional[AiGatewayConfigUpdateBodySettingsZeroDataRetention] = None
@dataclass
class AiGatewayConfigUpdateBodyLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class AiGatewayConfigUpdateBody:
    log_retention_days: Optional[float] = None
    settings: Optional[AiGatewayConfigUpdateBodySettings] = None
    limits: Optional[List[AiGatewayConfigUpdateBodyLimits]] = None


class mapAiGatewayConfigUpdateBodySettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateBodySettingsContentLogging:
        return AiGatewayConfigUpdateBodySettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateBodySettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateBodySettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateBodySettingsMetorialProvider:
        return AiGatewayConfigUpdateBodySettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateBodySettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateBodySettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateBodySettingsFallbacks:
        return AiGatewayConfigUpdateBodySettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateBodySettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateBodySettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateBodySettingsZeroDataRetention:
        return AiGatewayConfigUpdateBodySettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateBodySettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateBodySettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateBodySettings:
        return AiGatewayConfigUpdateBodySettings(
        content_logging=mapAiGatewayConfigUpdateBodySettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapAiGatewayConfigUpdateBodySettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapAiGatewayConfigUpdateBodySettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapAiGatewayConfigUpdateBodySettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateBodySettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateBodyLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateBodyLimits:
        return AiGatewayConfigUpdateBodyLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateBodyLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayConfigUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayConfigUpdateBody:
        return AiGatewayConfigUpdateBody(
        log_retention_days=data.get('log_retention_days'),
        settings=mapAiGatewayConfigUpdateBodySettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapAiGatewayConfigUpdateBodyLimits.from_dict(item) for item in data.get('limits', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayConfigUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

