from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerDevicesTelemetryTokenIssueOutput:
    object: str
    consumer_device_id: str
    token: str
    token_id: str
    ingest_url: str
    created_at: datetime
    expires_at: Optional[datetime] = None


class mapConsumerDevicesTelemetryTokenIssueOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerDevicesTelemetryTokenIssueOutput:
        return ConsumerDevicesTelemetryTokenIssueOutput(
        object=data.get('object'),
        consumer_device_id=data.get('consumer_device_id'),
        token=data.get('token'),
        token_id=data.get('token_id'),
        ingest_url=data.get('ingest_url'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerDevicesTelemetryTokenIssueOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

