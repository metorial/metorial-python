from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputSettingsContentLogging:
    enabled: bool
    retention_days: float
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider:
    enabled: bool
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputSettingsFallbacks:
    enabled: bool
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention:
    required: bool
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputSettings:
    content_logging: ManagementInstanceAiGatewayConfigUpdateOutputSettingsContentLogging
    metorial_provider: ManagementInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider
    fallbacks: ManagementInstanceAiGatewayConfigUpdateOutputSettingsFallbacks
    zero_data_retention: ManagementInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputPlanLimits:
    metric: str
    amount: float
    interval_seconds: float
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputDisabled:
    since: datetime
    reason: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutputBillingRestriction:
    since: datetime
    reason: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayConfigUpdateOutput:
    object: str
    log_retention_days: float
    settings: ManagementInstanceAiGatewayConfigUpdateOutputSettings
    limits: List[ManagementInstanceAiGatewayConfigUpdateOutputLimits]
    plan_limits: List[ManagementInstanceAiGatewayConfigUpdateOutputPlanLimits]
    updated_at: datetime
    disabled: Optional[ManagementInstanceAiGatewayConfigUpdateOutputDisabled] = None
    billing_restriction: Optional[ManagementInstanceAiGatewayConfigUpdateOutputBillingRestriction] = None


class mapManagementInstanceAiGatewayConfigUpdateOutputSettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputSettingsContentLogging:
        return ManagementInstanceAiGatewayConfigUpdateOutputSettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputSettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider:
        return ManagementInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputSettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputSettingsFallbacks:
        return ManagementInstanceAiGatewayConfigUpdateOutputSettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputSettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention:
        return ManagementInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputSettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputSettings:
        return ManagementInstanceAiGatewayConfigUpdateOutputSettings(
        content_logging=mapManagementInstanceAiGatewayConfigUpdateOutputSettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapManagementInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapManagementInstanceAiGatewayConfigUpdateOutputSettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapManagementInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputSettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputLimits:
        return ManagementInstanceAiGatewayConfigUpdateOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputPlanLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputPlanLimits:
        return ManagementInstanceAiGatewayConfigUpdateOutputPlanLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval_seconds=data.get('interval_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputPlanLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputDisabled:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputDisabled:
        return ManagementInstanceAiGatewayConfigUpdateOutputDisabled(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputDisabled, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutputBillingRestriction:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutputBillingRestriction:
        return ManagementInstanceAiGatewayConfigUpdateOutputBillingRestriction(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutputBillingRestriction, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateOutput:
        return ManagementInstanceAiGatewayConfigUpdateOutput(
        object=data.get('object'),
        log_retention_days=data.get('log_retention_days'),
        settings=mapManagementInstanceAiGatewayConfigUpdateOutputSettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapManagementInstanceAiGatewayConfigUpdateOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        plan_limits=[mapManagementInstanceAiGatewayConfigUpdateOutputPlanLimits.from_dict(item) for item in data.get('plan_limits', []) if item],
        disabled=mapManagementInstanceAiGatewayConfigUpdateOutputDisabled.from_dict(data.get('disabled')) if data.get('disabled') else None,
        billing_restriction=mapManagementInstanceAiGatewayConfigUpdateOutputBillingRestriction.from_dict(data.get('billing_restriction')) if data.get('billing_restriction') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayConfigUpdateBodySettingsContentLogging:
    enabled: Optional[bool] = None
    retention_days: Optional[float] = None
@dataclass
class ManagementInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider:
    enabled: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayConfigUpdateBodySettingsFallbacks:
    enabled: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention:
    required: Optional[bool] = None
@dataclass
class ManagementInstanceAiGatewayConfigUpdateBodySettings:
    content_logging: Optional[ManagementInstanceAiGatewayConfigUpdateBodySettingsContentLogging] = None
    metorial_provider: Optional[ManagementInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider] = None
    fallbacks: Optional[ManagementInstanceAiGatewayConfigUpdateBodySettingsFallbacks] = None
    zero_data_retention: Optional[ManagementInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention] = None
@dataclass
class ManagementInstanceAiGatewayConfigUpdateBodyLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class ManagementInstanceAiGatewayConfigUpdateBody:
    log_retention_days: Optional[float] = None
    settings: Optional[ManagementInstanceAiGatewayConfigUpdateBodySettings] = None
    limits: Optional[List[ManagementInstanceAiGatewayConfigUpdateBodyLimits]] = None


class mapManagementInstanceAiGatewayConfigUpdateBodySettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateBodySettingsContentLogging:
        return ManagementInstanceAiGatewayConfigUpdateBodySettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateBodySettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider:
        return ManagementInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateBodySettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateBodySettingsFallbacks:
        return ManagementInstanceAiGatewayConfigUpdateBodySettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateBodySettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention:
        return ManagementInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateBodySettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateBodySettings:
        return ManagementInstanceAiGatewayConfigUpdateBodySettings(
        content_logging=mapManagementInstanceAiGatewayConfigUpdateBodySettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapManagementInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapManagementInstanceAiGatewayConfigUpdateBodySettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapManagementInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateBodySettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateBodyLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateBodyLimits:
        return ManagementInstanceAiGatewayConfigUpdateBodyLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateBodyLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigUpdateBody:
        return ManagementInstanceAiGatewayConfigUpdateBody(
        log_retention_days=data.get('log_retention_days'),
        settings=mapManagementInstanceAiGatewayConfigUpdateBodySettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapManagementInstanceAiGatewayConfigUpdateBodyLimits.from_dict(item) for item in data.get('limits', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

