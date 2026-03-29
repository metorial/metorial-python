from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsParticipantsGetOutputData:
    identifier: str
    name: str
@dataclass
class DashboardInstanceSessionsParticipantsGetOutput:
    object: str
    id: str
    type: str
    identifier: str
    name: str
    data: DashboardInstanceSessionsParticipantsGetOutputData
    created_at: datetime
    provider_id: Optional[str] = None


class mapDashboardInstanceSessionsParticipantsGetOutputData:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsParticipantsGetOutputData:
        return DashboardInstanceSessionsParticipantsGetOutputData(
        identifier=data.get('identifier'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsParticipantsGetOutputData, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsParticipantsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsParticipantsGetOutput:
        return DashboardInstanceSessionsParticipantsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        data=mapDashboardInstanceSessionsParticipantsGetOutputData.from_dict(data.get('data')) if data.get('data') else None,
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsParticipantsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

