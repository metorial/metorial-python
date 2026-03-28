from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerProvidersDeployOutputEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class ConsumerProvidersDeployOutput:
    object: str
    id: str
    status: str
    session_template_id: str
    endpoints: List[ConsumerProvidersDeployOutputEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class mapConsumerProvidersDeployOutputEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputEndpoints:
        return ConsumerProvidersDeployOutputEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutput:
        return ConsumerProvidersDeployOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        session_template_id=data.get('session_template_id'),
        provider_template_id=data.get('provider_template_id'),
        endpoints=[mapConsumerProvidersDeployOutputEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerProvidersDeployBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[Dict[str, Any]] = None
    auth: Optional[Dict[str, Any]] = None


class mapConsumerProvidersDeployBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployBody:
        return ConsumerProvidersDeployBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        config=data.get('config'),
        auth=data.get('auth')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

