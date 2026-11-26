from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputSettingsContentLogging:
    enabled: bool
    retention_days: float
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider:
    enabled: bool
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputSettingsFallbacks:
    enabled: bool
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention:
    required: bool
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputSettings:
    content_logging: DashboardInstanceAiGatewayConfigUpdateOutputSettingsContentLogging
    metorial_provider: DashboardInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider
    fallbacks: DashboardInstanceAiGatewayConfigUpdateOutputSettingsFallbacks
    zero_data_retention: DashboardInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputPlanLimits:
    metric: str
    amount: float
    interval_seconds: float
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputDisabled:
    since: datetime
    reason: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutputBillingRestriction:
    since: datetime
    reason: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayConfigUpdateOutput:
    object: str
    log_retention_days: float
    settings: DashboardInstanceAiGatewayConfigUpdateOutputSettings
    limits: List[DashboardInstanceAiGatewayConfigUpdateOutputLimits]
    plan_limits: List[DashboardInstanceAiGatewayConfigUpdateOutputPlanLimits]
    updated_at: datetime
    disabled: Optional[DashboardInstanceAiGatewayConfigUpdateOutputDisabled] = None
    billing_restriction: Optional[DashboardInstanceAiGatewayConfigUpdateOutputBillingRestriction] = None


class mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputSettingsContentLogging:
        return DashboardInstanceAiGatewayConfigUpdateOutputSettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputSettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider:
        return DashboardInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputSettingsFallbacks:
        return DashboardInstanceAiGatewayConfigUpdateOutputSettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputSettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention:
        return DashboardInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputSettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputSettings:
        return DashboardInstanceAiGatewayConfigUpdateOutputSettings(
        content_logging=mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapDashboardInstanceAiGatewayConfigUpdateOutputSettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputSettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputLimits:
        return DashboardInstanceAiGatewayConfigUpdateOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputPlanLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputPlanLimits:
        return DashboardInstanceAiGatewayConfigUpdateOutputPlanLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval_seconds=data.get('interval_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputPlanLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputDisabled:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputDisabled:
        return DashboardInstanceAiGatewayConfigUpdateOutputDisabled(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputDisabled, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutputBillingRestriction:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutputBillingRestriction:
        return DashboardInstanceAiGatewayConfigUpdateOutputBillingRestriction(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutputBillingRestriction, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateOutput:
        return DashboardInstanceAiGatewayConfigUpdateOutput(
        object=data.get('object'),
        log_retention_days=data.get('log_retention_days'),
        settings=mapDashboardInstanceAiGatewayConfigUpdateOutputSettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapDashboardInstanceAiGatewayConfigUpdateOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        plan_limits=[mapDashboardInstanceAiGatewayConfigUpdateOutputPlanLimits.from_dict(item) for item in data.get('plan_limits', []) if item],
        disabled=mapDashboardInstanceAiGatewayConfigUpdateOutputDisabled.from_dict(data.get('disabled')) if data.get('disabled') else None,
        billing_restriction=mapDashboardInstanceAiGatewayConfigUpdateOutputBillingRestriction.from_dict(data.get('billing_restriction')) if data.get('billing_restriction') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayConfigUpdateBodySettingsContentLogging:
    enabled: Optional[bool] = None
    retention_days: Optional[float] = None
@dataclass
class DashboardInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider:
    enabled: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayConfigUpdateBodySettingsFallbacks:
    enabled: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention:
    required: Optional[bool] = None
@dataclass
class DashboardInstanceAiGatewayConfigUpdateBodySettings:
    content_logging: Optional[DashboardInstanceAiGatewayConfigUpdateBodySettingsContentLogging] = None
    metorial_provider: Optional[DashboardInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider] = None
    fallbacks: Optional[DashboardInstanceAiGatewayConfigUpdateBodySettingsFallbacks] = None
    zero_data_retention: Optional[DashboardInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention] = None
@dataclass
class DashboardInstanceAiGatewayConfigUpdateBodyLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class DashboardInstanceAiGatewayConfigUpdateBody:
    log_retention_days: Optional[float] = None
    settings: Optional[DashboardInstanceAiGatewayConfigUpdateBodySettings] = None
    limits: Optional[List[DashboardInstanceAiGatewayConfigUpdateBodyLimits]] = None


class mapDashboardInstanceAiGatewayConfigUpdateBodySettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateBodySettingsContentLogging:
        return DashboardInstanceAiGatewayConfigUpdateBodySettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateBodySettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider:
        return DashboardInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateBodySettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateBodySettingsFallbacks:
        return DashboardInstanceAiGatewayConfigUpdateBodySettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateBodySettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention:
        return DashboardInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateBodySettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateBodySettings:
        return DashboardInstanceAiGatewayConfigUpdateBodySettings(
        content_logging=mapDashboardInstanceAiGatewayConfigUpdateBodySettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapDashboardInstanceAiGatewayConfigUpdateBodySettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapDashboardInstanceAiGatewayConfigUpdateBodySettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapDashboardInstanceAiGatewayConfigUpdateBodySettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateBodySettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateBodyLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateBodyLimits:
        return DashboardInstanceAiGatewayConfigUpdateBodyLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateBodyLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigUpdateBody:
        return DashboardInstanceAiGatewayConfigUpdateBody(
        log_retention_days=data.get('log_retention_days'),
        settings=mapDashboardInstanceAiGatewayConfigUpdateBodySettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapDashboardInstanceAiGatewayConfigUpdateBodyLimits.from_dict(item) for item in data.get('limits', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

