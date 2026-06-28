from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutputFilters:
    object: str
    id: str
    key: str
    name: str
    issue_type: str
    severity: str
    score_weight: float
    default_enabled: bool
    enabled: bool
    default_alert_confidence_threshold: float
    alert_confidence_threshold: float
    description: Optional[str] = None
@dataclass
class ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput:
    object: str
    alert_filter_count_threshold: float
    filters: List[ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutputFilters]


class mapManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutputFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutputFilters:
        return ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutputFilters(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        issue_type=data.get('issue_type'),
        severity=data.get('severity'),
        score_weight=data.get('score_weight'),
        default_enabled=data.get('default_enabled'),
        enabled=data.get('enabled'),
        default_alert_confidence_threshold=data.get('default_alert_confidence_threshold'),
        alert_confidence_threshold=data.get('alert_confidence_threshold')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutputFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput:
        return ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput(
        object=data.get('object'),
        alert_filter_count_threshold=data.get('alert_filter_count_threshold'),
        filters=[mapManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutputFilters.from_dict(item) for item in data.get('filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdBody:
    threshold: Optional[float] = None


class mapManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdBody:
        return ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdBody(
        threshold=data.get('threshold')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProtoGuardConfigSetAlertFilterCountThresholdBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

