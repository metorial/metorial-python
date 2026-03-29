from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerProvidersRequestAccessOutputConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class ConsumerProvidersRequestAccessOutput:
    object: str
    id: str
    status: str
    consumer_profile: ConsumerProvidersRequestAccessOutputConsumerProfile
    target: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    message: Optional[str] = None
    resolution_message: Optional[str] = None
    reviewed_at: Optional[datetime] = None


class mapConsumerProvidersRequestAccessOutputConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersRequestAccessOutputConsumerProfile:
        return ConsumerProvidersRequestAccessOutputConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersRequestAccessOutputConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersRequestAccessOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersRequestAccessOutput:
        return ConsumerProvidersRequestAccessOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        message=data.get('message'),
        resolution_message=data.get('resolution_message'),
        consumer_profile=mapConsumerProvidersRequestAccessOutputConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        target=data.get('target'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        reviewed_at=datetime.fromisoformat(data.get('reviewed_at').replace('Z', '+00:00')) if data.get('reviewed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersRequestAccessOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerProvidersRequestAccessBody:
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapConsumerProvidersRequestAccessBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersRequestAccessBody:
        return ConsumerProvidersRequestAccessBody(
        message=data.get('message'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersRequestAccessBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

