from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProtoGuardConfigUpdateOutputFilters:
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
class DashboardInstanceProtoGuardConfigUpdateOutput:
    object: str
    enabled: bool
    alert_probability_threshold: float
    alert_filter_count_threshold: float
    filters: List[DashboardInstanceProtoGuardConfigUpdateOutputFilters]


class mapDashboardInstanceProtoGuardConfigUpdateOutputFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardConfigUpdateOutputFilters:
        return DashboardInstanceProtoGuardConfigUpdateOutputFilters(
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
    def to_dict(value: Union[DashboardInstanceProtoGuardConfigUpdateOutputFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProtoGuardConfigUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardConfigUpdateOutput:
        return DashboardInstanceProtoGuardConfigUpdateOutput(
        object=data.get('object'),
        enabled=data.get('enabled'),
        alert_probability_threshold=data.get('alert_probability_threshold'),
        alert_filter_count_threshold=data.get('alert_filter_count_threshold'),
        filters=[mapDashboardInstanceProtoGuardConfigUpdateOutputFilters.from_dict(item) for item in data.get('filters', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardConfigUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProtoGuardConfigUpdateBody:
    enabled: Optional[bool] = None
    alert_probability_threshold: Optional[float] = None
    alert_filter_count_threshold: Optional[float] = None


class mapDashboardInstanceProtoGuardConfigUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProtoGuardConfigUpdateBody:
        return DashboardInstanceProtoGuardConfigUpdateBody(
        enabled=data.get('enabled'),
        alert_probability_threshold=data.get('alert_probability_threshold'),
        alert_filter_count_threshold=data.get('alert_filter_count_threshold')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProtoGuardConfigUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

