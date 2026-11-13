from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerDevicesCheckInOutputClients:
    object: str
    key: str
    name: str
    detected: bool
    installable: bool
    supports_skills: bool
    enabled: bool
    excluded_magic_mcp_server_ids: List[str]
    excluded_skill_ids: List[str]
@dataclass
class ConsumerDevicesCheckInOutput:
    object: str
    id: str
    status: str
    consumer_profile_id: str
    name: str
    os: str
    arch: str
    app_version: str
    clients: List[ConsumerDevicesCheckInOutputClients]
    last_seen_at: datetime
    created_at: datetime
    updated_at: datetime
    revoked_at: Optional[datetime] = None


class mapConsumerDevicesCheckInOutputClients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerDevicesCheckInOutputClients:
        return ConsumerDevicesCheckInOutputClients(
        object=data.get('object'),
        key=data.get('key'),
        name=data.get('name'),
        detected=data.get('detected'),
        installable=data.get('installable'),
        supports_skills=data.get('supports_skills'),
        enabled=data.get('enabled'),
        excluded_magic_mcp_server_ids=data.get('excluded_magic_mcp_server_ids', []),
        excluded_skill_ids=data.get('excluded_skill_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ConsumerDevicesCheckInOutputClients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerDevicesCheckInOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerDevicesCheckInOutput:
        return ConsumerDevicesCheckInOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        consumer_profile_id=data.get('consumer_profile_id'),
        name=data.get('name'),
        os=data.get('os'),
        arch=data.get('arch'),
        app_version=data.get('app_version'),
        clients=[mapConsumerDevicesCheckInOutputClients.from_dict(item) for item in data.get('clients', []) if item],
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerDevicesCheckInOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerDevicesCheckInBodyClients:
    key: str
    name: str
    detected: bool
    installable: bool
    supports_skills: bool
@dataclass
class ConsumerDevicesCheckInBody:
    installation_id: str
    name: str
    os: str
    arch: str
    app_version: str
    clients: List[ConsumerDevicesCheckInBodyClients]
    magic_mcp_token_ids: Optional[List[str]] = None


class mapConsumerDevicesCheckInBodyClients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerDevicesCheckInBodyClients:
        return ConsumerDevicesCheckInBodyClients(
        key=data.get('key'),
        name=data.get('name'),
        detected=data.get('detected'),
        installable=data.get('installable'),
        supports_skills=data.get('supports_skills')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerDevicesCheckInBodyClients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerDevicesCheckInBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerDevicesCheckInBody:
        return ConsumerDevicesCheckInBody(
        installation_id=data.get('installation_id'),
        name=data.get('name'),
        os=data.get('os'),
        arch=data.get('arch'),
        app_version=data.get('app_version'),
        clients=[mapConsumerDevicesCheckInBodyClients.from_dict(item) for item in data.get('clients', []) if item],
        magic_mcp_token_ids=data.get('magic_mcp_token_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ConsumerDevicesCheckInBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

