from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class TestHelpersConsumerOauthAuthorizationsCreateOutput:
    object: str
    id: str
    url: str
    expires_at: datetime
    created_at: datetime


class mapTestHelpersConsumerOauthAuthorizationsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TestHelpersConsumerOauthAuthorizationsCreateOutput:
        return TestHelpersConsumerOauthAuthorizationsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        url=data.get('url'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[TestHelpersConsumerOauthAuthorizationsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class TestHelpersConsumerOauthAuthorizationsCreateBody:
    instance_id: str
    url: str
    consumer_profile_id: str
    magic_mcp_endpoint_id: str


class mapTestHelpersConsumerOauthAuthorizationsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TestHelpersConsumerOauthAuthorizationsCreateBody:
        return TestHelpersConsumerOauthAuthorizationsCreateBody(
        instance_id=data.get('instance_id'),
        url=data.get('url'),
        consumer_profile_id=data.get('consumer_profile_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[TestHelpersConsumerOauthAuthorizationsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

