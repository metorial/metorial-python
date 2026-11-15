from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderIssuesGetOutputDailyOccurrences:
    starts_at: datetime
    ends_at: datetime
    count: float
@dataclass
class DashboardInstanceProviderIssuesGetOutput:
    object: str
    id: str
    type: str
    subtype: str
    severity: str
    code: str
    message: str
    occurrence_count: float
    daily_occurrences: List[DashboardInstanceProviderIssuesGetOutputDailyOccurrences]
    first_seen_at: datetime
    last_seen_at: datetime
    created_at: datetime
    provider_id: Optional[str] = None
    protoguard_filter_id: Optional[str] = None


class mapDashboardInstanceProviderIssuesGetOutputDailyOccurrences:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderIssuesGetOutputDailyOccurrences:
        return DashboardInstanceProviderIssuesGetOutputDailyOccurrences(
        starts_at=datetime.fromisoformat(data.get('starts_at').replace('Z', '+00:00')) if data.get('starts_at') else None,
        ends_at=datetime.fromisoformat(data.get('ends_at').replace('Z', '+00:00')) if data.get('ends_at') else None,
        count=data.get('count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderIssuesGetOutputDailyOccurrences, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderIssuesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderIssuesGetOutput:
        return DashboardInstanceProviderIssuesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        subtype=data.get('subtype'),
        severity=data.get('severity'),
        code=data.get('code'),
        message=data.get('message'),
        provider_id=data.get('provider_id'),
        protoguard_filter_id=data.get('protoguard_filter_id'),
        occurrence_count=data.get('occurrence_count'),
        daily_occurrences=[mapDashboardInstanceProviderIssuesGetOutputDailyOccurrences.from_dict(item) for item in data.get('daily_occurrences', []) if item],
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at').replace('Z', '+00:00')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderIssuesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

