from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbacksEventsGetOutputError:
    code: Optional[str] = None
    message: Optional[str] = None
@dataclass
class DashboardInstanceCallbacksEventsGetOutput:
    object: str
    id: str
    type: str
    source_id: str
    trigger_key: str
    status: str
    delivery_status: str
    callback_id: str
    created_at: datetime
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    error: Optional[DashboardInstanceCallbacksEventsGetOutputError] = None
    callback_instance_id: Optional[str] = None


class mapDashboardInstanceCallbacksEventsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsGetOutputError:
        return DashboardInstanceCallbacksEventsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksEventsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsGetOutput:
        return DashboardInstanceCallbacksEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        source_id=data.get('source_id'),
        trigger_key=data.get('trigger_key'),
        input=data.get('input'),
        output=data.get('output'),
        status=data.get('status'),
        error=mapDashboardInstanceCallbacksEventsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        delivery_status=data.get('delivery_status'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

