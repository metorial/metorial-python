from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayConfigGetOutputSettingsContentLogging:
    enabled: bool
    retention_days: float
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputSettingsMetorialProvider:
    enabled: bool
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputSettingsFallbacks:
    enabled: bool
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention:
    required: bool
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputSettings:
    content_logging: ManagementInstanceAiGatewayConfigGetOutputSettingsContentLogging
    metorial_provider: ManagementInstanceAiGatewayConfigGetOutputSettingsMetorialProvider
    fallbacks: ManagementInstanceAiGatewayConfigGetOutputSettingsFallbacks
    zero_data_retention: ManagementInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputLimits:
    metric: str
    amount: float
    interval: str
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputPlanLimits:
    metric: str
    amount: float
    interval_seconds: float
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputDisabled:
    since: datetime
    reason: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayConfigGetOutputBillingRestriction:
    since: datetime
    reason: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayConfigGetOutput:
    object: str
    log_retention_days: float
    settings: ManagementInstanceAiGatewayConfigGetOutputSettings
    limits: List[ManagementInstanceAiGatewayConfigGetOutputLimits]
    plan_limits: List[ManagementInstanceAiGatewayConfigGetOutputPlanLimits]
    updated_at: datetime
    disabled: Optional[ManagementInstanceAiGatewayConfigGetOutputDisabled] = None
    billing_restriction: Optional[ManagementInstanceAiGatewayConfigGetOutputBillingRestriction] = None


class mapManagementInstanceAiGatewayConfigGetOutputSettingsContentLogging:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputSettingsContentLogging:
        return ManagementInstanceAiGatewayConfigGetOutputSettingsContentLogging(
        enabled=data.get('enabled'),
        retention_days=data.get('retention_days')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputSettingsContentLogging, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputSettingsMetorialProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputSettingsMetorialProvider:
        return ManagementInstanceAiGatewayConfigGetOutputSettingsMetorialProvider(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputSettingsMetorialProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputSettingsFallbacks:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputSettingsFallbacks:
        return ManagementInstanceAiGatewayConfigGetOutputSettingsFallbacks(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputSettingsFallbacks, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention:
        return ManagementInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention(
        required=data.get('required')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputSettings:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputSettings:
        return ManagementInstanceAiGatewayConfigGetOutputSettings(
        content_logging=mapManagementInstanceAiGatewayConfigGetOutputSettingsContentLogging.from_dict(data.get('content_logging')) if data.get('content_logging') else None,
        metorial_provider=mapManagementInstanceAiGatewayConfigGetOutputSettingsMetorialProvider.from_dict(data.get('metorial_provider')) if data.get('metorial_provider') else None,
        fallbacks=mapManagementInstanceAiGatewayConfigGetOutputSettingsFallbacks.from_dict(data.get('fallbacks')) if data.get('fallbacks') else None,
        zero_data_retention=mapManagementInstanceAiGatewayConfigGetOutputSettingsZeroDataRetention.from_dict(data.get('zero_data_retention')) if data.get('zero_data_retention') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputSettings, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputLimits:
        return ManagementInstanceAiGatewayConfigGetOutputLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval=data.get('interval')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputPlanLimits:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputPlanLimits:
        return ManagementInstanceAiGatewayConfigGetOutputPlanLimits(
        metric=data.get('metric'),
        amount=data.get('amount'),
        interval_seconds=data.get('interval_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputPlanLimits, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputDisabled:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputDisabled:
        return ManagementInstanceAiGatewayConfigGetOutputDisabled(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputDisabled, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutputBillingRestriction:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutputBillingRestriction:
        return ManagementInstanceAiGatewayConfigGetOutputBillingRestriction(
        reason=data.get('reason'),
        since=datetime.fromisoformat(data.get('since').replace('Z', '+00:00')) if data.get('since') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutputBillingRestriction, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayConfigGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayConfigGetOutput:
        return ManagementInstanceAiGatewayConfigGetOutput(
        object=data.get('object'),
        log_retention_days=data.get('log_retention_days'),
        settings=mapManagementInstanceAiGatewayConfigGetOutputSettings.from_dict(data.get('settings')) if data.get('settings') else None,
        limits=[mapManagementInstanceAiGatewayConfigGetOutputLimits.from_dict(item) for item in data.get('limits', []) if item],
        plan_limits=[mapManagementInstanceAiGatewayConfigGetOutputPlanLimits.from_dict(item) for item in data.get('plan_limits', []) if item],
        disabled=mapManagementInstanceAiGatewayConfigGetOutputDisabled.from_dict(data.get('disabled')) if data.get('disabled') else None,
        billing_restriction=mapManagementInstanceAiGatewayConfigGetOutputBillingRestriction.from_dict(data.get('billing_restriction')) if data.get('billing_restriction') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayConfigGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

