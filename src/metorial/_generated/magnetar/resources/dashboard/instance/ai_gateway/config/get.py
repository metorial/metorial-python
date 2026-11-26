from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayConfigGetOutputSettingsContentLogging:
    enabled: bool
    retention_days: float
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputSettingsMetorialProvider:
    enabled: bool
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputSettingsFallbacks:
    enabled: bool
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention:
    required: bool
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputSettings:
    content_logging: DashboardInstanceAiGatewayConfigGetOutputSettingsContentLogging
    metorial_provider: DashboardInstanceAiGatewayConfigGetOutputSettingsMetorialProvider
    fallbacks: DashboardInstanceAiGatewayConfigGetOutputSettingsFallbacks
    zero_data_retention: DashboardInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputPlanLimits:
    metric: str
    amount: float
    interval_seconds: float
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputDisabled:
    since: datetime
    reason: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayConfigGetOutputBillingRestriction:
    since: datetime
    reason: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayConfigGetOutput:
    object: str
    log_retention_days: float
    settings: DashboardInstanceAiGatewayConfigGetOutputSettings
    limits: List[DashboardInstanceAiGatewayConfigGetOutputLimits]
    plan_limits: List[DashboardInstanceAiGatewayConfigGetOutputPlanLimits]
    updated_at: datetime
    disabled: Optional[DashboardInstanceAiGatewayConfigGetOutputDisabled] = None
    billing_restriction: Optional[DashboardInstanceAiGatewayConfigGetOutputBillingRestriction] = None


class mapDashboardInstanceAiGatewayConfigGetOutputSettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputSettingsContentLogging:
        return DashboardInstanceAiGatewayConfigGetOutputSettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputSettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputSettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputSettingsMetorialProvider:
        return DashboardInstanceAiGatewayConfigGetOutputSettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputSettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputSettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputSettingsFallbacks:
        return DashboardInstanceAiGatewayConfigGetOutputSettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputSettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention:
        return DashboardInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputSettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputSettings:
        return DashboardInstanceAiGatewayConfigGetOutputSettings(
        content_logging=mapDashboardInstanceAiGatewayConfigGetOutputSettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapDashboardInstanceAiGatewayConfigGetOutputSettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapDashboardInstanceAiGatewayConfigGetOutputSettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapDashboardInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputSettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputLimits:
        return DashboardInstanceAiGatewayConfigGetOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputPlanLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputPlanLimits:
        return DashboardInstanceAiGatewayConfigGetOutputPlanLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval_seconds=data.get('interval_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputPlanLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputDisabled:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputDisabled:
        return DashboardInstanceAiGatewayConfigGetOutputDisabled(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputDisabled, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutputBillingRestriction:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutputBillingRestriction:
        return DashboardInstanceAiGatewayConfigGetOutputBillingRestriction(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutputBillingRestriction, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayConfigGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayConfigGetOutput:
        return DashboardInstanceAiGatewayConfigGetOutput(
        object=data.get('object'),
        log_retention_days=data.get('log_retention_days'),
        settings=mapDashboardInstanceAiGatewayConfigGetOutputSettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapDashboardInstanceAiGatewayConfigGetOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        plan_limits=[mapDashboardInstanceAiGatewayConfigGetOutputPlanLimits.from_dict(item) for item in data.get('plan_limits', []) if item],
        disabled=mapDashboardInstanceAiGatewayConfigGetOutputDisabled.from_dict(data.get('disabled')) if data.get('disabled') else None,
        billing_restriction=mapDashboardInstanceAiGatewayConfigGetOutputBillingRestriction.from_dict(data.get('billing_restriction')) if data.get('billing_restriction') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayConfigGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

