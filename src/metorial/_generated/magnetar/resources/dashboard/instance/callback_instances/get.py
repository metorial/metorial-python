from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbackInstancesGetOutput:
    object: str
    id: str
    status: str
    callback_id: str
    integration_instance_id: str
    integration_instance_provider_id: str
    created_at: datetime
    updated_at: datetime


class mapDashboardInstanceCallbackInstancesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackInstancesGetOutput:
        return DashboardInstanceCallbackInstancesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        callback_id=data.get('callback_id'),
        integration_instance_id=data.get('integration_instance_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackInstancesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

