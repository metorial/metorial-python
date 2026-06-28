from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksDestinationsUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    url: str
    method: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    signing_secret: Optional[str] = None


class mapCallbacksDestinationsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsUpdateOutput:
        return CallbacksDestinationsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        url=data.get('url'),
        method=data.get('method'),
        signing_secret=data.get('signing_secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksDestinationsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksDestinationsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    url: Optional[str] = None


class mapCallbacksDestinationsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksDestinationsUpdateBody:
        return CallbacksDestinationsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksDestinationsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

